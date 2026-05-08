"""
Lab Auto-Grader
───────────────
A small ST evaluator for grading PLC-FastTrack labs.

Approach: parse the source into a simple AST (assignments + if-blocks),
then walk it. Much more reliable than a token-stream walker.

Supports:
  - VAR / VAR_INPUT / VAR_OUTPUT blocks (declarations are skipped)
  - Comments  (* ... *)  and  // ...
  - Assignment:  ident := expr ;
  - IF ... THEN ... ELSIF ... THEN ... ELSE ... END_IF;
  - Operators: AND OR XOR NOT  =  <>  <  >  <=  >=  +  -  *  /  MOD
  - BOOL literals TRUE/FALSE; INT and REAL literals
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


# ══════════════════════ Lexer ══════════════════════

TOKEN_RE = re.compile(
    r"""
    (?P<COMMENT>\(\*.*?\*\)|//[^\n]*) |
    (?P<NUMBER>\d+\.\d+|\d+) |
    (?P<OP>:=|<>|<=|>=|[+\-*/<>=();,]) |
    (?P<IDENT>[A-Za-z_][A-Za-z_0-9]*)
    """,
    re.VERBOSE | re.DOTALL,
)

KEYWORDS = {
    "TRUE", "FALSE", "AND", "OR", "XOR", "NOT", "MOD",
    "IF", "THEN", "ELSIF", "ELSE", "END_IF",
    "VAR", "VAR_INPUT", "VAR_OUTPUT", "VAR_GLOBAL", "END_VAR",
    "BOOL", "INT", "DINT", "REAL", "LREAL", "TIME", "STRING",
}


def lex(src: str) -> list[tuple[str, str]]:
    tokens: list[tuple[str, str]] = []
    for m in TOKEN_RE.finditer(src):
        kind = m.lastgroup
        val = m.group()
        if kind == "COMMENT":
            continue
        if kind == "IDENT" and val.upper() in KEYWORDS:
            tokens.append(("KW", val.upper()))
        elif kind == "IDENT":
            tokens.append(("IDENT", val))
        elif kind == "NUMBER":
            tokens.append(("NUMBER", val))
        elif kind == "OP":
            tokens.append(("OP", val))
    return tokens


# ══════════════════════ Parser ══════════════════════


@dataclass
class Assign:
    name: str
    expr: list[tuple[str, str]]


@dataclass
class IfBlock:
    branches: list  # list of (cond_tokens, body_stmts)
    else_body: list = field(default_factory=list)


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self, offset=0):
        idx = self.pos + offset
        if idx < len(self.tokens):
            return self.tokens[idx]
        return ("EOF", "")

    def eat(self):
        t = self.tokens[self.pos]
        self.pos += 1
        return t

    def expect(self, kind, val=None):
        t = self.eat()
        if t[0] != kind or (val is not None and t[1] != val):
            raise SyntaxError(f"Expected {kind} {val}, got {t}")
        return t

    def parse_program(self):
        stmts = []
        while self.pos < len(self.tokens):
            stmt = self.parse_statement()
            if stmt is not None:
                stmts.append(stmt)
        return stmts

    def parse_statement(self):
        t = self.peek()
        if t[0] == "KW" and t[1] in {"VAR", "VAR_INPUT", "VAR_OUTPUT", "VAR_GLOBAL"}:
            while self.pos < len(self.tokens) and not (
                self.tokens[self.pos][0] == "KW"
                and self.tokens[self.pos][1] == "END_VAR"
            ):
                self.pos += 1
            if self.pos < len(self.tokens):
                self.pos += 1
            if self.peek() == ("OP", ";"):
                self.pos += 1
            return None

        if t[0] == "KW" and t[1] == "IF":
            return self.parse_if()

        if t[0] == "IDENT":
            name = self.eat()[1]
            self.expect("OP", ":=")
            expr_tokens = []
            while self.pos < len(self.tokens) and self.tokens[self.pos] != ("OP", ";"):
                expr_tokens.append(self.tokens[self.pos])
                self.pos += 1
            if self.pos < len(self.tokens):
                self.pos += 1
            return Assign(name, expr_tokens)

        while self.pos < len(self.tokens) and self.tokens[self.pos] != ("OP", ";"):
            self.pos += 1
        if self.pos < len(self.tokens):
            self.pos += 1
        return None

    def parse_if(self):
        self.expect("KW", "IF")
        branches = []
        cond = self._collect_until_keyword({"THEN"})
        self.expect("KW", "THEN")
        body = self._parse_body({"ELSIF", "ELSE", "END_IF"})
        branches.append((cond, body))

        else_body = []
        while True:
            t = self.peek()
            if t == ("KW", "ELSIF"):
                self.eat()
                cond = self._collect_until_keyword({"THEN"})
                self.expect("KW", "THEN")
                body = self._parse_body({"ELSIF", "ELSE", "END_IF"})
                branches.append((cond, body))
            elif t == ("KW", "ELSE"):
                self.eat()
                else_body = self._parse_body({"END_IF"})
            elif t == ("KW", "END_IF"):
                self.eat()
                if self.peek() == ("OP", ";"):
                    self.pos += 1
                break
            else:
                break
        return IfBlock(branches=branches, else_body=else_body)

    def _collect_until_keyword(self, stops):
        collected = []
        while self.pos < len(self.tokens):
            t = self.tokens[self.pos]
            if t[0] == "KW" and t[1] in stops:
                break
            collected.append(t)
            self.pos += 1
        return collected

    def _parse_body(self, stops):
        stmts = []
        while self.pos < len(self.tokens):
            t = self.peek()
            if t[0] == "KW" and t[1] in stops:
                break
            stmt = self.parse_statement()
            if stmt is not None:
                stmts.append(stmt)
        return stmts


# ══════════════════════ Evaluator ══════════════════════


def truthy(v):
    if isinstance(v, bool):
        return v
    if isinstance(v, (int, float)):
        return v != 0
    return bool(v)


PRECEDENCE = {
    "OR": 1, "XOR": 2, "AND": 3, "NOT": 4,
    "=": 5, "<>": 5, "<": 5, ">": 5, "<=": 5, ">=": 5,
    "+": 6, "-": 6,
    "*": 7, "/": 7, "MOD": 7,
}
RIGHT_ASSOC = {"NOT"}


def eval_expr(tokens, env):
    if not tokens:
        return False
    output = []
    ops = []
    for t in tokens:
        kind, val = t
        if kind == "NUMBER" or kind == "IDENT":
            output.append(t)
        elif kind == "KW" and val in ("TRUE", "FALSE"):
            output.append(t)
        elif kind == "OP" and val == "(":
            ops.append(t)
        elif kind == "OP" and val == ")":
            while ops and ops[-1] != ("OP", "("):
                output.append(ops.pop())
            if ops:
                ops.pop()
        elif (kind == "KW" or kind == "OP") and val in PRECEDENCE:
            while ops and ops[-1] != ("OP", "("):
                top_val = ops[-1][1]
                top_prec = PRECEDENCE.get(top_val, 0)
                cur_prec = PRECEDENCE[val]
                if top_prec > cur_prec or (
                    top_prec == cur_prec and val not in RIGHT_ASSOC
                ):
                    output.append(ops.pop())
                else:
                    break
            ops.append(t)
    while ops:
        output.append(ops.pop())

    stack = []
    for kind, val in output:
        if kind == "NUMBER":
            stack.append(float(val) if "." in val else int(val))
        elif kind == "KW" and val == "TRUE":
            stack.append(True)
        elif kind == "KW" and val == "FALSE":
            stack.append(False)
        elif kind == "IDENT":
            stack.append(env.get(val, 0))
        elif (kind == "KW" or kind == "OP") and val in PRECEDENCE:
            if val == "NOT":
                a = stack.pop()
                stack.append(not truthy(a))
            else:
                b = stack.pop()
                a = stack.pop() if stack else 0
                stack.append(apply_op(val, a, b))
    return stack[-1] if stack else False


def apply_op(op, a, b):
    if op == "AND":
        return truthy(a) and truthy(b)
    if op == "OR":
        return truthy(a) or truthy(b)
    if op == "XOR":
        return truthy(a) ^ truthy(b)
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        return a / b if b != 0 else 0
    if op == "MOD":
        return a % b if b != 0 else 0
    if op == "=":
        return a == b
    if op == "<>":
        return a != b
    if op == "<":
        return a < b
    if op == ">":
        return a > b
    if op == "<=":
        return a <= b
    if op == ">=":
        return a >= b
    return 0


def exec_stmts(stmts, env):
    for stmt in stmts:
        if isinstance(stmt, Assign):
            env[stmt.name] = eval_expr(stmt.expr, env)
        elif isinstance(stmt, IfBlock):
            executed = False
            for cond_tokens, body in stmt.branches:
                if truthy(eval_expr(cond_tokens, env)):
                    exec_stmts(body, env)
                    executed = True
                    break
            if not executed:
                exec_stmts(stmt.else_body, env)


def run_st(source, inputs):
    tokens = lex(source)
    parser = Parser(tokens)
    program = parser.parse_program()
    env = dict(inputs)
    exec_stmts(program, env)
    return env


# ══════════════════════ Grader ══════════════════════


def grade_lab(lab_dir):
    solution_file = None
    for name in ("solution.st", "main.st"):
        if (lab_dir / name).exists():
            solution_file = lab_dir / name
            break
    if solution_file is None:
        return {"lab": lab_dir.name, "status": "no_solution", "passed": 0, "total": 0, "details": []}

    tests_dir = lab_dir / "tests"
    if not tests_dir.exists():
        return {"lab": lab_dir.name, "status": "no_tests", "passed": 0, "total": 0, "details": []}

    test_files = sorted(tests_dir.glob("*.json"))
    if not test_files:
        return {"lab": lab_dir.name, "status": "no_tests", "passed": 0, "total": 0, "details": []}

    source = solution_file.read_text()
    passed = 0
    total = 0
    details = []

    for test_file in test_files:
        with test_file.open() as f:
            test = json.load(f)

        for case in test.get("cases", []):
            total += 1
            try:
                if "scans" in case:
                    env = {}
                    ok = True
                    fail_msg = ""
                    for scan in case["scans"]:
                        env.update(scan.get("inputs", {}))
                        env = run_st(source, env)
                        for k, v in scan.get("expect", {}).items():
                            if str(env.get(k)).lower() != str(v).lower():
                                ok = False
                                fail_msg = f"expected {k}={v}, got {k}={env.get(k)}"
                                break
                        if not ok:
                            break
                else:
                    env = run_st(source, case.get("inputs", {}))
                    ok = True
                    fail_msg = ""
                    for k, v in case.get("expect", {}).items():
                        if str(env.get(k)).lower() != str(v).lower():
                            ok = False
                            fail_msg = f"expected {k}={v}, got {k}={env.get(k)}"
                            break

                if ok:
                    passed += 1
                    details.append({"case": case.get("name", "?"), "result": "✅ pass"})
                else:
                    details.append({"case": case.get("name", "?"), "result": f"❌ {fail_msg}"})
            except Exception as e:
                details.append({"case": case.get("name", "?"), "result": f"💥 {type(e).__name__}: {e}"})

    return {
        "lab": lab_dir.name,
        "status": "graded",
        "passed": passed,
        "total": total,
        "details": details,
    }


def make_report(results):
    lines = ["# 🪜 Lab Auto-Grader Report\n"]
    if not results:
        lines.append("No labs detected in this PR.\n")
        return "\n".join(lines)

    for r in results:
        if r["status"] == "graded":
            if r["passed"] == r["total"] and r["total"] > 0:
                mark = "🟢"
            elif r["passed"] > 0:
                mark = "🟡"
            else:
                mark = "🔴"
            lines.append(f"## {mark} {r['lab']} — {r['passed']}/{r['total']} passed\n")
            for d in r["details"]:
                lines.append(f"- **{d['case']}** — {d['result']}")
            lines.append("")
        else:
            lines.append(f"## ⚠️ {r['lab']} — {r['status'].replace('_', ' ')}\n")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--labs", required=False, default="")
    ap.add_argument("--report", required=True)
    args = ap.parse_args()

    if args.labs.strip():
        lab_paths = [Path(p) for p in args.labs.strip().splitlines() if p.strip()]
    else:
        root = Path(__file__).resolve().parents[2]
        lab_paths = sorted((root / "challenge-labs").glob("lab-*"))

    results = [grade_lab(p) for p in lab_paths if p.exists()]
    report = make_report(results)
    Path(args.report).write_text(report)
    print(report)
    failed = any(r["status"] == "graded" and r["passed"] < r["total"] for r in results)
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
