import streamlit as st
import os

st.set_page_config(layout="wide")

def load_css():
    css_path = "assets/styles.css"
    if os.path.exists(css_path):
        with open(css_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
load_css()

# Navbar
st.markdown("""
<div class="navbar">
    <div class="nav-left">VectorAlgoAI</div>
    <div class="nav-right">
        <a href="/" class="nav-item">Home</a>
        <a href="/Product" class="nav-item active">Product</a>
        <a href="/Dashboard" class="nav-item nav-cta">Dashboard</a>
    </div>
</div>
""", unsafe_allow_html=True)

st.title("📦 Product")

st.markdown("""
<div class="section">
    <h2 class="section-title">What Makes VectorAlgoAI Different?</h2>

    <div class="features-grid">
        <div class="feature-box">
            <h4>We Don’t Predict Blindly</h4>
            <p>We analyze structure, edge, and risk—not astrology.</p>
        </div>

        <div class="feature-box">
            <h4>Institutional-Grade Stress Testing</h4>
            <p>Your strategy faces the same pressure as at hedge funds.</p>
        </div>

        <div class="feature-box">
            <h4>Actionable Feedback</h4>
            <p>Ruthless mentor gives edge-focused improvements.</p>
        </div>
    </div>

    <br><br>

    <h3 class="section-sub">Machine Learning (Coming Next)</h3>

    <ul class="big-list">
        <li>Per-instrument ML models</li>
        <li>Confidence scoring, not blind predictions</li>
        <li>XAI: Why this signal, why now, when it fails</li>
        <li>Prop-firm risk engine with DD alignment</li>
    </ul>
</div>
""", unsafe_allow_html=True)
