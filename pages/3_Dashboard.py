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
