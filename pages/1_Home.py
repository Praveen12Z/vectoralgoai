import streamlit as st

st.set_page_config(page_title="VectorAlgoAI", layout="wide")

# ---------------- HERO ----------------
st.markdown(
    """
    <h1 style="text-align:center;">
        VectorAlgoAI
    </h1>
    <h3 style="text-align:center; color:gray;">
        Turn Trading Ideas into Tested Strategies — Instantly
    </h3>
    """,
    unsafe_allow_html=True,
)

st.markdown("")
st.markdown(
    """
    <p style="text-align:center; font-size:18px; color:#9ca3af;">
    Build strategies, crash-test them on real data, and receive brutal AI feedback
    <br/>
    before risking real capital.
    </p>
    """,
    unsafe_allow_html=True,
)

st.markdown("---")

# ---------------- VALUE PROPS ----------------
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🧩 Strategy Builder")
    st.write(
        "Define your strategy logic using indicators, rules, and risk settings — without coding."
    )

with col2:
    st.subheader("🧪 Crash-Test Engine")
    st.write(
        "Run historical backtests and expose hidden weaknesses before the market does."
    )

with col3:
    st.subheader("🧠 AI Mentor")
    st.write(
        "Receive ruthless, professional-grade feedback on why your strategy works — or fails."
    )

st.markdown("---")

# ---------------- ML + XAI POSITIONING ----------------
st.subheader("Why this is NOT just indicators + ChatGPT")

st.write(
    """
- We do **not** guess market direction.
- We evaluate **decision quality**.
- Machine Learning is used to **measure edge**, not to sell predictions.
- Explainable AI shows *why* signals fire and *when they should be ignored*.
"""
)

st.info(
    "VectorAlgoAI focuses on *probability, robustness, and risk structure* — not hype."
)

st.markdown("---")

# ---------------- CTA ----------------
st.markdown(
    "<h3 style='text-align:center;'>Ready to test your idea?</h3>",
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div style="display:flex; justify-content:center; gap:20px;">
        <a href="/Dashboard" target="_self">
            <button style="
                padding:12px 24px;
                font-size:16px;
                background-color:#2563eb;
                color:white;
                border:none;
                border-radius:8px;
                cursor:pointer;
            ">
                Open Strategy Dashboard →
            </button>
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)
