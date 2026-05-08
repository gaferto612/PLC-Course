# Glossary

A working glossary for PLC-FastTrack. Add terms as you encounter them in Bolton.

## A

**Accumulator (ACC)** — The current count or elapsed-time value of a timer or counter.

**Actuator** — A device that converts an electrical signal into physical action: valve, contactor, motor starter.

**Address** — The location of an I/O point or memory bit. Vendor-specific notation (e.g., `I0.0`, `M100`, `B3:0/0`).

**Analog I/O** — Continuous-value signals, typically scaled from 4–20 mA or 0–10 V to engineering units.

**AWL** — *Anweisungsliste* — Siemens' name for Instruction List (IL).

## B

**BCD (Binary-Coded Decimal)** — Each decimal digit represented by 4 bits separately. Used by thumbwheel switches and 7-segment displays.

**Bit** — Smallest unit of memory; 0 or 1.

**Boolean** — Data type with two values, TRUE and FALSE.

## C

**Cat 0/1/2 Stop** — Stop categories defined in IEC 60204-1: Cat 0 = immediate power removal; Cat 1 = controlled stop then power removal; Cat 2 = controlled stop, power retained.

**Coil** — Output element in a ladder rung, drawn as `─( )─`.

**Contact** — Input element in a ladder rung; NO `─┤ ├─` or NC `─┤/├─`.

**Contactor** — Electromagnetic switch for switching motor power.

**CPU** — Central Processing Unit — the microprocessor that executes the program.

**CTU / CTD / CTUD** — Count-up, count-down, and bidirectional counters.

## D

**DCS** — Distributed Control System; alternative to PLC for large process plants.

**Discrete I/O** — On/off (binary) signals — limit switches, contactors.

**Double-coiling** — Bug where the same output is written from two different rungs. Last rung wins.

## E

**E-stop** — Emergency stop. Hardwired safety circuit, dual-channel for higher integrity.

**Edge detection** — Logic that detects rising (false→true) or falling (true→false) transitions.

## F

**FBD** — Function Block Diagram; one of the IEC 61131-3 languages.

**FMEA** — Failure Modes and Effects Analysis; systematic technique for finding failure paths.

**Force** — Override an input or output during commissioning. Dangerous if forgotten.

## G

**GRAPH** — Siemens name for SFC.

## H

**HMI** — Human-Machine Interface; the operator-facing screen.

## I

**IEC 61131-3** — International standard for PLC programming languages.

**IL** — Instruction List; assembly-like IEC 61131-3 language. Deprecated in 2013 edition.

**Image table (input/output)** — RAM copy of physical I/O states updated each scan.

**Internal relay** — Software-only memory bit; no physical existence.

## K

**KOP** — *Kontaktplan* — Siemens name for Ladder Diagram.

## L

**Latch** — Logic that holds a state on after the trigger goes away. Seal-in latch and SR latch are the two common patterns.

**LD** — Ladder Diagram; one of the IEC 61131-3 languages.

## M

**Mass I/O copy** — Strategy of reading all inputs at scan start and writing all outputs at scan end. Most common.

## N

**NC / NO** — Normally Closed / Normally Open. Refers to the rest state of a contact.

## O

**One-shot** — Logic that produces a single-scan pulse on a rising or falling edge.

## P

**PLC** — Programmable Logic Controller.

**PNP / NPN** — Sourcing / sinking transistor types — describes which side of the load the sensor switches.

**POU (Program Organization Unit)** — IEC 61131-3 term for a program, function block, or function.

**Preset (PT, PV)** — The target value of a timer (PT = preset time) or counter (PV = preset value).

## R

**Retentive** — A timer or coil that retains its value when disabled, only reset on explicit RES.

**RPN (Risk Priority Number)** — In FMEA, Severity × Likelihood × Detectability.

**Rung** — A horizontal line in a ladder diagram representing one logical statement.

## S

**Safety PLC** — Certified PLC for safety-related logic. Higher integrity than standard PLCs.

**Scan cycle** — The four-phase loop the PLC executes continuously.

**Scan time** — Time to complete one scan cycle.

**SCL** — *Structured Control Language* — Siemens name for Structured Text.

**Sensor** — Device that converts a physical quantity into an electrical signal.

**SFC** — Sequential Function Chart; one of the IEC 61131-3 languages.

**Shift register** — Memory structure where bits move along on each shift signal. Used for tracking parts on a conveyor.

**SIL** — Safety Integrity Level (1–4) defined in IEC 61508.

**ST** — Structured Text; Pascal-like IEC 61131-3 language.

## T

**TON / TOF / TP** — On-delay, off-delay, and pulse timer types.

**Two's complement** — Standard representation for signed integers in PLCs.

## V

**VFD** — Variable Frequency Drive; for variable-speed motor control.

## W

**Watchdog timer** — Hardware timer that faults the PLC if the program freezes.

**Word** — 16-bit value. Double word = 32 bit.
