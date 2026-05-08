"""
Number Base Converter
─────────────────────
Sprint 2 companion. Converts between denary, binary, octal, hex, and BCD,
with bit-pattern visualization.

Run locally:
    python app.py
"""

import gradio as gr


def to_bcd(n: int, digits: int = 4) -> str:
    """Convert a non-negative integer to packed BCD string of given digit count."""
    s = str(n).rjust(digits, "0")[-digits:]
    return " ".join(format(int(d), "04b") for d in s)


def bit_blocks(n: int, width: int = 16) -> tuple[str, str]:
    """Render an integer as a row of 0/1 blocks plus an aligned index ruler.

    Each bit takes the same number of columns as its index label (max two
    digits), so the ruler underneath always sits below the bit it refers to.
    """
    bits = format(n & ((1 << width) - 1), f"0{width}b")
    cell = max(2, len(str(width - 1))) if width > 0 else 1
    glyphs = [("█" if b == "1" else "·").center(cell) for b in bits]
    indices = [str(width - 1 - i).rjust(cell) for i in range(width)]
    return " ".join(glyphs), " ".join(indices)


def convert(value: str, base: str):
    base_map = {"Denary (decimal)": 10, "Binary": 2, "Octal": 8, "Hexadecimal": 16}
    try:
        n = int(value.strip().replace(" ", ""), base_map[base])
    except (ValueError, KeyError):
        return ("⚠️ Invalid input for base", "", "", "", "", "")

    if n < 0:
        return ("⚠️ Use unsigned positive values for now", "", "", "", "", "")
    if n >= 2**32:
        return ("⚠️ Out of 32-bit range", "", "", "", "", "")

    width = 8 if n < 256 else (16 if n < 65536 else 32)
    bits = format(n, f"0{width}b")
    binary_str = " ".join(bits[i : i + 4] for i in range(0, len(bits), 4))
    octal_str = format(n, "o")
    hex_str = format(n, "X")
    bcd_str = to_bcd(n, max(len(str(n)), 4))
    blocks, ruler = bit_blocks(n, width=width)

    return (
        str(n),
        binary_str,
        octal_str,
        hex_str,
        bcd_str,
        f"```\n{blocks}\n{ruler}\n```",
    )


with gr.Blocks(title="PLC-FastTrack — Number Base Converter") as demo:
    gr.Markdown(
        """
        # 🔢 Number Base Converter
        **Sprint 2 companion** — Bolton Ch. 3.
        Type a value, pick its base, and see all four representations plus the bit pattern.
        """
    )

    with gr.Row():
        value = gr.Textbox(label="Value", value="173", scale=2)
        base = gr.Dropdown(
            ["Denary (decimal)", "Binary", "Octal", "Hexadecimal"],
            value="Denary (decimal)",
            label="Input base",
            scale=1,
        )

    btn = gr.Button("Convert", variant="primary")

    with gr.Row():
        out_dec = gr.Textbox(label="Denary")
        out_bin = gr.Textbox(label="Binary (grouped in nibbles)")
    with gr.Row():
        out_oct = gr.Textbox(label="Octal")
        out_hex = gr.Textbox(label="Hexadecimal")
    out_bcd = gr.Textbox(label="BCD (4 bits per decimal digit)")
    gr.Markdown("**Bit pattern** *(MSB on the left)*")
    out_blocks = gr.Markdown()

    btn.click(
        convert,
        inputs=[value, base],
        outputs=[out_dec, out_bin, out_oct, out_hex, out_bcd, out_blocks],
    )

    gr.Markdown(
        """
        ### 💡 Try these
        - 173 in denary — what's it in hex?
        - `2F` in hex — note that BCD is **different** from binary
        - 100 in denary — its BCD is `0001 0000 0000`, not `1100100`
        - 255 — the all-ones byte; spot the pattern
        """
    )


if __name__ == "__main__":
    demo.launch()
