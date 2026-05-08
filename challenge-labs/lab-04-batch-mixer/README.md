# Lab 04 — Batch Mixer (SFC)

> **Sprint:** 5 — Timers, Counters, Registers (with SFC concepts from Sprint 4)
> **Time:** ~2 hours

---

## 🎯 Brief

Implement a 3-ingredient batch recipe:

1. Add 50 L of water (open `Y_Water` until `Flow_Total ≥ 50`)
2. Add 25 kg of sugar (open `Y_Sugar` until `Weight_Total ≥ 25`)
3. Run mixer for 30 seconds (`Mixer_Run` true, gated by `Mix_Done`)
4. Drain (open `Y_Drain` until `Tank_Empty`)
5. Return to idle

Implement as a phase machine in ST. The `Hold_Timer_EN` for the mixer is gated by the phase.

## I/O

| Tag | Type | Description |
|-----|------|-------------|
| `Start` / `Stop` / `EStop` | BOOL | Standard controls |
| `Flow_Total` | INT | Cumulative water (L) |
| `Weight_Total` | INT | Cumulative sugar (kg) |
| `Mix_Done` | BOOL | Mixer timer elapsed |
| `Tank_Empty` | BOOL | Drain complete sensor |
| `Y_Water` / `Y_Sugar` / `Y_Drain` | BOOL | Valves |
| `Mixer_Run` | BOOL | Mixer contactor |
| `Phase` | INT | 0=Idle, 1=Water, 2=Sugar, 3=Mix, 4=Drain |

## Test cases

See `tests/cases.json`. Submit as `solution.st`.

## Hint

Look at Lab 03 for the phase-machine pattern. This is the same pattern with more steps.
