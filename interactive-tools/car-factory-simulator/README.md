# 🚗 Car Factory PLC Simulator

A single-file interactive simulator that runs a small four-station automotive
assembly line under live PLC control. Open
[`index.html`](index.html) in any browser — no build, no install, no server.

## What you get

- **Live factory floor** — chassis enter at the infeed, ride a scrolling
  conveyor through Weld → Paint → Engine → Quality Check, and discharge to the
  output bin.
- **PLC I/O panel** — every input (`PB_Start`, `PB_Stop`, `PB_EStop`, four
  photoelectric eyes) and every output (`Y_Belt`, station enables, QC lamps,
  `Y_Alarm`) shown with a wired %I / %Q tag and an LED that lights when the
  bit is true. The animation is driven entirely by the output bits, never by
  direct DOM tweaks — the same way a real PLC drives a real plant.
- **Sequencer view** — the active SFC step, its description, and a live
  step-timer.
- **Equivalent ST source** with the line for the active step highlighted in
  real time, so the floor animation, the I/O panel, and the code stay in
  lock-step.
- **Operator controls** — Start, Stop, E-Stop (latching), Reset, plus a
  simulation-speed slider and an adjustable QC pass-rate.
- **Three control modes** —
  - **Auto** drives the line from the SFC (the default).
  - **Manual** bypasses the program; operator drives every `%Q` directly
    via the jog grid, including a manual `Spawn chassis` button. Excellent for
    feeling commissioning workflows and the output-to-floor mapping.
  - **Step** pauses the scan loop. `Scan once` and `+10 scans` advance the
    PLC one scan at a time so learners can watch each transition fire.
- **Fault injection** — stuck photoelectric sensors, conveyor jam (Y_Belt
  high but no motion), forced 100 % QC pass or 100 % QC fail. A safe way to
  practise Bolton Ch. 14 fault diagnosis.
- **Force any input** — click a row in the Inputs panel to lock that `%I`
  bit. Click again to release. The forced rows show a `· FORCED` chip.
- **Cycle-time sparkline** — a rolling chart of the last 10 cycle times,
  with running average and cars-per-minute throughput in the status bar.
- **Per-step teaching hint** — a one-line explanation of the active SFC
  step updates automatically as the program runs.

## How it maps to Bolton

- **Sprint 1 (Architecture & I/O)** — the simulator runs a fixed-cadence
  100 ms scan loop. Every scan: read inputs → execute program → write outputs.
- **Sprint 4 (IEC 61131-3)** — the program is a Sequential Function Chart
  rendered as a `CASE step OF …` statement in Structured Text.
- **Sprint 6 (Design & Safety)** — `PB_Stop` is wired NC (fail-safe) and
  `PB_EStop` opens the safety chain; pressing E-stop latches `Y_Alarm`,
  drops every motion output, and forces the program into `S_FAULT` until the
  operator releases the button and presses Reset.

## Try this

1. **The basics** — Press **Start** in Auto mode. Watch the chassis enter,
   the belt scroll while `Y_Belt` is high, and each station's LED pulse
   during its work step.
2. **Safety chain** — Press **E-Stop** mid-cycle. Notice how every motion
   output drops and `Y_Alarm` latches — pressing Reset before releasing the
   E-stop is refused (matching real safety practice).
3. **QC bias** — Drag the **QC pass rate** down to 30 %. The QC fail lamp
   will fire on most cycles and the failed-cars counter ticks up.
4. **Manual mode** — Switch to **Manual**. Press `Spawn chassis`, jog
   `Y_Belt` on and watch the chassis move under direct operator control.
   Drop the belt at the weld station, jog `Y_Weld` on, then continue.
5. **Step mode** — Switch to **Step**. Hit Start once to set `PB_Start`,
   then click `Scan once` repeatedly and read the highlighted ST line, the
   step pill, and the I/O panel after each scan.
6. **Fault diagnosis** — Open **Fault injection** and tick `Stuck PE_Weld`.
   The line will skip to `S3_WELD` the moment Start fires (the stuck eye is
   already high). Now untick it, tick `Belt motor jam` — the program looks
   normal but no chassis ever reaches the weld station because `Y_Belt`
   never produces motion.
7. **Force an input** — Click the `PE_QC` input row to lock it true. The
   program will jump straight to `S9_QC` the moment it reaches `S8_TO_QC`.
   Click again to release.
