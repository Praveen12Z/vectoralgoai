import streamlit as st
from ui.shared import load_css

st.set_page_config(page_title="VectorAlgoAI", layout="wide")
load_css()

st.title("🧪 VectorAlgoAI – Strategy Crash-Test Lab (MVP)")
# ...rest of your home content...
import streamlit as st
from ui.shared import load_css

st.set_page_config(page_title="VectorAlgoAI", layout="wide")
load_css()

# ---------- TOP HERO PANEL ----------
st.markdown(
    """
    <div class="hero">
        <div class="hero-left">
            <h1>VectorAlgoAI</h1>
            <p class="hero-sub">
                Build. Crash-test. Understand.<br>
                AI-powered strategy validation for serious traders.
            </p>

            <div class="hero-cta">
                <a href="/Dashboard" target="_self" class="cta-primary">🚀 Open Dashboard</a>
                <a href="/Product" target="_self" class="cta-secondary">📦 See Product</a>
            </div>
        </div>

        <div class="hero-right">
            <div class="hero-card">
                <h3>MVP Today</h3>
                <ul>
                    <li>Strategy Builder (No Code)</li>
                    <li>Backtest + Trades + Exports</li>
                    <li>Ruthless Mentor Feedback</li>
                </ul>
                <h4>Next</h4>
                <ul>
                    <li>ML models per instrument</li>
                    <li>XAI explanations</li>
                    <li>Prop-firm risk layer</li>
                </ul>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
