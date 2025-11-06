import streamlit as st
from datetime import datetime

# ---------- CONFIG ----------
LAUNCH_DATE = datetime(2026, 3, 5, 0, 0, 0)  # 5 March 2026

st.set_page_config(
    page_title="VectorAlgoAI",
    page_icon="🔷",
    layout="wide"
)

# ---------- STYLE ----------
st.markdown(
    """
    <style>
    /* Global */
    body {
        background-color: #f5f7fb;
        color: #111827;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }

    .main {
        padding-top: 1rem;
    }

    /* Hero section */
    .hero-title {
        font-size: 2.6rem;
        font-weight: 800;
        color: #0f172a;
        line-height: 1.1;
    }

    .hero-subtitle {
        font-size: 1.1rem;
        color: #4b5563;
        margin-top: 0.8rem;
    }

    .pill {
        display: inline-block;
        padding: 0.25rem 0.9rem;
        border-radius: 999px;
        background: #e0f2fe;
        color: #0369a1;
        font-size: 0.8rem;
        font-weight: 600;
        letter-spacing: 0.03em;
        text-transform: uppercase;
    }

    .countdown-box {
        padding: 1rem 1.4rem;
        border-radius: 1rem;
        background: white;
        box-shadow: 0 18px 45px rgba(15, 23, 42, 0.07);
        border: 1px solid #e5e7eb;
    }

    .countdown-number {
        font-size: 1.8rem;
        font-weight: 700;
        color: #0f172a;
    }

    .countdown-label {
        font-size: 0.8rem;
        text-transform: uppercase;
        color: #6b7280;
        letter-spacing: 0.06em;
    }

    /* Section titles */
    .section-title {
        font-size: 1.6rem;
        font-weight: 700;
        margin-bottom: 0.2rem;
        color: #0f172a;
    }

    .section-subtitle {
        font-size: 0.95rem;
        color: #6b7280;
        margin-bottom: 1.2rem;
    }

    /* Cards */
    .card {
        padding: 1.1rem 1.2rem;
        border-radius: 1rem;
        background: white;
        border: 1px solid #e5e7eb;
        box-shadow: 0 10px 30px rgba(15, 23, 42, 0.04);
        height: 100%;
    }
    .card-title {
        font-size: 1.05rem;
        font-weight: 600;
        margin-bottom: 0.3rem;
        color: #111827;
    }
    .card-tag {
        font-size: 0.8rem;
        color: #2563eb;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        margin-bottom: 0.4rem;
    }
    .card-text {
        font-size: 0.9rem;
        color: #4b5563;
    }

    /* Footer */
    .footer {
        margin-top: 2.5rem;
        font-size: 0.8rem;
        color: #9ca3af;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- NAVIGATION ----------
menu = st.sidebar.radio(
    "Navigate",
    ["Home", "About", "Services", "Founders", "Contact"],
    index=0
)

st.sidebar.markdown("----")
st.sidebar.markdown("**VectorAlgoAI**")
st.sidebar.markdown("Built by **Praveen Kumar**  
Strategic lead: **Sandhya Moni**")

# ---------- UTIL ----------
def get_countdown():
    now = datetime.now()
    delta = LAUNCH_DATE - now
    if delta.total_seconds() <= 0:
        return None
    days = delta.days
    hours, rem = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(rem, 60)
    return days, hours, minutes, seconds


# ---------- PAGES ----------
if menu == "Home":
    # HERO
    st.markdown("<span class='pill'>Launching Soon · 5 March 2026</span>", unsafe_allow_html=True)
    st.markdown(
        "<div class='hero-title'>VectorAlgoAI</div>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<div class='hero-subtitle'>Describe your trading idea in plain English. "
        "VectorAlgoAI turns it into an AI-driven strategy, a working trading bot, "
        "and a clean dashboard — no code, no installs.</div>",
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([2, 1])

    with col1:
        st.write("")
        st.write("")
        st.markdown("### Why we’re building this")
        st.markdown(
            """
            - 🧠 **From idea to bot** – Traders explain their logic in natural language; the platform builds the rules & code.  
            - 🤖 **AI-driven execution** – ML models, technicals, and news sentiment combined into one engine.  
            - 📊 **No-code dashboard** – Trade, monitor, and debug your strategies in a clean web interface.  
            
            > Our goal is simple: give retail traders the kind of tools only quant firms usually have.
            """
        )
        st.button("🚀 Join early access (coming soon)", disabled=True)

    with col2:
        st.markdown("#### Launch Countdown")
        cd = get_countdown()
        if cd is None:
            st.success("VectorAlgoAI has launched 🎉")
        else:
            days, hours, minutes, seconds = cd
            st.markdown("<div class='countdown-box'>", unsafe_allow_html=True)
            c1, c2 = st.columns(2)
            c3, c4 = st.columns(2)

            c1.markdown(f"<div class='countdown-number'>{days}</div>"
                        "<div class='countdown-label'>Days</div>", unsafe_allow_html=True)
            c2.markdown(f"<div class='countdown-number'>{hours}</div>"
                        "<div class='countdown-label'>Hours</div>", unsafe_allow_html=True)
            c3.markdown(f"<div class='countdown-number'>{minutes}</div>"
                        "<div class='countdown-label'>Minutes</div>", unsafe_allow_html=True)
            c4.markdown(f"<div class='countdown-number'>{seconds}</div>"
                        "<div class='countdown-label'>Seconds</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

elif menu == "About":
    st.markdown("<div class='section-title'>About VectorAlgoAI</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='section-subtitle'>A next-generation trading lab for serious retail traders.</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        VectorAlgoAI is being built as a **strategy-to-bot platform**.

        Instead of writing code, traders describe what they want:
        *entries, exits, risk rules, indicators, and even how the bot should react to news*.

        Under the hood, VectorAlgoAI:
        - converts text into a structured strategy config,  
        - attaches machine-learning models per instrument,  
        - and serves everything through a web dashboard and future API.
        """
    )

    st.markdown("### Our vision")
    st.markdown(
        """
        - Build tools that feel like **quant infrastructure**, not a toy.  
        - Stay **transparent and explainable** – every signal should have a reason.  
        - Help traders move from **intuition → structured logic → automated execution**.
        """
    )

elif menu == "Services":
    st.markdown("<div class='section-title'>What the platform will offer</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='section-subtitle'>A first look at the VectorAlgoAI feature set for launch and beyond.</div>",
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<div class='card-tag'>Core</div>", unsafe_allow_html=True)
        st.markdown("<div class='card-title'>Strategy-to-Bot Engine</div>", unsafe_allow_html=True)
        st.markdown(
            "<div class='card-text'>Describe your idea in plain English. "
            "We generate rule-based logic, backtest-ready config, and an executable trading bot.</div>",
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with c2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<div class='card-tag'>AI Layer</div>", unsafe_allow_html=True)
        st.markdown("<div class='card-title'>ML & Sentiment Signals</div>", unsafe_allow_html=True)
        st.markdown(
            "<div class='card-text'>Instrument-specific ML models, technical indicators, "
            "and news sentiment combined into hybrid AI signals.</div>",
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with c3:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<div class='card-tag'>Dashboard</div>", unsafe_allow_html=True)
        st.markdown("<div class='card-title'>No-Code Trading Workspace</div>", unsafe_allow_html=True)
        st.markdown(
            "<div class='card-text'>Clean, responsive web dashboard with charts, open positions, "
            "signal explanations, and risk metrics.</div>",
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
            "<div class='card-text'>For traders who don't yet have a strategy, "
            "an interactive wizard helps design one based on risk, style, and market preferences.</div>",
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with c5:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<div class='card-tag'>Future</div>", unsafe_allow_html=True)
        st.markdown("<div class='card-title'>Prop-Firm & API Integrations</div>", unsafe_allow_html=True)
        st.markdown(
            "<div class='card-text'>Long-term, VectorAlgoAI aims to integrate with prop firms "
            "and offer APIs for professional automation and research.</div>",
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

elif menu == "Founders":
    st.markdown("<div class='section-title'>The people behind VectorAlgoAI</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='section-subtitle'>Built by traders and technologists who care about real-world edge.</div>",
        unsafe_allow_html=True,
    )

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<div class='card-title'>Praveen Kumar</div>", unsafe_allow_html=True)
        st.markdown("<div class='card-tag'>Founder · AI & Trading Automation</div>", unsafe_allow_html=True)
        st.markdown(
            "<div class='card-text'>Praveen combines a background in Artificial Intelligence with several years of "
            "hands-on trading experience. VectorAlgoAI is his way of giving retail traders access to the kind of tools "
            "usually reserved for quant desks — transparent, explainable, and deeply practical.</div>",
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with c2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<div class='card-title'>Sandhya Moni</div>", unsafe_allow_html=True)
        st.markdown("<div class='card-tag'>Co-Founder · Strategy & Product</div>", unsafe_allow_html=True)
        st.markdown(
            "<div class='card-text'>Sandhya leads the business and product strategy for VectorAlgoAI. "
            "With experience in digital product ownership and strategic planning, she ensures the platform is "
            "built around real trader problems, clear UX, and sustainable business value.</div>",
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

elif menu == "Contact":
    st.markdown("<div class='section-title'>Stay in the loop</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='section-subtitle'>We’re building VectorAlgoAI in public. "
        "Early supporters will get first access when we launch.</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        For now, this is a simple placeholder contact section.

        In the future we’ll add:
        - Email capture for early-access list  
        - Telegram / Discord community links  
        - A lightweight feedback form for feature requests  
        """
    )

    st.info("You can add a real email form or newsletter signup here later (SendGrid, Mailchimp, etc.).")

# ---------- FOOTER ----------
st.markdown(
    "<div class='footer'>© "
    + str(datetime.now().year)
    + " VectorAlgoAI · Built by Praveen Kumar · Strategy & Product by Sandhya Moni</div>",
    unsafe_allow_html=True,
)
