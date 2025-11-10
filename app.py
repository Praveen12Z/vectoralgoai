Perfect, let’s lock in one clean version.
Here’s the **full updated `app.py`** with:

* Same layout & styling you already have
* Improved **Built-in Trading Intelligence Tools** section (tagline + sub-text)
* All CSS for nicer login/signup contrast, hero, navbar, etc.

You can replace your current `app.py` with this one:

```python
import streamlit as st
from datetime import datetime
import os
import json
import hashlib

from mvp_dashboard import run_mvp_dashboard

# ---------- Launch + simple user store ----------

LAUNCH_DATE = datetime(2026, 3, 5, 0, 0, 0)
USERS_FILE = "users.json"  # simple JSON store for MVP


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def load_users():
    if not os.path.exists(USERS_FILE):
        return []
    try:
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return []


def save_users(users):
    try:
        with open(USERS_FILE, "w") as f:
            json.dump(users, f)
    except Exception:
        # Silent fail – this is just an MVP helper
        pass


def find_user(email: str):
    users = load_users()
    email_lower = email.strip().lower()
    for u in users:
        if u.get("email", "").strip().lower() == email_lower:
            return u
    return None


def register_user(email: str, password: str):
    email = email.strip()
    if not email or "@" not in email:
        return False, "Please enter a valid email."
    if len(password) < 6:
        return False, "Password must be at least 6 characters."
    if find_user(email) is not None:
        return False, "An account with this email already exists."

    users = load_users()
    users.append(
        {
            "email": email,
            "password_hash": hash_password(password),
            "created_at": datetime.utcnow().isoformat() + "Z",
        }
    )
    save_users(users)
    return True, "Account created successfully. You can log in now."


def authenticate_user(email: str, password: str):
    user = find_user(email)
    if user is None:
        return False, "No account found with this email."
    if user.get("password_hash") != hash_password(password):
        return False, "Incorrect password."
    return True, ""


# ---------- Page config ----------

st.set_page_config(
    page_title="VectorAlgoAI | AI Trading for Serious Retail Traders",
    page_icon="💹",
    layout="wide",
)

# ---------- Global CSS ----------

st.markdown(
    """
<style>
/* Hide Streamlit chrome */
header[data-testid="stHeader"] {display:none;}
#MainMenu, footer {visibility:hidden;}

.block-container {
  padding-top:90px !important;
  padding-bottom:40px !important;
}

/* Hide any stray <pre> at very top (best effort for that white box) */
body > pre {
  display:none !important;
}

/* Background + typography */
body, .stApp {
  background:radial-gradient(circle at 0% 0%, #05091a 0%, #050317 40%, #020010 100%) !important;
  color:#e5e7eb !important;
  font-family:"Inter", system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}
h1,h2,h3,h4{font-weight:700;color:#f9fafb;}
p{font-size:0.95rem;line-height:1.6;}

/* ---------- NAVBAR ---------- */
.navbar{
  position:fixed;
  top:0; left:0; right:0;
  height:72px;
  background:rgba(5,5,20,0.92);
  backdrop-filter:blur(24px);
  display:flex;
  justify-content:space-between;
  align-items:center;
  padding:0 7%;
  border-bottom:1px solid rgba(148,163,184,0.2);
  z-index:9999;
}
.nav-left{
  display:flex;
  align-items:center;
  gap:0.7rem;
}
.nav-logo-mark{
  width:26px;height:26px;
  border-radius:9px;
  background:conic-gradient(from 220deg,#22d3ee,#a855f7,#4ade80,#22d3ee);
  box-shadow:0 0 20px rgba(96,165,250,0.8);
}
.nav-logo-text{
  font-weight:700;
  font-size:1.1rem;
  letter-spacing:0.12em;
  text-transform:uppercase;
  color:#e5e7eb;
}
.nav-logo-sub{
  font-size:0.75rem;
  color:#9ca3af;
}

.nav-center{
  background:rgba(15,23,42,0.95);
  border-radius:999px;
  padding:6px;
  display:flex;
  gap:6px;
  box-shadow:0 12px 35px rgba(15,23,42,0.9);
}
.nav-pill{
  padding:8px 18px;
  border-radius:999px;
  font-size:0.85rem;
  color:#e5e7eb;
  text-decoration:none;
  opacity:0.8;
  transition:0.2s ease;
}
.nav-pill.active,
.nav-pill:focus{
  background:linear-gradient(135deg,#7c3aed,#38bdf8);
  color:#f9fafb;
  opacity:1;
  outline:none;
}
.nav-pill:hover{opacity:1;}

.nav-right{
  display:flex;
  align-items:center;
  gap:12px;
}
.nav-user{
  font-size:0.8rem;
  color:#9ca3af;
}

/* CTA button in navbar */
.nav-cta-link{
  padding:8px 18px;
  border-radius:999px;
  border:1px solid rgba(129,140,248,0.8);
  background:rgba(15,23,42,0.98);
  font-size:0.85rem;
  font-weight:600;
  color:#e5e7eb;
  cursor:pointer;
  transition:0.2s ease;
  text-decoration:none;
}
.nav-cta-link:hover{
  border-color:#a855f7;
  color:#e9d5ff;
}

/* ---------- HERO ---------- */
.hero-wrapper{
  padding-top:40px;
  padding-bottom:40px;
}
.hero{
  text-align:center;
}
.hero-eyebrow{
  display:inline-flex;
  align-items:center;
  gap:6px;
  padding:6px 14px;
  border-radius:999px;
  background:rgba(15,23,42,0.85);
  border:1px solid rgba(148,163,184,0.35);
  font-size:0.8rem;
  color:#c4b5fd;
  letter-spacing:0.14em;
  text-transform:uppercase;
}
.hero-eyebrow span.icon{
  width:8px;height:8px;
  border-radius:999px;
  background:radial-gradient(circle,#22c55e,#166534);
  box-shadow:0 0 10px rgba(34,197,94,0.9);
}
.hero-title{
  margin-top:24px;
  font-size:clamp(2.8rem, 6vw, 4.5rem);
  line-height:1.05;
  letter-spacing:-0.04em;
  background:linear-gradient(120deg,#e5e7eb,#e0e7ff,#c4b5fd);
  -webkit-background-clip:text;
  -webkit-text-fill-color:transparent;
}
.hero-sub{
  margin-top:18px;
  max-width:640px;
  margin-left:auto;
  margin-right:auto;
  color:#a5b4fc;
  font-size:1rem;
}

/* Launch pill */
@keyframes pulseGlow{
  0%{box-shadow:0 0 18px rgba(129,140,248,.45),0 0 32px rgba(129,140,248,.7);}
  50%{box-shadow:0 0 32px rgba(167,139,250,.95),0 0 52px rgba(129,140,248,1);}
  100%{box-shadow:0 0 18px rgba(129,140,248,.45),0 0 32px rgba(129,140,248,.7);}
}
.launch-pill{
  display:inline-flex;
  align-items:center;
  justify-content:center;
  gap:8px;
  margin-top:26px;
  padding:12px 30px;
  border-radius:999px;
  background:radial-gradient(circle at 0% 0%,rgba(129,140,248,0.18),rgba(15,23,42,0.98));
  border:1px solid rgba(129,140,248,0.9);
  color:#e0e7ff;
  font-size:0.95rem;
  font-weight:500;
  animation:pulseGlow 3s infinite ease-in-out;
}
.launch-pill span.date{
  font-weight:700;
  color:#c4b5fd;
}

/* Hero CTAs */
.hero-cta{
  margin-top:26px;
  display:flex;
  justify-content:center;
  gap:14px;
}
.primary-cta{
  display:inline-flex;
  align-items:center;
  justify-content:center;
  padding:12px 26px;
  border-radius:999px;
  background:linear-gradient(135deg,#7c3aed,#a855f7,#38bdf8);
  border:none;
  text-decoration:none;
  color:#f9fafb;
  font-weight:600;
  font-size:0.95rem;
  box-shadow:0 18px 40px rgba(88,28,135,0.9);
  transition:0.23s ease;
}
.primary-cta:hover{
  transform:translateY(-1px);
  box-shadow:0 22px 55px rgba(109,40,217,1);
}
.secondary-cta{
  display:inline-flex;
  align-items:center;
  justify-content:center;
  padding:12px 22px;
  border-radius:999px;
  background:rgba(15,23,42,0.9);
  border:1px solid rgba(148,163,184,0.5);
  text-decoration:none;
  color:#e5e7eb;
  font-weight:500;
  font-size:0.9rem;
}
.secondary-cta:hover{border-color:#a5b4fc;}

/* Notify area */
.notify-wrap{
  max-width:480px;
  margin:24px auto 0 auto;
}
.notify-caption{
  font-size:0.85rem;
  color:#9ca3af;
  margin-bottom:4px;
}

/* ---------- Inputs & buttons ---------- */
[data-testid="stTextInput"] input{
  background:rgba(15,23,42,0.95);
  border-radius:999px;
  border:1px solid rgba(148,163,184,0.7);
  padding:10px 14px;
  color:#e5e7eb;
}
[data-testid="stTextInput"] input::placeholder{
  color:#9ca3af;
}
[data-testid="stTextInput"] input:focus{
  outline:none;
  border:1px solid #7c3aed;
  box-shadow:0 0 0 1px rgba(124,58,237,0.7);
}

/* Streamlit buttons */
.stButton>button{
  border-radius:999px;
  border:1px solid rgba(124,58,237,0.9);
  background:linear-gradient(135deg,#7c3aed,#6d28d9);
  color:#f9fafb;
  font-weight:600;
  padding:0.45rem 1.4rem;
}
.stButton>button:hover{
  filter:brightness(1.05);
}

/* ---------- Countdown ---------- */
.countdown-wrapper{
  margin-top:26px;
}
.countdown{
  display:flex;
  justify-content:center;
  gap:14px;
  flex-wrap:wrap;
}
.countdown-item{
  background:radial-gradient(circle at 0% 0%,rgba(15,23,42,1),rgba(15,23,42,0.98));
  border-radius:18px;
  padding:12px 18px;
  min-width:80px;
  border:1px solid rgba(30,64,175,0.7);
  box-shadow:0 14px 35px rgba(15,23,42,1);
}
.countnum{
  font-size:1.4rem;
  font-weight:700;
  color:#f9fafb;
}
.countlbl{
  font-size:.7rem;
  color:#9ca3af;
  text-transform:uppercase;
}

/* ---------- Sections & cards ---------- */
.section{
  padding:80px 8% 0 8%;
  text-align:center;
}
.section h2{
  font-size:2.2rem;
  margin-bottom:.4rem;
}
.section p.section-lead{
  color:#9ca3af;
  max-width:720px;
  margin:0.3rem auto 0 auto;
}

/* New tagline + subtext for tools section */
.section-tagline{
  margin-top:0.5rem;
  font-size:0.85rem;
  text-transform:uppercase;
  letter-spacing:0.14em;
  color:#a5b4fc;
}
.section-subtext{
  margin-top:0.75rem;
  max-width:720px;
  margin-left:auto;
  margin-right:auto;
  font-size:0.95rem;
  color:#9ca3af;
}

.card-grid{
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(230px,1fr));
  gap:22px;
  margin-top:34px;
}
.card{
  background:radial-gradient(circle at 0% 0%,rgba(15,23,42,0.9),rgba(15,23,42,1));
  border-radius:18px;
  padding:20px;
  border:1px solid rgba(30,64,175,0.65);
  box-shadow:0 18px 40px rgba(15,23,42,1);
  text-align:left;
  transition:0.2s ease;
}
.card:hover{
  transform:translateY(-4px);
  box-shadow:0 24px 55px rgba(15,23,42,1);
  border-color:rgba(129,140,248,0.9);
}
.card h4{
  margin-bottom:.3rem;
  font-size:1rem;
}
.card p{
  color:#cbd5f5;
  font-size:0.9rem;
}
.card ul{
  margin:0.45rem 0 0;
  padding-left:1.1rem;
  font-size:0.85rem;
  color:#9ca3af;
}

/* Auth cards (login / signup) */
.auth-card{
  background:radial-gradient(circle at 0% 0%,rgba(15,23,42,0.98),rgba(15,23,42,1));
  border-radius:18px;
  padding:20px 22px;
  border:1px solid rgba(37,99,235,0.9);
  box-shadow:0 18px 40px rgba(15,23,42,1);
}
.auth-card h3, .auth-card h4{
  margin-bottom:0.6rem;
}
.auth-card label{
  color:#f9fafb !important;
  font-size:0.9rem !important;
  font-weight:500 !important;
}
.auth-card [data-testid="stTextInput"] input{
  background:rgba(15,23,42,0.96);
  border:1px solid rgba(148,163,184,0.9);
}
.auth-card [data-testid="stTextInput"] input::placeholder{
  color:#e5e7eb;
}

/* Social links */
.social-links{text-align:center;margin-top:40px;margin-bottom:10px;}
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
.social-icon.instagram i{color:#E4405F;}
.social-icon.twitter i{color:#000000;}
.social-icon.linkedin i{color:#0077B5;}
.social-icon.youtube i{color:#FF0000;}
.social-icon.telegram i{color:#0088CC;}
.social-icon:hover i{transform:scale(1.15);}

/* Footer */
.footer{
  padding:40px 0 10px 0;
  text-align:center;
  font-size:0.9rem;
  color:#64748b;
  border-top:1px solid rgba(30,41,59,0.9);
  margin-top:50px;
}
</style>

<link rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
""",
    unsafe_allow_html=True,
)

# ---------- Meta tags ----------

st.markdown(
    """
<meta name="title" content="VectorAlgoAI | AI Trading for Serious Retail Traders">
<meta name="description" content="VectorAlgoAI turns your trading ideas into AI-driven strategies — combining machine learning, technical indicators, and sentiment in one platform.">
<meta property="og:type" content="website">
<meta property="og:url" content="https://www.vectoralgoai.com/">
<meta property="og:title" content="VectorAlgoAI | AI Trading for Serious Retail Traders">
<meta property="og:description" content="Build AI-driven trading bots. No code. No limits. Join the future of trading automation with VectorAlgoAI.">
<meta property="og:image" content="https://www.vectoralgoai.com/static/og-preview.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="VectorAlgoAI | AI Trading for Serious Retail Traders">
<meta name="twitter:description" content="AI-native trading lab for serious retail traders. Build bots, test ideas, and analyze with machine learning.">
<meta name="twitter:image" content="https://www.vectoralgoai.com/static/og-preview.png">
""",
    unsafe_allow_html=True,
)

# ---------- Countdown ----------


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
    st.markdown(
        f"""
    <div class='countdown'>
      <div class='countdown-item'><div class='countnum'>{days}</div><div class='countlbl'>Days</div></div>
      <div class='countdown-item'><div class='countnum'>{hrs}</div><div class='countlbl'>Hours</div></div>
      <div class='countdown-item'><div class='countnum'>{mins}</div><div class='countlbl'>Mins</div></div>
      <div class='countdown-item'><div class='countnum'>{secs}</div><div class='countlbl'>Secs</div></div>
    </div>
    </div>
    """,
        unsafe_allow_html=True,
    )


# ---------- Navbar ----------

current_user = st.session_state.get("user_email")
nav_user_html = (
    f"<div class='nav-user'>Signed in as {current_user}</div>" if current_user else ""
)
cta_text = "Open Lab" if current_user else "Sign in to Lab"

st.markdown(
    f"""
<div class="navbar">
  <div class="nav-left">
    <div class="nav-logo-mark"></div>
    <div>
      <div class="nav-logo-text">VECTORALGOAI</div>
      <div class="nav-logo-sub">AI-native trading lab</div>
    </div>
  </div>
  <div class="nav-center">
    <a class="nav-pill active" href="#home">Home</a>
    <a class="nav-pill" href="#services">Features</a>
    <a class="nav-pill" href="#mvp">Trading Lab</a>
    <a class="nav-pill" href="#contact">Contact</a>
  </div>
  <div class="nav-right">
    {nav_user_html}
    <a class="nav-cta-link" href="#mvp">{cta_text}</a>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# ---------- Hero section ----------

st.markdown(
    """
<div class="hero-wrapper" id="home">
  <div class="hero">
    <div class="hero-eyebrow">
      <span class="icon"></span>
      <span>AI-NATIVE TRADING PLATFORM</span>
    </div>
    <div class="hero-title">
      Revolutionize your trading process.
    </div>
    <div class="hero-sub">
      VectorAlgoAI lets serious retail traders design, test, and automate strategies with AI –
      without wrestling with code, infrastructure, or opaque black-box bots.
    </div>

    <div class="launch-pill">
      🚀 Public launch on <span class="date">5 March 2026</span>
    </div>

    <div class="hero-cta">
      <a href="#mvp" class="primary-cta">Open Live Trading Lab</a>
      <a href="#services" class="secondary-cta">Explore Features</a>
    </div>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# ---------- Notify-me form ----------

st.markdown("<div class='notify-wrap'>", unsafe_allow_html=True)
st.markdown(
    "<div class='notify-caption'>Get a personal email from the founders when we go live. No spam.</div>",
    unsafe_allow_html=True,
)

col1, col2 = st.columns([3, 1])
with col1:
    notify_email = st.text_input(
        "Email address", key="notify_email", label_visibility="collapsed"
    )
with col2:
    notify_clicked = st.button("Notify Me", key="notify_button")

if notify_clicked:
    if notify_email and "@" in notify_email:
        try:
            with open("early_access_emails.txt", "a") as f:
                f.write(notify_email.strip() + "\n")
        except Exception:
            pass
        st.success("You're on the launch list ✅")
    else:
        st.error("Please enter a valid email address.")

st.markdown("</div>", unsafe_allow_html=True)

countdown()

# ---------- About / infrastructure ----------

st.markdown(
    """
<section class="section" id="about">
  <h2>AI-native infrastructure for retail traders</h2>
  <p class="section-lead">
    VectorAlgoAI is built for traders who think in playbooks and edge – not in Python stack traces.
    Describe your strategy, plug into real data, and let the system handle structure, execution logic,
    and explainability.
  </p>
</section>
""",
    unsafe_allow_html=True,
)

# ---------- Features / Trading intelligence tools ----------

st.markdown(
    """
<section class="section" id="services">
  <h2>Built-in Trading Intelligence Tools</h2>
  <p class="section-tagline">
    Everything you need to go from idea → validated strategy → AI-assisted automation.
  </p>
  <p class="section-subtext">
    Describe your playbook in plain English, let VectorAlgoAI turn it into a structured config,
    layer in AI probabilities and news context, then test it safely in a sandbox before you ever
    risk real capital.
  </p>
  <div class="card-grid">
    <div class="card">
      <h4>🧠 Strategy-to-Bot Engine</h4>
      <p>Turn plain-English strategy descriptions into structured configs the system can test and visualize.</p>
      <ul>
        <li>Capture entries, exits, and risk in one config.</li>
        <li>Generate YAML / JSON ready for backtesting or execution.</li>
        <li>Version strategies as you iterate.</li>
      </ul>
    </div>
    <div class="card">
      <h4>📈 Hybrid Signal Layer</h4>
      <p>Blend indicators, ML probabilities, and regime filters for adaptive signals – not static rules.</p>
      <ul>
        <li>Combine EMA, RSI, Bollinger and custom filters.</li>
        <li>Overlay AI probability of next-bar up/down.</li>
        <li>Quickly toggle filters on/off to see impact.</li>
      </ul>
    </div>
    <div class="card">
      <h4>📰 News & Context</h4>
      <p>Layer macro events and sentiment on top of your technical view so you’re never trading blind.</p>
      <ul>
        <li>Tag events like CPI, FOMC, and earnings around your trades.</li>
        <li>See when signals cluster around high-risk news windows.</li>
        <li>Build rules that react to regime or sentiment shifts.</li>
      </ul>
    </div>
    <div class="card">
      <h4>🧩 Explainable Decisions</h4>
      <p>Every entry and exit is traceable to rules and probabilities, so you always know <em>why</em>.</p>
      <ul>
        <li>Inspect the exact rule stack that fired each signal.</li>
        <li>See AI confidence next to every trade idea.</li>
        <li>Use explanations to refine or de-risk your playbook.</li>
      </ul>
    </div>
    <div class="card">
      <h4>🧪 Sandbox Lab</h4>
      <p>Experiment on historical and live data, iterate on your playbook, and version your strategies safely.</p>
      <ul>
        <li>Swap instruments and timeframes without rewriting logic.</li>
        <li>Test multiple parameter sets side by side.</li>
        <li>Keep experiments separate from live capital.</li>
      </ul>
    </div>
    <div class="card">
      <h4>🔗 Execution-ready Roadmap</h4>
      <p>Roadmap includes broker integrations, portfolio risk engines, and automated execution rails.</p>
      <ul>
        <li>Connect to brokers via APIs for live orders.</li>
        <li>Portfolio-level risk & exposure controls.</li>
        <li>Alerts, webhooks, and automation hooks.</li>
      </ul>
    </div>
  </div>
</section>
""",
    unsafe_allow_html=True,
)

# ---------- Founders ----------

st.markdown(
    """
<section class="section" id="founders">
  <h2>Meet the team behind VectorAlgoAI</h2>
  <p class="section-lead">Trading, AI, and product – aligned around one mission: empower serious retail traders.</p>
  <div class="card-grid">
    <div class="card">
      <h4>👨‍💻 Praveen Kumar</h4>
      <p><strong>Founder & AI Architect</strong></p>
      <p>AI researcher and quant-focused builder behind VectorAlgoAI. Praveen has spent years turning market
      hypotheses into programmable systems and is now packaging that experience into a platform built for traders,
      not just developers.</p>
    </div>
    <div class="card">
      <h4>👩‍💼 Sandhya Moni</h4>
      <p><strong>Co-Founder & Product Strategist</strong></p>
      <p>Product leader with experience at global brands, responsible for turning complex trading workflows into
      clean, opinionated product experiences. Sandhya keeps VectorAlgoAI grounded in real trader needs and clarity.</p>
    </div>
  </div>
</section>
""",
    unsafe_allow_html=True,
)

# ---------- MVP / Auth + dash ----------

st.markdown(
    """
<section class="section" id="mvp">
  <h2>Live Trading Lab (MVP)</h2>
  <p class="section-lead">
    Sign up or log in to access the full MVP dashboard. Or open a one-click demo if you just want to explore.
  </p>
</section>
""",
    unsafe_allow_html=True,
)

user_email = st.session_state.get("user_email")

if user_email:
    st.success(f"Signed in as {user_email}")
    logout_col, _ = st.columns([1, 3])
    with logout_col:
        if st.button("Log out"):
            st.session_state["user_email"] = None
            st.experimental_rerun()

    st.markdown("#### Full Trading Lab")
    run_mvp_dashboard()

else:
    col_login, col_signup = st.columns(2)

    # --- Log in ---
    with col_login:
        st.markdown("<div class='auth-card'>", unsafe_allow_html=True)
        st.subheader("Log in")
        with st.form("login_form"):
            login_email = st.text_input("Email", key="login_email")
            login_password = st.text_input(
                "Password", type="password", key="login_password"
            )
            submitted_login = st.form_submit_button("Log in")
        if submitted_login:
            ok, msg = authenticate_user(login_email, login_password)
            if ok:
                st.session_state["user_email"] = login_email.strip()
                st.success("Welcome back! Redirecting to the lab...")
                st.experimental_rerun()
            else:
                st.error(msg)
        st.markdown("</div>", unsafe_allow_html=True)

    # --- Sign up ---
    with col_signup:
        st.markdown("<div class='auth-card'>", unsafe_allow_html=True)
        st.subheader("Create account")
        with st.form("signup_form"):
            signup_email = st.text_input("Work email", key="signup_email")
            signup_password = st.text_input(
                "Password (min 6 chars)", type="password", key="signup_password"
            )
            signup_password2 = st.text_input(
                "Confirm password", type="password", key="signup_password2"
            )
            submitted_signup = st.form_submit_button("Sign up")
        if submitted_signup:
            if signup_password != signup_password2:
                st.error("Passwords do not match.")
            else:
                ok, msg = register_user(signup_email, signup_password)
                if ok:
                    st.success(msg)
                else:
                    st.error(msg)
        st.markdown("</div>", unsafe_allow_html=True)

    # Instant demo
    st.markdown("### Instant demo (no login)")
    st.caption(
        "Play with the strategy-to-bot MVP in this session. Nothing is stored – this is just a sandbox."
    )
    with st.expander("Open demo trading lab", expanded=False):
        run_mvp_dashboard()

# ---------- Contact + social ----------

st.markdown(
    """
<section class="section" id="contact">
  <h2>Contact & Early Access</h2>
  <p class="section-lead">
    We’re onboarding a small group of serious traders and collaborators ahead of launch.
  </p>
  <div class="card-grid">
    <div class="card">
      <h4>🚀 Founder Access</h4>
      <p>Email: <a href="mailto:founder@vectoralgoai.com" style="color:#a5b4fc;">founder@vectoralgoai.com</a></p>
    </div>
    <div class="card">
      <h4>📩 General Inquiries</h4>
      <p>Email: <a href="mailto:contact@vectoralgoai.com" style="color:#a5b4fc;">contact@vectoralgoai.com</a></p>
    </div>
    <div class="card">
      <h4>📚 Info & Docs</h4>
      <p>Email: <a href="mailto:info@vectoralgoai.com" style="color:#a5b4fc;">info@vectoralgoai.com</a></p>
    </div>
  </div>
</section>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<section class="section">
  <h2>Follow VectorAlgoAI</h2>
  <p class="section-lead">Stay close to launch updates, roadmap drops, and deep-dive content.</p>
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
</section>
""",
    unsafe_allow_html=True,
)

st.markdown(
    f"""
<div class="footer">
© {datetime.now().year} VectorAlgoAI · Built by Praveen Kumar · Strategy & Product by Sandhya Moni ·
Contact: founder@vectoralgoai.com · contact@vectoralgoai.com · info@vectoralgoai.com
</div>
""",
    unsafe_allow_html=True,
)
```

Next step: run this `app.py` and send me a fresh screenshot of any section you still don’t like (colors, spacing, wording, etc.), and I’ll keep giving you **full updated files** every time we tweak something.
