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
header[data-testid="stHeader"] {display:none;}
#MainMenu, footer {visibility:hidden;}

.block-container {padding-top:90px!important; padding-bottom:40px!important;}
body,.stApp {
  background:radial-gradient(circle at 20% 20%,#001b2e 0%,#000814 90%)!important;
  color:#f8fafc!important;
  font-family:"Inter",system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
}
h1,h2,h3,h4{font-weight:700;color:#f9fafb}

/* Navbar */
.navbar{
  position:fixed;top:0;left:0;right:0;height:64px;
  background:rgba(3,7,18,0.9);backdrop-filter:blur(18px);
  display:flex;justify-content:space-between;align-items:center;
  padding:0 5%;border-bottom:1px solid rgba(148,163,184,0.3);z-index:9999;
}
.nav-logo{
  display:flex;align-items:center;gap:.5rem;
  font-weight:700;font-size:1.15rem;color:#e5f2ff;letter-spacing:.04em;
}
.nav-logo-mark{
  width:22px;height:22px;border-radius:7px;
  background:conic-gradient(from 160deg,#22d3ee,#a855f7,#22c55e,#22d3ee);
  box-shadow:0 0 18px rgba(56,189,248,0.7);
}
.nav-logo span:last-child{
  background:linear-gradient(90deg,#38bdf8,#22c55e);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
}
.nav-menu a{
  margin:0 .7rem;text-decoration:none;font-weight:500;font-size:.95rem;
  color:#cbd5f5;transition:.18s ease;
}
.nav-menu a:hover{color:#22d3ee}

/* Hero */
.hero{text-align:center;padding-top:10px;padding-bottom:60px;}
.hero h1{
  font-size:3.1rem;
  line-height:1.15;
  margin-bottom:0.7rem;
  background:linear-gradient(90deg,#22d3ee,#a855f7,#22c55e);
  -webkit-background-clip:text;
  -webkit-text-fill-color:transparent;
}
.hero p{
  max-width:700px;
  margin:auto;
  color:#94a3b8;
  font-size:1.05rem;
}

/* Glowing Launch Box */
@keyframes pulseGlow{
  0%{box-shadow:0 0 15px rgba(34,197,94,.4),0 0 30px rgba(34,197,94,.6);}
  50%{box-shadow:0 0 35px rgba(34,197,94,.8),0 0 55px rgba(34,197,94,1);}
  100%{box-shadow:0 0 15px rgba(34,197,94,.4),0 0 30px rgba(34,197,94,.6);}
}
.launch-box{
  display:inline-flex;
  align-items:center;
  justify-content:center;
  gap:10px;
  margin-top:25px;
  padding:14px 40px;
  border-radius:20px;
  background:rgba(16,185,129,0.12);
  border:1px solid rgba(34,197,94,0.5);
  color:#a7f3d0;
  font-size:1.25rem;
  font-weight:600;
  text-shadow:0 0 10px rgba(52,211,153,0.6);
  backdrop-filter:blur(8px);
  animation:pulseGlow 2.5s infinite ease-in-out;
}
.launch-box span{color:#22c55e;font-weight:700;}

/* Countdown */
.countdown-wrapper{margin-top:28px;}
.countdown{
  display:flex;
  justify-content:center;
  gap:12px;
  flex-wrap:wrap;
}
.countdown-item{
  background:rgba(15,23,42,.85);
  border-radius:12px;
  padding:12px 16px;
  min-width:75px;
  border:1px solid rgba(148,163,184,.45);
}
.countnum{font-size:1.5rem;font-weight:700;color:#22d3ee;}
.countlbl{font-size:.8rem;color:#9ca3af;text-transform:uppercase;}

/* Buttons */
.btn-primary{
  background:radial-gradient(circle at 0% 0%,#4ade80,#16a34a);
  padding:.8rem 1.8rem;
  border-radius:999px;
  font-weight:600;
  color:#022c22;
  box-shadow:0 0 26px rgba(34,197,94,.55);
  text-decoration:none;
  display:inline-block;
  transition:all .25s;
}
.btn-primary:hover{
  transform:translateY(-1px) scale(1.04);
  box-shadow:0 0 40px rgba(34,197,94,.9);
}

/* Section Layouts */
.section{padding:70px 8% 0 8%;text-align:center;}
.section h2{font-size:2rem;margin-bottom:.4rem;}
.section p{color:#94a3b8;max-width:720px;margin:auto;}

/* Cards */
.card-grid{
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(260px,1fr));
  gap:24px;
  margin-top:40px;
}
.card{
  background:rgba(15,23,42,0.8);
  border:1px solid rgba(148,163,184,0.45);
  border-radius:20px;
  padding:22px;
  backdrop-filter:blur(12px);
  box-shadow:0 18px 45px rgba(15,23,42,0.9);
  transition:0.25s ease;
}
.card:hover{
  transform:translateY(-4px);
  box-shadow:0 22px 55px rgba(34,197,94,0.3);
  border-color:rgba(34,197,94,0.4);
}
.card h4{margin-bottom:0.4rem;}
.card p{color:#cbd5f5;font-size:.95rem;}

/* Footer */
.footer{
  padding:40px 0 10px 0;
  text-align:center;
  font-size:0.9rem;
  color:#64748b;
  border-top:1px solid rgba(148,163,184,0.2);
  margin-top:40px;
}
</style>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
""", unsafe_allow_html=True)

# ---------------- Countdown ----------------
def countdown():
    now = datetime.now()
    delta = LAUNCH_DATE - now
    st.markdown("<div class='countdown-wrapper'>", unsafe_allow_html=True)
    if delta.total_seconds() < 0:
        st.success("🚀 VectorAlgoAI has launched!")
        return
    days = delta.days
    hrs, rem = divmod(delta.seconds, 3600)
    mins, secs = divmod(rem, 60)
    st.markdown(f"""
    <div class='countdown'>
      <div class='countdown-item'><div class='countnum'>{days}</div><div class='countlbl'>Days</div></div>
      <div class='countdown-item'><div class='countnum'>{hrs}</div><div class='countlbl'>Hours</div></div>
      <div class='countdown-item'><div class='countnum'>{mins}</div><div class='countlbl'>Mins</div></div>
      <div class='countdown-item'><div class='countnum'>{secs}</div><div class='countlbl'>Secs</div></div>
    </div>
    </div>""", unsafe_allow_html=True)

# ---------------- Navbar ----------------
st.markdown("""
<div class="navbar">
  <div class="nav-logo">
    <div class="nav-logo-mark"></div>
    <span>VectorAlgoAI</span>
  </div>
  <div class="nav-menu">
    <a href="#home">Home</a>
    <a href="#about">About</a>
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
  <p>VectorAlgoAI helps traders design, test, and automate strategies using AI — without writing a single line of code.</p>
  <div class="launch-box">🚀 Launches on <span>5 March 2026</span></div>
  <br><br>
  <a href="#mvp" class="btn-primary">Open Live Trading Lab</a>
</section>
""", unsafe_allow_html=True)
countdown()

# ---------------- About ----------------
st.markdown("""
<section class="section" id="about">
  <h2>About VectorAlgoAI</h2>
  <p>VectorAlgoAI bridges the gap between AI innovation and real-world trading. We’re building tools for serious retail traders to transform their ideas into live, adaptive AI-powered bots — without coding.</p>
</section>
""", unsafe_allow_html=True)

# ---------------- Services ----------------
st.markdown("""
<section class="section" id="services">
  <h2>Our Core Features</h2>
  <div class="card-grid">
    <div class="card"><h4>🧠 Strategy-to-Bot Engine</h4><p>Describe strategies in natural language and instantly generate structured bots.</p></div>
    <div class="card"><h4>📈 Hybrid AI Signal Layer</h4><p>Merge indicators, patterns, and AI predictions for smarter, evolving trading signals.</p></div>
    <div class="card"><h4>📰 News Intelligence</h4><p>Stay aligned with global sentiment — GPT-powered summaries of market-moving events.</p></div>
    <div class="card"><h4>🧩 Explainable Decisions</h4><p>See exactly why your bot made each decision — transparency meets automation.</p></div>
  </div>
</section>
""", unsafe_allow_html=True)

# ---------------- Founders ----------------
st.markdown("""
<section class="section" id="founders">
  <h2>Meet the Founders</h2>
  <div class="card-grid">
    <div class="card">
      <h4>👨‍💻 Praveen Kumar</h4>
      <p><strong>Founder & AI Architect</strong></p>
      <p>AI researcher, quant trader, and builder of VectorAlgoAI. Focused on making algorithmic intelligence accessible to every serious trader.</p>
    </div>
    <div class="card">
      <h4>👩‍💼 Sandhya Moni</h4>
      <p><strong>Co-Founder & Product Strategist</strong></p>
      <p>Product leader with expertise in digital experience and strategy. Ensures VectorAlgoAI stays intuitive, elegant, and focused on real trader workflows.</p>
    </div>
  </div>
</section>
""", unsafe_allow_html=True)

# ---------------- MVP ----------------
st.markdown("""
<section class="section" id="mvp">
  <h2>Live Trading Lab (MVP)</h2>
  <p>Prototype of VectorAlgoAI’s strategy-to-bot engine, connecting AI signals, indicators, and sentiment in one dashboard.</p>
</section>
""", unsafe_allow_html=True)
run_mvp_dashboard()

# ---------------- Contact ----------------
st.markdown(f"""
<section class="section" id="contact">
  <h2>Contact & Early Access</h2>
  <p>We’re currently onboarding early users and collaborators. Join us for exclusive early access before our launch.</p>
  <div class="card-grid">
    <div class="card"><h4>🚀 Founder Access</h4><p><a href="mailto:founder@vectoralgoai.com" style="color:#38bdf8;">founder@vectoralgoai.com</a></p></div>
    <div class="card"><h4>📩 General Inquiries</h4><p><a href="mailto:contact@vectoralgoai.com" style="color:#38bdf8;">contact@vectoralgoai.com</a></p></div>
    <div class="card"><h4>📚 Info & Docs</h4><p><a href="mailto:info@vectoralgoai.com" style="color:#38bdf8;">info@vectoralgoai.com</a></p></div>
  </div>
  <br>
  <a href="mailto:founder@vectoralgoai.com?subject=VectorAlgoAI%20Early%20Access" class="btn-primary">Join Early Access</a>
</section>
""", unsafe_allow_html=True)

# ---------------- Footer ----------------
st.markdown(f"""
<div class="footer">
© {datetime.now().year} VectorAlgoAI · Built by Praveen Kumar · Strategy & Product by Sandhya Moni ·
Contact: founder@vectoralgoai.com · contact@vectoralgoai.com · info@vectoralgoai.com
</div>
""", unsafe_allow_html=True)
