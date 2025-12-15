import streamlit as st

st.set_page_config(page_title="VectorAlgoAI", layout="wide")

# ----------------------------------------------------------
# GLOBAL CSS (Premium AISaaS Style)
# ----------------------------------------------------------
st.markdown("""
<style>

body {
    background: #040613;
    font-family: 'Inter', sans-serif;
    color: white;
}

.navbar {
    width: 100%;
    padding: 18px 40px;
    background: #2c3440;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-radius: 6px;
}

.nav-left {
    font-size: 22px;
    font-weight: 700;
}

.nav-right a {
    margin-left: 25px;
    text-decoration: none;
    font-size: 16px;
    color: white;
    opacity: 0.85;
}

.nav-right a:hover {
    opacity: 1;
}

.hero-title {
    font-size: 60px;
    font-weight: 800;
    text-align: center;
    margin-top: 80px;
    background: linear-gradient(90deg, #7bb4ff, #c0bfff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-sub {
    text-align: center;
    font-size: 18px;
    opacity: 0.7;
    margin-top: -10px;
}

.hero-buttons {
    text-align: center;
    margin-top: 40px;
}

.btn-primary {
    background: #5b7bff;
    padding: 14px 26px;
    border-radius: 10px;
    color: white;
    margin-right: 15px;
    text-decoration: none;
}

.btn-secondary {
    background: #3a3f47;
    padding: 14px 26px;
    border-radius: 10px;
    color: white;
    text-decoration: none;
}

.section-title {
    font-size: 36px;
    font-weight: 700;
    margin-top: 80px;
    text-align: center;
}

.feature-box {
    background: #111525;
    padding: 20px 30px;
    border-radius: 12px;
    margin: 10px 0;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------------
# NAVIGATION SYSTEM
# ----------------------------------------------------------
page = st.experimental_get_query_params().get("page", ["home"])[0]

def goto(page_name):
    st.experimental_set_query_params(page=page_name)


# ----------------------------------------------------------
# NAV BAR
# ----------------------------------------------------------
st.markdown("""
<div class="navbar">
    <div class="nav-left">⚡ VectorAlgoAI</div>
    <div class="nav-right">
        <a href="?page=home">Home</a>
        <a href="?page=product">Product</a>
        <a href="?page=dashboard">Dashboard</a>
    </div>
</div>
""", unsafe_allow_html=True)


# ----------------------------------------------------------
# HOMEPAGE
# ----------------------------------------------------------
if page == "home":
    st.markdown('<div class="hero-title">Revolutionize Your Trading Process</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-sub">AI-powered strategy validation, ruthless feedback, and ML-enhanced trading insights.</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="hero-buttons">
        <a class="btn-primary" href="?page=dashboard">🚀 Open Dashboard</a>
        <a class="btn-secondary" href="?page=product">📦 View Product</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Why VectorAlgoAI?</div>', unsafe_allow_html=True)

    cols = st.columns(3)
    cols[0].markdown('<div class="feature-box">✨ No-Code Strategy Builder</div>', unsafe_allow_html=True)
    cols[1].markdown('<div class="feature-box">📊 Backtest + Trades + Exports</div>', unsafe_allow_html=True)
    cols[2].markdown('<div class="feature-box">🧠 Ruthless Mentor Feedback</div>', unsafe_allow_html=True)

    cols = st.columns(3)
    cols[0].markdown('<div class="feature-box">🤖 ML Models (Phase 2)</div>', unsafe_allow_html=True)
    cols[1].markdown('<div class="feature-box">🔍 XAI Explanations</div>', unsafe_allow_html=True)
    cols[2].markdown('<div class="feature-box">🛡 Prop-Firm Risk Layer</div>', unsafe_allow_html=True)


# ----------------------------------------------------------
# PRODUCT PAGE
# ----------------------------------------------------------
elif page == "product":
    st.title("📦 Product Overview")
    st.write("Why VectorAlgoAI is built different:")
    st.markdown("""
    - No-code strategy builder  
    - Brutal transparency about failing strategies  
    - Fast backtesting engine  
    - ML + XAI roadmap  
    """)


# ----------------------------------------------------------
# DASHBOARD (MVP WILL BE ATTACHED NEXT)
# ----------------------------------------------------------
elif page == "dashboard":
    st.title("📊 Dashboard (MVP Loading Soon...)")
    st.write("This page will host your full Crash-Test MVP.")


