import streamlit as st
import base64
import time

# -------------------------------------------------------
# Load CSS
# -------------------------------------------------------
def load_css():
    with open("styles.css", "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# -------------------------------------------------------
# SESSION INITIALIZATION
# -------------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# -------------------------------------------------------
# NAVIGATION BAR (top menu)
# -------------------------------------------------------
def navbar():
    st.markdown(
        """
        <div class="navbar">
            <div class="nav-left">
                <span class="brand">⚡ VectorAlgoAI</span>
            </div>
            <div class="nav-center">
                <a href="?page=home">Home</a>
                <a href="?page=product">Product</a>
                <a href="?page=pricing">Pricing</a>
                <a href="?page=dashboard">Dashboard</a>
            </div>
            <div class="nav-right">
                <a href="?page=login" class="login-btn">Login</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# -------------------------------------------------------
# ROUTING HANDLER
# -------------------------------------------------------
query_params = st.query_params

if "page" in query_params:
    st.session_state.page = query_params["page"]


# -------------------------------------------------------
# PAGE FUNCTIONS
# -------------------------------------------------------

# =======================
# HOME PAGE
# =======================
def page_home():
    navbar()

    st.markdown(
        """
        <div class="hero-shapes"></div>

        <div class="hero">
            <h1>Revolutionize<br>Your Trading Process</h1>
            <p class="hero-sub">
                AI-powered strategy validation, ruthless feedback, and ML-enhanced trading insights.
            </p>

            <div class="hero-buttons">
                <a href="?page=dashboard" class="cta-primary">🚀 Open Dashboard</a>
                <a href="?page=product" class="cta-secondary">📦 View Product</a>
            </div>
        </div>

        <div class="section">
            <h2 class="section-title">Why VectorAlgoAI?</h2>

            <div class="feature-grid">
                <div class="feature-card">⚙️ No-Code Strategy Builder</div>
                <div class="feature-card">📊 Backtest + Trades + Exports</div>
                <div class="feature-card">🧠 Ruthless Mentor Feedback</div>
                <div class="feature-card">🤖 ML Models (Phase 2)</div>
                <div class="feature-card">🔎 XAI Explanations</div>
                <div class="feature-card">🏛 Prop-Firm Risk Layer</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    footer()


# =======================
# PRODUCT PAGE
# =======================
def page_product():
    navbar()

    st.markdown(
        """
        <div class="section">
            <h2 class="section-title">What Makes VectorAlgoAI Different?</h2>

            <ul class="product-list">
                <li>We don’t predict blindly — we validate intelligently.</li>
                <li>We stress-test ideas across historical regimes.</li>
                <li>We explain WHY a strategy works or fails.</li>
                <li>We prepare traders for prop-firm evaluation reality.</li>
                <li>Upcoming: ML per instrument & XAI breakdowns.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    footer()


# =======================
# PRICING PAGE
# =======================
def page_pricing():
    navbar()

    st.markdown(
        """
        <div class="section">
            <h2 class="pricing-title">Pricing Plans Tailored For You</h2>

            <div class="pricing-grid">
                <div class="pricing-card">
                    <h3>€1 Starter</h3>
                    <p class="price">€1 / mo</p>
                    <ul>
                        <li>Strategy Builder</li>
                        <li>Basic Backtests</li>
                        <li>Exports</li>
                    </ul>
                </div>

                <div class="pricing-card highlight">
                    <h3>Pro</h3>
                    <p class="price">€29 / mo</p>
                    <ul>
                        <li>Advanced Filters</li>
                        <li>More Indicators</li>
                        <li>Better Reports</li>
                    </ul>
                </div>

                <div class="pricing-card">
                    <h3>Prop / Teams</h3>
                    <p class="price">€89 / mo</p>
                    <ul>
                        <li>Risk Layer</li>
                        <li>Team Libraries</li>
                        <li>Compliance Dashboard</li>
                    </ul>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    footer()


# =======================
# LOGIN PAGE
# =======================
def page_login():
    navbar()

    st.markdown("<div class='login-box'>", unsafe_allow_html=True)
    st.markdown("### Login to Continue")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login", use_container_width=True):
        if len(email) > 3:
            st.session_state.logged_in = True
            st.session_state.page = "dashboard"
            st.rerun()
        else:
            st.error("Invalid login.")

    st.markdown("</div>", unsafe_allow_html=True)
    footer()


# =======================
# DASHBOARD (built-in MVP)
# =======================
def page_dashboard():
    if not st.session_state.logged_in:
        st.session_state.page = "login"
        st.rerun()

    navbar()

    st.markdown("<h2>📊 VectorAlgoAI Dashboard</h2>", unsafe_allow_html=True)

    # RUN YOUR EXISTING MVP DASHBOARD HERE
    import mvp_dashboard
    mvp_dashboard.run_mvp_dashboard()

    footer()


# -------------------------------------------------------
# FOOTER
# -------------------------------------------------------
def footer():
    st.markdown(
        """
        <div class="footer">
            <div class="footer-brand">⚡ VectorAlgoAI</div>
            <div class="footer-links">
                <a href="?page=home">Home</a>
                <a href="?page=product">Product</a>
                <a href="?page=pricing">Pricing</a>
                <a href="?page=dashboard">Dashboard</a>
            </div>
            <div class="footer-social">
                <span>🌐</span>
                <span>📘</span>
                <span>📸</span>
                <span>🐦</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# -------------------------------------------------------
# PAGE ROUTING EXECUTION
# -------------------------------------------------------
if st.session_state.page == "home":
    page_home()
elif st.session_state.page == "product":
    page_product()
elif st.session_state.page == "pricing":
    page_pricing()
elif st.session_state.page == "login":
    page_login()
elif st.session_state.page == "dashboard":
    page_dashboard()

