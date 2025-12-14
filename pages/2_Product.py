import streamlit as st
from pages_shared import load_css, top_nav

st.set_page_config(page_title="VectorAlgoAI — Product", layout="wide")
load_css()
top_nav(active="Product")

st.markdown(
    """
    <div class="hero">
      <div class="hero-title" style="font-size:34px;">What makes VectorAlgoAI different?</div>
      <div class="hero-sub" style="max-width:900px;">
        You’re not buying “predictions”. You’re buying a system that turns strategy ideas into testable logic,
        then stress-tests them until they either become robust — or get exposed.
      </div>

      <div class="pricing-grid" style="margin-top:18px;">
        <div class="pricing">
          <div class="tier">We don’t predict blindly</div>
          <ul><li>Signals are validated against historical regimes</li><li>Confidence comes from evidence, not vibes</li></ul>
        </div>

        <div class="pricing">
          <div class="tier">We stress-test ideas</div>
          <ul><li>Backtest, trade logs, exports</li><li>Failure modes & brutal critique</li></ul>
        </div>

        <div class="pricing">
          <div class="tier">We explain why it fails</div>
          <ul><li>Next phase: XAI explanations</li><li>“why this signal, why now”</li></ul>
        </div>
      </div>
    </div>
    """,
    unsafe_allow_html=True
)
