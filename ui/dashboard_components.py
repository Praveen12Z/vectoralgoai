import streamlit as st
from ui.dashboard_kpis import render_kpis
from ui.dashboard_charts import render_price_chart
from ui.dashboard_tables import render_trades
from ui.dashboard_mentor import render_mentor

def render_dashboard(bt):
    render_kpis(bt["metrics"])
    st.divider()
    render_price_chart(bt)
    st.divider()
    render_trades(bt["trades"])
    st.divider()
    render_mentor(bt)

