---
hide:
  - navigation
  - toc
---

<div class="plc-hero" markdown="0">
  <div class="plc-hero__inner">
    <span class="plc-hero__eyebrow"><span class="plc-dot"></span> RUN MODE · LIVE COURSE</span>
    <h1>Become a PLC engineer in <span class="plc-hero__accent">6 sprints</span>, not 6 months.</h1>
    <p>PLC-FastTrack turns Bolton's <em>Programmable Logic Controllers</em> into an interactive curriculum — animated infographics, in-browser simulators, auto-graded labs, and a capstone that runs real Structured Text on a virtual factory floor.</p>
    <div class="plc-hero__actions">
      <a class="plc-btn plc-btn--primary" href="../sprints/00-orientation/README.md">▶ Start Sprint 0</a>
      <a class="plc-btn plc-btn--ghost" href="../interactive-tools/car-factory-simulator/index.html">🚗 Try the factory sim</a>
    </div>
  </div>
</div>

<div class="plc-stats plc-reveal" markdown="0">
  <div class="plc-stat plc-stat--blue">
    <span class="plc-stat__num" data-count="7">0</span>
    <span class="plc-stat__label">Sprints + Capstone</span>
  </div>
  <div class="plc-stat plc-stat--amber">
    <span class="plc-stat__num" data-count="6">0</span>
    <span class="plc-stat__label">Challenge labs · auto-graded</span>
  </div>
  <div class="plc-stat plc-stat--green">
    <span class="plc-stat__num" data-count="5">0</span>
    <span class="plc-stat__label">In-browser simulators</span>
  </div>
  <div class="plc-stat plc-stat--violet">
    <span class="plc-stat__num" data-count="40" data-suffix="+">0</span>
    <span class="plc-stat__label">Hours to confident IEC 61131-3</span>
  </div>
</div>

<h2 class="plc-section-title">The Sprint Roadmap</h2>
<div class="plc-rail" markdown="0"><span class="plc-rail__fill"></span></div>

<div class="plc-roadmap plc-reveal" markdown="0">
  <a class="plc-step" data-sprint-id="s0" href="../sprints/00-orientation/README.md">
    <span class="plc-step__title">Orientation</span>
    <span class="plc-step__meta">Pre-assessment · Tooling</span>
  </a>
  <a class="plc-step" data-sprint-id="s1" href="../sprints/01-architecture-and-io/README.md">
    <span class="plc-step__title">Architecture &amp; I/O</span>
    <span class="plc-step__meta">Bolton Ch. 1–2</span>
  </a>
  <a class="plc-step" data-sprint-id="s2" href="../sprints/02-digital-foundations/README.md">
    <span class="plc-step__title">Digital Foundations</span>
    <span class="plc-step__meta">Bolton Ch. 3–4</span>
  </a>
  <a class="plc-step" data-sprint-id="s3" href="../sprints/03-ladder-and-fbd/README.md">
    <span class="plc-step__title">Ladder &amp; FBD</span>
    <span class="plc-step__meta">Bolton Ch. 5</span>
  </a>
  <a class="plc-step" data-sprint-id="s4" href="../sprints/04-iec-61131-languages/README.md">
    <span class="plc-step__title">IEC 61131-3 Languages</span>
    <span class="plc-step__meta">Bolton Ch. 6</span>
  </a>
  <a class="plc-step" data-sprint-id="s5" href="../sprints/05-timers-counters-registers/README.md">
    <span class="plc-step__title">Timers · Counters · Registers</span>
    <span class="plc-step__meta">Bolton Ch. 7–12</span>
  </a>
  <a class="plc-step" data-sprint-id="s6" href="../sprints/06-program-design-and-safety/README.md">
    <span class="plc-step__title">Design &amp; Safety</span>
    <span class="plc-step__meta">Bolton Ch. 13–14</span>
  </a>
  <a class="plc-step plc-step--capstone" data-sprint-id="cap" href="../sprints/07-capstone/README.md">
    <span class="plc-step__title">Capstone — Burner Sequence</span>
    <span class="plc-step__meta">Synthesis · SFC</span>
  </a>
</div>

> 💡 **Tip** · `Alt`-click any step above to mark it complete. Your progress lives in the browser so the rail stays accurate across visits.

<h2 class="plc-section-title">How a PLC Thinks — in 4 steps</h2>

<div class="plc-flow plc-reveal" markdown="0">
  <div class="plc-flow__step" data-icon="📥">
    <strong>1 · Read inputs</strong>
    <span>Sensors, buttons, limit switches snapshotted into the input image table.</span>
  </div>
  <div class="plc-flow__step" data-icon="⚙️">
    <strong>2 · Execute logic</strong>
    <span>Ladder / ST / SFC runs top-to-bottom against the input image.</span>
  </div>
  <div class="plc-flow__step" data-icon="📤">
    <strong>3 · Update outputs</strong>
    <span>Coils, lamps, valves driven from the output image table.</span>
  </div>
  <div class="plc-flow__step" data-icon="🔁">
    <strong>4 · Housekeeping</strong>
    <span>Comms, diagnostics, watchdog — then loop. Typical scan: 1–50 ms.</span>
  </div>
</div>

<h2 class="plc-section-title">⚡ Try one scan, right now</h2>

<div class="plc-demo plc-reveal" id="plc-demo" markdown="0">
  <div class="plc-demo__head">
    <span class="plc-demo__title">Mini PLC — seal-in start/stop with alarm</span>
    <span class="plc-demo__hint" data-step="Idle · press an input">Idle · press an input</span>
  </div>
  <div class="plc-demo__grid">
    <div>
      <div class="plc-io">
        <button class="plc-io__btn" data-btn="Start">START</button>
        <span class="plc-io__label">I0.0 · Start<br><span class="plc-io__sub">Latching pushbutton</span></span>
      </div>
      <div class="plc-io" style="margin-top:.6rem">
        <button class="plc-io__btn" data-btn="Stop">STOP</button>
        <span class="plc-io__label">I0.1 · Stop<br><span class="plc-io__sub">Momentary NC</span></span>
      </div>
      <div class="plc-io" style="margin-top:.6rem">
        <button class="plc-io__btn" data-btn="Sensor">SENSE</button>
        <span class="plc-io__label">I0.2 · Sensor<br><span class="plc-io__sub">Trips the alarm</span></span>
      </div>
    </div>

    <div class="plc-cpu">
      <small>CPU · ST RUNG</small>
      ▶ scanning
      <span class="plc-cpu__rung" data-rung>Run := (Start OR Run) AND NOT Stop</span>
    </div>

    <div>
      <div class="plc-io">
        <span class="plc-io__lamp" data-out="Run"></span>
        <span class="plc-io__label">Q0.0 · Run<br><span class="plc-io__sub">Sealed-in coil</span></span>
      </div>
      <div class="plc-io" style="margin-top:.6rem">
        <span class="plc-io__lamp is-amber" data-out="Lamp"></span>
        <span class="plc-io__label">Q0.1 · Running lamp<br><span class="plc-io__sub">Amber</span></span>
      </div>
      <div class="plc-io" style="margin-top:.6rem">
        <span class="plc-io__lamp is-red" data-out="Alarm"></span>
        <span class="plc-io__label">Q0.2 · Alarm<br><span class="plc-io__sub">Run · Sensor</span></span>
      </div>
    </div>
  </div>
</div>

<h2 class="plc-section-title">🧪 In-browser simulators</h2>

<div class="plc-cards plc-reveal" markdown="0">
  <a class="plc-card plc-card--blue" href="../interactive-tools/car-factory-simulator/index.html">
    <span class="plc-card__icon">🚗</span>
    <span class="plc-card__title">Car Factory Simulator</span>
    <span class="plc-card__body">A four-station automotive line driven by a live SFC + ST program. Watch outputs animate the floor with the active code line highlighted.</span>
    <span class="plc-card__cta">Open simulator</span>
  </a>
  <a class="plc-card plc-card--violet" href="../interactive-tools/ladder-simulator/index.html">
    <span class="plc-card__icon">🪜</span>
    <span class="plc-card__title">Ladder Playground</span>
    <span class="plc-card__body">Build rungs with contacts, coils, timers, counters — single-page, zero install. Perfect for sprint 3.</span>
    <span class="plc-card__cta">Build a rung</span>
  </a>
  <a class="plc-card plc-card--cyan" href="../interactive-tools/scan-cycle-visualizer/index.html">
    <span class="plc-card__icon">🎛️</span>
    <span class="plc-card__title">Scan Cycle Visualizer</span>
    <span class="plc-card__body">See exactly how a slow scan misses a fast pulse. Drag the scan-time slider and watch logic miss the input.</span>
    <span class="plc-card__cta">Visualize</span>
  </a>
  <a class="plc-card plc-card--green" href="../interactive-tools/number-converter/index.html">
    <span class="plc-card__icon">🔢</span>
    <span class="plc-card__title">Number Base Converter</span>
    <span class="plc-card__body">Denary · binary · octal · hex · BCD with click-to-toggle bits. The fastest way to internalise Sprint 2.</span>
    <span class="plc-card__cta">Toggle bits</span>
  </a>
  <a class="plc-card plc-card--red" href="../interactive-tools/timer-counter-playground/index.html">
    <span class="plc-card__icon">⏱️</span>
    <span class="plc-card__title">Timer / Counter Playground</span>
    <span class="plc-card__body">TON · TOF · TP · CTU side-by-side on the same pulse train. The IEC 61131-3 timing diagram you wish your textbook had.</span>
    <span class="plc-card__cta">Run a pulse</span>
  </a>
  <a class="plc-card" href="../challenge-labs/lab-01-traffic-light/README.md">
    <span class="plc-card__icon">🧪</span>
    <span class="plc-card__title">Challenge Labs</span>
    <span class="plc-card__body">Six structured-text labs from traffic lights to a full burner sequence — auto-graded against test vectors by our ST interpreter.</span>
    <span class="plc-card__cta">Open Lab 01</span>
  </a>
</div>

<h2 class="plc-section-title">🗺️ Course flow</h2>

```mermaid
flowchart LR
    Start([📚 Start]) --> S0[Sprint 0<br/>Orientation]
    S0 --> S1[Sprint 1<br/>Architecture & I/O]
    S1 --> S2[Sprint 2<br/>Digital]
    S2 --> S3[Sprint 3<br/>Ladder & FBD]
    S3 --> S4[Sprint 4<br/>IEC Languages]
    S4 --> S5[Sprint 5<br/>Timers & Counters]
    S5 --> S6[Sprint 6<br/>Design & Safety]
    S6 --> Cap[🏆 Capstone<br/>Burner Sequence]

    classDef sprint fill:#ede9fe,stroke:#7c3aed,stroke-width:1.5px,color:#1f2937;
    classDef cap fill:#f59e0b,stroke:#b45309,stroke-width:2px,color:#1c1917;
    class S0,S1,S2,S3,S4,S5,S6 sprint;
    class Cap cap;
```

<h2 class="plc-section-title">📦 What's in the box</h2>

<div class="plc-cards plc-reveal" markdown="0">
  <div class="plc-card plc-card--blue">
    <span class="plc-card__icon">📑</span>
    <span class="plc-card__title">One-page cheat sheets</span>
    <span class="plc-card__body">Every sprint distilled into a printable single-page reference, indexed against Bolton's chapters.</span>
  </div>
  <div class="plc-card plc-card--violet">
    <span class="plc-card__icon">🧠</span>
    <span class="plc-card__title">Spaced repetition</span>
    <span class="plc-card__body">Anki + Obsidian flashcards for the vocabulary, addressing schemes, and IEC operators that come up daily on the floor.</span>
  </div>
  <div class="plc-card plc-card--green">
    <span class="plc-card__icon">🤖</span>
    <span class="plc-card__title">CI-graded labs</span>
    <span class="plc-card__body">A real Structured-Text interpreter runs your <code>solution.st</code> against JSON test vectors and posts results on every PR.</span>
  </div>
  <div class="plc-card plc-card--cyan">
    <span class="plc-card__icon">🖼️</span>
    <span class="plc-card__title">Editable visuals</span>
    <span class="plc-card__body">All diagrams ship as Mermaid sources — remix them for your own slides, runbooks, or onboarding decks.</span>
  </div>
</div>

<h2 class="plc-section-title">📚 Reference shelf</h2>

| | | |
|---|---|---|
| 📖 [Glossary](../reference/glossary.md) | ⚙️ [IEC 61131-3 quickref](../reference/iec-61131-3-quickref.md) | 🏭 [Manufacturer mapping](../reference/manufacturer-mapping.md) |

---

> **Source text** · Bolton, W. (2009). *Programmable Logic Controllers* (5th ed.). Newnes / Elsevier. ISBN 978-1-85617-751-1. This site is a study companion — it doesn't reproduce the book.
>
> **Contributing** · Issues & PRs welcome on [GitHub](https://github.com/gaferto612/PLC-Course). See [CONTRIBUTING.md](../CONTRIBUTING.md). MIT licensed.
