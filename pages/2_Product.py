import streamlit as st
from pages_shared import load_css, top_nav

st.set_page_config(page_title="Product — VectorAlgoAI", layout="wide")
load_css()
top_nav(active="Product")

st.markdown(
"""
<div class='hero'>
  <div class='hero-title' style='font-size:34px;'>What makes VectorAlgoAI different?</div>

  <div class='hero-sub'>
    We don’t predict markets blindly — we stress-test ideas.
  </div>

  <div class='pricing-grid' style='margin-top:20px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:20px;'>

    <div class='card'>
      <h3>No Blind Predictions</h3>
      <ul>
        <li>Evidence-driven signals</li>
        <li>No black-box guessing</li>
      </ul>
    </div>

    <div class='card'>
      <h3>Stress-Test Engine</h3>
      <ul>
        <li>Backtest on real market conditions</li>
        <li>Find failure modes early</li>
      </ul>
    </div>

    <div class='card'>
      <h3>XAI (Next Phase)</h3>
      <ul>
        <li>Why this signal?</li>
        <li>Why now?</li>
        <li>When does it fail?</li>
      </ul>
    </div>

  </div>
</div>
""",
unsafe_allow_html=True
)
