# Orientation Cheat Sheet

A one-page map of what you're about to learn.

## The Six Pillars

| Pillar | What it answers |
|--------|-----------------|
| Architecture | What is a PLC actually made of? |
| I/O | How does the program touch the physical world? |
| Numbers | How does the PLC represent data? |
| Logic Languages | How do I tell the PLC what to do? |
| Stateful Building Blocks | How does the program remember and count? |
| Design & Safety | How do I make my code trustworthy? |

## Mental Model

A PLC is a **deterministic loop** that:

1. Takes a snapshot of all inputs
2. Runs your program top-to-bottom against that snapshot
3. Writes all outputs in one batch
4. Does maintenance and starts over

That's it. Everything else is a refinement of that loop.

## What Bolton's Book Is (and Isn't)

✅ A vendor-agnostic introduction tied to the IEC 61131-3 standard
✅ Strong on Boolean logic, ladder, timers, counters, basic safety
✅ Examples drawn from Siemens, Mitsubishi, Allen-Bradley, Telemecanique

❌ Not a deep dive on any one platform's tooling
❌ Not a reference for advanced motion control or modern HMI design
❌ Not a substitute for hands-on time with real hardware

This course bridges the third gap with simulators and labs.
