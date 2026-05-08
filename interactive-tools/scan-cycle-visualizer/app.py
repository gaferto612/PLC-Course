"""
Scan Cycle Visualizer
─────────────────────
An interactive Streamlit demo of the PLC scan cycle. Lets the learner play with
scan time vs. input pulse width and *see* why fast events get missed.

Run locally:
    streamlit run app.py

Deploy on Streamlit Community Cloud — point it at this file.
"""

import time

import streamlit as st
import numpy as np
import pandas as pd
import altair as alt


st.set_page_config(page_title="PLC Scan Cycle Visualizer", layout="wide")

st.title("🎛️ PLC Scan Cycle Visualizer")
st.caption(
    "Sprint 1 companion tool — based on Bolton, *Programmable Logic Controllers*, Ch. 1 & 4."
)

st.markdown(
    """
    The PLC takes a snapshot of inputs once per scan, executes the program against
    that snapshot, then writes outputs in one batch. **An input pulse shorter than
    the scan time can be invisible.** Use the sliders to see this in action.
    """
)

# ─── Controls ────────────────────────────────────────────────────────────────
col_a, col_b, col_c = st.columns(3)
with col_a:
    scan_ms = st.slider("Scan time (ms)", 1, 200, 50, 1)
with col_b:
    pulse_ms = st.slider("Input pulse width (ms)", 1, 200, 20, 1)
with col_c:
    pulse_start_ms = st.slider("Pulse start time (ms)", 0, 500, 75, 1)

window_ms = 600
latched = st.checkbox("Use a latching circuit (seal-in)", value=False)

# ─── Simulate ────────────────────────────────────────────────────────────────
t = np.arange(0, window_ms, 1)  # 1 ms resolution

# Physical input — square pulse
phys = ((t >= pulse_start_ms) & (t < pulse_start_ms + pulse_ms)).astype(int)

# PLC samples once per scan, at the start of each scan
sampled = np.zeros_like(phys)
output = np.zeros_like(phys)

input_image = 0
output_image = 0
last_sample_t = 0

for i in range(len(t)):
    # At each scan boundary, sample the input
    if i % scan_ms == 0:
        input_image = phys[i]
        last_sample_t = i
        # Execute "program" — copy input to output, with optional latch
        if latched:
            if input_image == 1:
                output_image = 1
        else:
            output_image = input_image
    sampled[i] = input_image
    output[i] = output_image

df = pd.DataFrame(
    {
        "Time (ms)": np.tile(t, 3),
        "Signal": (
            ["Physical input"] * len(t)
            + ["PLC input image"] * len(t)
            + ["PLC output"] * len(t)
        ),
        "Value": np.concatenate([phys, sampled, output]),
    }
)

# Offset so the three traces don't overlap
offsets = {"Physical input": 0, "PLC input image": 1.5, "PLC output": 3.0}
df["Display"] = df["Value"] + df["Signal"].map(offsets)

# ─── Plot ────────────────────────────────────────────────────────────────────
chart = (
    alt.Chart(df)
    .mark_line(interpolate="step-after", strokeWidth=2.5)
    .encode(
        x=alt.X("Time (ms):Q"),
        y=alt.Y(
            "Display:Q",
            axis=alt.Axis(
                values=[0, 1, 1.5, 2.5, 3.0, 4.0],
                labelExpr=(
                    "datum.value == 0 ? 'Phys 0' : "
                    "datum.value == 1 ? 'Phys 1' : "
                    "datum.value == 1.5 ? 'Img 0' : "
                    "datum.value == 2.5 ? 'Img 1' : "
                    "datum.value == 3.0 ? 'Out 0' : "
                    "datum.value == 4.0 ? 'Out 1' : ''"
                ),
            ),
            title=None,
        ),
        color=alt.Color(
            "Signal:N",
            scale=alt.Scale(
                domain=["Physical input", "PLC input image", "PLC output"],
                range=["#3b82f6", "#f59e0b", "#22c55e"],
            ),
        ),
    )
    .properties(height=320)
)

# Add scan boundaries
scan_marks = pd.DataFrame({"x": np.arange(0, window_ms, scan_ms)})
boundaries = (
    alt.Chart(scan_marks)
    .mark_rule(color="#94a3b8", strokeDash=[4, 4])
    .encode(x="x:Q")
)

st.altair_chart(boundaries + chart, use_container_width=True)

# ─── Diagnostic ──────────────────────────────────────────────────────────────
caught = bool((sampled == 1).any())
phys_high_count = int(phys.sum())
img_high_count = int(sampled.sum())

st.subheader("📊 What happened?")

c1, c2, c3 = st.columns(3)
c1.metric("Pulse vs. scan", f"{pulse_ms}/{scan_ms} ms", f"{pulse_ms/scan_ms:.1f}× ratio")
c2.metric("Physical pulse duration", f"{phys_high_count} ms")
c3.metric("PLC saw it as high for", f"{img_high_count} ms")

if caught:
    st.success(
        f"✅ The PLC caught the input. The input image was high for "
        f"{img_high_count} ms (rounded up to a multiple of the scan time)."
    )
else:
    st.error(
        f"❌ The PLC **missed the pulse entirely.** "
        f"The {pulse_ms} ms pulse fell between two scan-cycle samples that are "
        f"{scan_ms} ms apart."
    )

if latched and caught:
    st.info(
        "🔒 With the latching circuit, the output stays on after the input drops — "
        "this is how you keep fast pulses from being lost downstream."
    )

# ─── Teaching notes ──────────────────────────────────────────────────────────
with st.expander("💡 Try these scenarios"):
    st.markdown(
        """
        1. **Slow scan, short pulse** — set scan = 100 ms, pulse = 10 ms. Toggle the pulse start
           time and watch the pulse get caught or missed depending on timing.
        2. **Fast scan, same pulse** — drop scan to 5 ms with the same 10 ms pulse. Now it's
           always caught.
        3. **Latching rescue** — turn on the latch with a slow scan and shifted pulse. Even
           if the pulse is short, the output stays on.
        4. **Worst case** — the maximum delay between an input change and the corresponding
           output change is *two scan times* in the worst case.
        """
    )

st.caption(
    "Built for [PLC-FastTrack](https://github.com/your-username/plc-fasttrack) · "
    "Sprint 1 — Architecture & I/O"
)
