# ui/strategy_builder.py
import streamlit as st


def render_strategy_builder():
    st.subheader("🧩 Strategy Builder (No Coding Required)")

    # -----------------------------
    # Market & Timeframe
    # -----------------------------
    market = st.selectbox(
        "Market",
        ["NAS100", "EURUSD (Coming Soon)", "XAUUSD (Coming Soon)"],
        index=0,
    )

    timeframe = st.selectbox(
        "Timeframe",
        ["1h", "4h (Coming Soon)", "1d (Coming Soon)"],
        index=0,
    )

    if "Coming Soon" in market or "Coming Soon" in timeframe:
        st.warning("Only NAS100 on 1h is supported in this MVP.")
        return

    # -----------------------------
    # Indicators
    # -----------------------------
    st.markdown("### Indicators")

    use_ema = st.checkbox("Use EMA Trend Filter", value=True)
    ema_fast = st.number_input("EMA Fast Period", 5, 50, 20)
    ema_slow = st.number_input("EMA Slow Period", 20, 200, 50)

    use_rsi = st.checkbox("Use RSI Filter", value=True)
    rsi_period = st.number_input("RSI Period", 5, 30, 14)

    # -----------------------------
    # Entry Logic
    # -----------------------------
    st.markdown("### Entry Logic")

    long_rule = st.selectbox(
        "Long Entry Condition",
        [
            "EMA Fast > EMA Slow",
            "Price Pullback to EMA",
            "RSI Oversold (<40)",
        ],
    )

    short_rule = st.selectbox(
        "Short Entry Condition",
        [
            "EMA Fast < EMA Slow",
            "Price Rejection from EMA",
            "RSI Overbought (>60)",
        ],
    )

    # -----------------------------
    # Risk Settings
    # -----------------------------
    st.markdown("### Risk Management")

    capital = st.number_input("Account Size (€)", 1000, 1_000_000, 10_000)
    risk_pct = st.slider("Risk per Trade (%)", 0.1, 5.0, 1.0)

    # -----------------------------
    # Build YAML
    # -----------------------------
    if st.button("🚀 Build Strategy"):
        indicators_yaml = []

        if use_ema:
            indicators_yaml.extend(
                [
                    f"""
  - name: ema_fast
    type: ema
    period: {ema_fast}
    source: close
""",
                    f"""
  - name: ema_slow
    type: ema
    period: {ema_slow}
    source: close
""",
                ]
            )

        if use_rsi:
            indicators_yaml.append(
                f"""
  - name: rsi
    type: rsi
    period: {rsi_period}
    source: close
"""
            )

        # Entry mapping
        entry_long = []
        entry_short = []

        if long_rule == "EMA Fast > EMA Slow":
            entry_long.append(
                """
    - left: ema_fast
      op: ">"
      right: ema_slow
"""
            )
        if long_rule == "RSI Oversold (<40)":
            entry_long.append(
                """
    - left: rsi
      op: "<"
      right: 40
"""
            )

        if short_rule == "EMA Fast < EMA Slow":
            entry_short.append(
                """
    - left: ema_fast
      op: "<"
      right: ema_slow
"""
            )
        if short_rule == "RSI Overbought (>60)":
            entry_short.append(
                """
    - left: rsi
      op: ">"
      right: 60
"""
            )

        strategy_yaml = f"""
name: "NAS100 Strategy Builder"
market: "NAS100"
timeframe: "1h"

indicators:
{''.join(indicators_yaml)}

entry:
  long:
{''.join(entry_long) if entry_long else "    []"}

  short:
{''.join(entry_short) if entry_short else "    []"}

exit:
  long:
    - type: atr_sl
      atr_col: atr14
      multiple: 2.0
    - type: atr_tp
      atr_col: atr14
      multiple: 3.0

  short:
    - type: atr_sl
      atr_col: atr14
      multiple: 2.0
    - type: atr_tp
      atr_col: atr14
      multiple: 3.0

risk:
  capital: {capital}
  risk_per_trade_pct: {risk_pct}
"""

        st.session_state["strategy_yaml"] = strategy_yaml
        st.success("Strategy built! You can now run the Crash-Test.")
