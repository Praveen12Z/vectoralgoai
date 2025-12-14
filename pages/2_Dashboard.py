import streamlit as st
from ui.dashboard_kpis import render_kpis
from ui.dashboard_sections import render_dashboard_sections
from ui.ml_confidence import render_ml_confidence

st.set_page_config(layout="wide")

st.title("📊 Strategy Crash-Test Dashboard")

render_kpis()
st.markdown("---")
render_dashboard_sections()
st.markdown("---")
render_ml_confidence()
import streamlit as st

st.set_page_config(layout="wide")
st.title("📊 VectorAlgoAI Dashboard")

try:
    from mvp_dashboard import run_mvp_dashboard
    run_mvp_dashboard()
except Exception as e:
    st.error("Dashboard failed to load.")
    st.exception(e)
