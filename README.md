# 🎛️ PLC-FastTrack

> An interactive, fast-track course based on **_Programmable Logic Controllers, 5th Edition_** by W. Bolton (Newnes, 2009).
>
> **Mission:** Move beyond passive reading. In 6 weeks, go from zero PLC knowledge to designing, documenting, and debugging IEC 61131-3 programs with confidence.

---

## 📜 Why This Repo Exists

Bolton's book is a fantastic foundation — 398 pages covering architecture, the five IEC 61131-3 languages, timers, counters, safety, and fault diagnosis. But reading isn't doing. This repo turns the book into:

- **6 sprints** of structured study (one per week)
- **Cheat sheets** that compress each chapter to one page
- **Interactive tools** (Streamlit + Gradio) for scan cycles, number bases, timers
- **Challenge labs** that auto-grade your structured text submissions
- **Flashcards** (Anki + Obsidian) for spaced-repetition retention
- **Visual assets** (Mermaid + Excalidraw) you can edit and remix

---

## 🗺️ Course Map

| Step | Sprint | Bolton Chapters |
|:----:|:-------|:----------------|
| 📚 | **Start here** | Preface |
| 0 | [Orientation](sprints/00-orientation/) | — |
| 1 | [Architecture & I/O](sprints/01-architecture-and-io/) | 1–2 |
| 2 | [Digital Foundations](sprints/02-digital-foundations/) | 3–4 |
| 3 | [Ladder & FBD](sprints/03-ladder-and-fbd/) | 5 |
| 4 | [IL, ST, SFC](sprints/04-iec-61131-languages/) | 6 |
| 5 | [Timers, Counters, Registers](sprints/05-timers-counters-registers/) | 7–12 |
| 6 | [Design & Safety](sprints/06-program-design-and-safety/) | 13–14 |
| 🏆 | [Capstone — Burner Start-up Sequence](sprints/07-capstone/) | Synthesis |

> **Path:** Start → 0 → 1 → 2 → 3 → 4 → 5 → 6 → 🏆
>
> The flowchart version of this map is rendered live on the [course site](https://gaferto612.github.io/PLC-Course/).

---

## 🏃 The Six Sprints

| # | Sprint | Bolton Chapters | Core Concept |
|---|--------|-----------------|--------------|
| 1 | [Architecture & I/O](sprints/01-architecture-and-io/) | 1–2 | A PLC is a hardened computer that scans inputs, runs logic, updates outputs. |
| 2 | [Digital Foundations](sprints/02-digital-foundations/) | 3–4 | PLCs think in bits — fluency in binary, octal, hex, and BCD is mandatory. |
| 3 | [Ladder & FBD](sprints/03-ladder-and-fbd/) | 5 | Ladder logic is graphical Boolean algebra disguised as a relay schematic. |
| 4 | [IEC 61131-3 Languages](sprints/04-iec-61131-languages/) | 6 | Five languages, one standard — pick the right tool for each part of the program. |
| 5 | [Timers, Counters, Registers](sprints/05-timers-counters-registers/) | 7–12 | Real automation is mostly about time, count, and memory. |
| 6 | [Design & Safety](sprints/06-program-design-and-safety/) | 13–14 | Working code is easy. Safe, debuggable, maintainable code is engineering. |

Plus the **[Capstone](sprints/07-capstone/)** — a complete burner start-up sequence in SFC.

---

## ⚡ Quick Start

1. **Fork this repo** so you can track your progress in your own copy.
2. Open an Issue from the `sprint-progress.md` template — one for each sprint.
3. Start with **[Sprint 0: Orientation](sprints/00-orientation/)** to take the pre-assessment.
4. Work one sprint per week. Each sprint = ~5–7 hours.
5. Submit lab solutions as PRs. The CI auto-grades structured text against test vectors.
6. Drop into **Discussions** when you get stuck or want to share a slick rung.

---

## 🧰 What's In The Box

```
plc-fasttrack/
├── sprints/              # The six-week curriculum
├── visuals/              # Mermaid, Excalidraw, infographics
├── interactive-tools/    # Streamlit + Gradio simulators
├── workbooks/            # Jupyter notebooks
├── challenge-labs/       # Auto-graded structured text labs
├── flashcards/           # Anki deck + Obsidian markdown
├── reference/            # Glossary, quickref, manufacturer mapping
└── docs/                 # GitHub Pages source
```

---

## 🌐 Live Course Site

GitHub Pages renders this as a browsable course at **<https://gaferto612.github.io/PLC-Course/>**, with every sprint, cheat sheet, lab and reference reachable from the side nav.

---

## 🛠️ Stack

- **Markdown + Mermaid** for content (renders natively on GitHub)
- **Streamlit / Gradio** for interactive tools
- **Jupyter** for workbooks
- **Python** for the auto-grader and Streamlit apps
- **Anki + Obsidian** for flashcards
- **GitHub Actions** for the daily-challenge bot and lab CI
- **GitHub Pages (MkDocs Material)** for the public course site

---

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). PRs welcome for additional labs, manufacturer translations, and bug fixes in the auto-grader.

---

## 📚 Source Text

Bolton, W. (2009). *Programmable Logic Controllers* (5th ed.). Newnes / Elsevier. ISBN: 978-1-85617-751-1.

This repo is a **study companion** — it does not reproduce the book. You'll need a copy of Bolton to follow along.

---

## ⚖️ License

MIT — see [LICENSE](LICENSE).
