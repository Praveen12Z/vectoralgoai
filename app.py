import streamlit as st

# ------------------ THEME / CSS ------------------
BRAND = {
    "bg": "#0B1220",
    "panel": "#0F1A2E",
    "text": "#E6EEF8",
    "muted": "#9FB3C8",
    "blue": "#4F8CFF",
    "cyan": "#2BE4FF",
    "border": "rgba(255,255,255,0.10)",
}

def inject_css():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: radial-gradient(1200px 600px at 10% 10%, rgba(79,140,255,0.22), transparent 60%),
                        radial-gradient(900px 500px at 90% 20%, rgba(43,228,255,0.14), transparent 55%),
                        {BRAND["bg"]};
            color: {BRAND["text"]};
        }}
        h1, h2, h3, h4, h5, h6, p, div, span {{
            color: {BRAND["text"]};
        }}
        .va-card {{
            background: linear-gradient(180deg, rgba(255,255,255,0.05), rgba(255,255,255,0.02));
            border: 1px solid {BRAND["border"]};
            border-radius: 18px;
            padding: 18px 18px;
        }}
        .va-pill {{
            display: inline-block;
            padding: 6px 10px;
            border-radius: 999px;
            border: 1px solid {BRAND["border"]};
            background: rgba(255,255,255,0.03);
            color: {BRAND["muted"]};
            font-size: 12px;
        }}
        .va-hero-title {{
            font-size: 44px;
            font-weight: 800;
            line-height: 1.05;
            letter-spacing: -0.02em;
        }}
        .va-hero-sub {{
            color: {BRAND["muted"]};
            font-size: 16px;
            line-height: 1.6;
        }}
        .va-btn a {{
            text-decoration: none;
            font-weight: 700;
            color: white !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="VectorAlgoAI — Turn strategies into bots",
    page_icon="🧠",
    layout="wide",
)

inject_css()

# ------------------ TOP NAV ------------------
top = st.columns([3, 1, 1, 1])
with top[0]:
    st.markdown("### **VectorAlgoAI**")
with top[1]:
    st.page_link("pages/1_Product.py", label="Product", icon="📦")
with top[2]:
    st.page_link("pages/2_Dashboard.py", label="Dashboard", icon="📊")
with top[3]:
    st.markdown('<div class="va-pill">Launch target: 25 Jan 2026</div>', unsafe_allow_html=True)

st.write("")
st.write("")

# ------------------ HERO ------------------
left, right = st.columns([1.2, 1])

with left:
    st.markdown('<div class="va-pill">AI Trading SaaS • Strategy → Backtest → Insights</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="va-hero-title">
            Turn trading ideas into<br/>
            <span style="color:#4F8CFF">bots</span> — instantly.
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <div class="va-hero-sub">
        VectorAlgoAI helps retail traders describe a strategy in plain English, generate a structured strategy,
        backtest it on real market data, and get brutally clear feedback — fast.
        <br/><br/>
        <b>Later:</b> ML + XAI explanations for “why this signal” and “when it fails”.
        </div>
        """,
        unsafe_allow_html=True
    )

    cta = st.columns([1, 1, 2])
    with cta[0]:
        st.page_link("pages/2_Dashboard.py", label="🚀 Open Dashboard", use_container_width=True)
    with cta[1]:
        st.page_link("pages/1_Product.py", label="📦 See Product", use_container_width=True)

with right:
    st.markdown(
        f"""
        <div class="va-card">
            <h3 style="margin:0 0 6px 0;">Business Goal</h3>
            <p style="margin:0;color:{BRAND["muted"]};">
            Acquire <b>1,000 paying users</b> in the first 6 months and reach ~<b>€85,000/year</b> via a low-cost membership,
            while validating product-market fit in retail trading + prop firm space.
            </p>
            <hr style="border:0;border-top:1px solid {BRAND["border"]};margin:14px 0;">
            <h4 style="margin:0 0 6px 0;">MVP Today</h4>
            <ul style="margin:0;color:{BRAND["muted"]};">
              <li>Strategy Builder (no code)</li>
              <li>Backtest + trades + exports</li>
              <li>Ruthless mentor feedback</li>
            </ul>
            <hr style="border:0;border-top:1px solid {BRAND["border"]};margin:14px 0;">
            <h4 style="margin:0 0 6px 0;">Next</h4>
            <ul style="margin:0;color:{BRAND["muted"]};">
              <li>ML models per instrument</li>
              <li>XAI explanations (why / confidence / drivers)</li>
              <li>Prop-ready constraints + risk layer</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")
st.write("")

# ------------------ FEATURE STRIP ------------------
a, b, c = st.columns(3)
with a:
    st.markdown('<div class="va-card"><h4>🧩 Strategy → YAML</h4><p style="color:#9FB3C8;margin:0;">Convert rules into structured config with indicators, entries, exits, risk.</p></div>', unsafe_allow_html=True)
with b:
    st.markdown('<div class="va-card"><h4>🧪 Crash-Test</h4><p style="color:#9FB3C8;margin:0;">Backtest fast, see trades, equity, failure modes, and exports.</p></div>', unsafe_allow_html=True)
with c:
    st.markdown('<div class="va-card"><h4>🧠 Mentor Feedback</h4><p style="color:#9FB3C8;margin:0;">Brutal review: what breaks, what to fix, what’s deployable.</p></div>', unsafe_allow_html=True)

st.write("")
st.write("")

# ------------------ PRICING ------------------
st.markdown("## Pricing")
p1, p2, p3 = st.columns(3)

with p1:
    st.markdown(
        '<div class="va-card"><h3>€1 Starter</h3><p style="color:#9FB3C8;">Entry membership to build trust + traction.</p><ul style="color:#9FB3C8;"><li>Strategy Builder</li><li>Basic Backtest</li><li>Exports</li></ul></div>',
        unsafe_allow_html=True
    )
with p2:
    st.markdown(
        '<div class="va-card"><h3>Pro</h3><p style="color:#9FB3C8;">Serious traders who iterate weekly.</p><ul style="color:#9FB3C8;"><li>Advanced filters</li><li>Better reports</li><li>More instruments</li></ul></div>',
        unsafe_allow_html=True
    )
with p3:
    st.markdown(
        '<div class="va-card"><h3>Prop / Teams</h3><p style="color:#9FB3C8;">Risk constraints + compliance style checks.</p><ul style="color:#9FB3C8;"><li>Risk layer</li><li>Portfolio view</li><li>Team strategy library</li></ul></div>',
        unsafe_allow_html=True
    )

st.write("")
st.caption("Built by Praveen Kumar • VectorAlgoAI")
