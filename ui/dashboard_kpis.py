import streamlit as st

def render_kpis():
    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total Return", "12.4%")
    c2.metric("Profit Factor", "1.31")
    c3.metric("Win Rate", "47%")
    c4.metric("Max Drawdown", "-6.2%")
