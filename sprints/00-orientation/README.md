# Sprint 0 — Orientation

> Before the clock starts. Set up your tools, take the pre-assessment, and get your bearings.

---

## ⏱️ Time Budget

~1 hour

## 🎯 Goals

By the end of Sprint 0 you should:

1. Have forked this repo and opened your six sprint-progress Issues
2. Know roughly where you stand — the pre-assessment tells you what to focus on
3. Have a copy of Bolton's *Programmable Logic Controllers, 5th Edition* on your desk
4. (Optional) Have a working Python environment if you want to run the workbooks or the legacy Streamlit/Gradio versions of the interactive tools locally

---

## 🛠️ Setup

### 1. Fork this repo

Click **Fork** in the top-right of the GitHub page. Clone your fork:

```bash
git clone https://github.com/<your-username>/PLC-Course.git
cd PLC-Course
```

### 2. Interactive tools — no install required

Every interactive tool ships as a single static HTML page that runs in any
browser. You can use them straight from the live course site:

- [Number Base Converter](../../interactive-tools/number-converter/index.html) — Sprint 2
- [Scan Cycle Visualizer](../../interactive-tools/scan-cycle-visualizer/index.html) — Sprint 1
- [Timer / Counter Playground](../../interactive-tools/timer-counter-playground/index.html) — Sprint 5
- [Ladder Playground](../../interactive-tools/ladder-simulator/index.html) — Sprints 3–6
- [Car Factory Simulator](../../interactive-tools/car-factory-simulator/index.html) — capstone-level

If you'd rather hack on the tools or run them offline, each folder also
contains the original Streamlit / Gradio version (`app.py`) with its own
`requirements.txt`. The workbooks under `workbooks/` are Jupyter notebooks
and need a Python environment.

```bash
# Optional — only if you want the Python versions locally
python3 -m venv .venv
source .venv/bin/activate          # on Windows: .venv\Scripts\activate
pip install jupyter
```

### 3. Open your six sprint-progress Issues

Use the `🏃 Sprint Progress Tracker` template — one Issue per sprint. This is your dashboard.

### 4. Install Anki (optional but recommended)

Install [Anki](https://apps.ankiweb.net/). The course's flashcards live as
markdown in `flashcards/obsidian/all-sprints.md`. Until the prebuilt
`.apkg` ships, the simplest paths are:

- Open the markdown in Obsidian with the Spaced Repetition plugin, **or**
- Paste the Q/A pairs into Anki's basic-card creator.

See `flashcards/anki/README.md` for details.

---

## 📝 Pre-Assessment

Take the [pre-assessment](pre-assessment.md). 20 questions, ~15 minutes. Don't look anything up. Score yourself honestly.

The score tells you which sprints to dig into deepest:

| Score | What it means |
|-------|---------------|
| 0–6   | Bolton from page 1, no skipping. You're in for a great ride. |
| 7–12  | Skim Sprints 1–2, focus on 3–6. |
| 13–17 | You have the basics. Use this course to firm up IEC 61131-3 fluency and safety. |
| 18–20 | You probably know more than this course teaches. Try the capstone first; come back for whatever bites you. |

---

## 📚 What to Read This Week (in Bolton)

- Preface (pages ix–xii) — the book's own roadmap
- Chapter 1 introduction (pages 1–6) — sets the stage for Sprint 1

---

## ➡️ Next

Once setup is done and the pre-assessment is scored, head to **[Sprint 1: Architecture & I/O](../01-architecture-and-io/README.md)**.
