Nice, this is coming together really well now 👌

I’ve updated the page so that:

1. **Launch date is shown clearly together with the countdown** (“Launches on 5 March 2026”).
2. There’s a proper **Contact section** with all three emails:

   * `founder@vectoralgoai.com` (early access / founder)
   * `contact@vectoralgoai.com` (general queries)
   * `info@vectoralgoai.com` (info / docs)
3. The **“Join Early Access”** button now emails `founder@vectoralgoai.com`.

Below is the full, updated `app.py`. You can replace your current one with this.

---

### 🔁 Updated `app.py` (with launch date + full contact page)

```python
import streamlit as st
from datetime import datetime
from mvp_dashboard import run_mvp_dashboard

LAUNCH_DATE = datetime(2026, 3, 5, 0, 0, 0)

st.set_page_config(
    page_title="VectorAlgoAI | AI Trading SaaS Platform",
    page_icon="💹",
    layout="wide",
)

# ---------------- CSS ----------------
st.markdown("""
<style>
/* Hide default Streamlit chrome */
header[data-testid="stHeader"] {display: none;}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* Main container padding (because we removed header) */
.block-container {
    padding-top: 90px !important;
    padding-bottom: 40px !important;
}

/* Global background + typography */
body, .stApp {
    background: radial-gradient(circle at 20% 20%, #001b2e 0%, #000814 90%) !important;
    color: #f8fafc !important;
    font-family: "Inter", system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}
h1, h2, h3, h4 {font-weight: 700;}

/* NAVBAR */
.navbar {
    position: fixed; top: 0; left: 0; right: 0;
    height: 64px;
    background: rgba(3,7,18,0.85);
    backdrop-filter: blur(18px);
    display: flex; justify-content: space-between; align-items: center;
    padding: 0 5%;
    border-bottom: 1px solid rgba(148,163,184,0.35);
    z-index: 9999;
}
.nav-logo {
    display: flex; align-items: center; gap: 0.5rem;
    font-weight: 700;
    font-size: 1.15rem;
    color: #e5f2ff;
    letter-spacing: 0.04em;
}
.nav-logo-mark {
    width: 22px; height: 22px;
    border-radius: 7px;
    background: conic-gradient(from 160deg, #22d3ee, #a855f7, #22c55e, #22d3ee);
    box-shadow: 0 0 18px rgba(56,189,248,0.7);
}
.nav-logo span:last-child {
    background: linear-gradient(90deg, #38bdf8, #22c55e);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.nav-menu a {
    margin: 0 0.7rem;
    text-decoration: none;
    font-weight: 500;
    font-size: 0.95rem;
    color: #cbd5f5;
    transition: 0.18s ease;
}
.nav-menu a:hover {
    color: #22d3ee;
}

/* HERO */
.hero {
    text-align: center;
    padding-top: 10px;
    padding-bottom: 60px;
}
.hero h1 {
    font-size: 3rem;
    line-height: 1.15;
    margin-bottom: 0.7rem;
    background: linear-gradient(90deg, #22d3ee, #a855f7, #22c55e);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.hero p {
    max-width: 700px;
    margin: auto;
    color: #94a3b8;
    font-size: 1.05rem;
}
.hero-launch-text {
    margin-top: 0.6rem;
    font-size: 0.9rem;
    color: #a5b4fc;
    letter-spacing: 0.12em;
    text-transform: uppercase;
}

/* BUTTONS */
.btn-primary {
    background: radial-gradient(circle at 0% 0%, #4ade80, #16a34a);
    padding: 0.75rem 1.7rem;
    border-radius: 999px;
    font-weight: 600;
    color: #022c22;
    box-shadow: 0 0 26px rgba(34,197,94,0.55);
    text-decoration: none;
    display: inline-block;
    transition: all 0.25s;
}
.btn-primary:hover {
    transform: translateY(-1px) scale(1.04);
    box-shadow: 0 0 40px rgba(34,197,94,0.9);
}

/* SECTIONS */
.section {
    padding: 70px 8% 0 8%;
    text-align: center;
}
.section h2 {
    font-size: 2rem;
    margin-bottom: 0.4rem;
}
.section p {
    color: #94a3b8;
}

/* FEATURE CARDS */
.card-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 24px;
    margin-top: 40px;
}
.card {
    background: rgba(15,23,42,0.75);
    border: 1px solid rgba(148,163,184,0.45);
    border-radius: 20px;
    padding: 22px;
    backdrop-filter: blur(12px);
    box-shadow: 0 18px 45px rgba(15,23,42,0.9);
    transition: 0.25s ease;
}
.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 22px 55px rgba(34,197,94,0.25);
}
.card h4 {
    margin-bottom: 0.4rem;
}
.card p {
    color: #cbd5f5;
    font-size: 0.95rem;
}

/* COUNTDOWN */
.countdown-wrapper {
    margin-top: 26px;
}
.countdown-label {
    font-size: 0.9rem;
    color: #e5e7eb;
    margin-bottom: 0.4rem;
}
.countdown {
    display: flex;
    justify-content: center;
    gap: 10px;
    flex-wrap: wrap;
}
.countdown-item {
    background: rgba(15,23,42,0.85);
    border-radius: 12px;
    padding: 10px 14px;
    min-width: 70px;
    border: 1px solid rgba(148,163,184,0.45);
}
.countnum { font-size: 1.4rem; font-weight: 700; color: #22d3ee; }
.countlbl { font-size: 0.75rem; color: #9ca3af; text-transform: uppercase; }

/* FOOTER */
.footer {
    padding: 40px 0 10px 0;
    text-align: center;
    font-size: 0.9rem;
    color: #64748b;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Countdown helper ----------------
def countdown():
    now = datetime.now()
    delta = LAUNCH_DATE - now
    st.markdown(
        "<div class='countdown-wrapper'>"
        "<div class='countdown-label'>Launches on <strong>5 March 2026</strong></div>",
        unsafe_allow_html=True,
    )
    if delta.total_seconds() < 0:
        st.markdown("</div>", unsafe_allow_html=True)
        st.success("🚀 VectorAlgoAI has launched!")
        return
    days = delta.days
    hrs, rem = divmod(delta.seconds, 3600)
    mins, secs = divmod(rem, 60)
    st.markdown("""
    <div class='countdown'>
        <div class='countdown-item'><div class='countnum'>{}</div><div class='countlbl'>Days</div></div>
        <div class='countdown-item'><div class='countnum'>{}</div><div class='countlbl'>Hours</div></div>
        <div class='countdown-item'><div class='countnum'>{}</div><div class='countlbl'>Mins</div></div>
        <div class='countdown-item'><div class='countnum'>{}</div><div class='countlbl'>Secs</div></div>
    </div>
    </div>
    """.format(days, hrs, mins, secs), unsafe_allow_html=True)

# ---------------- Navbar ----------------
st.markdown("""
<div class="navbar">
  <div class="nav-logo">
    <div class="nav-logo-mark"></div>
    <span>VectorAlgoAI</span>
  </div>
  <div class="nav-menu">
    <a href="#home">Home</a>
    <a href="#services">Services</a>
    <a href="#founders">Founders</a>
    <a href="#mvp">MVP</a>
    <a href="#contact">Contact</a>
  </div>
</div>
""", unsafe_allow_html=True)

# ---------------- Hero ----------------
st.markdown("""
<section class="hero" id="home">
  <h1>Build AI-Driven Trading Bots. No Code. No Limits.</h1>
  <p>VectorAlgoAI turns your trading ideas into executable AI strategies — blending indicators, machine learning, and news sentiment in one unified dashboard.</p>
  <br>
  <a href="#mvp" class="btn-primary">Launch Trading Lab</a>
  <div class="hero-launch-text">Official launch · 5 March 2026</div>
</section>
""", unsafe_allow_html=True)

countdown()

# ---------------- Services ----------------
st.markdown("""
<section class="section" id="services">
  <h2>Our Core Features</h2>
  <p>Everything you need to go from idea → strategy → automation.</p>
  <div class="card-grid">
    <div class="card">
      <h4>🧠 Strategy-to-Bot Engine</h4>
      <p>Convert plain-English trading ideas into rule-based bots and executable strategies automatically.</p>
    </div>
    <div class="card">
      <h4>📈 Hybrid AI Signal Layer</h4>
      <p>Combine ML models, indicators, and regime filters to generate adaptive market signals.</p>
    </div>
    <div class="card">
      <h4>📰 News Intelligence</h4>
      <p>AI parses real-time news and macro events to align your strategy with sentiment and risk.</p>
    </div>
    <div class="card">
      <h4>🧩 Explainable Decisions</h4>
      <p>Every signal includes reasoning — transparency and trust in your AI system.</p>
    </div>
  </div>
</section>
""", unsafe_allow_html=True)

# ---------------- Founders ----------------
st.markdown("""
<section class="section" id="founders">
  <h2>Meet the Founders</h2>
  <p>Trading, AI, and product – aligned around one mission: empower serious retail traders.</p>
  <div class="card-grid">
    <div class="card">
      <h4>Praveen Kumar</h4>
      <p>Founder · AI & Trading Automation<br>Creator of VectorAlgoAI, building the bridge between practical trading and modern AI.</p>
    </div>
    <div class="card">
      <h4>Sandhya Moni</h4>
      <p>Co-Founder · Strategy & Product<br>Leads the business vision and product experience so the platform fits real trader workflows.</p>
    </div>
  </div>
</section>
""", unsafe_allow_html=True)

# ---------------- MVP ----------------
st.markdown("""
<section class="section" id="mvp">
  <h2>Live Trading Lab (MVP)</h2>
  <p>Prototype version of VectorAlgoAI’s interactive dashboard.</p>
</section>
""", unsafe_allow_html=True)
run_mvp_dashboard()

# ---------------- Contact ----------------
st.markdown("""
<section class="section" id="contact">
  <h2>Contact & Early Access</h2>
  <p>We’d love to hear from you. Reach out depending on what you need.</p>
  <div class="card-grid">
    <div class="card">
      <h4>🚀 Early Access & Founder Chat</h4>
      <p>Email: <a href="mailto:founder@vectoralgoai.com" style="color:#38bdf8;">founder@vectoralgoai.com</a><br>
      Use this to request early access, share your trading setup, or talk directly with the founder about the roadmap.</p>
    </div>
    <div class="card">
      <h4>📩 General Questions & Support</h4>
      <p>Email: <a href="mailto:contact@vectoralgoai.com" style="color:#38bdf8;">contact@vectoralgoai.com</a><br>
      For general inquiries, collaborations, or support once the platform is live.</p>
    </div>
    <div class="card">
      <h4>📚 Info & Documentation</h4>
      <p>Email: <a href="mailto:info@vectoralgoai.com" style="color:#38bdf8;">info@vectoralgoai.com</a><br>
      For documentation, press material, or anything related to how VectorAlgoAI works under the hood.</p>
    </div>
  </div>
  <br>
  <a href="mailto:founder@vectoralgoai.com?subject=VectorAlgoAI%20Early%20Access" class="btn-primary">
    Join Early Access
  </a>
</section>
""", unsafe_allow_html=True)

# ---------------- Footer ----------------
st.markdown(f"""
<div class="footer">
© {datetime.now().year} VectorAlgoAI · Built by Praveen Kumar · Strategy & Product by Sandhya Moni ·
Contact: founder@vectoralgoai.com · contact@vectoralgoai.com · info@vectoralgoai.com
</div>
""", unsafe_allow_html=True)
```

---

Once you paste this into `app.py`, commit, push, and redeploy:

* Above the countdown you’ll see **“Launches on 5 March 2026”** and below the hero: **“Official launch · 5 March 2026”**
* The **Contact** section will have three clear cards plus the **Join Early Access** button sending to `founder@vectoralgoai.com`.

If you want to tweak wording or which email is used where, tell me and I’ll adjust copy + links.
