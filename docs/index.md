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

## Quick Start

1. **Fork** the [GitHub repository](https://github.com/your-username/plc-fasttrack)
2. Open your six sprint-progress Issues from the template
3. Start with [Sprint 0](https://github.com/your-username/plc-fasttrack/tree/main/sprints/00-orientation)
4. Submit lab solutions as PRs — the auto-grader reviews them

## Live Tools

- **Scan Cycle Visualizer** — see the PLC scan loop in action *(Streamlit Cloud link goes here)*
- **Number Base Converter** — convert across denary, binary, octal, hex, BCD *(link)*
- **Timer/Counter Playground** — explore TON/TOF/TP/CTU timing diagrams *(link)*
- **Ladder Playground** — interactive truth tables for the seven gates and latches *(link)*

## Source Text

Bolton, W. (2009). *Programmable Logic Controllers* (5th ed.). Newnes / Elsevier. ISBN: 978-1-85617-751-1.

This site is a **study companion** — it doesn't reproduce the book.

## Contributing

Issues and PRs welcome on [GitHub](https://github.com/your-username/plc-fasttrack). See `CONTRIBUTING.md`.

## License

MIT — feel free to fork, adapt, and share.
