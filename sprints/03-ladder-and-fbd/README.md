# Sprint 3 — Ladder Logic & Function Block Diagrams

> **Bolton chapter:** 5
> **Time budget:** 6–8 hours
> **Core concept:** Ladder logic is graphical Boolean algebra disguised as a relay schematic — every rung is one logical statement evaluated left-to-right, top-to-bottom.

---

## 🎯 Sprint Goals

- Read and write ladder rungs for AND, OR, NOT, NAND, NOR, XOR, XNOR
- Build latching circuits (seal-in and SR latches)
- Recognize and avoid double-coiling, race conditions, and order-of-evaluation bugs
- Translate the same logic between LD and FBD comfortably
- Decide when LD vs. FBD is the better fit

---

## 📚 Bolton Reading

- Ch. 5 — Ladder and Functional Block Programming (full chapter)
- Cross-reference with Ch. 7 (internal relays) for latch examples

---

## 🗂️ Materials

- 📄 [Cheat sheet](cheatsheet.md)
- 🪜 [Ladder Playground](../../interactive-tools/ladder-simulator/index.html) — open in any browser, no install
- 🧮 [Workbook](../../workbooks/03-ladder-translation.ipynb)
- 🧪 [Lab 02: Conveyor Sort by Height](../../challenge-labs/lab-02-conveyor-sort/README.md)

---

## 📋 Sprint Plan

**Day 1** — Read Ch. 5. Hand-draw a ladder rung for each of the 7 logic gates.
**Day 2** — Open Ladder Playground. Build each gate, verify the truth table.
**Day 3** — Build a seal-in latch. Then build an SR latch. Compare behavior.
**Day 4** — Workbook: 10 written specs → ladder + FBD side by side.
**Day 5** — Lab 02. Submit PR.

---

## ✅ Definition of Done

- [ ] Bolton Ch. 5 read
- [ ] All 7 gates implemented in Ladder Playground
- [ ] Seal-in and SR latches built and explored
- [ ] Workbook completed
- [ ] Lab 02 submitted (auto-grader green)
- [ ] Flashcards reviewed
