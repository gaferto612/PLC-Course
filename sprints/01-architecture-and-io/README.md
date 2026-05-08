# Sprint 1 — Architecture & I/O Reality

> **Bolton chapters:** 1–2
> **Time budget:** 5–7 hours
> **Core concept:** A PLC is a hardened computer that scans inputs, runs logic, and updates outputs in a deterministic cycle — the I/O devices are where the physical world meets the program.

---

## 🎯 Sprint Goals

By the end of this week you will be able to:

- Describe the five core hardware blocks of a PLC and what each does
- Walk through a scan cycle and explain why scan time matters
- Distinguish discrete from analog I/O and pick the right type for a given device
- Tell sourcing from sinking inputs and read a wiring diagram for a 24 VDC sensor
- Explain why a 5 ms pulse can be invisible to a PLC with a 50 ms scan time
- Map at least 10 real-world devices to their PLC I/O type

---

## 📚 What to Read in Bolton

| Section | Pages | Why |
|---------|-------|-----|
| Ch. 1 — Programmable Logic Controllers | full chapter | Core architecture and history |
| Ch. 2 — Input-Output Devices | full chapter | The catalog of sensors and actuators |
| Ch. 4 — I/O Processing | first half | Scan cycle deep-dive |

You'll come back to Ch. 4 in Sprint 2 for the digital details.

---

## 🗂️ Sprint Materials

- 📄 **[Cheat sheet](cheatsheet.md)** — one-page distillation
- 🧮 **[Workbook](../../workbooks/01-io-mapping.ipynb)** — map 10 devices, classify each
- 🔧 **[Scan Cycle Visualizer](../../interactive-tools/scan-cycle-visualizer/README.md)** — animated demo
- 🧪 **[Lab 01: Traffic Light Controller](../../challenge-labs/lab-01-traffic-light/README.md)** — your first auto-graded submission
- 🃏 **[Flashcards](flashcards.md)** — sprint-1 cards for spaced repetition

---

## 📋 Sprint Plan

### Day 1 — Read & Anchor (1.5 h)

Read Bolton Chapter 1. As you read, sketch (on paper or Excalidraw) the five core blocks and how they connect. No copying — your sketch is the proof you understood it.

### Day 2 — I/O Catalogue (1 h)

Read Bolton Chapter 2. Open the workbook (`workbooks/01-io-mapping.ipynb`) and classify the 10 devices listed. There's no "right" answer for every one — the discussion is the point.

### Day 3 — Scan Cycle Deep-Dive (1.5 h)

Skim the first half of Chapter 4. Then open the **Scan Cycle Visualizer** in this repo. Run it three times:

1. Slow scan (100 ms), short input pulse (10 ms) — watch the pulse get missed
2. Fast scan (5 ms), same pulse — watch it get caught
3. Slow scan, but with a latching rung — see how latching rescues you

### Day 4 — Lab (1.5 h)

Tackle **Lab 01: Traffic Light Controller**. The spec is in the lab folder. Submit your structured text as a PR. The CI auto-grades it.

### Day 5 — Recall & Reflect (0.5 h)

Run through the sprint flashcards. Update your sprint-progress Issue with the reflection notes.

---

## ✅ Definition of Done

- [ ] Bolton Ch. 1 + 2 read
- [ ] Cheat sheet read and bookmarked
- [ ] Workbook completed
- [ ] Scan Cycle Visualizer run with all three scenarios
- [ ] Lab 01 submitted as PR (auto-grader green)
- [ ] Flashcards reviewed
- [ ] Sprint-progress Issue updated

---

## ➡️ Next

Once Lab 01 passes CI, head to **[Sprint 2: Digital Foundations](../02-digital-foundations/README.md)**.
