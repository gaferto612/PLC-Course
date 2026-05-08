# Lab 06 — Emergency Stop with Safety Relay (Cat 1 Stop)

> **Sprint:** 6 — Design & Safety
> **Time:** ~1 hour

---

## 🎯 Brief

Implement the PLC-side logic for a Category 1 controlled stop. Real safety logic lives in a dedicated safety relay or safety PLC — but the standard PLC needs to react correctly when E-stop is pressed:

1. Issue controlled-stop command to the drive
2. After `T_Decel_Done` (deceleration timer), allow safety relay to remove power
3. Refuse to restart until: E-stop reset AND `Reset` button pressed AND drive at zero speed

## 📋 I/O

| Tag | Type | Description |
|-----|------|-------------|
| `EStop_OK` | BOOL | Dual-channel E-stop says OK (both channels true) |
| `Reset` | BOOL | Manual reset button |
| `Start` | BOOL | Start request |
| `Drive_AtZero` | BOOL | Drive feedback: speed = 0 |
| `T_Decel_Done` | BOOL | Deceleration timer elapsed |
| `Drive_Run_Cmd` | BOOL | Output: drive run command |
| `Drive_Stop_Cmd` | BOOL | Output: controlled stop request |
| `Power_Permit` | BOOL | Output to safety relay: OK to keep contactor energized |
| `Ready` | BOOL | System ready (idle, awaiting start) |
| `State` | INT | 0=Faulted, 1=Ready, 2=Running, 3=Stopping |

## 🚦 Transitions

- 0 → 1: EStop_OK AND Reset AND Drive_AtZero
- 1 → 2: Start AND EStop_OK
- 2 → 3: NOT EStop_OK
- 3 → 0: T_Decel_Done OR Drive_AtZero
- Any → 0: NOT EStop_OK in states other than 2 and 3 (already handled)

## 🛡️ Output Rules

- `Drive_Run_Cmd` = (State = 2)
- `Drive_Stop_Cmd` = (State = 3)
- `Power_Permit` = (State = 1) OR (State = 2) OR (State = 3) — power kept on during deceleration
- `Ready` = (State = 1)
