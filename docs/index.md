# 🎛️ PLC-FastTrack

> An interactive, fast-track course based on **_Programmable Logic Controllers, 5th Edition_** by W. Bolton.

## Move beyond passive reading.

In 6 weeks, go from zero PLC knowledge to designing, documenting, and debugging IEC 61131-3 programs with confidence.

## Course Map

```mermaid
flowchart LR
    Start([📚 Start]) --> S0[Sprint 0]
    S0 --> S1[Sprint 1<br/>Architecture & I/O]
    S1 --> S2[Sprint 2<br/>Digital]
    S2 --> S3[Sprint 3<br/>Ladder & FBD]
    S3 --> S4[Sprint 4<br/>IEC Languages]
    S4 --> S5[Sprint 5<br/>Timers & Counters]
    S5 --> S6[Sprint 6<br/>Design & Safety]
    S6 --> Cap[🏆 Capstone]

    style Cap fill:#22c55e,color:#fff
```

## What's Inside

- **6 sprints** of structured study, one per week
- **Cheat sheets** that compress each chapter to one page
- **Interactive simulators** (Streamlit + Gradio) for scan cycles, number bases, and timers
- **Auto-graded labs** in Structured Text
- **Flashcards** for spaced repetition
- **Visual assets** — Mermaid diagrams and Excalidraw templates

## Where to Start

1. **[Sprint 0 — Orientation](../sprints/00-orientation/README.md)** — set up your environment and take the pre-assessment
2. **[Sprint 1 — Architecture & I/O](../sprints/01-architecture-and-io/README.md)** — Bolton chapters 1–2
3. Work through one sprint per week. Each sprint = ~5–7 hours.
4. Tackle the **[Capstone](../sprints/07-capstone/README.md)** when you're ready.

## Sprint Index

| # | Sprint | Bolton |
|---|--------|--------|
| 0 | [Orientation](../sprints/00-orientation/README.md) | Preface |
| 1 | [Architecture & I/O](../sprints/01-architecture-and-io/README.md) | Ch. 1–2 |
| 2 | [Digital Foundations](../sprints/02-digital-foundations/README.md) | Ch. 3–4 |
| 3 | [Ladder & FBD](../sprints/03-ladder-and-fbd/README.md) | Ch. 5 |
| 4 | [IEC 61131-3 Languages](../sprints/04-iec-61131-languages/README.md) | Ch. 6 |
| 5 | [Timers, Counters, Registers](../sprints/05-timers-counters-registers/README.md) | Ch. 7–12 |
| 6 | [Design & Safety](../sprints/06-program-design-and-safety/README.md) | Ch. 13–14 |
| 🏆 | [Capstone — Burner Sequence](../sprints/07-capstone/README.md) | Synthesis |

## Interactive Tools

These are run locally — clone the repo and follow each tool's README to launch:

- **[Scan Cycle Visualizer](../interactive-tools/scan-cycle-visualizer/README.md)** *(Streamlit)* — see how a slow scan misses a fast pulse
- **Number Base Converter** *(Gradio)* — `interactive-tools/number-converter/`
- **Timer / Counter Playground** *(Streamlit)* — `interactive-tools/timer-counter-playground/`
- **[Ladder Playground](../interactive-tools/ladder-simulator/index.html)** *(plain HTML, runs in any browser)*

## Reference

- [Glossary](../reference/glossary.md)
- [IEC 61131-3 Quick Reference](../reference/iec-61131-3-quickref.md)
- [Manufacturer Mapping](../reference/manufacturer-mapping.md)
- [Further Reading](../reference/further-reading.md)

## Source Text

Bolton, W. (2009). *Programmable Logic Controllers* (5th ed.). Newnes / Elsevier. ISBN: 978-1-85617-751-1.

This site is a **study companion** — it doesn't reproduce the book.

## Contributing

Issues and PRs welcome on [GitHub](https://github.com/gaferto612/PLC-Course). See [CONTRIBUTING.md](../CONTRIBUTING.md).

## License

MIT — feel free to fork, adapt, and share.
