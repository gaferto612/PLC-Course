# Pre-Assessment

20 questions. Don't look anything up. Score yourself honestly.

Answers at the bottom.

---

## Section A — Architecture & I/O (5 questions)

1. Name the four phases of a PLC scan cycle, in order.

2. What is the difference between a sourcing input and a sinking input?

3. Give one example of a discrete sensor and one example of an analog sensor.

4. What signal range is most common for industrial 2-wire analog transmitters: 0–5 V, 4–20 mA, or 0–24 VDC?

5. What does the PLC do during the "housekeeping" phase of the scan?

## Section B — Numbers & Logic (4 questions)

6. Convert the decimal number 173 to binary.

7. Convert the hex number `2F` to decimal.

8. What does BCD stand for, and where would you typically encounter it?

9. In Boolean algebra, what is `A AND (NOT A)` always equal to?

## Section C — Ladder & IEC 61131-3 (5 questions)

10. In ladder logic, what does a normally-closed contact `─┤/├─` do?

11. Two contacts in series represent which logical operation?

12. Name the five languages defined by IEC 61131-3.

13. Which of those five is best suited for batch sequence control?

14. What is "double-coiling" and why is it considered bad practice?

## Section D — Timers, Counters, Safety (6 questions)

15. What does TON stand for, and how does it differ from TOF?

16. A counter has a preset of 10 and an accumulator of 7. When does its done bit go high?

17. What is a retentive timer?

18. What is the purpose of an emergency stop relay (safety relay)?

19. Name one common cause of intermittent PLC bugs that's tied to scan time.

20. What is the difference between a Category 0 and a Category 1 stop?

---

## Scoring

Give yourself 1 point per question. Half-credit is fine for partial answers.

---

## Answer Key

<details>
<summary>Click to reveal</summary>

1. Read inputs → Execute program → Update outputs → Housekeeping
2. Sourcing supplies current to the load (PNP); sinking sinks current from the load (NPN)
3. Discrete: limit switch, push button, photoelectric. Analog: thermocouple, RTD, pressure transducer
4. 4–20 mA
5. Diagnostics, communications, watchdog reset, housekeeping
6. 10101101
7. 47
8. Binary-Coded Decimal — thumbwheel switches, 7-segment displays
9. 0 (always false — the law of contradiction)
10. Conducts (passes power flow) when its associated bit is 0
11. AND
12. Ladder Diagram (LD), Function Block Diagram (FBD), Instruction List (IL), Structured Text (ST), Sequential Function Chart (SFC)
13. SFC (Sequential Function Chart)
14. Writing to the same output coil from two different rungs — the last rung wins, making behavior depend on rung order
15. TON = on-delay timer (delays activation); TOF = off-delay timer (delays deactivation)
16. When the accumulator reaches the preset (≥10), not at 7
17. A timer that retains its accumulator value when disabled, only resetting on an explicit RES instruction
18. To monitor the emergency stop circuit and reliably de-energize machine power even under fault conditions
19. Fast inputs missed because pulse width is shorter than scan time; race conditions between rungs; latch traps
20. Cat 0 = immediate removal of power. Cat 1 = controlled stop, then power removal

</details>
