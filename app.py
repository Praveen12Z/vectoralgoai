import streamlit as st
from mvp_dashboard import run_mvp_dashboard

# -----------------------------------------------------------
# GLOBAL CONFIG
# -----------------------------------------------------------
st.set_page_config(page_title="VectorAlgoAI", layout="wide")

# -----------------------------------------------------------
# CUSTOM CSS
# -----------------------------------------------------------
CSS = """
<style>
html, body, [class*="css"] {
    background: #070b14 !important;
    color: #e8eefc !important;
}

.topbar {
    display: flex;
    gap: 20px;
    padding: 12px 20px;
    background: #0b1120;
    border-bottom: 1px solid rgba(148,163,184,.2);
}

.topbar button {
    padding: 10px 18px;
    border-radius: 8px;
    background: rgba(148,163,184,.1);
    color: #e8eefc;
    border: 1px solid rgba(148,163,184,.2);
}

.topbar-title {
    font-size: 24px;
    font-weight: 800;
    margin-right: auto;
}

.hero {
    padding: 40px;
    border-radius: 18px;
    background: linear-gradient(135deg, #1e293b, #0f172a 60%);
    box-shadow: 0 20px 60px rgba(0,0,0,.4);
}

.card {
    padding: 20px;
    border-radius: 14px;
    background: rgba(2,6,23,.5);
    border: 1px solid rgba(148,163,184,.2);
    margin-top: 20px;
}

.cta-primary {
    padding: 12px 18px;
    background: #2563eb;
    color: white !important;
    border-radius: 10px;
    text-decoration: none;
}

.cta-secondary {
    padding: 12px 18px;
    background: rgba(148,163,184,.15);
    border: 1px solid rgba(148,163,184,.25);
    color: #e8eefc !important;
    border-radius: 10px;
    text-decoration: none;
}
</style>
"""

st.markdown(CSS, unsafe_allow_html=True)

# -----------------------------------------------------------
# NAVIGATION STATE
# -----------------------------------------------------------
if "page" not in st.session_state:
    st.session_state["page"] = "Home"

def go(page):
    st.session_state["page"] = page
    st.rerun()

# -----------------------------------------------------------
# TOP NAV BAR
# -----------------------------------------------------------
st.markdown(
    """
    <div class="topbar">
        <div class="topbar-title">VectorAlgoAI</div>
        </div>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🏠 Home"):
        go("Home")
with col2:
    if st.button("📦 Product"):
        go("Product")
with col3:
    if st.button("📊 Dashboard"):
        go("Dashboard")

st.write("---")

# -----------------------------------------------------------
# PAGE LOGIC
# -----------------------------------------------------------

# HOME PAGE
if st.session_state["page"] == "Home":
    st.markdown(
    """
    <div class="hero">
        <h1>Build. Crash-test. Understand.</h1>
        <p>AI-powered strategy validation for serious traders.</p>
        <br>
        <a href="#" onclick="window.location.reload()" class="cta-primary">🚀 Open Dashboard</a>
        <a href="#" onclick="window.location.reload()" class="cta-secondary">📦 See Product</a>
    </div>

    <div class="card">
        <h3>MVP Today</h3>
        <ul>
            <li>Strategy Builder (no code)</li>
            <li>Backtest + Trades + Exports</li>
            <li>Ruthless Mentor Feedback</li>
        </ul>

        <h3>Next</h3>
        <ul>
            <li>ML Models per instrument</li>
            <li>XAI Explanations</li>
            <li>Prop-firm risk layer</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
    )

# PRODUCT PAGE
elif st.session_state["page"] == "Product":
    st.markdown(
    """
    <div class="hero">
        <h1>What makes VectorAlgoAI different?</h1>
        <p>We don’t predict blindly — we validate ideas like a quant.</p>
    </div>

    <div class="card">
        <h3>No Blind Predictions</h3>
        <ul>
            <li>No black-box ML</li>
            <li>Evidence-based decision layers</li>
        </ul>

        <h3>Stress-Test Engine</h3>
        <ul>
            <li>Real market conditions</li>
            <li>Failure-mode analysis</li>
        </ul>

        <h3>XAI (Next Phase)</h3>
        <ul>
            <li>Why this signal?</li>
            <li>When does it fail?</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# DASHBOARD PAGE
elif st.session_state["page"] == "Dashboard":
    run_mvp_dashboard()
