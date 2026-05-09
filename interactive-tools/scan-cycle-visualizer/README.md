# 🎛️ Scan Cycle Visualizer

A browser-based timing-diagram simulator that shows you why a 5 ms input pulse
can be invisible to a PLC with a 50 ms scan time. Open
[`index.html`](index.html) in any browser — no build, no install, no server.

The same tool is wired into the [live course
site](https://gaferto612.github.io/PLC-Course/interactive-tools/scan-cycle-visualizer/index.html).

## What you get

- **Three synchronized traces** — physical input, PLC input image, PLC output
  — drawn with step transitions over a 600 ms window.
- **Scan boundaries** rendered as dashed verticals so you can see exactly
  *when* the PLC samples the world.
- **Live diagnostics** — pulse/scan ratio, physical pulse duration, time the
  PLC actually saw the input as high, plus a verdict explaining whether the
  pulse was caught or missed.
- **Latching toggle** — turn on a seal-in circuit and watch the output stay
  high even after the physical input drops.

## How it maps to Bolton

- **Sprint 1 (Architecture & I/O)** — Bolton Ch. 1 introduces the scan cycle;
  Ch. 4 reinforces the input image / output image abstraction.
- The "missed pulse" failure mode is the canonical motivation for either
  faster scans, hardware latching, or interrupts on real PLCs.

## Try this

1. **Slow scan, short pulse** — scan = 100 ms, pulse = 10 ms; drag the start
   slider and watch the pulse flip between caught and missed.
2. **Fast scan rescue** — drop the scan to 5 ms and the same 10 ms pulse is
   always caught.
3. **Latch rescue** — leave the slow scan but turn on the latch. Now even a
   pulse that arrives mid-scan stays held in the output once it's seen.
4. **Worst-case latency** — the maximum delay between an input change and the
   matching output change is roughly two scan times.

## Legacy Streamlit app

`app.py` is the original Streamlit version retained for offline / Python use.
The HTML version above is what the live course site links to because GitHub
Pages can't host Streamlit.
