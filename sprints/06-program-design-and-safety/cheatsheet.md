# Sprint 6 Cheat Sheet — Design & Safety

## 🏗️ Top-Down Design Workflow

```
1. SPEC               What does the system need to do?
   ↓                  Write it as plain English.
2. I/O LIST           Every sensor, every actuator, with tag, type, address.
   ↓                  This is your contract with the electrician.
3. STATE DIAGRAM      What states exist? What transitions between them?
   ↓                  SFC or simple state machine sketch.
4. CODE               Now write it. Match structure to design.
   ↓
5. TEST               Simulate, dry-run, force inputs, observe outputs.
   ↓
6. DOCUMENT           Comments, tag descriptions, version history.
   ↓
7. COMMISSION         FAT (Factory) → SAT (Site) → handover.
```

## 📋 The I/O List Template

| Tag | Type | Address | Range | Description | Fail-safe state |
|-----|------|---------|-------|-------------|-----------------|
| LSH_T01 | DI | I0.0 | — | Tank 1 high level switch | NC (broken wire = high) |
| TT_T01 | AI | IW64 | 0–100 °C | Tank 1 temperature | Below range = fault |
| Y_FILL | DO | Q0.0 | — | Fill valve solenoid | De-energized = closed |
| MX_T01 | DO | Q0.1 | — | Mixer contactor | De-energized = stopped |

**Rule:** every safety-critical signal should fail to a safe state. NC switches for E-stop, drop-out for valves, etc.

## 🛡️ Stop Categories (per IEC 60204-1)

| Category | What happens | Use case |
|----------|--------------|----------|
| **Cat 0** | Immediate removal of power | Most reliable; fine for systems that coast safely (small motors) |
| **Cat 1** | Controlled stop, then power removal | Required for hazardous motion (large motors, presses) |
| **Cat 2** | Controlled stop, power maintained | Process where stopping is normal but power-off would cause damage |

**Rule of thumb:** if a coast-down causes danger (kinetic energy, falling parts, hot surfaces), use Cat 1.

## 🔐 Safety Architecture

| Tier | What it is | When to use |
|------|------------|-------------|
| **Hardwired safety relay** (e.g., Pilz, Sick) | Dedicated relay logic for E-stops, gates | Simple machines, single safety zone |
| **Safety PLC** (e.g., Siemens S7-1500F, Allen-Bradley GuardLogix) | Programmable, dual-channel, certified | Multi-zone, complex sequences, networks |
| **Standard PLC for safety** | Just don't | Not certifiable, not legal in EU machinery |

**Standards to know:**
- ISO 13849-1 — Performance Levels (PL a–e)
- IEC 62061 — SIL 1–3 for machinery
- IEC 61508 — General functional safety (process)

## 🔍 Fault Diagnosis Toolkit

| Tool | Purpose |
|------|---------|
| **Diagnostic LEDs** | Run/Stop/Error on the CPU; status on each I/O point |
| **Status bits** | Internal flags showing module health, comms |
| **Watchdog timer** | Detects program freeze; faults the CPU if not pet |
| **Force tables** | Override an input or output during commissioning |
| **Online monitoring** | Watch live values during execution |
| **Diagnostic buffer** | Time-stamped log of CPU events |
| **Cross-reference** | Find every rung that touches a tag |

⚠️ **Forces are dangerous.** Always remove them after use, document while in place, and never leave a system in service with active forces.

## 📑 FMEA — Failure Modes & Effects Analysis

For each component, ask:

1. **Failure mode:** how can this fail?
2. **Effect:** what happens if it does?
3. **Severity:** 1–10 (10 = catastrophic)
4. **Likelihood:** 1–10
5. **Detectability:** 1–10 (10 = undetectable)
6. **RPN:** Severity × Likelihood × Detectability
7. **Mitigation:** what changes the score?

| Component | Failure Mode | Effect | S | L | D | RPN | Mitigation |
|-----------|--------------|--------|---|---|---|-----|------------|
| Level switch | Stuck closed | Pump runs dry | 8 | 3 | 4 | 96 | Add high-level timer + pressure switch |

## 🐛 The Bug Hunter's Checklist

When something doesn't work:

1. **Is it powered?** Check 24 V at the input, output card LEDs.
2. **Is the input being read?** Force-monitor the bit. Compare to physical state.
3. **Is the rung evaluating true?** Online monitoring shows rung state.
4. **Is the output being written?** Force the output. Does the device respond?
5. **Is there a double-coil?** Cross-reference all writes to the tag.
6. **Is a jump skipping the rung?** Check JMP labels active.
7. **Is the scan time too long?** Check diagnostic buffer for watchdog warnings.

## 📝 Documentation Minimums

Every PLC program should have:

- **Cover page** — project name, version, date, author, hardware list
- **I/O list** — all tags with descriptions
- **Sequence of operations** — plain-English description of what the program does
- **Rung comments** — every non-trivial rung explained in one line
- **Tag descriptions** — every tag has a description (no `M0`, `M1`, `M2` mysteries)
- **Change log** — date, author, what changed, why

If maintenance can't read your code at 2 AM with a flashlight, you haven't documented enough.
