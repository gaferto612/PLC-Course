# Lab 01 — Traffic Light Controller

> **Sprint:** 1 — Architecture & I/O (with timer concepts previewed)
> **Languages allowed:** ST or LD (this auto-grader checks ST)
> **Time:** ~90 minutes

---

## 🎯 Brief

Implement a basic traffic light controller for a single intersection (north-south and east-west). When the START button is pressed, the system runs through the standard sequence. STOP returns it to all-red.

For Sprint 1 we keep this simple — full timer-driven sequencing comes back in Sprint 5. Here you'll handle the **state transitions only**, given pre-computed timer outputs.

## 📋 I/O List

### Inputs

| Tag | Type | Description |
|-----|------|-------------|
| `Start` | BOOL | Start button (pulse) |
| `Stop` | BOOL | Stop button (pulse) |
| `T_Green_Done` | BOOL | True when the green-phase timer has elapsed |
| `T_Yellow_Done` | BOOL | True when the yellow-phase timer has elapsed |

### Outputs

| Tag | Type | Description |
|-----|------|-------------|
| `Sequence_Active` | BOOL | True between Start and Stop |
| `RedNS` | BOOL | North-south red lamp |
| `YellowNS` | BOOL | North-south yellow lamp |
| `GreenNS` | BOOL | North-south green lamp |
| `RedEW` | BOOL | East-west red lamp |
| `YellowEW` | BOOL | East-west yellow lamp |
| `GreenEW` | BOOL | East-west green lamp |
| `Phase` | INT | Current phase (0–4) |

### State variables (you'll need these)

| Tag | Type | Description |
|-----|------|-------------|
| `Phase` | INT | 0=Stopped, 1=NS_Green, 2=NS_Yellow, 3=EW_Green, 4=EW_Yellow |

---

## 📐 Sequence

```
Phase 0: STOPPED      All red, sequence inactive
Phase 1: NS_GREEN     NS green, EW red             (until T_Green_Done)
Phase 2: NS_YELLOW    NS yellow, EW red            (until T_Yellow_Done)
Phase 3: EW_GREEN     NS red, EW green             (until T_Green_Done)
Phase 4: EW_YELLOW    NS red, EW yellow            (until T_Yellow_Done)
        → back to Phase 1
```

### Transitions

- **Phase 0 → 1:** Start pressed
- **Phase 1 → 2:** T_Green_Done
- **Phase 2 → 3:** T_Yellow_Done
- **Phase 3 → 4:** T_Green_Done
- **Phase 4 → 1:** T_Yellow_Done
- **Any phase → 0:** Stop pressed

---

## ✅ Your Task

Open [`solution-template.st`](solution-template.st), implement the logic, save as `solution.st`, and submit a PR.

The auto-grader will run your solution against `tests/cases.json` and post a Markdown report on your PR.

---

## 💡 Hints

- The grader runs your code **once per test scan**. You don't need to write a real-time loop — just respond to the inputs as they're presented.
- Phase is an INT. Use `IF...ELSIF` or `CASE` to set the lamp outputs from it.
- Don't double-coil the lamps — set them once per scan based on Phase.
