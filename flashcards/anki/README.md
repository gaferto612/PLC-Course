# Anki Deck

The full Anki package (`plc-fasttrack.apkg`) is generated from the Obsidian markdown source in `../obsidian/all-sprints.md`.

## Generate the .apkg

The simplest way:

1. Install Anki and the [CrowdAnki](https://ankiweb.net/shared/info/1788670778) addon
2. Or use the CLI tool [genanki](https://github.com/kerrickstaley/genanki):

```bash
pip install genanki
python build-anki.py
```

The `build-anki.py` script (TODO — community contribution welcome) reads the Obsidian markdown, splits on `?`, and emits a tagged Anki deck.

## Use the existing markdown for now

Until the .apkg is built, you can:

1. Open `../obsidian/all-sprints.md` in Obsidian with the Spaced Repetition plugin
2. Or paste Q/A pairs into Anki's basic-card creator manually

The cards work — the format conversion is the only step missing.
