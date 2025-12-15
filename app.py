import streamlit as st

# -----------------------------
#  Global page config
# -----------------------------
st.set_page_config(page_title="VectorAlgoAI", layout="wide")

# -----------------------------
#  CSS THEME (Premium – Dark / Purple)
# -----------------------------
page_css = """
<style>

body {
    background-color: #060b18;
    color: #e8e8e8;
    font-family: 'Inter', sans-serif;
}

/* NAVBAR */
.navbar {
    width: 100%;
    padding: 18px 40px;
    background: #111827cc;
    display: flex;
    justify-content: space-between;
    border-bottom: 1px solid rgba(255,255,255,0.05);
}
.nav-left {
    font-size: 26px;
    font-weight: 700;
    color: #7dd3fc;
}
.nav-menu a {
    margin-right: 28px;
    color: #c3cbe0;
    text-decoration: none;
    font-size: 16px;
}
.nav-menu a.active {
    color: #ffffff;
    font-weight: 700;
}
.nav-menu a:hover {
    color: #ffffff;
}

/* HERO */
.hero {
    padding: 80px 0;
    text-align: center;
}
.hero h1 {
    font-size: 60px;
    font-weight: 800;
    background: linear-gradient(90deg,#a78bfa,#7dd3fc);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.hero-sub {
    font-size: 20px;
    margin-top: -10px;
    color: #cbd5e1;
}

/* Buttons */
.cta {
    margin-top: 28px;
}
.cta a {
    padding: 12px 26px;
    border-radius: 10px;
    margin-right: 12px;
    text-decoration: none;
    font-size: 17px;
    font-weight: 600;
}
.cta-primary {
    background: #7c3aed;
    color: white;
}
.cta-secondary {
    background: #1f2937;
    color: #e2e8f0;
}

/* FEATURE GRID */
.feature-section {
    padding: 40px;
    margin-top: 30px;
}
.feature-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 22px;
}
.feature-box {
    background: #111827;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid rgba(255,255,255,0.06);
}

</style>
"""
st.markdown(page_css, unsafe_allow_html=True)

# -----------------------------
# NAVIGATION SYSTEM
# -----------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

def goto(page):
    st.session_state.page = page
    st.rerun()

# NAVBAR
st.markdown(
    f"""
    <div class="navbar">
        <div class="nav-left">⚡ VectorAlgoAI</div>
        <div class="nav-menu">
            <a href="#" {'class="active"' if st.session_state.page=='home' else ''} onclick="window.location.href='?page=home'">Home</a>
            <a href="#" {'class="active"' if st.session_state.page=='product' else ''} onclick="window.location.href='?page=product'">Product</a>
            <a href="#" {'class="active"' if st.session_state.page=='dashboard' else ''} onclick="window.location.href='?page=dashboard'">Dashboard</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# URL read
query_params = st.experimental_get_query_params()
if "page" in query_params:
    st.session_state.page = query_params["page"][0]

# -----------------------------
# PAGE: HOME
# -----------------------------
if st.session_state.page == "home":
    st.markdown("""
    <div class="hero">
        <h1>Revolutionize Your Trading Process</h1>
        <p class="hero-sub">AI-powered strategy validation, ruthless feedback, and ML-enhanced trading insights.</p>

        <div class="cta">
            <a class="cta-primary" href="?page=dashboard">🚀 Open Dashboard</a>
            <a class="cta-secondary" href="?page=product">📦 View Product</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="feature-section">
        <h2>Why VectorAlgoAI?</h2>
        <br>
        <div class="feature-grid">

            <div class="feature-box">✨ No-Code Strategy Builder</div>
            <div class="feature-box">📊 Backtest + Trades + Exports</div>
            <div class="feature-box">🧠 Ruthless Mentor Feedback</div>

            <div class="feature-box">🤖 ML Models Per Instrument (Phase 2)</div>
            <div class="feature-box">🔍 XAI Explanations</div>
            <div class="feature-box">📉 Prop-Firm Risk Layer</div>

        </div>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# PAGE: PRODUCT
# -----------------------------
elif st.session_state.page == "product":
    st.title("📦 Product Overview")
    st.write("""
    **What makes VectorAlgoAI different?**

    - We don’t predict blindly — we stress-test ideas  
    - We explain WHY strategies fail  
    - We prepare traders for prop-firm evaluations  
    - ML confidence scoring (Phase 2)  
    - XAI: Why this signal, why now  
    """)

# -----------------------------
# PAGE: DASHBOARD (MVP placeholder)
# -----------------------------
elif st.session_state.page == "dashboard":
    st.title("📊 Strategy Crash-Test Dashboard (MVP)")
    st.info("Your full MVP with backtesting will load here. Ready to integrate next!")

