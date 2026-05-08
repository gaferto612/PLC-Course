# Contributing to PLC-FastTrack

First — thanks for considering a contribution. This course gets better when learners turn into teachers.

## Ways to Contribute

### 🐛 Fix typos, bugs, or broken links
Open a PR directly. Small fixes don't need an Issue first.

### 📚 Add a new Challenge Lab
Labs live in `/challenge-labs/lab-XX-name/`. Each lab needs:
- `README.md` — the problem statement and I/O list
- `solution-template.st` — a structured text skeleton
- `tests/` — test vectors as JSON (see existing labs for format)
- `discussion.md` — link to a Discussions thread

### 🌍 Add manufacturer translations
The same logic looks slightly different in Siemens SCL, Allen-Bradley Logix, and CODESYS. Add entries to `reference/manufacturer-mapping.md`.

### 🎨 Improve visuals
Mermaid diagrams in `/visuals/mermaid/` and Excalidraw files in `/visuals/excalidraw/` are all editable. PRs that improve clarity are very welcome.

### 🧠 Add flashcards
Add cards to `/flashcards/obsidian/` in the spaced-repetition format. Tag them by sprint.

## Code Style

- Structured text: 2-space indent, ALL_CAPS for variables, `PascalCase` for function blocks
- Python: PEP 8, type hints encouraged
- Markdown: 80-char line wrap where reasonable, Mermaid for diagrams

## PR Checklist

- [ ] Tests pass (`pytest` in the repo root)
- [ ] New labs have ≥5 test vectors
- [ ] Visuals have an editable source file, not just a PNG
- [ ] You've added yourself to `CONTRIBUTORS.md` if it's your first PR

## Code of Conduct

Be kind. Industrial automation is collaborative — your PR reviewer might be the engineer who saves your plant from a 2 AM call someday.
