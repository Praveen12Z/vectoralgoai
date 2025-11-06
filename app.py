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

.block-container {
  padding-top:90px!important;
  padding-bottom:40px!important;
}

/* Base background + typography */
body,.stApp {
  background:radial-gradient(circle at 10% 0%,#020617 0%,#020617 40%,#000814 100%)!important;
  color:#e5e7eb!important;
  font-family:"Inter",system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
}
h1,h2,h3,h4{font-weight:700;color:#f9fafb}
p{font-size:0.95rem;line-height:1.6}

/* Container for readable width */
.section-inner {
  max-width: 900px;
  margin: 0 auto;
}

/* Navbar */
.navbar{
  position:fixed;top:0;left:0;right:0;height:64px;
  background:rgba(2,6,23,0.96);
  backdrop-filter:blur(16px);
  display:flex;justify-content:space-between;align-items:center;
  padding:0 5%;
  border-bottom:1px solid rgba(148,163,184,0.25);
  z-index:9999;
}
.nav-logo{
  display:flex;align-items:center;gap:.5rem;
  font-weight:700;font-size:1.05rem;color:#e5f2ff;letter-spacing:.04em;
}
.nav-logo-mark{
  width:20px;height:20px;border-radius:6px;
  background:linear-gradient(135deg,#06b6d4,#22c55e);
}
.nav-logo span:last-child{
  background:linear-gradient(90deg,#e5e7eb,#cbd5f5);
  -webkit-background-clip:text;
  -webkit-text-fill-color:transparent;
}
.nav-menu a{
  margin:0 .7rem;text-decoration:none;font-weight:500;font-size:.9rem;
  color:#cbd5f5;transition:.18s ease;
}
.nav-menu a:hover{color:#06b6d4}

/* Hero */
.hero{
  text-align:center;
  padding-top:10px;
  padding-bottom:60px;
}
.hero h1{
  font-size:2.7rem;
  line-height:1.15;
  margin-bottom:.7rem;
  background:linear-gradient(90deg,#e5e7eb,#cbd5f5);
  -webkit-background-clip:text;
  -webkit-text-fill-color:transparent;
}
.hero p{
  max-width:640px;
  margin:0 auto;
  color:#9ca3af;
  font-size:1rem;
}

/* Launch badge (more subtle) */
.launch-box{
  display:inline-flex;
  align-items:center;
  gap:8px;
  margin-top:18px;
  padding:8px 18px;
  border-radius:999px;
  background:rgba(15,23,42,0.9);
  border:1px solid rgba(148,163,184,0.5);
  color:#e5e7eb;
  font-size:0.9rem;
  font-weight:500;
}
.launch-box span{
  color:#22c55e;
  font-weight:600;
}

/* Countdown (simple, no glow) */
.countdown-wrapper{
  margin-top:24px;
}
.countdown{
  display:flex;
  justify-content:center;
  gap:10px;
  flex-wrap:wrap;
}
.countdown-item{
  background:#020617;
  border-radius:10px;
  padding:10px 14px;
  min-width:70px;
  border:1px solid rgba(51,65,85,0.9);
}
.countnum{font-size:1.25rem;font-weight:700;color:#e5e7eb;}
.countlbl{font-size:.7rem;color:#9ca3af;text-transform:uppercase;}

/* Buttons */
.btn-primary{
  background:linear-gradient(135deg,#06b6d4,#22c55e);
  padding:.7rem 1.6rem;
  border-radius:999px;
  font-weight:600;
  color:#022c22;
  box-shadow:0 10px 30px rgba(15,118,110,0.4);
  text-decoration:none;
  display:inline-flex;
  align-items:center;
  justify-content:center;
  gap:6px;
  font-size:0.95rem;
  transition:all .2s;
}
.btn-primary:hover{
  transform:translateY(-1px);
  box-shadow:0 14px 40px rgba(15,118,110,0.6);
}

/* Sections */
.section{
  padding:70px 8% 0 8%;
  text-align:center;
}
.section h2{
  font-size:2rem;
  margin-bottom:.6rem;
}
.section p.section-lead{
  color:#9ca3af;
  max-width:720px;
  margin:0.2rem auto 0 auto;
  font-size:0.95rem;
}

/* Cards */
.card-grid{
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(260px,1fr));
  gap:22px;
  margin-top:32px;
}
.card{
  background:rgba(15,23,42,0.85);
  border:1px solid rgba(30,64,175,0.45);
  border-radius:16px;
  padding:20px;
  box-shadow:0 14px 30px rgba(15,23,42,0.85);
  transition:transform .18s ease, box-shadow .18s ease, border-color .18s ease;
}
.card:hover{
  transform:translateY(-3px);
  box-shadow:0 18px 40px rgba(15,23,42,0.95);
  border-color:rgba(37,99,235,0.7);
}
.card h4{margin-bottom:.3rem;font-size:1rem;}
.card p{color:#cbd5f5;font-size:.9rem;}

/* Social links */
.social-links{text-align:center;margin-top:50px;margin-bottom:20px;}
.social-icons{
  display:flex;
  justify-content:center;
  flex-wrap:wrap;
  gap:28px;
  margin-top:18px;
}
.social-icon{
  display:flex;
  flex-direction:column;
  align-items:center;
  text-decoration:none;
  color:#e5f2ff;
  transition:0.25s ease;
}
.social-icon i{
  font-size:26px;
  margin-bottom:4px;
  transition:0.25s ease;
}
.social-icon span{
  font-size:0.85rem;
  color:#cbd5f5;
}

/* Brand Colors */
.social-icon.instagram i{color:#E4405F;}
.social-icon.twitter i{color:#000;}
.social-icon.linkedin i{color:#0077B5;}
.social-icon.youtube i{color:#FF0000;}
.social-icon.telegram i{color:#0088CC;}

.social-icon:hover i{transform:scale(1.15);}
.social-icon.instagram:hover i{text-shadow:0 0 12px rgba(255,105,180,0.7);}
.social-icon.twitter:hover i{text-shadow:0 0 10px rgba(255,255,255,0.4);}
.social-icon.linkedin:hover i{text-shadow:0 0 10px rgba(0,119,181,0.7);}
.social-icon.youtube:hover i{text-shadow:0 0 12px rgba(255,0,0,0.7);}
.social-icon.telegram:hover i{text-shadow:0 0 12px rgba(0,136,204,0.7);}

/* Footer */
.footer{
  padding:40px 0 10px 0;
  text-align:center;
  font-size:.85rem;
  color:#6b7280;
  border-top:1px solid rgba(31,41,55,0.9);
  margin-top:40px;
}
</style>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
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
  <p>VectorAlgoAI helps traders design, test, and automate strategies using AI — without writing a single line of code.</p>
  <div class="launch-box">
    <span>🚀 Launches on 5 March 2026</span>
  </div>
  <br><br>
  <a href="#mvp" class="btn-primary">
    <span>Open Live Trading Lab</span>
  </a>
</section>
""", unsafe_allow_html=True)
countdown()

# ---------------- About ----------------
st.markdown("""
<section class="section" id="about">
  <div class="section-inner">
    <h2>About VectorAlgoAI</h2>
    <p class="section-lead">
      VectorAlgoAI was created to bring institutional-grade AI trading tools to serious retail traders and independent quants.
    </p>
    <br>
    <p>
      Most traders either spend months learning to code or end up relying on rigid black-box bots. We believe there is a better way:
      a platform where you describe the strategy, and the system helps you structure it, test it, and refine it – with full transparency
      into the logic and risk behind every decision.
    </p>
    <p>
      VectorAlgoAI combines indicator logic, machine learning models, and news context into a single workflow designed for power users.
      Our goal is not to replace the trader, but to remove the friction between idea and execution – so you can spend more time thinking
      about edge, not debugging code.
    </p>
  </div>
</section>
""", unsafe_allow_html=True)

# ---------------- Services ----------------
st.markdown("""
<section class="section" id="services">
  <div class="section-inner">
    <h2>Our Core Features</h2>
    <p class="section-lead">Everything you need to go from idea → strategy → automation.</p>
    <div class="card-grid">
      <div class="card">
        <h4>🧠 Strategy-to-Bot Engine</h4>
        <p>Describe your setup in plain English and generate structured, machine-readable strategy configs ready to test and automate.</p>
      </div>
      <div class="card">
        <h4>📈 Hybrid AI Signal Layer</h4>
        <p>Blend indicators, price-action logic, and ML signals to adapt to changing market regimes instead of static rules.</p>
      </div>
      <div class="card">
        <h4>📰 Market & News Context</h4>
        <p>Incorporate macro events and sentiment into your strategy so you’re not trading in isolation from the real world.</p>
      </div>
      <div class="card">
        <h4>🧩 Explainable Decisions</h4>
        <p>See why a signal fired, what rules were met, and how risk was calculated – no opaque black boxes.</p>
      </div>
    </div>
  </div>
</section>
""", unsafe_allow_html=True)

# ---------------- Founders ----------------
st.markdown("""
<section class="section" id="founders">
  <div class="section-inner">
    <h2>Meet the Founders</h2>
    <p class="section-lead">Product, AI, and trading – aligned around one mission: empower serious traders with real tools.</p>
    <div class="card-grid">
      <div class="card">
        <h4>👨‍💻 Praveen Kumar</h4>
        <p><strong>Founder &amp; AI Architect</strong></p>
        <p>
          Praveen Kumar is the technical architect behind VectorAlgoAI. With deep experience in AI, quantitative trading,
          and neural network design, he has spent years building and testing algorithmic systems in real-market conditions.
          VectorAlgoAI is his attempt to compress that experience into a platform traders can actually use.
        </p>
      </div>
      <div class="card">
        <h4>👩‍💼 Sandhya Moni</h4>
        <p><strong>Co-Founder &amp; Product Strategist</strong></p>
        <p>
          Sandhya Moni leads product and go-to-market. Drawing on her background in digital product leadership at global
          brands like Electrolux, she ensures that the platform stays grounded in real workflows, clean UX, and long-term
          customer value – not just features for the sake of features.
        </p>
      </div>
    </div>
  </div>
</section>
""", unsafe_allow_html=True)

# ---------------- MVP ----------------
st.markdown("""
<section class="section" id="mvp">
  <div class="section-inner">
    <h2>Live Trading Lab (MVP)</h2>
    <p class="section-lead">Early version of VectorAlgoAI’s interactive strategy-to-bot engine.</p>
  </div>
</section>
""", unsafe_allow_html=True)
run_mvp_dashboard()

# ---------------- Contact ----------------
st.markdown("""
<section class="section" id="contact">
  <div class="section-inner">
    <h2>Contact &amp; Early Access</h2>
    <p class="section-lead">We’re currently onboarding a small group of serious traders and early design partners.</p>
    <div class="card-grid">
      <div class="card">
        <h4>🚀 Early Access &amp; Founder Chat</h4>
        <p>Email: <a href="mailto:founder@vectoralgoai.com" style="color:#67e8f9;">founder@vectoralgoai.com</a></p>
      </div>
      <div class="card">
        <h4>📩 General Questions &amp; Support</h4>
        <p>Email: <a href="mailto:contact@vectoralgoai.com" style="color:#67e8f9;">contact@vectoralgoai.com</a></p>
      </div>
      <div class="card">
        <h4>📚 Info &amp; Documentation</h4>
        <p>Email: <a href="mailto:info@vectoralgoai.com" style="color:#67e8f9;">info@vectoralgoai.com</a></p>
      </div>
    </div>
    <br>
    <a href="mailto:founder@vectoralgoai.com?subject=VectorAlgoAI%20Early%20Access" class="btn-primary">
      Request Early Access
    </a>
  </div>
</section>
""", unsafe_allow_html=True)

# ---------------- Social Links ----------------
st.markdown("""
<section class="section">
  <div class="section-inner">
    <h2>Follow Us</h2>
    <p class="section-lead">Stay close to the roadmap, launch updates, and deep-dive content.</p>
    <div class="social-links">
      <div class="social-icons">
        <a href="https://instagram.com/vectoralgoai" target="_blank" class="social-icon instagram">
          <i class="fab fa-instagram"></i><span>Instagram</span>
        </a>
        <a href="https://twitter.com/vectoralgoai" target="_blank" class="social-icon twitter">
          <i class="fab fa-x-twitter"></i><span>Twitter (X)</span>
        </a>
        <a href="https://linkedin.com/company/vectoralgoai" target="_blank" class="social-icon linkedin">
          <i class="fab fa-linkedin"></i><span>LinkedIn</span>
        </a>
        <a href="https://youtube.com/@vectoralgoai" target="_blank" class="social-icon youtube">
          <i class="fab fa-youtube"></i><span>YouTube</span>
        </a>
        <a href="https://t.me/vectoralgoai" target="_blank" class="social-icon telegram">
          <i class="fab fa-telegram"></i><span>Telegram</span>
        </a>
      </div>
    </div>
  </div>
</section>
""", unsafe_allow_html=True)

# ---------------- Footer ----------------
st.markdown(f"""
<div class="footer">
© {datetime.now().year} VectorAlgoAI · Built by Praveen Kumar · Strategy &amp; Product by Sandhya Moni ·
Contact: founder@vectoralgoai.com · contact@vectoralgoai.com · info@vectoralgoai.com
</div>
""", unsafe_allow_html=True)
