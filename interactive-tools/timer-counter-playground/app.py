"""
Timer / Counter Playground
──────────────────────────
Sprint 5 companion. Visualizes TON, TOF, TP, and CTU side-by-side
with adjustable presets and a configurable input pattern.
"""

import streamlit as st
import numpy as np
import pandas as pd
import altair as alt


st.set_page_config(page_title="Timer/Counter Playground", layout="wide")
st.title("⏱️ Timer / Counter Playground")
st.caption("Sprint 5 companion — Bolton Ch. 9 & 10")

# ─── Controls ────────────────────────────────────────────────────────────────
st.sidebar.header("⚙️ Settings")
sim_seconds = st.sidebar.slider("Simulation length (s)", 5, 60, 20)
preset_s = st.sidebar.slider("Timer preset PT (s)", 1, 20, 5)
counter_preset = st.sidebar.slider("Counter preset PV", 1, 20, 5)

st.sidebar.markdown("---")
st.sidebar.subheader("Input pattern")
pulse_width_s = st.sidebar.slider("Pulse width (s)", 1, 10, 3)
pulse_period_s = st.sidebar.slider("Pulse period (s)", 2, 20, 7)

# ─── Simulate ────────────────────────────────────────────────────────────────
dt = 0.1  # 100 ms resolution
t = np.arange(0, sim_seconds + dt, dt)

# Input pulse train
en = np.zeros_like(t)
for i, ti in enumerate(t):
    phase = ti % pulse_period_s
    en[i] = 1 if phase < pulse_width_s else 0

# TON: accumulator counts up while EN, resets when EN drops
ton_acc = np.zeros_like(t)
ton_q = np.zeros_like(t)
for i in range(1, len(t)):
    if en[i] == 1:
        ton_acc[i] = min(ton_acc[i - 1] + dt, preset_s)
    else:
        ton_acc[i] = 0
    ton_q[i] = 1 if ton_acc[i] >= preset_s else 0

# TOF: accumulator counts up after EN drops, Q stays high while timing
tof_acc = np.zeros_like(t)
tof_q = np.zeros_like(t)
for i in range(1, len(t)):
    if en[i] == 1:
        tof_acc[i] = 0
        tof_q[i] = 1
    else:
        if en[i - 1] == 1:  # falling edge — start timing
            tof_acc[i] = dt
        else:
            tof_acc[i] = min(tof_acc[i - 1] + dt, preset_s)
        tof_q[i] = 1 if tof_acc[i] < preset_s else 0

# TP: pulse of fixed duration on rising edge of EN
tp_acc = np.zeros_like(t)
tp_q = np.zeros_like(t)
tp_active = False
for i in range(1, len(t)):
    if en[i] == 1 and en[i - 1] == 0 and not tp_active:
        tp_active = True
        tp_acc[i] = dt
    elif tp_active:
        tp_acc[i] = tp_acc[i - 1] + dt
        if tp_acc[i] >= preset_s:
            tp_active = False
    tp_q[i] = 1 if tp_active else 0

# CTU: count rising edges
ctu_acc = np.zeros_like(t, dtype=int)
ctu_q = np.zeros_like(t)
for i in range(1, len(t)):
    if en[i] == 1 and en[i - 1] == 0:
        ctu_acc[i] = ctu_acc[i - 1] + 1
    else:
        ctu_acc[i] = ctu_acc[i - 1]
    ctu_q[i] = 1 if ctu_acc[i] >= counter_preset else 0

# ─── Plot ────────────────────────────────────────────────────────────────────
def gantt(df_signal, color):
    return (
        alt.Chart(df_signal)
        .mark_line(interpolate="step-after", strokeWidth=2.5, color=color)
        .encode(x="t:Q", y=alt.Y("v:Q", scale=alt.Scale(domain=[-0.1, 1.2])))
        .properties(height=80)
    )


en_df = pd.DataFrame({"t": t, "v": en})
ton_q_df = pd.DataFrame({"t": t, "v": ton_q})
tof_q_df = pd.DataFrame({"t": t, "v": tof_q})
tp_q_df = pd.DataFrame({"t": t, "v": tp_q})
ctu_q_df = pd.DataFrame({"t": t, "v": ctu_q})

st.subheader("Input (EN)")
st.altair_chart(gantt(en_df, "#3b82f6"), use_container_width=True)

st.subheader(f"TON output (PT = {preset_s} s)")
st.altair_chart(gantt(ton_q_df, "#22c55e"), use_container_width=True)
st.caption("Goes high after EN has been continuously true for PT seconds.")

st.subheader(f"TOF output (PT = {preset_s} s)")
st.altair_chart(gantt(tof_q_df, "#f59e0b"), use_container_width=True)
st.caption("Stays high while EN is true; drops PT seconds after EN goes false.")

st.subheader(f"TP output (PT = {preset_s} s)")
st.altair_chart(gantt(tp_q_df, "#a855f7"), use_container_width=True)
st.caption("Fires for exactly PT seconds on each rising edge of EN.")

st.subheader(f"CTU output (PV = {counter_preset})")
st.altair_chart(gantt(ctu_q_df, "#ef4444"), use_container_width=True)
st.caption(
    f"Rises after {counter_preset} rising edges of EN have been counted. "
    f"Final count: **{int(ctu_acc[-1])}**"
)

with st.expander("💡 Try these"):
    st.markdown(
        """
        1. **Pulse train shorter than PT** — set pulse width to 2 s, PT to 5 s. The TON
           never completes because it resets every cycle. This is a classic bug source.
        2. **CTU vs. TON** — they look similar, but CTU counts events while TON measures
           continuous time.
        3. **TP for clean one-shots** — TP gives you a guaranteed-width pulse regardless
           of how long the input stays high. Great for valve actuation pulses.
        """
    )
