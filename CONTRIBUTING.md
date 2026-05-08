# Contributing to PLC-FastTrack

First — thanks for considering a contribution. This course gets better when learners turn into teachers.

## Ways to Contribute

### 🐛 Fix typos, bugs, or broken links
Open a PR directly. Small fixes don't need an Issue first.

### 📚 Add a new Challenge Lab
Labs live in `/challenge-labs/lab-XX-name/`. Each lab needs:
- `README.md` — the problem statement and I/O list
- `solution-template.st` — a structured text skeleton
- `tests/` — at least one JSON file of test vectors (see existing labs for format)

### 🌍 Add manufacturer translations
The same logic looks slightly different in Siemens SCL, Allen-Bradley Logix, and CODESYS. Add entries to `reference/manufacturer-mapping.md`.

### 🎨 Improve visuals
Mermaid diagram sources live in `/visuals/mermaid/` and are editable as plain
text. PRs that improve clarity are very welcome — additional formats (SVG,
Excalidraw, etc.) are also welcome alongside the Mermaid source.

### 🧠 Add flashcards
Add cards to `/flashcards/obsidian/` in the spaced-repetition format. Tag them by sprint.

## Code Style

- Structured text: 2-space indent, ALL_CAPS for variables, `PascalCase` for function blocks
- Python: PEP 8, type hints encouraged
- Markdown: 80-char line wrap where reasonable, Mermaid for diagrams

## PR Checklist

- [ ] If you changed a lab solution, the auto-grader (`python interactive-tools/ladder-simulator/grader.py --report /tmp/report.md`) passes locally
- [ ] New labs ship with ≥5 test vectors
- [ ] Visuals include an editable source file (Mermaid `.mmd`, SVG, etc.), not just a rendered PNG

## Code of Conduct

Be kind. Industrial automation is collaborative — your PR reviewer might be the engineer who saves your plant from a 2 AM call someday.
