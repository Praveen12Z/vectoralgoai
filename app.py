import streamlit as st
import os

st.set_page_config(page_title="VectorAlgoAI", layout="wide")

# ----------------------------------------
# Load CSS
# ----------------------------------------
def load_css():
    css_path = "assets/styles.css"
    if os.path.exists(css_path):
        with open(css_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
load_css()

# ----------------------------------------
# NAVBAR
# ----------------------------------------
st.markdown("""
<div class="navbar">
    <div class="nav-left">VectorAlgoAI</div>
    <div class="nav-right">
        <a href="/" class="nav-item">Home</a>
        <a href="/Product" class="nav-item">Product</a>
        <a href="/Dashboard" class="nav-item nav-cta">Dashboard</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ----------------------------------------
# HERO SECTION
# ----------------------------------------
st.markdown("""
<div class="hero-container">

    <div class="hero-left">
        <h1 class="hero-title">Build. Crash-test. Understand.</h1>
        <p class="hero-subtitle">AI-powered strategy validation for serious traders.</p>

        <div class="hero-buttons">
            <a href="/Dashboard" class="hero-btn-primary">🚀 Open Dashboard</a>
            <a href="/Product" class="hero-btn-secondary">📦 See Product</a>
        </div>
    </div>

    <div class="hero-right">
        <div class="hero-card">
            <h3>MVP Today</h3>
            <ul>
                <li>No-code Strategy Builder</li>
                <li>Backtest + Trades + Exports</li>
                <li>Ruthless Mentor Feedback</li>
            </ul>

            <h3>Next</h3>
            <ul>
                <li>ML models per instrument</li>
                <li>XAI explanations</li>
                <li>Prop-firm risk layer</li>
            </ul>
        </div>
    </div>

</div>
""", unsafe_allow_html=True)

# ----------------------------------------
# FEATURES SECTION
# ----------------------------------------
st.markdown("""
<div class="section">
    <h2 class="section-title">Why VectorAlgoAI?</h2>

    <div class="features-grid">
        <div class="feature-box">
            <h4>No-Code Strategy Builder</h4>
            <p>Build institutional-style logic without touching code.</p>
        </div>

        <div class="feature-box">
            <h4>True Market Backtesting</h4>
            <p>Execution-quality rules, ATR stops, RR, and more.</p>
        </div>

        <div class="feature-box">
            <h4>Ruthless Mentor Feedback</h4>
            <p>Objective, brutal, PM-level commentary on your strategy.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ----------------------------------------
# FOOTER
# ----------------------------------------
st.markdown("""
<div class="footer">
    <p>© 2025 VectorAlgoAI — Built by Praveen Kumar • Product by Sandhya Moni</p>
</div>
""", unsafe_allow_html=True)
