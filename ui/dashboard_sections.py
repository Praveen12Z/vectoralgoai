import streamlit as st

def render_dashboard_sections(trades, weaknesses, suggestions):
    st.subheader("📋 Trade Log")
    st.dataframe(trades)

    st.subheader("🧨 Detected Weaknesses")
    for w in weaknesses:
        st.warning(w)

    st.subheader("🧠 Improvement Suggestions")
    for s in suggestions:
        st.info(s)
