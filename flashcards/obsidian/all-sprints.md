# PLC-FastTrack Flashcard Bundle (Obsidian Spaced-Repetition format)

A consolidated set of flashcards covering all six sprints. Import into Obsidian with the [Spaced Repetition plugin](https://github.com/st3v3nmw/obsidian-spaced-repetition), or copy the Q/A pairs into Anki.

Tags: `#plc-fasttrack`. Per-sprint tag e.g. `#sprint-1`.

---

## Sprint 1 — Architecture & I/O

What are the four phases of a PLC scan cycle, in order?
?
1. Read inputs (input image table is updated)
2. Execute program (rung-by-rung evaluation)
3. Update outputs (output image table written to physical outputs)
4. Housekeeping (diagnostics, comms, watchdog reset)

What are the five core hardware blocks of a PLC?
?
Power supply, CPU + memory, I/O modules, programming device, field devices.

What is the difference between sourcing (PNP) and sinking (NPN) inputs?
?
Sourcing supplies current to the input from the sensor (sensor pulls high when active). Sinking sinks current to the sensor (sensor pulls low when active). They cannot be mixed on the same input card.

Why is a 4-20 mA signal preferred over 0-10 V for industrial transmitters?
?
Live-zero (4 mA = 0%, so 0 mA detects a broken wire), better noise immunity, and minimal voltage drop over long cable runs.

Why can a 5 ms input pulse be invisible to a PLC with a 50 ms scan time?
?
The PLC samples physical inputs once per scan, during the Read Inputs phase. If the pulse rises and falls between two samples, the input image never sees it.

---

## Sprint 2 — Digital Foundations

Convert 173 decimal to binary.
?
10101101

Convert hex 2F to decimal.
?
47

What does BCD stand for and where do you encounter it?
?
Binary-Coded Decimal — each decimal digit in 4 bits separately. Common with thumbwheel switches, 7-segment displays, and some operator interface devices.

How do you represent -5 in 8-bit two's complement?
?
1. Write +5: 00000101
2. Invert all bits: 11111010
3. Add 1: 11111011

Why is the octal addressing on older Mitsubishi/Allen-Bradley a trap?
?
Bit numbers jump from 7 to 10 (octal), not 7 to 8. So X10 is the 9th input, not the 11th.

---

## Sprint 3 — Ladder & FBD

What does a normally-closed contact `-|/|-` do?
?
Conducts (passes power flow) when its associated bit is 0 (false).

Two contacts in series represent which logical operation?
?
AND.

Two contacts in parallel represent which logical operation?
?
OR.

What is double-coiling and why is it bad?
?
Writing the same output coil from two different rungs. The PLC scans top-to-bottom, so the last rung wins — making behavior depend on rung order rather than logic. Brittle and hard to debug.

Why must a STOP button typically be wired with NC contacts?
?
So that a broken wire de-energizes the input — failing safe. With NO contacts, a broken wire would prevent stopping the machine.

What is a seal-in latch?
?
A rung pattern where an output's own contact is paralleled with the start condition, "sealing" the output on after the start condition releases. Most common motor start/stop pattern.

---

## Sprint 4 — IL, ST, SFC

What does IEC 61131-3 standardize?
?
The five PLC programming languages (LD, FBD, IL, ST, SFC), data types, program organization units (POUs: programs, function blocks, functions), and configuration elements.

Which IEC 61131-3 language is best for sequence control like batch processes?
?
SFC — Sequential Function Chart.

Which IEC 61131-3 language is best for math, loops, and complex conditions?
?
ST — Structured Text.

Which IEC 61131-3 language is being deprecated?
?
IL — Instruction List. Edition 3 of IEC 61131-3 (2013) deprecates it in favor of ST.

What is the Siemens equivalent of Structured Text?
?
SCL — Structured Control Language.

What is the Siemens equivalent of SFC?
?
GRAPH.

---

## Sprint 5 — Timers, Counters, Registers

What's the difference between a TON and a TOF?
?
TON (on-delay): accumulator counts up while EN is true; Q goes high when ACC ≥ PT. TOF (off-delay): Q stays high while EN is true; when EN goes false, the timer counts up — Q drops when ACC ≥ PT.

What is a TP (pulse) timer?
?
On rising edge of EN, Q goes high for exactly PT seconds and then falls, regardless of EN. Useful for clean fixed-width output pulses.

What is a retentive timer?
?
A timer that holds its accumulator value when EN goes false. Only a separate RES instruction resets it. Used for tracking total runtime across power cycles.

How does a CTU counter work?
?
Counts rising edges of CU input. ACC increments each rising edge. Q goes high when ACC ≥ PV. Reset via RES.

What is a shift register and where is it useful?
?
A memory structure where bits move along on each shift signal. Common use: tracking parts on a conveyor — set bit 0 when a part is detected, shift on each conveyor index pulse, fire reject solenoid when the bit reaches the right slot.

What hazard does a JMP instruction skipping past coils create?
?
Skipped coils retain their previous state. This is the "stuck output after fault" bug — outputs that should have de-energized stay on because the rung wasn't evaluated.

---

## Sprint 6 — Design & Safety

What is the difference between a Cat 0 and a Cat 1 stop?
?
Cat 0 = immediate removal of power (uncontrolled stop). Cat 1 = controlled stop, then power removal. Cat 1 is required for hazardous motion that needs deceleration (large motors, presses).

What is the difference between a safety relay and a safety PLC?
?
A safety relay is a hardwired device with internal redundancy — fixed function, very high reliability. A safety PLC is programmable with certified safety logic and dual-channel hardware — flexible for complex multi-zone systems. Both are certified to safety standards; standard PLCs are not.

What does FMEA stand for and what does the RPN value mean?
?
Failure Modes and Effects Analysis. RPN = Risk Priority Number = Severity × Likelihood × Detectability. Higher RPN means more important to mitigate.

What is the watchdog timer's purpose?
?
Hardware timer that the program must "pet" (reset) periodically. If the program freezes or hangs, the watchdog times out and faults the CPU, putting outputs in safe state.

Why are forces dangerous when left on a running system?
?
A force overrides the actual program logic, so the system behaves differently from what the code says. Maintenance personnel investigating a problem may not know forces are active and could be confused or harmed by unexpected behavior.

What does ISO 13849 measure for safety functions?
?
Performance Levels (PL a through e), based on category, MTTFd, DC, and CCF. PL e is the highest integrity.

Why is the trial-for-ignition timeout in burner control safety-critical?
?
Multiple ignition attempts with unburned gas in the firebox cause explosions. A strict timeout (typically 5–10 seconds) followed by lockout prevents this.
