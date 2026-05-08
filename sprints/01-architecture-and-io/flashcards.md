# Sprint 1 Flashcards

Format: Obsidian Spaced-Repetition plugin. Question on top, `?` separator, answer below.

Tags: `#plc-fasttrack #sprint-1 #architecture-and-io`

---

What are the four phases of a PLC scan cycle, in order?
?
1. Read inputs (input image table is updated from physical inputs)
2. Execute program (rung-by-rung evaluation against the input image)
3. Update outputs (output image table written to physical outputs)
4. Housekeeping (diagnostics, comms, watchdog reset)
<!--SR:!2026-05-15,7,250-->

---

What are the five core hardware blocks of a PLC?
?
Power supply, CPU + memory, I/O modules, programming device, field devices (sensors/actuators).
<!--SR:!2026-05-16,7,250-->

---

What is the difference between sourcing (PNP) and sinking (NPN) inputs?
?
Sourcing inputs receive current FROM the sensor (sensor supplies +24 V when active). Sinking inputs supply current TO the sensor (sensor pulls the line to 0 V when active). They cannot be mixed on the same input card without damage or inverted logic.
<!--SR:!2026-05-17,7,250-->

---

What does a 4–20 mA signal represent and why is it preferred over 0–10 V for industrial transmitters?
?
A continuous analog value where 4 mA = 0% and 20 mA = 100%. The "live zero" at 4 mA lets the system detect a broken wire (0 mA = fault). Current loops are also far less susceptible to noise and voltage drop over long cable runs than voltage signals.
<!--SR:!2026-05-15,5,250-->

---

Why can a 5 ms input pulse be invisible to a PLC with a 50 ms scan time?
?
Because the PLC only samples physical inputs once per scan, during the "Read Inputs" phase. If the pulse rises and falls entirely between two read phases, the input image never sees it. Solutions: faster scan, latching circuit, or a dedicated high-speed input module.
<!--SR:!2026-05-18,7,250-->

---

Give one discrete sensor and one analog sensor commonly found in industrial applications.
?
Discrete: limit switch, push button, inductive proximity sensor, photoelectric sensor.
Analog: thermocouple, RTD, pressure transducer, ultrasonic level sensor.
<!--SR:!2026-05-15,4,250-->

---

What is the difference between an inductive and a capacitive proximity sensor?
?
Inductive sensors detect metal targets only, using a magnetic field. Capacitive sensors detect almost any material including liquids, plastics, and solids, using changes in capacitance. Inductive sensors are more selective and immune to environmental contamination; capacitive are more versatile.
<!--SR:!2026-05-16,5,250-->

---

What is the difference between a relay output and a transistor output module?
?
Relay outputs use mechanical contacts — flexible (AC or DC, wide voltage range), but slow (~10 ms switching), and wear out. Transistor outputs are solid-state — DC only, fast (~microseconds), high cycle life, but more sensitive to surges and limited current.
<!--SR:!2026-05-17,5,250-->

---

What is "scan time" and why does it matter for control engineers?
?
Scan time is the time it takes to complete one full PLC loop (read inputs → execute → update outputs → housekeeping). It determines the responsiveness of the system, the minimum detectable input pulse width, and the worst-case delay between an input change and an output reaction. Typical values are 1–50 ms.
<!--SR:!2026-05-19,7,250-->

---

Where in the scan cycle does the PLC actually communicate with the programming device or other PLCs over a network?
?
During the housekeeping phase (sometimes called overhead or service phase) at the end of each scan. Communications run between scans, not during program execution, so heavy comms traffic can extend the overall scan time.
<!--SR:!2026-05-15,4,250-->
