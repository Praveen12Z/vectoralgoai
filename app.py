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
body, .stApp {
    background: radial-gradient(circle at 20% 20%, #001b2e 0%, #000814 90%) !important;
    color: #f8fafc !important;
    font-family: "Inter", sans-serif;
}
h1, h2, h3, h4 {font-weight: 700;}

.navbar {
    position: fixed; top: 0; left: 0; right: 0;
    height: 70px;
    background: rgba(0,0,0,0.4);
    backdrop-filter: blur(14px);
    display: flex; justify-content: space-between; align-items: center;
    padding: 0 4%;
    border-bottom: 1px solid rgba(255,255,255,0.07);
    z-index: 999;
}
.nav-logo {
    font-weight: 700;
    font-size: 1.3rem;
    color: #38bdf8;
    letter-spacing: 0.02em;
}
.nav-menu a {
    margin: 0 1rem;
    text-decoration: none;
    font-weight: 500;
    color: #e2e8f0;
    transition: 0.2s;
}
.nav-menu a:hover {
    color: #22d3ee;
}
.hero {
    text-align: center;
    padding-top: 120px;
    padding-bottom: 60px;
}
.hero h1 {
    font-size: 3rem;
    background: linear-gradient(90deg, #22d3ee, #a855f7, #22c55e);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: hue 6s linear infinite;
}
@keyframes hue { from {filter:hue-rotate(0deg);} to {filter:hue-rotate(360deg);} }
.hero p {
    max-width: 700px;
    margin: auto;
    color: #94a3b8;
    font-size: 1.1rem;
}
.btn-primary {
    background: linear-gradient(90deg, #22c55e, #16a34a);
    padding: 0.75rem 1.6rem;
    border-radius: 999px;
    font-weight: 600;
    color: #fff;
    box-shadow: 0 0 25px rgba(34,197,94,0.4);
    text-decoration: none;
    transition: all 0.25s;
}
.btn-primary:hover {
    transform: scale(1.05);
    box-shadow: 0 0 45px rgba(34,197,94,0.7);
}
.section {
    padding: 80px 10%;
    text-align: center;
}
.card-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 25px;
    margin-top: 40px;
}
.card {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 20px;
    padding: 25px;
    backdrop-filter: blur(8px);
    transition: 0.3s ease;
}
.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 35px rgba(0,255,200,0.08);
}
.countdown {
    margin-top: 30px;
    display: flex;
    justify-content: center;
    gap: 10px;
}
.countdown-item {
    background: rgba(255,255,255,0.05);
    border-radius: 10px;
    padding: 10px 14px;
    min-width: 70px;
}
.countnum { font-size: 1.4rem; font-weight: 700; color: #22d3ee; }
.countlbl { font-size: 0.75rem; color: #9ca3af; text-transform: uppercase; }
.footer {
    padding: 40px 0;
    text-align: center;
    font-size: 0.9rem;
    color: #64748b;
}
</style>
""", unsafe_allow_html=True)


# ---------------- Countdown ----------------
def countdown():
    now = datetime.now()
    delta = LAUNCH_DATE - now
    if delta.total_seconds() < 0:
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
    """.format(days, hrs, mins, secs), unsafe_allow_html=True)


# ---------------- Navbar ----------------
st.markdown("""
<div class="navbar">
  <div class="nav-logo">VectorAlgoAI</div>
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
      <p>Combine LSTM, GPT sentiment, and technical indicators to generate adaptive market signals.</p>
    </div>
    <div class="card">
      <h4>📰 News Intelligence</h4>
      <p>AI parses real-time news to align your strategy with market sentiment and macro events.</p>
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
  <div class="card-grid">
    <div class="card">
      <h4>Praveen Kumar</h4>
      <p>Founder · AI & Trading Automation<br>Creator of VectorAlgoAI, building the bridge between AI and practical trading systems.</p>
    </div>
    <div class="card">
      <h4>Sandhya Moni</h4>
      <p>Co-Founder · Strategy & Product<br>Leads the business vision and product strategy, ensuring VectorAlgoAI empowers every trader.</p>
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
  <h2>Stay Connected</h2>
  <p>We’re launching on <b>March 5, 2026</b>. Join our journey as we build the future of retail trading automation.</p>
  <a href="mailto:hello@vectoralgoai.com" class="btn-primary">Join Early Access</a>
</section>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="footer">
© {datetime.now().year} VectorAlgoAI · Built by Praveen Kumar · Strategy & Product by Sandhya Moni
</div>
""", unsafe_allow_html=True)
