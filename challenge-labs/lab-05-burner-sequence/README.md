# Lab 05 — Boiler Burner Start-Up Sequence

> **Sprint:** 6 — Design & Safety (preview of Capstone)
> **Time:** ~2 hours
>
> 🔗 **This lab is a stepping stone to the Capstone.** It implements a simplified version of the burner start-up. The Capstone adds full safety logic, FMEA, and documentation.

---

## 🎯 Brief

Implement a simplified burner start-up sequence:

1. **STANDBY** — Idle, all closed
2. **PURGE** — Run fan with `T_Purge_Done` gating (typically 30 s in real life)
3. **PILOT** — Open pilot valve, energize igniter, wait for `Flame_OK`. If `T_TFI_Done` (trial-for-ignition timeout) elapses without flame, lock out.
4. **MAIN** — Open main gas valve. Igniter off. Stable run until Stop.
5. **POST_PURGE** — Close gas, fan runs for `T_PostPurge_Done`
6. **LOCKOUT** — Manual reset required

## 📋 I/O

| Tag | Type | Description |
|-----|------|-------------|
| `Start` / `Stop` / `Reset` | BOOL | Operator controls |
| `EStop` | BOOL | E-stop (NC, true when OK) |
| `Flame_OK` | BOOL | Flame detected |
| `T_Purge_Done` | BOOL | Pre-purge timer elapsed |
| `T_TFI_Done` | BOOL | Trial-for-ignition timer elapsed |
| `T_PostPurge_Done` | BOOL | Post-purge timer elapsed |
| `Y_Fan` / `Y_Pilot` / `Y_Main` / `Y_Igniter` | BOOL | Outputs |
| `Alarm` | BOOL | Lockout alarm |
| `Phase` | INT | 0=Standby, 1=Purge, 2=Pilot, 3=Main, 4=PostPurge, 5=Lockout |

## 🚦 Transitions

- 0 → 1: Start AND EStop
- 1 → 2: T_Purge_Done
- 2 → 3: Flame_OK
- 2 → 5: T_TFI_Done AND NOT Flame_OK (LOCKOUT — no flame in time)
- 3 → 5: NOT Flame_OK (flame loss during run = lockout)
- 3 → 4: Stop
- 4 → 0: T_PostPurge_Done
- 5 → 0: Reset (only path out of lockout)
- Any active phase → 5: NOT EStop (E-stop forces lockout, not idle)

## 🛡️ Safety Note

In real burner management systems, lockout is implemented in hardware and certified safety-rated logic — not in standard PLC code like this. This lab is for understanding the sequence; do not deploy this to a real burner.
