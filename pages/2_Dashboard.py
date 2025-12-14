import streamlit as st
from pages.shared import load_css

from core.strategy_config import parse_strategy_yaml
from core.data_loader import load_ohlcv
from core.indicators import apply_all_indicators
from core.backtester_adapter import run_backtest_v2

from ui.dashboard_kpis import render_kpis
from ui.dashboard_sections import render_dashboard_sections
from ui.ml_confidence import render_ml_confidence

st.set_page_config(layout="wide")
load_css()

st.title("📊 Strategy Crash-Test Dashboard")

strategy_yaml = st.text_area(
    "Strategy YAML",
    height=260,
    placeholder="Paste strategy YAML here"
)

run = st.button("🔴 Run Crash-Test", use_container_width=True)

if run:
    cfg = parse_strategy_yaml(strategy_yaml)
    df_price = load_ohlcv(cfg.market, cfg.timeframe)
    df_feat = apply_all_indicators(df_price, cfg)

    metrics, weaknesses, suggestions, trades_df = run_backtest_v2(
        df_feat, cfg
    )

    st.session_state["bt"] = {
        "metrics": metrics,
        "trades": trades_df,
        "weaknesses": weaknesses,
        "suggestions": suggestions,
    }

if "bt" in st.session_state:
    bt = st.session_state["bt"]

    render_kpis(bt["metrics"])
    st.markdown("---")

    render_dashboard_sections(
        bt["trades"],
        bt["weaknesses"],
        bt["suggestions"]
    )

    st.markdown("---")
    render_ml_confidence()
