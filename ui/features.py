import streamlit as st

def render_features():
    c1, c2, c3 = st.columns(3)

    with c1:
        st.subheader("🧩 Strategy Builder")
        st.write("Define rules, indicators, and risk logic without coding.")

    with c2:
        st.subheader("🧪 Crash-Test Engine")
        st.write("Backtest on historical data and reveal structural flaws.")

    with c3:
        st.subheader("🧠 AI Mentor")
        st.write("Professional-grade feedback, not motivational noise.")
