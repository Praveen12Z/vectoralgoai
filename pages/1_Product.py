import streamlit as st
import yaml

st.set_page_config(layout="wide")

st.markdown("# Strategy Builder")

mode = st.radio("Choose Mode", ["Guided (No Coding)", "Advanced (YAML)"])

if mode == "Guided (No Coding)":
    st.subheader("Market Setup")

    asset = st.selectbox("Asset Class", ["Forex", "Indices", "Commodities"])
    instrument = st.selectbox("Instrument", ["EURUSD", "NAS100", "XAUUSD"])
    timeframe = st.selectbox("Timeframe", ["5m", "15m", "1h", "4h"])

    st.subheader("Edge Type")
    trend = st.multiselect("Trend", ["EMA"])
    momentum = st.multiselect("Momentum", ["RSI"])
    volatility = st.multiselect("Volatility", ["ATR"])

    st.subheader("Risk")
    risk_pct = st.slider("Risk per trade (%)", 0.1, 2.0, 1.0)

    st.subheader("News & AI")
    avoid_news = st.checkbox("Avoid high-impact news")
    use_ml = st.checkbox("Use ML confirmation")

    if st.button("Generate Strategy"):
        strategy = {
            "market": instrument,
            "timeframe": timeframe,
            "risk": {"risk_per_trade_pct": risk_pct},
            "features": {
                "trend": trend,
                "momentum": momentum,
                "volatility": volatility,
                "avoid_news": avoid_news,
                "use_ml": use_ml,
            }
        }

        yaml_out = yaml.dump(strategy)
        st.markdown("### Generated Strategy (YAML)")
        st.code(yaml_out, language="yaml")

else:
    st.subheader("Advanced YAML")
    st.text_area("Paste your YAML strategy here", height=400)
