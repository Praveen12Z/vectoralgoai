import streamlit as st

def render_dashboard_sections():
    st.subheader("📈 Performance Overview")
    st.info("Price chart + trades (your existing Plotly chart goes here)")

    st.subheader("📋 Trade Log")
    st.info("Trade table, export buttons")

    st.subheader("🧨 Weakness Detection")
    st.warning("Detected issues will appear here")
