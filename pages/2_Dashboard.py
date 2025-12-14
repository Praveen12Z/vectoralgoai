from mvp_dashboard import run_mvp_dashboard

run_mvp_dashboard()
import streamlit as st

st.set_page_config(layout="wide")
st.title("📊 VectorAlgoAI Dashboard")

try:
    from mvp_dashboard import run_mvp_dashboard
    run_mvp_dashboard()
except Exception as e:
    st.error("Dashboard failed to load.")
    st.exception(e)
