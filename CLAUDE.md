# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

PLC-FastTrack is a **course / curriculum repository**, not a software product. The bulk of the content is Markdown (sprints, cheat sheets, labs, references, flashcards). The only meaningful executable code is:

- `interactive-tools/ladder-simulator/grader.py` — a self-contained Structured Text (ST) interpreter that auto-grades challenge-lab submissions.
- A handful of Streamlit/Gradio apps under `interactive-tools/*/app.py` (number converter, scan-cycle visualizer, timer/counter playground).
- Two interactive tools (`car-factory-simulator`, `ladder-simulator`) that are static `index.html` pages with no Python build step.
- An MkDocs Material site that publishes the whole repo as a browsable course.

## Common commands

```bash
# Install grader / Python tool deps
pip install -r interactive-tools/ladder-simulator/requirements.txt

# Run the lab auto-grader over ALL labs (CI behavior with no --labs arg)
python interactive-tools/ladder-simulator/grader.py --report /tmp/report.md

# Grade only specific labs (newline-separated paths, matches CI usage)
python interactive-tools/ladder-simulator/grader.py \
  --labs $'challenge-labs/lab-01-traffic-light\nchallenge-labs/lab-03-tank-fill-drain' \
  --report /tmp/report.md

# Run an interactive tool locally (number-converter uses Gradio; the rest use Streamlit)
python interactive-tools/number-converter/app.py
streamlit run interactive-tools/scan-cycle-visualizer/app.py
streamlit run interactive-tools/timer-counter-playground/app.py

# Build the docs site (MkDocs writes to ../../_site by design — see note below)
pip install mkdocs-material mkdocs-mermaid2-plugin
mkdocs build --config-file docs/mkdocs.yml
```

The grader exits with status `1` if any graded lab has failing cases — the CI workflow uses this signal.

## Architecture notes that aren't obvious from a directory listing

### The auto-grader is a real ST interpreter
`interactive-tools/ladder-simulator/grader.py` is pure stdlib (no deps from `requirements.txt` are actually needed to run it) and implements three stages:

1. **Lexer** (`lex`) — regex-based, recognises `(* ... *)` and `// ...` comments, ST keywords, identifiers, numbers, and operators including `:=`, `<>`, `<=`, `>=`.
2. **Parser** (`Parser`) — builds an AST of `Assign` and `IfBlock` nodes. `VAR* … END_VAR` declaration blocks are skipped entirely; the grader does not type-check.
3. **Evaluator** (`eval_expr`, `exec_stmts`) — shunting-yard for expressions with the precedence table in `PRECEDENCE` (note: `NOT` is right-associative); supports `AND OR XOR NOT MOD`, comparison ops, `+ - * /`, and `TRUE`/`FALSE` literals.

When extending the language (e.g. adding `CASE`, `FOR`, function blocks), changes need to land in **all three** stages. Treat the supported subset as the contract for what labs may use.

### Lab test-vector format
Each lab lives under `challenge-labs/lab-NN-name/` with:
- `solution-template.st` — given to the learner (skeleton)
- `solution.st` *or* `main.st` — the file the grader actually runs (first match wins)
- `tests/*.json` — one or more case files

Two case shapes are supported:
- **Single-scan**: `{ "name": …, "inputs": {…}, "expect": {…} }` — one evaluation, asserts final env values.
- **Multi-scan** (stateful): `{ "name": …, "scans": [ { "inputs": {…}, "expect": {…} }, … ] }` — `env` carries between scans (`env.update(scan.inputs); env = run_st(source, env)`), so `Phase`/latching variables persist. Use this for any state-machine lab.

Value comparison is done as **case-insensitive string match** (`str(env.get(k)).lower() == str(v).lower()`), so `true`/`True`/`TRUE` all match. New labs should ship with ≥5 test vectors (per CONTRIBUTING.md).

### MkDocs uses the repo root as `docs_dir`
`docs/mkdocs.yml` sets `docs_dir: ..` and `site_dir: ../../_site`. The build output lives **outside** the repo (MkDocs forbids `site_dir` inside `docs_dir`). The `pages-deploy.yml` workflow runs `mkdocs build` then `mv ../_site ./_site` before uploading. If you add a new top-level Markdown file, it is built by default; only files matched by `exclude_docs` or absent from `nav` are dropped from navigation (they still build for cross-links — see `not_in_nav`).

### GitHub Actions wiring
- **`ladder-validator.yml`** — fires on PRs touching `challenge-labs/**/*.st|*.il|solution.*`. It detects changed lab directories from the diff against `origin/main` and passes them to the grader via `--labs`. Results are posted as a sticky PR comment.
- **`daily-challenge.yml`** — cron at 07:00 UTC Mon–Fri, picks a random non-blank line from `reference/daily-questions.txt` and opens an Issue labelled `daily-challenge, sprint-active`. New daily prompts are added by appending to that file.
- **`pages-deploy.yml`** — deploys MkDocs on push to `main` for changes under content paths.

### Sprint / lab numbering is the API
The course path Start → 0 → 1 → … → 6 → 🏆 is encoded in three places that must stay in sync: the README course-map table, the `nav:` block in `docs/mkdocs.yml`, and the `sprints/NN-*` / `challenge-labs/lab-NN-*` directory names. Renaming a sprint folder breaks both the live site nav and inbound links from sprint READMEs.

## Conventions from CONTRIBUTING.md

- **Structured text**: 2-space indent, `ALL_CAPS` for variables, `PascalCase` for function blocks. Stick to the operator subset the grader supports (see above).
- **Python**: PEP 8, type hints encouraged.
- **Visuals**: editable source (Mermaid `.mmd`, SVG, Excalidraw) must accompany any rendered PNG.
