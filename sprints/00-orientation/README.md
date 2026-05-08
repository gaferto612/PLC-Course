# Sprint 0 — Orientation

> Before the clock starts. Set up your tools, take the pre-assessment, and get your bearings.

---

## ⏱️ Time Budget

~1 hour

## 🎯 Goals

By the end of Sprint 0 you should:

1. Have a working environment for Python, Jupyter, and Streamlit
2. Have forked this repo and opened your six sprint-progress Issues
3. Know roughly where you stand — the pre-assessment tells you what to focus on
4. Have a copy of Bolton's *Programmable Logic Controllers, 5th Edition* on your desk

---

## 🛠️ Setup

### 1. Fork this repo

Click **Fork** in the top-right of the GitHub page. Clone your fork:

```bash
git clone https://github.com/<your-username>/plc-fasttrack.git
cd plc-fasttrack
```

### 2. Python environment

```bash
python3 -m venv .venv
source .venv/bin/activate          # on Windows: .venv\Scripts\activate
pip install -r interactive-tools/ladder-simulator/requirements.txt
```

### 3. Open your six sprint-progress Issues

Use the `🏃 Sprint Progress Tracker` template — one Issue per sprint. This is your dashboard.

### 4. Install Anki (optional but recommended)

[apps.ankiweb.net](https://apps.ankiweb.net/) — then import `flashcards/anki/plc-fasttrack.apkg`.

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

Once setup is done and the pre-assessment is scored, head to **[Sprint 1: Architecture & I/O](../01-architecture-and-io/)**.
