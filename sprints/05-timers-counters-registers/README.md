# Sprint 5 — Timers, Counters, Shift Registers, Sequencers, Data Handling

> **Bolton chapters:** 7–12
> **Time budget:** 7–9 hours
> **Core concept:** Real-world automation is mostly about *time* and *count* — internal relays, timers, and counters turn instantaneous Boolean logic into stateful machines that remember, delay, and sequence.

---

## 🎯 Sprint Goals

- Use TON, TOF, TP, and retentive timers correctly
- Use CTU, CTD, CTUD counters
- Build a shift register for tracking parts on a conveyor
- Use jumps, calls, and subroutines without creating scan-time hazards
- Move and compare data with MOV, GT, LT, EQ, and the basic math instructions

---

## 📚 Bolton Reading

| Chapter | Topic |
|---------|-------|
| 7 | Internal relays |
| 8 | Jump and call |
| 9 | Timers |
| 10 | Counters |
| 11 | Shift registers |
| 12 | Data handling |

This is the longest reading load in the course. Pace it across the whole week.

---

## 🗂️ Materials

- 📄 [Cheat sheet](cheatsheet.md)
- ⏱️ Timer/Counter Playground (Streamlit) — `interactive-tools/timer-counter-playground/app.py`
- 🧮 [Workbook](../../workbooks/05-timer-state-machines.ipynb)
- 🧪 [Lab 03: Tank Fill/Drain](../../challenge-labs/lab-03-tank-fill-drain/README.md)
- 🧪 [Lab 04: Batch Mixer](../../challenge-labs/lab-04-batch-mixer/README.md)

---

## 📋 Sprint Plan

**Day 1** — Read Ch. 7 + 9. Open Timer/Counter Playground. Build a TON, then chain two TONs for a flasher.
**Day 2** — Read Ch. 10. Build CTU and CTUD examples. Make a parts counter that resets each shift.
**Day 3** — Read Ch. 8 + 11. Build a shift register conveyor model.
**Day 4** — Read Ch. 12. Workbook: implement temperature scaling (RTD raw → °C) in ST.
**Day 5** — Lab 03 (tank) and Lab 04 (batch mixer). Submit both PRs.

---

## ✅ Definition of Done

- [ ] Bolton Ch. 7–12 read
- [ ] Timer/Counter Playground used for ≥4 scenarios
- [ ] Workbook completed
- [ ] Lab 03 + Lab 04 submitted (auto-grader green)
- [ ] Flashcards reviewed
