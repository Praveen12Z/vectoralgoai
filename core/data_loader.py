# core/data_loader.py
from __future__ import annotations

import os
from datetime import datetime, timedelta
import pandas as pd

# -----------------------------------------------------------
# Optional Massive / Polygon client (DISABLED IN MVP)
# -----------------------------------------------------------
try:
    from massive import RESTClient
    MASSIVE_AVAILABLE = True
except ImportError:
    RESTClient = None
    MASSIVE_AVAILABLE = False


# -----------------------------------------------------------
# Environment & paths
# -----------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

API_KEY = os.getenv("MASSIVE_API_KEY")

client = None
if MASSIVE_AVAILABLE and API_KEY:
    try:
        client = RESTClient(API_KEY)
    except Exception:
        client = None


# -----------------------------------------------------------
# Market mapper
# -----------------------------------------------------------
MARKET_MAP = {
    "NAS100": "NDX",
    "US30": "DJI",
    "SPX500": "SPX",
    "XAUUSD": "XAUUSD",
    "EURUSD": "EURUSD",
}


def get_symbol(symbol: str) -> str:
    return MARKET_MAP.get(symbol.upper(), symbol.upper())


# -----------------------------------------------------------
# SAMPLE DATA LOADER (MVP MODE)
# -----------------------------------------------------------
def _load_sample_data(symbol: str, timeframe: str) -> pd.DataFrame:
    """
    Load OHLCV from local CSV for MVP / demo mode.
    """
    fname = f"sample_{symbol.lower()}_{timeframe}.csv"
    path = os.path.join(DATA_DIR, fname)

    if not os.path.exists(path):
        return pd.DataFrame()

    df = pd.read_csv(path, parse_dates=["timestamp"])
    df = df.set_index("timestamp")

    return df[["open", "high", "low", "close", "volume"]]


# -----------------------------------------------------------
# Massive fetch (ONLY USED LATER – NOT MVP)
# -----------------------------------------------------------
def _fetch_massive(
    symbol: str,
    multiplier: int,
    timespan: str,
    years: int,
) -> pd.DataFrame:
    if not MASSIVE_AVAILABLE or client is None:
        return pd.DataFrame()

    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=365 * years)

    bars = []
    try:
        for bar in client.list_aggs(
            symbol,
            multiplier=multiplier,
            timespan=timespan,
            from_=start_date.strftime("%Y-%m-%d"),
            to=end_date.strftime("%Y-%m-%d"),
            limit=50000,
        ):
            bars.append(bar)
    except Exception:
        return pd.DataFrame()

    if not bars:
        return pd.DataFrame()

    df = pd.DataFrame(
        [
            {
                "timestamp": pd.to_datetime(b.timestamp, unit="ms"),
                "open": b.open,
                "high": b.high,
                "low": b.low,
                "close": b.close,
                "volume": b.volume,
            }
            for b in bars
        ]
    )

    df = (
        df.sort_values("timestamp")
        .drop_duplicates(subset=["timestamp"])
        .set_index("timestamp")
    )

    return df[["open", "high", "low", "close", "volume"]]


# -----------------------------------------------------------
# MAIN OHLCV LOADER (USED BY MVP)
# -----------------------------------------------------------
def load_ohlcv(symbol: str, timeframe: str, years: int = 2) -> pd.DataFrame:
    """
    Unified OHLCV loader.

    MVP behaviour:
    - Uses local CSV sample data only
    - NEVER crashes if data is missing
    """

    timeframe = timeframe.lower()

    # --- MVP MODE ---
    if not MASSIVE_AVAILABLE or client is None:
        df = _load_sample_data(symbol, timeframe)
        return df

    # --- FUTURE: LIVE MODE ---
    mapped_symbol = get_symbol(symbol)

    df_1h = _fetch_massive(mapped_symbol, multiplier=1, timespan="hour", years=years)
    if df_1h.empty:
        return df_1h

    df_1h = df_1h.sort_index()

    if timeframe == "1h":
        return df_1h

    if timeframe == "4h":
        return (
            df_1h.resample("4H")
            .agg(
                {
                    "open": "first",
                    "high": "max",
                    "low": "min",
                    "close": "last",
                    "volume": "sum",
                }
            )
            .dropna()
        )

    if timeframe in ("1d", "1day", "d"):
        return (
            df_1h.resample("1D")
            .agg(
                {
                    "open": "first",
                    "high": "max",
                    "low": "min",
                    "close": "last",
                    "volume": "sum",
                }
            )
            .dropna()
        )

    return df_1h
