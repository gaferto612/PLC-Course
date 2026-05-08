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

1. Press **Start**. Watch the chassis enter, the belt scroll while
   `Y_Belt` is high, and each station's LED pulse during its work step.
2. Press **E-Stop** mid-cycle. Notice how every motion output drops and
   `Y_Alarm` latches — pressing Reset before releasing the E-stop is
   refused (matching real safety practice).
3. Drag the **QC pass rate** down to 30 %. The QC fail lamp will fire on
   most cycles and the failed-cars counter ticks up.
