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
h1,h2,h3,h4{font-weight:700}

/* Navbar */
.navbar{
  position:fixed;top:0;left:0;right:0;height:64px;
  background:rgba(3,7,18,0.85);backdrop-filter:blur(18px);
  display:flex;justify-content:space-between;align-items:center;
  padding:0 5%;border-bottom:1px solid rgba(148,163,184,0.35);z-index:9999
}
.nav-logo{
  display:flex;align-items:center;gap:.5rem;
  font-weight:700;font-size:1.15rem;color:#e5f2ff;letter-spacing:.04em
}
.nav-logo-mark{
  width:22px;height:22px;border-radius:7px;
  background:conic-gradient(from 160deg,#22d3ee,#a855f7,#22c55e,#22d3ee);
  box-shadow:0 0 18px rgba(56,189,248,0.7)
}
.nav-logo span:last-child{
  background:linear-gradient(90deg,#38bdf8,#22c55e);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent
}
.nav-menu a{
  margin:0 .7rem;text-decoration:none;font-weight:500;font-size:.95rem;
  color:#cbd5f5;transition:.18s ease
}
.nav-menu a:hover{color:#22d3ee}

/* Hero */
.hero{text-align:center;padding-top:10px;padding-bottom:60px}
.hero h1{
  font-size:3rem;line-height:1.15;margin-bottom:.7rem;
  background:linear-gradient(90deg,#22d3ee,#a855f7,#22c55e);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent
}
.hero p{
  max-width:700px;margin:auto;color:#94a3b8;font-size:1.05rem
}

/* Launch box + pulse */
@keyframes pulseGlow{
  0%{box-shadow:0 0 20px rgba(34,197,94,.6),inset 0 0 12px rgba(16,185,129,.25)}
  50%{box-shadow:0 0 30px rgba(34,197,94,.9),inset 0 0 14px rgba(16,185,129,.4)}
  100%{box-shadow:0 0 20px rgba(34,197,94,.6),inset 0 0 12px rgba(16,185,129,.25)}
}
.launch-box{
  display:inline-block;margin-top:20px;padding:12px 30px;border-radius:16px;
  background:rgba(16,185,129,.08);border:1px solid rgba(34,197,94,.45);
  color:#a7f3d0;font-size:1.2rem;font-weight:600;letter-spacing:.04em;
  text-align:center;text-shadow:0 0 8px rgba(52,211,153,.5);
  backdrop-filter:blur(6px);animation:pulseGlow 2.8s infinite ease-in-out
}
.launch-box span{color:#22c55e;font-weight:700}

/* Countdown glow */
.countdown-wrapper{margin-top:26px;animation:pulseGlow 3s infinite ease-in-out}
.countdown{display:flex;justify-content:center;gap:10px;flex-wrap:wrap}
.countdown-item{
  background:rgba(15,23,42,.85);border-radius:12px;padding:10px 14px;
  min-width:70px;border:1px solid rgba(34,197,94,.45)
}
.countnum{font-size:1.4rem;font-weight:700;color:#22d3ee}
.countlbl{font-size:.75rem;color:#9ca3af;text-transform:uppercase}

/* Buttons */
.btn-primary{
  background:radial-gradient(circle at 0% 0%,#4ade80,#16a34a);
  padding:.75rem 1.7rem;border-radius:999px;font-weight:600;color:#022c22;
  box-shadow:0 0 26px rgba(34,197,94,.55);text-decoration:none;display:inline-block;
  transition:all .25s
}
.btn-primary:hover{
  transform:translateY(-1px) scale(1.04);
  box-shadow:0 0 40px rgba(34,197,94,.9)
}

/* Sections */
.section{padding:70px 8% 0 8%;text-align:center}
.section h2{font-size:2rem;margin-bottom:.4rem}
.section p{color:#94a3b8}

/* Cards */
.card-grid{
  display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));
  gap:24px;margin-top:40px
}
.card{
  background:rgba(15,23,42,.75);border:1px solid rgba(148,163,184,.45);
  border-radius:20px;padding:22px;backdrop-filter:blur(12px);
  box-shadow:0 18px 45px rgba(15,23,42,.9);transition:.25s ease
}
.card:hover{transform:translateY(-5px);box-shadow:0 22px 55px rgba(34,197,94,.25)}
.card h4{margin-bottom:.4rem}
.card p{color:#cbd5f5;font-size:.95rem}

/* Timeline */
.timeline-wrapper{
  max-width:850px;
  margin:40px auto 0 auto;
  text-align:left;
}
.timeline{
  position:relative;
  margin-left:10px;
  padding-left:20px;
  border-left:1px solid rgba(148,163,184,0.5);
}
.timeline-item{
  position:relative;
  margin-bottom:22px;
  opacity:0;
  transform:translateY(10px);
  animation:slideUp 0.7s forwards;
}
.timeline-item:nth-child(1){animation-delay:0.1s;}
.timeline-item:nth-child(2){animation-delay:0.25s;}
.timeline-item:nth-child(3){animation-delay:0.4s;}
.timeline-dot{
  position:absolute;
  left:-10px;
  top:4px;
  width:14px;height:14px;
  border-radius:999px;
  background:radial-gradient(circle,#4ade80,#16a34a);
  box-shadow:0 0 14px rgba(74,222,128,0.9);
}
.timeline-content{
  margin-left:18px;
}
.timeline-title{
  font-size:1rem;
  font-weight:600;
  color:#e5e7eb;
}
.timeline-date{
  font-size:0.8rem;
  text-transform:uppercase;
  letter-spacing:0.08em;
  color:#a5b4fc;
}
.timeline-text{
  font-size:0.9rem;
  color:#cbd5f5;
  margin-top:4px;
}
@keyframes slideUp{
  to {opacity:1;transform:translateY(0);}
}

/* Footer */
.footer{
  padding:40px 0 10px 0;
  text-align:center;
  font-size:.9rem;
  color:#64748b
}
</style>
""", unsafe_allow_html=True)

# ---------------- Countdown helper ----------------
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
  <p>VectorAlgoAI turns your trading ideas into executable AI strategies — blending indicators, machine learning, and news sentiment in one unified dashboard.</p>
  <div class="launch-box">🚀 Launches on <span>5 March 2026</span></div>
  <br><br>
  <a href="#mvp" class="btn-primary">Launch Trading Lab</a>
</section>
""", unsafe_allow_html=True)
countdown()

# ---------------- About + Journey Timeline ----------------
st.markdown("""
<section class="section" id="about">
  <h2>About VectorAlgoAI</h2>
  <p>VectorAlgoAI was founded with a single goal — to bridge the gap between advanced Artificial Intelligence and everyday traders. 
  We believe AI shouldn’t be reserved for hedge funds and quant desks. 
  Our mission is to make intelligent automation accessible, transparent, and personal for every trader in the world.</p>
  <p>Our journey began when we realized that traders waste countless hours manually testing strategies or coding bots that quickly become obsolete. 
  By combining deep learning models, news sentiment analysis, and intuitive design, we built a platform that understands traders’ language — literally. 
  You describe your idea, VectorAlgoAI builds the strategy, tests it, and explains the logic behind each trade.</p>
  <p>We’re building the future of trading — one where AI doesn’t replace the trader, but empowers them with clarity, speed, and precision. 
  Whether you’re a beginner experimenting with indicators or a professional fine-tuning risk parameters, 
  VectorAlgoAI is your AI-powered copilot in the markets.</p>

  <div class="timeline-wrapper">
    <h3 style="margin-bottom:0.5rem;">Our Journey</h3>
    <p style="color:#9ca3af;font-size:0.9rem;margin-bottom:1.2rem;">
      From idea to live trading lab — focused on building for serious traders step by step.
    </p>
    <div class="timeline">
      <div class="timeline-item">
        <div class="timeline-dot"></div>
        <div class="timeline-content">
          <div class="timeline-date">Q4 2024</div>
          <div class="timeline-title">Idea & Research</div>
          <div class="timeline-text">
            Praveen and Sandhya started exploring how AI could remove the friction between strategy design and automation for retail traders, 
            validating the core problem across trading communities.
          </div>
        </div>
      </div>

      <div class="timeline-item">
        <div class="timeline-dot"></div>
        <div class="timeline-content">
          <div class="timeline-date">2025</div>
          <div class="timeline-title">MVP: Strategy-to-Bot Engine</div>
          <div class="timeline-text">
            The first VectorAlgoAI MVP was built — turning natural language strategies into structured configs, 
            running on real market data with signal overlays and early AI probability models.
          </div>
        </div>
      </div>

      <div class="timeline-item">
        <div class="timeline-dot"></div>
        <div class="timeline-content">
          <div class="timeline-date">2026</div>
          <div class="timeline-title">Public Launch & Early Access</div>
          <div class="timeline-text">
            VectorAlgoAI opens to early access users, focusing on power traders who want automation without sacrificing control, 
            with a roadmap toward broker integration, live execution, and advanced risk engines.
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
""", unsafe_allow_html=True)

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
  <p>Driven by innovation, discipline, and vision — building the bridge between human intuition and machine intelligence.</p>
  <div class="card-grid">
    <div class="card">
      <h4>Praveen Kumar</h4>
      <p><strong>Founder & AI Architect</strong></p>
      <p>Praveen Kumar is the technical architect and creator behind VectorAlgoAI. 
      With a deep background in Artificial Intelligence, quantitative trading, and neural network design, 
      he brings 7+ years of experience building intelligent trading systems. 
      His vision is to democratize access to AI-driven trading automation — empowering every trader, regardless of coding skill, 
      to build institutional-grade systems.</p>
    </div>
    <div class="card">
      <h4>Sandhya Moni</h4>
      <p><strong>Co-Founder & Product Strategist</strong></p>
      <p>Sandhya Moni leads VectorAlgoAI’s product and business strategy. 
      With a background in digital product management and leadership at global firms like Electrolux, 
      she ensures that every AI feature serves real trader workflows. 
      Her strategic mindset shapes the platform’s user experience, growth, and brand direction.</p>
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
      <p>Email: <a href="mailto:founder@vectoralgoai.com" style="color:#38bdf8;">founder@vectoralgoai.com</a></p>
    </div>
    <div class="card">
      <h4>📩 General Questions & Support</h4>
      <p>Email: <a href="mailto:contact@vectoralgoai.com" style="color:#38bdf8;">contact@vectoralgoai.com</a></p>
    </div>
    <div class="card">
      <h4>📚 Info & Documentation</h4>
      <p>Email: <a href="mailto:info@vectoralgoai.com" style="color:#38bdf8;">info@vectoralgoai.com</a></p>
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
