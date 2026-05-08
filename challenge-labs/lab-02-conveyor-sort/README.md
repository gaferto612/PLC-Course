# Lab 02 — Conveyor Sort by Height

> **Sprint:** 3 — Ladder & FBD (uses early shift register concept previewed)
> **Languages allowed:** ST or LD
> **Time:** ~90 minutes

---

## 🎯 Brief

A conveyor moves boxes past two photoelectric sensors. The lower sensor detects every box; the upper sensor only detects "tall" boxes. A reject solenoid 4 conveyor positions downstream pushes tall boxes off the line.

You need to:
1. Detect a box at the inspection point
2. Determine if it's tall (upper sensor active when lower also active)
3. Track which conveyor positions hold a tall box
4. Fire the reject solenoid for one scan when a tall box reaches the reject position

## 📋 I/O List

### Inputs

| Tag | Type | Description |
|-----|------|-------------|
| `Sensor_Low` | BOOL | Lower photo-eye (any box present) |
| `Sensor_High` | BOOL | Upper photo-eye (tall box present) |
| `Index_Pulse` | BOOL | Conveyor index (one pulse per position advance) |
| `EStop` | BOOL | Emergency stop (NC, fail-safe — true when OK) |

### Outputs

| Tag | Type | Description |
|-----|------|-------------|
| `Reject_Sol` | BOOL | Reject solenoid (pulse high for one scan when needed) |
| `Tall_Detected` | BOOL | Status — tall box detected at inspection point |

### Internal state

| Tag | Type | Description |
|-----|------|-------------|
| `Track_P0` | BOOL | Inspection position |
| `Track_P1` | BOOL | One position downstream |
| `Track_P2` | BOOL | Two positions downstream |
| `Track_P3` | BOOL | Three positions downstream |
| `Track_P4` | BOOL | Reject position |
| `Last_Index` | BOOL | For edge detection on Index_Pulse |

## 💡 Hints

- Use `Track_P0..P4` as a manual shift register — on the rising edge of `Index_Pulse`, shift the values along.
- `Tall_Detected` is true only when **both** sensors are active in the same scan.
- `Reject_Sol` should fire when `Track_P4` is true.
- `EStop` should clear all tracking when false.

Submit your solution as `solution.st`.
