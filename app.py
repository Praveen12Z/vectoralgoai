import streamlit as st
from datetime import datetime
from mvp_dashboard import run_mvp_dashboard

LAUNCH_DATE = datetime(2026, 3, 5, 0, 0, 0)

# Basic page config
st.set_page_config(
    page_title="VectorAlgoAI – AI Trading SaaS",
    page_icon="🧠",
    layout="wide",
)

# ----------------------- GLOBAL STYLES -----------------------
st.markdown(
    """
    <style>
    /* Remove default padding */
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 1.5rem;
        max-width: 1200px;
    }

    /* Dark gradient background */
    body, .stApp {
        background: radial-gradient(circle at top left, #0f766e 0%, #020617 45%, #000000 100%) !important;
        color: #e5e7eb;
        font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #020617 0%, #020617 40%, #022c22 100%) !important;
        border-right: 1px solid rgba(148, 163, 184, 0.25);
    }

    .sidebar-title {
        font-size: 1.1rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: #a5b4fc;
    }

    /* Hero */
    .hero-pill {
        display: inline-flex;
        align-items: center;
        padding: 0.25rem 0.9rem;
        border-radius: 999px;
        background: linear-gradient(90deg, #22c55e 0%, #22d3ee 100%);
        color: #022c22;
        font-size: 0.7rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.12em;
    }

    .hero-eyebrow {
        font-size: 0.85rem;
        color: #a5b4fc;
        text-transform: uppercase;
        letter-spacing: 0.18em;
        margin-top: 0.8rem;
        margin-bottom: 0.2rem;
    }

    .hero-title {
        font-size: 2.6rem;
        font-weight: 800;
        line-height: 1.05;
        letter-spacing: -0.04em;
        color: #f9fafb;
    }

    .hero-gradient-text {
        background: linear-gradient(90deg, #22c55e, #a855f7, #38bdf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero-subtitle {
        font-size: 1rem;
        color: #9ca3af;
        margin-top: 0.8rem;
        max-width: 32rem;
    }

    .hero-buttons {
        margin-top: 1.4rem;
        display: flex;
        gap: 0.8rem;
        flex-wrap: wrap;
    }

    .btn-primary {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        padding: 0.55rem 1.4rem;
        border-radius: 999px;
        background: radial-gradient(circle at 0% 0%, #22c55e 0%, #16a34a 45%, #15803d 100%);
        color: #022c22;
        font-size: 0.9rem;
        font-weight: 700;
        text-decoration: none;
        box-shadow: 0 0 25px rgba(34, 197, 94, 0.45);
        border: 1px solid rgba(74, 222, 128, 0.6);
    }

    .btn-secondary {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        padding: 0.55rem 1.4rem;
        border-radius: 999px;
        background: rgba(15, 23, 42, 0.8);
        color: #e5e7eb;
        font-size: 0.9rem;
        font-weight: 600;
        text-decoration: none;
        border: 1px solid rgba(148, 163, 184, 0.6);
    }

    .btn-secondary span {
        color: #22c55e;
        margin-left: 0.4rem;
    }

    /* Countdown bar */
    .countdown-wrapper {
        margin-top: 1.6rem;
        padding: 0.85rem 1.1rem;
        border-radius: 999px;
        border: 1px solid rgba(148, 163, 184, 0.4);
        background: radial-gradient(circle at top left, rgba(16, 185, 129, 0.2), rgba(15, 23, 42, 0.8));
        display: flex;
        align-items: center;
        gap: 1.5rem;
    }

    .countdown-label-main {
        font-size: 0.9rem;
        color: #e5e7eb;
        font-weight: 600;
    }

    .countdown-chip {
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.14em;
        color: #a5b4fc;
    }

    .countdown-pill {
        display: inline-flex;
        padding: 0.25rem 0.65rem;
        border-radius: 999px;
        background: rgba(15, 23, 42, 0.9);
        border: 1px solid rgba(148, 163, 184, 0.5);
        font-size: 0.8rem;
    }

    .count-num {
        font-weight: 700;
        color: #f9fafb;
        margin-right: 0.2rem;
    }
    .count-unit {
        color: #9ca3af;
        text-transform: uppercase;
        font-size: 0.7rem;
    }

    /* Right hero card */
    .hero-card {
        border-radius: 1.5rem;
        padding: 1.4rem 1.3rem;
        background: radial-gradient(circle at top left, rgba(45, 212, 191, 0.25), rgba(15, 23, 42, 0.95));
        border: 1px solid rgba(94, 234, 212, 0.4);
        box-shadow: 0 26px 70px rgba(8, 47, 73, 0.9);
        position: relative;
        overflow: hidden;
        min-height: 250px;
    }

    .hero-card-badge {
        font-size: 0.7rem;
        text-transform: uppercase;
        letter-spacing: 0.16em;
        color: #a5b4fc;
    }

    .hero-card-title {
        font-size: 1.2rem;
        font-weight: 700;
        margin-top: 0.4rem;
        margin-bottom: 0.4rem;
        color: #f9fafb;
    }

    .hero-card-text {
        font-size: 0.85rem;
        color: #d1d5db;
        max-width: 16rem;
    }

    .hero-glow-orb {
        position: absolute;
        width: 160px;
        height: 160px;
        border-radius: 999px;
        right: -40px;
        bottom: -40px;
        background: radial-gradient(circle, #22c55e 0%, #166534 40%, transparent 70%);
        opacity: 0.95;
        filter: blur(1px);
    }

    .hero-metric-pill {
        position: absolute;
        left: 1.1rem;
        bottom: 1.1rem;
        padding: 0.35rem 0.7rem;
        border-radius: 999px;
        background: rgba(15,23,42,0.9);
        border: 1px solid rgba(148,163,184,0.55);
        font-size: 0.75rem;
        color: #e5e7eb;
    }

    .hero-metric-pill span {
        color: #22c55e;
        font-weight: 600;
    }

    /* Sections */
    .section-title {
        font-size: 1.6rem;
        font-weight: 700;
        color: #f9fafb;
        margin-bottom: 0.35rem;
    }

    .section-subtitle {
        font-size: 0.95rem;
        color: #9ca3af;
        margin-bottom: 1.2rem;
    }

    .card {
        padding: 1.2rem 1.3rem;
        border-radius: 1.2rem;
        background: radial-gradient(circle at top left, rgba(30, 64, 175, 0.35), rgba(15, 23, 42, 0.96));
        border: 1px solid rgba(148, 163, 184, 0.55);
        box-shadow: 0 20px 45px rgba(15, 23, 42, 0.95);
        height: 100%;
    }

    .card-tag {
        font-size: 0.75rem;
        letter-spacing: 0.16em;
        text-transform: uppercase;
        color: #a5b4fc;
        margin-bottom: 0.35rem;
    }

    .card-title {
        font-size: 1.05rem;
        font-weight: 600;
        color: #e5e7eb;
        margin-bottom: 0.4rem;
    }

    .card-text {
        font-size: 0.9rem;
        color: #cbd5f5;
    }

    .founder-name {
        font-size: 1.05rem;
        font-weight: 600;
        color: #f9fafb;
        margin-bottom: 0.2rem;
    }

    .founder-role {
        font-size: 0.8rem;
        letter-spacing: 0.16em;
        text-transform: uppercase;
        color: #a5b4fc;
        margin-bottom: 0.4rem;
    }

    .footer {
        margin-top: 2.8rem;
        font-size: 0.8rem;
        text-align: center;
        color: #6b7280;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------- HELPERS -----------------------
def get_countdown():
    now = datetime.now()
    delta = LAUNCH_DATE - now
    if delta.total_seconds() <= 0:
        return None
    days = delta.days
    hours, rem = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(rem, 60)
    return days, hours, minutes, seconds


# ----------------------- SIDEBAR NAV -----------------------
st.sidebar.markdown("<div class='sidebar-title'>VectorAlgoAI</div>", unsafe_allow_html=True)
st.sidebar.markdown("Built by **Praveen Kumar**  \nStrategic & product by **Sandhya Moni**")

menu = st.sidebar.radio(
    "Navigate",
    ["Home", "About", "Services", "Founders", "Trading Lab (MVP)", "Contact"],
    index=0,
)


# ----------------------- PAGES -----------------------
if menu == "Home":
    col_left, col_right = st.columns([1.6, 1.2])

    with col_left:
        st.markdown("<div class='hero-pill'>AI Trading SaaS · Launching Soon</div>", unsafe_allow_html=True)
        st.markdown("<div class='hero-eyebrow'>Launching · 5 March 2026</div>", unsafe_allow_html=True)
        st.markdown(
            """
            <div class="hero-title">
                The <span class="hero-gradient-text">AI-native trading lab</span>  
                for serious retail traders.
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <div class="hero-subtitle">
                Describe your strategy in plain English. VectorAlgoAI turns it into 
                executable logic, AI-enhanced signals, and a live trading dashboard –
                without writing a single line of code.
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="hero-buttons">
                <a class="btn-primary" href="#mvp" onclick="window.location.reload(false);">
                    Get early access
                </a>
                <a class="btn-secondary" href="#learn">
                    Learn more <span>↗</span>
                </a>
            </div>
            """,
            unsafe_allow_html=True,
        )

        cd = get_countdown()
        if cd is not None:
            d, h, m, s = cd
            st.markdown(
                f"""
                <div class="countdown-wrapper">
                    <div>
                        <div class="countdown-chip">Countdown to launch</div>
                        <div class="countdown-label-main">
                            VectorAlgoAI goes live on <strong>5 March 2026</strong>.
                        </div>
                    </div>
                    <div class="countdown-pill">
                        <span class="count-num">{d}</span><span class="count-unit">days</span>
                    </div>
                    <div class="countdown-pill">
                        <span class="count-num">{h}</span><span class="count-unit">hrs</span>
                    </div>
                    <div class="countdown-pill">
                        <span class="count-num">{m}</span><span class="count-unit">min</span>
                    </div>
                    <div class="countdown-pill">
                        <span class="count-num">{s}</span><span class="count-unit">sec</span>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.success("VectorAlgoAI has launched 🎉")

    with col_right:
        st.markdown(
            """
            <div class="hero-card">
                <div class="hero-card-badge">Live trading preview</div>
                <div class="hero-card-title">AI-enhanced signal engine</div>
                <div class="hero-card-text">
                    Hybrid models combining price action, technical indicators, and
                    macro news sentiment – designed to help you navigate volatility
                    with conviction, not noise.
                </div>
                <div class="hero-metric-pill">
                    Reimagining retail trading with <span>explainable AI</span>.
                </div>
                <div class="hero-glow-orb"></div>
            </div>
            """,
            unsafe_allow_html=True,
        )

elif menu == "About":
    st.markdown('<div id="learn"></div>', unsafe_allow_html=True)
    st.markdown("<div class='section-title'>About VectorAlgoAI</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='section-subtitle'>Built for traders who want quant-grade tooling without the quant-sized team.</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        VectorAlgoAI is a **strategy-to-bot platform** for retail traders and prop-firm traders.

        Instead of wrestling with code, you describe your idea:

        - *“Buy XAUUSD when London session breaks yesterday’s high with strong news flow.”*  
        - *“Fade mean-reversion on EURUSD when volatility compresses near key levels.”*  

        Our engine translates that into:
        - structured strategy config,  
        - execution-ready logic,  
        - and a live dashboard that you can monitor, tweak, and scale.
        """
    )

    st.markdown("### Our core principles")
    st.markdown(
        """
        - **Explainability first** – every signal comes with a human-readable explanation.  
        - **You in the loop** – the system learns from your behaviour and preferences.  
        - **No black-box magic** – we combine ML, rules, and risk in a way you can actually trust.
        """
    )

elif menu == "Services":
    st.markdown("<div class='section-title'>What VectorAlgoAI will offer</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='section-subtitle'>From idea capture to execution, all in one AI-native workspace.</div>",
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<div class='card-tag'>Core Engine</div>", unsafe_allow_html=True)
        st.markdown("<div class='card-title'>Strategy-to-Bot builder</div>", unsafe_allow_html=True)
        st.markdown(
            "<div class='card-text'>Turn natural-language strategy descriptions into structured rules, "
            "backtest-ready configs, and a deployable execution bot – all inside a browser.</div>",
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with c2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<div class='card-tag'>AI Signal Layer</div>", unsafe_allow_html=True)
        st.markdown("<div class='card-title'>Hybrid technical + ML</div>", unsafe_allow_html=True)
        st.markdown(
            "<div class='card-text'>Instrument-specific classifiers and time-series models combined with "
            "indicators, regime detection, and risk overlays to produce interpretable signals.</div>",
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with c3:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<div class='card-tag'>News & Macro</div>", unsafe_allow_html=True)
        st.markdown("<div class='card-title'>Sentiment-aware trading</div>", unsafe_allow_html=True)
        st.markdown(
            "<div class='card-text'>Headline feeds and economic calendars are summarised by GPT-style models, "
            "then aligned with your strategy so you can see when fundamentals confirm or fight your signals.</div>",
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("")
    c4, c5 = st.columns(2)

    with c4:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<div class='card-tag'>Onboarding</div>", unsafe_allow_html=True)
        st.markdown("<div class='card-title'>AI Strategy Wizard</div>", unsafe_allow_html=True)
        st.markdown(
            "<div class='card-text'>For traders who are still shaping their edge, an interactive wizard "
            "asks about risk tolerance, markets, and style – then proposes a starting framework you can refine.</div>",
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with c5:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<div class='card-tag'>Future</div>", unsafe_allow_html=True)
        st.markdown("<div class='card-title'>Prop-firm & API integrations</div>", unsafe_allow_html=True)
        st.markdown(
            "<div class='card-text'>Long-term, VectorAlgoAI aims to plug into prop-firm accounts and provide "
            "an API layer so advanced users and teams can build on top of the platform.</div>",
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

elif menu == "Founders":
    st.markdown("<div class='section-title'>Founders</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='section-subtitle'>Trading, AI, and product – aligned around one mission: "
        "give retail traders serious tools.</div>",
        unsafe_allow_html=True,
    )

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<div class='founder-name'>Praveen Kumar</div>", unsafe_allow_html=True)
        st.markdown("<div class='founder-role'>Founder · AI & Trading Automation</div>", unsafe_allow_html=True)
        st.markdown(
            "<div class='card-text'>Praveen blends a background in Artificial Intelligence with years of live "
            "trading experience. VectorAlgoAI started as his attempt to build the kind of explainable, "
            "hybrid AI tools he wished he had when trading discretionary and systematic strategies.</div>",
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with c2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<div class='founder-name'>Sandhya Moni</div>", unsafe_allow_html=True)
        st.markdown("<div class='founder-role'>Co-Founder · Strategy & Product</div>", unsafe_allow_html=True)
        st.markdown(
            "<div class='card-text'>Sandhya leads the product and business side of VectorAlgoAI. "
            "With a background in digital product ownership and strategy, she ensures the platform stays anchored "
            "to real trader workflows, clear UX, and a sustainable SaaS model.</div>",
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

elif menu == "Trading Lab (MVP)":
    st.markdown("<div id='mvp'></div>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Trading Lab (MVP)</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='section-subtitle'>This is the live prototype of the VectorAlgoAI dashboard – "
        "where strategy configs, signals, and charts come together.</div>",
        unsafe_allow_html=True,
    )
    run_mvp_dashboard()

elif menu == "Contact":
    st.markdown("<div class='section-title'>Stay in the loop</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='section-subtitle'>We’re building VectorAlgoAI in public. "
        "Early supporters will get first access when we open the doors.</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        For now, this is a lightweight contact section.

        In the next iterations we’ll add:

        - Email capture for an **early-access waitlist**  
        - A Telegram / Discord community for feedback and roadmap voting  
        - A simple form so you can tell us about your **current trading setup** and tools
        """
    )

    st.info("You can add a real email / newsletter integration here later using services like Mailchimp or SendGrid.")

# ----------------------- FOOTER -----------------------
st.markdown(
    f"<div class='footer'>© {datetime.now().year} VectorAlgoAI · Built by Praveen Kumar · "
    "Strategy & Product by Sandhya Moni</div>",
    unsafe_allow_html=True,
)
