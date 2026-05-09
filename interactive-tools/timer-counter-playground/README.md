# ⏱️ Timer / Counter Playground

A browser-based, side-by-side visualizer for the four IEC 61131-3 timing
primitives — TON, TOF, TP, and CTU — driven by a configurable input pulse
train. Open [`index.html`](index.html) in any browser — no build, no install,
no server.

The same tool is wired into the [live course
site](https://gaferto612.github.io/PLC-Course/interactive-tools/timer-counter-playground/index.html).

## What you get

- **One input, four outputs** — the same EN pulse train drives a TON, TOF,
  TP, and CTU; their Q outputs are stacked so you can read the differences at
  a glance.
- **Adjustable presets** — independent sliders for the timer preset PT and
  the counter preset PV.
- **Adjustable input pattern** — pulse width and pulse period control the
  EN train. Make EN slower than PT and watch the TON never fire.

## How it maps to Bolton

- **Sprint 5 (Timers, Counters, Registers)** — Bolton Ch. 9 covers the four
  timer types, Ch. 10 covers counters. This tool puts them on the same time
  axis so you stop confusing them.
- The "TON resets every cycle if EN drops" failure mode is the canonical bug
  source in beginner ladder logic and is on full display here.

## Try this

1. **Pulse < PT** — set pulse width = 2 s, PT = 5 s. The TON never completes
   because EN drops before the accumulator reaches PT.
2. **Pulse > PT** — set pulse width = 4 s, PT = 2 s. Now the TON fires every
   cycle.
3. **CTU vs TON** — both look similar at a glance, but CTU counts events while
   TON measures continuous time. Drop pulse width below PT and see CTU keep
   ticking up while TON stays at zero.
4. **TP for one-shots** — TP gives a guaranteed-width pulse regardless of how
   long EN stays high. Compare it to the TON output for the same input.

## Legacy Streamlit app

`app.py` is the original Streamlit version retained for offline / Python use.
The HTML version above is what the live course site links to because GitHub
Pages can't host Streamlit.
