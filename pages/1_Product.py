import streamlit as st

st.set_page_config(page_title="VectorAlgoAI — Product", page_icon="📦", layout="wide")

st.title("📦 Product")
st.write("A clean overview of what VectorAlgoAI does today, and where ML + XAI will fit next.")

st.markdown("### What you get today (MVP)")
st.markdown(
"""
- **Strategy Builder (No code):** choose market/timeframe, indicators, entry/exit logic
- **Crash-Test Backtest:** trades, equity, grade, exports
- **Ruthless Mentor:** plain-language diagnosis + fixes
"""
)

st.markdown("### Why we are NOT “just ChatGPT for trading”")
st.markdown(
"""
ChatGPT can *talk*. VectorAlgoAI must **execute**:
- Convert intent → **structured strategy config**
- Run consistent **backtests** and produce **traceable trade logs**
- Track performance metrics and failure modes repeatedly
- Later: attach **ML predictions + XAI explanations** to each decision
"""
)

st.markdown("### Where Machine Learning fits (Phase 4+)")
st.markdown(
"""
ML is not replacing strategy rules — it becomes an **edge module**:
1) **Regime detection** (trend / range / volatility / news-driven)
2) **Probability layer**: “signal strength” / “expected RR” / “confidence”
3) **Trade filtering**: skip low-quality setups your rules would still take
4) **Personalization**: adapt to the trader’s style + instrument behavior

**XAI later:** show *why* ML scored a trade high/low (top features, regime tag, similar historical cases).
"""
)

st.markdown("### Next steps")
st.page_link("pages/2_Dashboard.py", label="🚀 Open Dashboard", use_container_width=True)
