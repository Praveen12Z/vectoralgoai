import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------------------------------
# LOAD CSS
# -----------------------------------------------------
def load_css():
    with open("styles.css", "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# -----------------------------------------------------
# TOP NAVIGATION BAR (WEBSITE)
# -----------------------------------------------------
st.markdown("""
<div class="top-nav">
    <div class="nav-left">
        <span class="brand">⚡ VectorAlgoAI</span>
    </div>

    <div class="nav-right">
        <a class="nav-item" href="?page=home">Home</a>
        <a class="nav-item" href="?page=features">Features</a>
        <a class="nav-item" href="?page=pricing">Pricing</a>
        <a class="nav-item" href="?page=product">Product</a>
        <a class="nav-item nav-dashboard" href="?page=dashboard">Dashboard</a>
    </div>
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------
# ROUTING LOGIC
# -----------------------------------------------------
page = st.query_params.get("page", ["home"])[0]


# -----------------------------------------------------
# 3️⃣ LANDING PAGE (HOME)
# -----------------------------------------------------
def render_home():
    st.markdown("""
    <div class="hero-section">
        <h1 class="hero-title">Revolutionize your trading workflow</h1>
        <p class="hero-sub">
            AI-powered strategy validation, ruthless insights, and real-time risk intelligence.
        </p>

        <div class="hero-buttons">
            <a href="?page=dashboard" class="cta-primary">🚀 Open Dashboard</a>
            <a href="?page=product" class="cta-secondary">📦 Explore Product</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Features Section
    st.markdown("""
    <div class="section-title">Built for real traders</div>

    <div class="feature-grid">
        <div class="feature-card">🤖 AI Strategy Builder<br><span>No code. Instant YAML.</span></div>
        <div class="feature-card">📉 Backtesting Engine<br><span>Fast, accurate, powerful.</span></div>
        <div class="feature-card">💀 Ruthless Mentor<br><span>Unfiltered institutional feedback.</span></div>
        <div class="feature-card">📊 ML Confidence Scoring<br><span>Coming next...</span></div>
    </div>
    """, unsafe_allow_html=True)


# -----------------------------------------------------
# 4️⃣ PRODUCT PAGE
# -----------------------------------------------------
def render_product():
    st.markdown("""
    <div class="section-title">What makes VectorAlgoAI different?</div>

    <ul class="product-list">
        <li>We don’t predict blindly — we validate ideas.</li>
        <li>We explain WHY a strategy succeeds or fails.</li>
        <li>We prepare traders for prop-firm evaluation reality.</li>
        <li>We bring ML + XAI to real trading workflows.</li>
    </ul>
    """ , unsafe_allow_html=True)


# -----------------------------------------------------
# 5️⃣ PRICING PAGE
# -----------------------------------------------------
def render_pricing():
    st.markdown("""
    <div class="section-title">Pricing Plans</div>

    <div class="pricing-grid">

        <div class="price-card">
            <h3>€1 Starter</h3>
            <p>Entry membership to build confidence</p>
            <ul>
                <li>Strategy Builder</li>
                <li>Backtesting</li>
                <li>Exports</li>
            </ul>
        </div>

        <div class="price-card price-popular">
            <h3>Pro</h3>
            <p>For serious weekly iterators</p>
            <ul>
                <li>Advanced filters</li>
                <li>Better reports</li>
                <li>More instruments</li>
            </ul>
        </div>

        <div class="price-card">
            <h3>Prop / Teams</h3>
            <p>Risk constraints + team strategy tools</p>
            <ul>
                <li>Risk layer</li>
                <li>Portfolio tools</li>
                <li>Team library</li>
            </ul>
        </div>

    </div>
    """ , unsafe_allow_html=True)


# -----------------------------------------------------
# 6️⃣ FEATURES PAGE
# -----------------------------------------------------
def render_features():
    st.markdown("""
    <div class="section-title">Supercharge your workflow</div>

    <div class="code-box">
    <pre>
// VectorAlgoAI ML Pipeline
def train_model(data):
    clean = preprocess(data)
    features = engineer(clean)
    model = fit(features)
    return model
    </pre>
    </div>
    """, unsafe_allow_html=True)


# -----------------------------------------------------
# 7️⃣ DASHBOARD PAGE (Dastone-style)
# -----------------------------------------------------
def render_dashboard():

    st.sidebar.markdown("<h2 class='sidebar-title'>📊 Dashboard</h2>", unsafe_allow_html=True)

    st.sidebar.write("Navigation")
    st.sidebar.button("Overview")
    st.sidebar.button("Analytics")
    st.sidebar.button("Trades")
    st.sidebar.button("Settings")

    st.markdown("<h1 class='dash-title'>Trading Dashboard</h1>", unsafe_allow_html=True)

    # KPI ROW
    col1, col2, col3 = st.columns(3)
    col1.metric("Win Rate", "54%", "+3%")
    col2.metric("Profit Factor", "1.42", "+0.12")
    col3.metric("Total Trades", "248", "+19")

    # Chart
    df = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "PnL": [1200, 900, 3000, 2800, 4000, 3500]
    })

    fig = px.line(df, x="Month", y="PnL", title="Equity Curve", markers=True)
    st.plotly_chart(fig, use_container_width=True)


# -----------------------------------------------------
# PAGE ROUTING EXECUTION
# -----------------------------------------------------
if page == "home":
    render_home()
elif page == "product":
    render_product()
elif page == "pricing":
    render_pricing()
elif page == "features":
    render_features()
elif page == "dashboard":
    render_dashboard()
else:
    render_home()
