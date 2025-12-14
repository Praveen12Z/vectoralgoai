import streamlit as st
import os

CSS_PATH = "assets/styles.css"

if os.path.exists(CSS_PATH):
    with open(CSS_PATH) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
else:
    st.error(f"❌ CSS file not found: {CSS_PATH}")


# NAVBAR
st.markdown("""
<div class="navbar">
    <div class="left">
        <img src="https://i.imgur.com/FRQfZ4P.png" class="logo">
        <span class="brand">VectorAlgoAI</span>
    </div>
    <div class="center">
        <a href="#home">Home</a>
        <a href="#why">Why</a>
        <a href="#pricing">Pricing</a>
        <a href="#dashboard">Dashboard</a>
    </div>
    <div class="right">
        <button class="login-btn">Login</button>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------- HOME SECTION ----------
st.markdown("""
<div id="home" class="hero-section">
    <h1 class="hero-title">Revolutionize<br>Your Trading Process</h1>
    <p class="hero-subtitle">
        AI-powered strategy validation, ruthless feedback,<br>
        and ML-enhanced trading insights.
    </p>

    <div class="hero-buttons">
        <a onclick="window.location.href='#dashboard'" class="cta-primary">🚀 Open Dashboard</a>
        <a onclick="window.location.href='#why'" class="cta-secondary">📦 View Product</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------- WHY SECTION ----------
st.markdown("""
<div id="why" class="why-section">
    <h2>Why VectorAlgoAI?</h2>

    <div class="feature-grid">
        <div class="feature-card">⚡ No-Code Strategy Builder</div>
        <div class="feature-card">📊 Backtest + Trades + Exports</div>
        <div class="feature-card">🧠 Ruthless Mentor Feedback</div>
        <div class="feature-card">🤖 ML Models (Phase 2)</div>
        <div class="feature-card">👁️ XAI Explanations</div>
        <div class="feature-card">📉 Prop-Firm Risk Layer</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------- PRICING ----------
st.markdown("""
<div id="pricing" class="pricing-section">
    <h2>Pricing Plans</h2>

    <div class="pricing-grid">
        <div class="price-card">
            <h3>€1 Starter</h3>
            <p>Perfect for learning & testing.</p>
            <ul>
                <li>Strategy Builder</li>
                <li>Basic Backtest</li>
                <li>Exports</li>
            </ul>
        </div>

        <div class="price-card popular">
            <h3>Pro</h3>
            <p>Best for active traders.</p>
            <ul>
                <li>Advanced Indicators</li>
                <li>Better Reports</li>
                <li>Multi-Instrument</li>
            </ul>
        </div>

        <div class="price-card">
            <h3>Prop / Teams</h3>
            <p>For serious evaluation.</p>
            <ul>
                <li>Risk Layer</li>
                <li>Portfolio View</li>
                <li>Team Strategy Library</li>
            </ul>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------- DASHBOARD SECTION ----------
st.markdown('<div id="dashboard"></div>', unsafe_allow_html=True)

with st.container():
    st.write("## 📊 VectorAlgoAI – Strategy Crash-Test Dashboard")
    run_mvp_dashboard()
