# Sprint 5 Cheat Sheet — Timers, Counters, Registers, Data

## ⏱️ Timer Family

| Timer | Behavior | When done bit (Q) goes high |
|-------|----------|-----------------------------|
| **TON** (on-delay) | Accumulator counts up while EN is true | When ACC ≥ PT (preset time) |
| **TOF** (off-delay) | Accumulator counts up while EN is **false** (after EN goes true→false) | While timing — drops when ACC ≥ PT |
| **TP** (pulse) | Fixed-duration pulse triggered by EN rising edge | For exactly PT seconds, regardless of EN |
| **Retentive (RTO)** | Holds ACC across EN drops, only resets on RES | When ACC ≥ PT (across multiple enables) |

### Timing diagram (TON)

```
EN    ────┐         ┌────────
          │         │
          └─────────┘
ACC   ────/┐         /┐──────
          /│         /│
PT  - - -/-│- - - -/-│- - -
        /  │       /  │
Q     ──────┐       ┌────────
            │       │
            └───────┘
              (high once ACC reaches PT)
```

## 🔢 Counter Family

| Counter | Increment trigger | Reset |
|---------|-------------------|-------|
| **CTU** | Rising edge of CU input | When RES is true |
| **CTD** | Rising edge of CD input | When LD (load preset) is true |
| **CTUD** | Up on CU↑, down on CD↑ | RES or LD |

**Done bit (Q):** high when ACC ≥ PV.

## 🚂 Shift Register (SHR / SHL)

Tracks bits moving through a sequence — perfect for parts on a conveyor.

```
Bit slot:    7  6  5  4  3  2  1  0
Initial:     0  0  0  0  0  0  0  0
After SHL:   0  0  0  0  0  0  0  ←IN
After SHL:   0  0  0  0  0  0  IN ←IN
...
```

Each shift, every bit moves one position; the new bit-in enters at one end, the old bit-out drops off the other.

**Use case:** photoelectric sensor at start of conveyor sets bit 0 when a part passes; each conveyor index pulse shifts the register; reject solenoid fires when the right slot reaches the inspection station.

## 🧠 Internal Relays (Memory Bits)

- Software-only flags — no physical wires
- Used for intermediate logic, status flags, one-shots
- Vendor names: M (Siemens), B3:0/0 (Allen-Bradley SLC), M (Mitsubishi)
- **Rule:** if you find yourself writing the same long Boolean expression in three rungs, store it in an internal relay and reference it.

## 🔁 Jumps, Calls, Subroutines

| Instruction | Effect |
|-------------|--------|
| `JMP label` | Skip to a label later in the program |
| `LBL label` | Marks the jump destination |
| `JSR routine` | Call a subroutine |
| `RET` | Return from subroutine |

**Hazard:** if a jump skips past a coil, that coil keeps its previous state. This is the classic "stuck output after fault" bug. Always put outputs *outside* of jumps unless you really know what you're doing.

## 📦 Data Handling Instructions

| Instruction | Purpose |
|-------------|---------|
| `MOV src, dst` | Copy value |
| `ADD a, b, dst` | Addition |
| `SUB a, b, dst` | Subtraction |
| `MUL`, `DIV`, `MOD` | Math |
| `EQ`, `NE`, `GT`, `LT`, `GE`, `LE` | Comparisons |
| `LIM lo, val, hi` | True if lo ≤ val ≤ hi |
| `BCD_TO_INT`, `INT_TO_BCD` | Conversions |
| `SCL` | Linear scaling (raw counts → engineering units) |

### Common scaling formula

For a 4–20 mA signal mapped to 0–100% in a 16-bit raw word (0–32767 counts for 4–20 mA on Siemens):

```
percent = (raw - raw_min) * (eng_max - eng_min) / (raw_max - raw_min) + eng_min
```

In ST:

```pascal
Percent := REAL_TO_INT((Raw - 0) * 100 / 32767);
```

## 🏗️ Common Patterns You'll Reuse

**One-shot rising edge (rising-edge detector):**

```pascal
Pulse := Input AND NOT Last_Input;
Last_Input := Input;
```

**Toggle (on/off button):**

```pascal
IF Button AND NOT Last_Button THEN
    Output := NOT Output;
END_IF;
Last_Button := Button;
```

**Watchdog timer:**

```pascal
Heartbeat_Timer(IN := NOT Heartbeat_Timer.Q, PT := T#1s);
IF Heartbeat_Timer.Q THEN
    Heartbeat := NOT Heartbeat;
END_IF;
```

## 🐛 Watch out for

1. **Timer never enables** because EN is always true on power-up — use a one-shot.
2. **Counter accumulator overflows** because RES is never asserted — schedule resets.
3. **Shift register skips a slot** because shift signal pulses faster than scan time — use a synchronized index pulse.
4. **MOV inside a jump skipped** — the destination keeps stale data.
