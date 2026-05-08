# Sprint 2 Cheat Sheet — Digital Foundations

## 🔢 The Four Number Systems

| System | Base | Digits | Where it shows up |
|--------|------|--------|-------------------|
| Denary (decimal) | 10 | 0–9 | Human-readable values |
| Binary | 2 | 0–1 | Native to silicon, every bit in memory |
| Octal | 8 | 0–7 | Older Mitsubishi/Allen-Bradley I/O addresses |
| Hexadecimal | 16 | 0–9, A–F | Memory addresses, data words |
| BCD | special | 4 bits per decimal digit | Thumbwheel switches, 7-segment displays |

## ⚡ Quick Conversion Reference

```
Decimal  Binary    Octal  Hex   BCD (per digit)
   0     0000        0     0     0000
   1     0001        1     1     0001
   2     0010        2     2     0010
   ...
   9     1001        11    9     1001
  10     1010        12    A     0001 0000
  15     1111        17    F     0001 0101
  16    10000        20   10     0001 0110
 173    10101101    255   AD     0001 0111 0011
```

## 🧠 Mental Tricks

**Decimal → Binary:** repeatedly divide by 2, write remainders bottom-up.
**Binary → Hex:** group bits in 4s from the right, look up each nibble.
**Decimal → BCD:** convert each decimal digit to 4 bits separately. **173 ≠ 10101101 in BCD; it's 0001 0111 0011.**

## ➖ Negative Numbers (Two's Complement)

To represent `-5` in 8-bit two's complement:
1. Write +5 in binary: `0000 0101`
2. Invert all bits: `1111 1010`
3. Add 1: `1111 1011`

Range of 8-bit signed: –128 to +127.
Range of 16-bit signed: –32 768 to +32 767.

The MSB acts as a "sign bit" — 0 for positive, 1 for negative.

## 🧱 Word Sizes

| Name | Bits | Range (unsigned) |
|------|------|------------------|
| Bit | 1 | 0–1 |
| Nibble | 4 | 0–15 |
| Byte | 8 | 0–255 |
| Word | 16 | 0–65 535 |
| Double word | 32 | 0–4 294 967 295 |

## 🔌 I/O Addressing Across Vendors

A discrete input on terminal 0 of card 1:

| Vendor | Notation | Example |
|--------|----------|---------|
| Siemens (S7) | `Ix.y` | `I0.0`, `I1.3` |
| Allen-Bradley (Logix) | tag-based | `Local:1:I.Data.0` |
| Allen-Bradley (PLC-5/SLC) | `I:s/b` (octal!) | `I:1/0`, `I:1/17` (= bit 15 decimal) |
| Mitsubishi | `Xn` (octal!) | `X0`, `X10` (= 8 decimal) |

⚠️ **Octal trap:** in older Allen-Bradley and Mitsubishi, the bit number jumps from 7 to 10, NOT 7 to 8. `X10` is the 9th input, not the 11th.

## 🔄 I/O Update Strategies

| Strategy | How | Pros | Cons |
|----------|-----|------|------|
| Mass I/O copy | Read all inputs at scan start, write all outputs at scan end | Deterministic, simple | Slight delay on output |
| Continuous update | Inputs/outputs accessed directly during scan | Lower latency for specific signals | Less deterministic, can race |
| Immediate I/O | Special instructions to bypass image table mid-scan | Fastest reaction | Only for critical signals |

Most PLCs default to mass I/O copy; immediate I/O is reserved for safety-critical or fast-loop applications.
