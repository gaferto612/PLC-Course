# Scan Cycle Visualizer

A Streamlit app that animates the PLC scan cycle, showing input sampling, program execution, and output update — and lets you discover for yourself why a 5 ms input pulse can be invisible to a PLC with a 50 ms scan time.

## Run locally

```bash
cd interactive-tools/scan-cycle-visualizer
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud

1. Push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. New app → point at `interactive-tools/scan-cycle-visualizer/app.py`

## What you can play with

- **Scan time** (1–200 ms)
- **Input pulse width** (1–200 ms)
- **Pulse start time** (when the pulse arrives in the scan window)
- **Latching circuit** on/off

## Recommended exercises

See the bottom of the app for the three scenarios from Sprint 1.
