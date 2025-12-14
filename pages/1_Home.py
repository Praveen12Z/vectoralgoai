import streamlit as st
from pages_shared import load_css, top_nav

st.set_page_config(page_title="Home — VectorAlgoAI", layout="wide")
load_css()
top_nav(active="Home")

st.markdown(
"""
<div class="hero">
  <div class="hero-grid">

    <div>
      <div class="hero-title">Build. Crash-test. Understand.</div>
      <div class="hero-sub">
        AI-powered strategy validation for serious traders.
      </div>

      <div class="hero-cta" style="margin-top:18px;">
        <a href="/Dashboard" class="cta-primary">🚀 Open Dashboard</a>
        <a href="/Product" class="cta-secondary">📦 See Product</a>
      </div>
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

  </div>
</div>
""",
unsafe_allow_html=True
)
