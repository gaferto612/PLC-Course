# Lab 03 — Tank Fill/Drain with Level Control

> **Sprint:** 5 — Timers, Counters, Registers
> **Languages allowed:** ST or LD
> **Time:** ~2 hours

---

## 🎯 Brief

A water tank has a level transducer (4–20 mA → 0–100% scaled value). When the operator presses START, the system runs an automatic fill-then-drain cycle:

1. Open inlet valve until level ≥ 80%
2. Close inlet, hold for 5 seconds
3. Open outlet valve until level ≤ 10%
4. Close outlet, return to idle

The system must abort safely on STOP or EStop.

## 📋 I/O List

| Tag | Type | Description |
|-----|------|-------------|
| `Start` | BOOL | Start cycle |
| `Stop` | BOOL | Stop cycle |
| `EStop` | BOOL | E-stop (NC, true when OK) |
| `Level_Pct` | INT | Level 0–100 % (scaled from 4–20 mA) |
| `Hold_Done` | BOOL | True when hold timer has elapsed |
| `Inlet_Valve` | BOOL | Inlet solenoid |
| `Outlet_Valve` | BOOL | Outlet solenoid |
| `Hold_Timer_EN` | BOOL | Enable for the hold timer |
| `Phase` | INT | 0=Idle, 1=Filling, 2=Holding, 3=Draining |
| `Cycle_Active` | BOOL | True between Start and end of Drain |

## 🚦 Phase Transitions

- 0 → 1: Start AND EStop AND NOT Stop
- 1 → 2: Level_Pct ≥ 80
- 2 → 3: Hold_Done
- 3 → 0: Level_Pct ≤ 10
- Any → 0: Stop OR NOT EStop

The `Hold_Timer_EN` should be true only during Phase 2.

Submit `solution.st`.
