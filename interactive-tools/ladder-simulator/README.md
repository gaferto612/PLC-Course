# Ladder Simulator & Lab Auto-Grader

Two tools in one folder:

## 🤖 `grader.py` — Auto-grades structured-text submissions

A tiny IEC 61131-3 Structured Text interpreter (just enough for course labs) that:

- Parses your `.st` file
- Evaluates it against test vectors in JSON (`tests/*.json`)
- Emits a Markdown report

The CI workflow `.github/workflows/ladder-validator.yml` runs it on every PR and posts the report as a sticky comment.

### Test vector format

```json
{
  "lab": "lab-01-traffic-light",
  "cases": [
    {
      "name": "Initial state — all stop",
      "inputs": { "Start": false, "Stop": false },
      "expect": { "GreenNS": false, "RedNS": true }
    },
    {
      "name": "Multi-scan sequence",
      "scans": [
        { "inputs": { "Start": true }, "expect": { "Sequence_Active": true } },
        { "inputs": { "Start": false }, "expect": { "Sequence_Active": true } }
      ]
    }
  ]
}
```

### Run locally

```bash
python grader.py --report /tmp/report.md
# or grade just one lab
python grader.py --labs "challenge-labs/lab-01-traffic-light" --report /tmp/report.md
```

## 🪜 Ladder Playground (planned)

The React-based drag-and-drop ladder editor lives in `index.html`. It's a single-file app that runs in any browser — no build step. (Stub provided; ready for community contribution.)

Contributions welcome — see [CONTRIBUTING.md](../../CONTRIBUTING.md).
