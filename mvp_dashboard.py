import os
import textwrap
from datetime import datetime

import numpy as np
import pandas as pd
import streamlit as st
import yaml
import joblib

# Optional: OpenAI for GPT parsing
try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False
    OpenAI = None  # type: ignore

# Optional: yfinance for real market data
try:
    import yfinance as yf
    YFIN_AVAILABLE = True
except ImportError:
    YFIN_AVAILABLE = False
    yf = None  # type: ignore


APP_TITLE = "VectorAlgoAI – Strategy-to-Bot MVP"
DEFAULT_INSTRUCTIONS = """Example:
"I want to trade EURUSD on the 15-minute timeframe. 
Use a 50/200 EMA crossover: buy when 50 EMA crosses above 200 EMA and price is above RSI 50.
Risk 1% per trade, SL at last swing low, TP 2R."
"""


# ---------------- OPENAI UTILS ---------------- #

def get_openai_client():
    if not OPENAI_AVAILABLE:
        return None

    api_key = None
    ui_key = st.session_state.get("openai_api_key", "").strip()
    if ui_key:
        api_key = ui_key
    if api_key is None:
        env_key = os.getenv("OPENAI_API_KEY", "").strip()
        if env_key:
            api_key = env_key
    if not api_key:
        return None
    return OpenAI(api_key=api_key)


def call_gpt_strategy_parser(prompt: str) -> dict:
    client = get_openai_client()
    if client is None:
        # fallback static config
        return {
            "meta": {
                "name": "EMA Crossover Strategy",
                "created_at": datetime.utcnow().isoformat() + "Z",
                "version": "0.1.0",
            },
            "market": {"symbol": "EURUSD", "timeframe": "1h"},
            "indicators": [
                {"name": "ema_fast", "type": "EMA", "period": 50, "source": "close"},
                {"name": "ema_slow", "type": "EMA", "period": 200, "source": "close"},
                {"name": "rsi", "type": "RSI", "period": 14, "source": "close"},
            ],
            "entry_rules": [
                "go_long when ema_fast crosses_above ema_slow and rsi > 50",
            ],
            "exit_rules": [
                "close_long when ema_fast crosses_below ema_slow or rsi < 45",
            ],
            "risk": {
                "per_trade_risk_pct": 1.0,
                "take_profit_r_multiple": 2.0,
                "stop_loss": "last_swing_low",
            },
            "notes": "Fallback static config used because OpenAI client or API key is not configured.",
        }

    system_msg = (
        "You are a trading strategy compiler for VectorAlgoAI. "
        "Convert the user's natural language strategy into a STRICT JSON config. "
        "Keys to include: meta, market, indicators, entry_rules, exit_rules, risk, notes. "
        "Output ONLY JSON. Do NOT wrap it in markdown, code fences, or explanations."
    )

    user_msg = f"User strategy description:\n{prompt}"

    completion = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_msg},
        ],
        temperature=0.2,
    )

    raw = completion.choices[0].message.content or ""

    import json, re

    text = raw.strip()
    match = re.search(r"\{.*\}", text, re.DOTALL)
    json_str = match.group(0) if match else text

    try:
        cfg = json.loads(json_str)
        meta = cfg.setdefault("meta", {})
        meta.setdefault("name", "VectorAlgoAI Strategy")
        meta.setdefault("created_at", datetime.utcnow().isoformat() + "Z")
        meta.setdefault("version", "0.1.0")
        return cfg
    except Exception:
        return {
            "meta": {
                "name": "Parsed Strategy (fallback JSON)",
                "created_at": datetime.utcnow().isoformat() + "Z",
                "version": "0.1.0",
            },
            "raw_model_output": raw,
            "notes": "Model response could not be parsed as JSON; raw content is included here.",
        }


# ---------------- DATA UTILS ---------------- #

def generate_dummy_price_data(n_points: int = 300) -> pd.DataFrame:
    np.random.seed(42)
    returns = np.random.normal(loc=0.0, scale=0.3, size=n_points)
    price = 100 + np.cumsum(returns)
    idx = pd.date_range(end=pd.Timestamp.utcnow(), periods=n_points, freq="60min")
    df = pd.DataFrame({"close": price}, index=idx)
    df["open"] = df["close"].shift(1).fillna(df["close"])
    df["high"] = df[["open", "close"]].max(axis=1) + np.random.uniform(0, 0.2, size=n_points)
    df["low"] = df[["open", "close"]].min(axis=1) - np.random.uniform(0, 0.2, size=n_points)
    return df


def normalize_timeframe(tf: str) -> str:
    if not tf:
        return "1h"
    tf = tf.strip().lower()
    if tf in ("m15", "15m", "15"):
        return "15m"
    if tf in ("m5", "5m", "5"):
        return "5m"
    if tf in ("h1", "1h", "60m"):
        return "1h"
    if tf in ("h4", "4h", "240m"):
        return "4h"
    if tf in ("d1", "1d", "day", "daily"):
        return "1d"
    return tf


def symbol_to_yf_ticker(symbol: str) -> str:
    if not symbol:
        return "EURUSD=X"
    s = symbol.strip().upper()
    if len(s) == 6 and s.isalpha():
        return s + "=X"
    return s


def load_eurusd_1h_from_csv(path: str) -> pd.DataFrame:
    if not os.path.exists(path):
        raise FileNotFoundError(f"EURUSD csv not found: {path}")

    df = pd.read_csv(path)
    df = df[~df["Price"].isin(["Ticker", "datetime"])].copy()
    df["datetime"] = pd.to_datetime(df["Price"])
    df.set_index("datetime", inplace=True)
    df.drop(columns=["Price"], inplace=True)

    for c in ["Close", "High", "Low", "Open", "Volume"]:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")

    df = df.dropna(subset=["Close"])
    df.sort_index(inplace=True)

    out = df[["Open", "High", "Low", "Close"]].copy()
    out.rename(
        columns={"Open": "open", "High": "high", "Low": "low", "Close": "close"},
        inplace=True,
    )
    return out


def load_price_data(symbol: str = "EURUSD", timeframe: str = "1h", n_points: int = 300):
    sym = symbol.strip().upper() if symbol else "EURUSD"
    tf = normalize_timeframe(timeframe)

    if sym == "EURUSD" and tf == "1h":
        csv_path = os.path.join("data", "eurusd_1h.csv")
        if os.path.exists(csv_path):
            try:
                df = load_eurusd_1h_from_csv(csv_path)
                df = df.tail(n_points)
                return df, f"file: {csv_path} (local EURUSD 1h data)"
            except Exception as e:
                return generate_dummy_price_data(n_points), f"dummy: error reading {csv_path} -> {e}"

    if not YFIN_AVAILABLE:
        return generate_dummy_price_data(n_points), "dummy: yfinance not installed"

    yf_symbol = symbol_to_yf_ticker(symbol)

    if tf == "5m":
        interval, period = "5m", "5d"
    elif tf == "15m":
        interval, period = "15m", "7d"
    elif tf == "1h":
        interval, period = "60m", "730d"
    elif tf == "4h":
        interval, period = "60m", "730d"
    else:
        interval, period = "1d", "5y"

    try:
        data = yf.download(yf_symbol, period=period, interval=interval, progress=False)
        if data.empty:
            return generate_dummy_price_data(n_points), f"dummy: empty download for {yf_symbol} ({interval}, {period})"

        df = data[["Open", "High", "Low", "Close"]].copy()
        df.rename(
            columns={"Open": "open", "High": "high", "Low": "low", "Close": "close"},
            inplace=True,
        )
        df.index = pd.to_datetime(df.index)
        df = df.tail(n_points)
        return df, f"real: {yf_symbol} ({interval}, {period})"
    except Exception as e:
        return generate_dummy_price_data(n_points), f"dummy: error downloading {yf_symbol} -> {e.__class__.__name__}"


# ---------------- STRATEGY INDICATOR LOGIC ---------------- #

def extract_indicator_config(cfg: dict):
    ema_fast = 20
    ema_slow = 50
    rsi_period = 14

    indicators = cfg.get("indicators", {})

    if isinstance(indicators, dict):
        for name, spec in indicators.items():
            t = str(spec.get("type", "")).upper()
            length = spec.get("length") or spec.get("period")
            if t == "EMA":
                if "fast" in name.lower() and length:
                    ema_fast = int(length)
                elif "slow" in name.lower() and length:
                    ema_slow = int(length)
            if t == "RSI" and length:
                rsi_period = int(length)
    elif isinstance(indicators, list):
        ema_candidates = []
        for spec in indicators:
            t = str(spec.get("type", "")).upper()
            period = spec.get("period") or spec.get("length")
            if t == "EMA" and period:
                ema_candidates.append(int(period))
            if t == "RSI" and period:
                rsi_period = int(period)
        if len(ema_candidates) >= 2:
            ema_candidates = sorted(set(ema_candidates))
            ema_fast = ema_candidates[0]
            ema_slow = ema_candidates[-1]
        elif len(ema_candidates) == 1:
            ema_fast = ema_candidates[0]

    if ema_fast >= ema_slow:
        ema_fast, ema_slow = min(ema_fast, ema_slow), max(ema_fast, ema_slow)

    return ema_fast, ema_slow, rsi_period


def extract_bollinger_config(cfg: dict):
    indicators = cfg.get("indicators", {})
    period = 20
    std_dev = 2.0
    has_bb = False

    def check_spec(name, spec):
        nonlocal has_bb, period, std_dev
        t = str(spec.get("type", "")).upper()
        nm = str(name).lower()
        if (
            "bollinger" in nm
            or "bbands" in nm
            or t in ("BOLLINGER", "BOLLINGER_BANDS", "BBANDS", "BB")
        ):
            has_bb = True
            per = spec.get("period") or spec.get("length") or spec.get("window")
            if per:
                period = int(per)
            sd = spec.get("std_dev") or spec.get("std") or spec.get("deviation")
            if sd:
                std_dev = float(sd)

    if isinstance(indicators, dict):
        for name, spec in indicators.items():
            check_spec(name, spec)
    elif isinstance(indicators, list):
        for spec in indicators:
            name = spec.get("name", "")
            check_spec(name, spec)

    return has_bb, period, std_dev


def add_signals_from_config(df: pd.DataFrame, cfg: dict):
    df = df.copy()
    has_bb, bb_period, bb_std = extract_bollinger_config(cfg)

    if has_bb:
        close = df["close"]
        mid = close.rolling(bb_period, min_periods=bb_period).mean()
        std = close.rolling(bb_period, min_periods=bb_period).std()
        upper = mid + bb_std * std
        lower = mid - bb_std * std

        df["bb_mid"] = mid
        df["bb_upper"] = upper
        df["bb_lower"] = lower

        df["signal"] = 0
        df.loc[
            (df["close"] < df["bb_lower"]) & (df["close"].shift(1) >= df["bb_lower"].shift(1)),
            "signal",
        ] = 1
        df.loc[
            (df["close"] > df["bb_upper"]) & (df["close"].shift(1) <= df["bb_upper"].shift(1)),
            "signal",
        ] = -1

        desc = (
            f"Signals generated using Bollinger Bands({bb_period}, {bb_std}σ): "
            f"long when price crosses below the lower band, short when price crosses above the upper band."
        )
        return df, desc

    ema_fast_p, ema_slow_p, rsi_p = extract_indicator_config(cfg)

    df["ema_fast"] = df["close"].ewm(span=ema_fast_p, adjust=False).mean()
    df["ema_slow"] = df["close"].ewm(span=ema_slow_p, adjust=False).mean()

    delta = df["close"].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    window = rsi_p
    avg_gain = gain.rolling(window=window, min_periods=window).mean()
    avg_loss = loss.rolling(window=window, min_periods=window).mean()
    rs = avg_gain / (avg_loss + 1e-9)
    df["rsi"] = 100 - (100 / (1 + rs))

    df["signal"] = 0
    df.loc[
        (df["ema_fast"] > df["ema_slow"])
        & (df["ema_fast"].shift(1) <= df["ema_slow"].shift(1))
        & (df["rsi"] > 50),
        "signal",
    ] = 1
    df.loc[
        (df["ema_fast"] < df["ema_slow"])
        & (df["ema_fast"].shift(1) >= df["ema_slow"].shift(1))
        & (df["rsi"] < 50),
        "signal",
    ] = -1

    desc = (
        f"Signals generated using EMA({ema_fast_p}) / EMA({ema_slow_p}) crossover "
        f"with RSI({rsi_p}) > 50 for longs and < 50 for shorts."
    )
    return df, desc


# ---------------- ML MODEL (EURUSD 1H) ---------------- #

def load_ml_model(symbol: str, timeframe: str):
    tf = normalize_timeframe(timeframe)
    sym = symbol.strip().upper() if symbol else ""
    if sym != "EURUSD" or tf != "1h":
        return None
    model_path = os.path.join("models", "eurusd_1h_clf.pkl")
    if not os.path.exists(model_path):
        return None
    bundle = joblib.load(model_path)
    return bundle


def compute_model_features(close: pd.Series) -> pd.DataFrame:
    close = close.astype(float)
    feat = pd.DataFrame(index=close.index)
    feat["close"] = close

    feat["ret_1"] = close.pct_change(1)
    feat["ret_3"] = close.pct_change(3)
    feat["ret_6"] = close.pct_change(6)

    feat["ema_10"] = close.ewm(span=10, adjust=False).mean()
    feat["ema_20"] = close.ewm(span=20, adjust=False).mean()
    feat["ema_50"] = close.ewm(span=50, adjust=False).mean()

    delta = close.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    window = 14
    avg_gain = gain.rolling(window=window, min_periods=window).mean()
    avg_loss = loss.rolling(window=window, min_periods=window).mean()
    rs = avg_gain / (avg_loss + 1e-9)
    feat["rsi_14"] = 100 - (100 / (1 + rs))

    feat["vol_20"] = feat["ret_1"].rolling(window=20, min_periods=20).std()

    feat = feat.dropna()
    return feat


def get_ml_predictions(symbol: str, timeframe: str, df: pd.DataFrame):
    """
    Returns (df_with_ai, prob_series, description)

    - If a real model bundle exists in models/eurusd_1h_clf.pkl and symbol/timeframe match,
      use it to compute probabilities.
    - Otherwise, create a smooth, demo-style probability series from price action so
      the UI still shows an 'AI' overlay.
    """
    bundle = load_ml_model(symbol, timeframe)

    # Real model available
    if bundle is not None:
        model = bundle["model"]
        feature_names = bundle.get(
            "feature_names",
            ["ret_1", "ret_3", "ret_6", "ema_10", "ema_20", "ema_50", "rsi_14", "vol_20"],
        )

        feat = compute_model_features(df["close"])
        if feat.empty:
            return df, None, "Not enough data to compute AI features."

        X = feat[feature_names].values
        probs = model.predict_proba(X)[:, 1]
        prob_series = pd.Series(probs, index=feat.index, name="ai_prob_up")

        df_ai = df.copy()
        df_ai["ai_prob_up"] = prob_series.reindex(df_ai.index)

        desc = (
            "AI model (RandomForest) trained on EURUSD 1h predicting the probability "
            "that the NEXT 1h candle closes higher than the current close."
        )
        return df_ai, prob_series, desc

    # No model -> simulated overlay
    ret = df["close"].pct_change().fillna(0)
    signal = ret.rolling(5, min_periods=1).sum()
    probs = 0.5 + 0.15 * np.tanh(signal * 20)
    probs = probs.clip(0.05, 0.95)

    prob_series = pd.Series(probs, index=df.index, name="ai_prob_up")
    df_ai = df.copy()
    df_ai["ai_prob_up"] = prob_series

    desc = (
        "Prototype AI overlay (simulated from recent price action). "
        "A real trained model will replace this once models/eurusd_1h_clf.pkl is added."
    )
    return df_ai, prob_series, desc


def config_to_yaml(config: dict) -> str:
    return yaml.safe_dump(config, sort_keys=False, allow_unicode=True)


# ---------------- STREAMLIT DASHBOARD ENTRY ---------------- #

def run_mvp_dashboard():
    """Called from app.py to render the full MVP dashboard inside the landing page."""
    st.title("📈 VectorAlgoAI – Strategy-to-Bot MVP")
    st.caption("Built by Praveen Kumar – AI-powered trading bot generator (v0.4)")

    # Show AI model status
    ml_bundle = load_ml_model("EURUSD", "1h")
    if ml_bundle is not None:
        st.markdown("🧠 **AI model status:** Real EURUSD 1h classifier loaded.")
    else:
        st.markdown(
            "🧠 **AI model status:** Demo probability overlay (no trained model file yet)."
        )

    with st.sidebar:
        st.header("⚙️ Settings")
        st.markdown(
            """
            - Step 1: Describe your strategy in plain English  
            - Step 2: Paste an OpenAI API key (optional)  
            - Step 3: Click **Generate Bot**  
            - Step 4: See REAL data + config-driven signals  
            - Step 5: AI probability overlay for EURUSD 1h  
            """
        )
        st.divider()

        default_key = st.session_state.get("openai_api_key", "")
        api_key_ui = st.text_input(
            "🔑 OpenAI API key (optional)",
            value=default_key,
            type="password",
            help="Paste your OpenAI key here. It stays only in this session.",
        )
        st.session_state["openai_api_key"] = api_key_ui.strip()

        client = get_openai_client()

        key_source = None
        if api_key_ui.strip():
            key_source = "ui"
        elif os.getenv("OPENAI_API_KEY", "").strip():
            key_source = "env"

        if not OPENAI_AVAILABLE:
            status_text = "❌ openai package not installed (using offline fallback)"
        else:
            if client and key_source == "ui":
                status_text = "✅ using key from input field"
            elif client and key_source == "env":
                status_text = "✅ using key from environment"
            else:
                status_text = "⚠️ no API key set (using offline fallback)"

        st.markdown(f"OpenAI status: {status_text}")

        if not client:
            st.info(
                "You can paste your OpenAI API key above to enable real GPT parsing. "
                "Without it, the app uses a built-in fallback template.",
                icon="💡",
            )

        if not YFIN_AVAILABLE:
            st.warning(
                "yfinance is not installed – chart will use dummy random data for non-EURUSD/1h.",
                icon="📦",
            )

        st.divider()
        st.subheader("🧠 AI Options")
        ai_filter_enabled = st.checkbox(
            "Enable AI filter (EURUSD 1h only for now)",
            value=False,
            help="When ON, strategy signals will be filtered by the EURUSD 1h ML model (if available).",
        )

    col_left, col_right = st.columns([1.2, 1])

    with col_left:
        st.subheader("1️⃣ Describe your strategy")
        user_strategy = st.text_area(
            "Tell VectorAlgoAI what you want your bot to do:",
            value=textwrap.dedent(DEFAULT_INSTRUCTIONS).strip(),
            height=220,
        )
        generate = st.button("🚀 Generate Bot", type="primary")

    with col_right:
        st.subheader("👤 About VectorAlgoAI")
        st.markdown(
            """
            **VectorAlgoAI** turns your strategy idea into a structured bot config.

            This MVP shows:
            - Natural language ➜ structured config (JSON/YAML)  
            - Real market data when available (yfinance or your local CSV)  
            - Config-driven signals (EMA/RSI **or** Bollinger Bands)  
            - AI model overlay for EURUSD 1h (probability of next bar up)  
            """
        )

    if generate and user_strategy.strip():
        with st.spinner("Translating your strategy into a bot config..."):
            cfg = call_gpt_strategy_parser(user_strategy)

        st.success("Bot config generated ✅")

        tab_yaml, tab_json, tab_chart, tab_summary = st.tabs(
            ["🧾 YAML Config", "🧩 Raw JSON", "📊 Chart + AI", "🧠 Bot Summary"]
        )

        # --- YAML tab ---
        with tab_yaml:
            st.code(config_to_yaml(cfg), language="yaml")

        # --- JSON tab ---
        with tab_json:
            st.json(cfg)

        # --- Chart + AI tab ---
        with tab_chart:
            import plotly.graph_objects as go

            symbol = cfg.get("market", {}).get("symbol", "EURUSD")
            timeframe = cfg.get("market", {}).get("timeframe", "1h")

            df, data_source = load_price_data(symbol, timeframe, n_points=300)
            df, logic_desc = add_signals_from_config(df, cfg)

            df_ai, prob_series, ai_desc = get_ml_predictions(symbol, timeframe, df)

            plot_df = df_ai.copy()
            if ai_filter_enabled and prob_series is not None:
                plot_df["signal_filtered"] = 0
                long_mask = (plot_df["signal"] == 1) & (plot_df.get("ai_prob_up", 0) >= 0.55)
                short_mask = (plot_df["signal"] == -1) & (plot_df.get("ai_prob_up", 0) <= 0.45)
                plot_df.loc[long_mask, "signal_filtered"] = 1
                plot_df.loc[short_mask, "signal_filtered"] = -1

                buys = plot_df[plot_df["signal_filtered"] == 1]
                sells = plot_df[plot_df["signal_filtered"] == -1]
                signal_caption = (
                    "Signals filtered by AI: only longs with prob_up ≥ 0.55 "
                    "and shorts with prob_up ≤ 0.45 (EURUSD 1h model or demo overlay)."
                )
            else:
                buys = plot_df[plot_df["signal"] == 1]
                sells = plot_df[plot_df["signal"] == -1]
                signal_caption = "Signals from strategy logic only (no AI filtering)."

            fig = go.Figure()
            fig.add_trace(
                go.Candlestick(
                    x=plot_df.index,
                    open=plot_df["open"],
                    high=plot_df["high"],
                    low=plot_df["low"],
                    close=plot_df["close"],
                    name="Price",
                )
            )

            # EMAs
            if "ema_fast" in plot_df.columns:
                fig.add_trace(
                    go.Scatter(
                        x=plot_df.index,
                        y=plot_df["ema_fast"],
                        mode="lines",
                        name="EMA Fast",
                    )
                )
            if "ema_slow" in plot_df.columns:
                fig.add_trace(
                    go.Scatter(
                        x=plot_df.index,
                        y=plot_df["ema_slow"],
                        mode="lines",
                        name="EMA Slow",
                    )
                )

            # Bollinger bands
            if "bb_upper" in plot_df.columns:
                fig.add_trace(
                    go.Scatter(
                        x=plot_df.index,
                        y=plot_df["bb_upper"],
                        mode="lines",
                        name="BB Upper",
                    )
                )
            if "bb_lower" in plot_df.columns:
                fig.add_trace(
                    go.Scatter(
                        x=plot_df.index,
                        y=plot_df["bb_lower"],
                        mode="lines",
                        name="BB Lower",
                    )
                )
            if "bb_mid" in plot_df.columns:
                fig.add_trace(
                    go.Scatter(
                        x=plot_df.index,
                        y=plot_df["bb_mid"],
                        mode="lines",
                        name="BB Mid",
                    )
                )

            # Buy / sell markers
            fig.add_trace(
                go.Scatter(
                    x=buys.index,
                    y=buys["close"],
                    mode="markers",
                    marker_symbol="triangle-up",
                    marker_size=10,
                    name="Buy",
                )
            )
            fig.add_trace(
                go.Scatter(
                    x=sells.index,
                    y=sells["close"],
                    mode="markers",
                    marker_symbol="triangle-down",
                    marker_size=10,
                    name="Sell",
                )
            )

            fig.update_layout(
                title=f"{symbol} – {timeframe} | Config-driven signals",
                xaxis_title="Time",
                yaxis_title="Price",
                xaxis_rangeslider_visible=False,
            )

            st.plotly_chart(fig, use_container_width=True)
            st.caption(f"Data source: {data_source}")
            st.caption(f"Signal logic: {logic_desc}")
            st.caption(signal_caption)

            if prob_series is not None:
                st.subheader("🧠 AI probability of next-bar up")
                st.line_chart(prob_series)
                st.caption(ai_desc)
            else:
                st.info("No AI probability series available.", icon="🧠")

        # --- Summary tab ---
        with tab_summary:
            summary_lines = [
                f"**Bot name:** {cfg.get('meta', {}).get('name', 'VectorAlgoAI Bot')}",
            ]
            market = cfg.get("market", {})
            summary_lines.append(
                f"**Market:** {market.get('symbol', 'N/A')} – {market.get('timeframe', 'N/A')}"
            )
            summary_lines.append("")

            entry_rules = cfg.get("entry_rules", [])
            if isinstance(entry_rules, dict):
                long_rules = entry_rules.get("long", [])
                short_rules = entry_rules.get("short", [])
                if long_rules:
                    summary_lines.append("**Entry rules (long):**")
                    for r in long_rules:
                        summary_lines.append(f"- {r}")
                if short_rules:
                    summary_lines.append("")
                    summary_lines.append("**Entry rules (short):**")
                    for r in short_rules:
                        summary_lines.append(f"- {r}")
            else:
                summary_lines.append("**Entry rules:**")
                for r in entry_rules:
                    summary_lines.append(f"- {r}")

            summary_lines.append("")

            exit_rules = cfg.get("exit_rules", [])
            if isinstance(exit_rules, dict):
                summary_lines.append("**Exit rules:**")
                for k, v in exit_rules.items():
                    summary_lines.append(f"- **{k}**: {v}")
            else:
                summary_lines.append("**Exit rules:**")
                for r in exit_rules:
                    summary_lines.append(f"- {r}")

            summary_lines.append("")
            risk = cfg.get("risk", {})
            if risk:
                summary_lines.append("**Risk settings:**")
                for k, v in risk.items():
                    summary_lines.append(f"- **{k}**: {v}")

            notes = cfg.get("notes")
            if notes:
                summary_lines.append("")
                summary_lines.append("**Notes:**")
                summary_lines.append(notes)

            st.markdown("\n".join(summary_lines))
