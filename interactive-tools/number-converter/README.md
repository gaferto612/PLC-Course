# 🔢 Number Base Converter

A browser-based converter between denary, binary, octal, hexadecimal, and BCD,
with a click-to-toggle bit pattern. Open
[`index.html`](index.html) in any browser — no build, no install, no server.

The same tool is wired into the [live course
site](https://gaferto612.github.io/PLC-Course/interactive-tools/number-converter/index.html).

## What you get

- **Live conversions** — type a value, pick its base, see all four
  representations update instantly.
- **Toggle-able bit pattern** — click any bit to flip it; the value, the
  other bases and the BCD view all follow.
- **BCD breakdown** — each decimal digit gets its own nibble, so you can see
  why <code>100 dec → 0110 0100 binary</code> but <code>0001 0000 0000</code>
  in BCD.
- **Auto-sized bit width** — 8 bits for values under 256, 16 bits up to
  65 535, 32 bits beyond that.

## How it maps to Bolton

- **Sprint 2 (Digital Foundations)** — Bolton Ch. 3 covers binary, octal, hex,
  and BCD. This tool lets you stress-test the conversions until they're
  automatic.
- The "thumbwheel switch reads BCD" example in Ch. 3.4 becomes obvious once
  you see the per-digit nibbles light up.

## Try this

1. Type **173** and switch the input base from Denary to Hex — note that the
   *same digits* mean different numbers depending on base.
2. Type **2F** in hex and watch the binary view land on `0010 1111`. Compare
   that to the BCD view, which is invalid (F isn't a decimal digit, so BCD
   only renders the decimal value 47 → `0100 0111`).
3. Click bits in the bit-pattern panel to toggle them. Watch the decimal value
   change by powers of two — that's positional notation made tactile.

## Legacy Gradio app

`app.py` is the original Gradio version retained for offline / Python use.
The HTML version above is what the live course site links to.
