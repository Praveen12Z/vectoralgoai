import streamlit as st
from pages_shared import load_css, top_nav

st.set_page_config(page_title="VectorAlgoAI — Home", layout="wide")
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
            Turn rules into YAML, backtest fast, get ruthless feedback — and iterate like a pro.
          </div>

          <div class="hero-cta">
            <a class="cta-primary" href="Dashboard">🚀 Open Dashboard</a>
            <a class="cta-secondary" href="Product">📦 See Product</a>
          </div>
        </div>

        <div class="card">
          <h3>MVP Today</h3>
          <ul>
            <li>Strategy Builder (No Code)</li>
            <li>Backtest + Trades + Exports</li>
            <li>Ruthless Mentor Feedback</li>
          </ul>
          <h3 style="margin-top:14px;">Next</h3>
          <ul>
            <li>ML models per instrument</li>
            <li>XAI explanations (why/when it fails)</li>
            <li>Prop-firm risk layer</li>
          </ul>
        </div>
      </div>
    </div>

    <div class="section-title">Pricing</div>
    <div class="pricing-grid">
      <div class="pricing">
        <div class="tier">€1 Starter</div>
        <div class="price">€1 / month</div>
        <ul>
          <li>Strategy Builder</li>
          <li>Basic Backtest</li>
          <li>Exports</li>
        </ul>
      </div>

      <div class="pricing">
        <div class="tier">Pro</div>
        <div class="price">Coming soon</div>
        <ul>
          <li>Advanced filters</li>
          <li>Better reports</li>
          <li>More instruments</li>
        </ul>
      </div>

      <div class="pricing">
        <div class="tier">Prop / Teams</div>
        <div class="price">Coming soon</div>
        <ul>
          <li>Risk constraints</li>
          <li>Portfolio view</li>
          <li>Team strategy library</li>
        </ul>
      </div>
    </div>
    """,
    unsafe_allow_html=True
)
