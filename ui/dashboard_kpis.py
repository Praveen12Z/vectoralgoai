import streamlit as st

def render_kpis(metrics):
    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total Return", f"{metrics['total_return_pct']:.2f}%")
    c2.metric("Profit Factor", f"{metrics['profit_factor']:.2f}")
    c3.metric("Win Rate", f"{metrics['win_rate_pct']:.2f}%")
    c4.metric("Max DD", f"{metrics['max_drawdown_pct']:.2f}%")
