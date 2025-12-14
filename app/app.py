import streamlit as st
import streamlit as st

st.set_page_config(
    page_title="VectorAlgoAI",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

import pandas as pd
from datetime import datetime, timezone

st.set_page_config(
    page_title="VectorAlgoAI",
    layout="wide"
)

# ------------------ HERO ------------------
st.markdown("# Turn Trading Ideas Into Tested Strategies — Instantly")
st.markdown(
    """
VectorAlgoAI helps traders transform strategy ideas into structured systems,  
stress-test them across real market data, and receive **brutal AI feedback**  
**before risking capital**.
"""
)

col1, col2 = st.columns([1,1])

with col1:
    st.button("🚀 Request Early Access")
    st.button("🧪 View Strategy Crash-Test")

with col2:
    st.image("assets/hero.png", use_container_width=True)

st.divider()

# ------------------ WHAT IT DOES ------------------
c1, c2, c3 = st.columns(3)

c1.markdown("### 🧠 Strategy Builder\nBuild strategies using dropdowns or YAML.")
c2.markdown("### 🧪 Strategy Crash-Test\nExpose drawdowns, RR, and hidden risk.")
c3.markdown("### 💀 AI Mentor\nBrutal feedback on structure and regimes.")

st.divider()

# ------------------ COUNTDOWN ------------------
LAUNCH_DATE = datetime(2026, 1, 25, 0, 0, tzinfo=timezone.utc)
now = datetime.now(timezone.utc)
delta = LAUNCH_DATE - now

st.markdown("## ⏳ Private Beta Launch")

if delta.total_seconds() > 0:
    days = delta.days
    hours, rem = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(rem, 60)
    st.markdown(
        f"### {days} Days : {hours} Hours : {minutes} Minutes : {seconds} Seconds"
    )
else:
    st.success("🚀 Beta is Live")

st.caption("Early access is limited. We onboard deliberately.")

st.divider()

# ------------------ EMAIL CAPTURE ------------------
st.markdown("## 📬 Request Early Access")

email = st.text_input("Email address")

if st.button("Join Early Access"):
    if email:
        df = pd.DataFrame([[email, datetime.utcnow()]],
                          columns=["email", "timestamp"])
        df.to_csv("data/early_access.csv", mode="a", header=False, index=False)
        st.success("You're on the list.")
    else:
        st.error("Enter a valid email.")

st.divider()

# ------------------ FOUNDERS ------------------
st.markdown("## Built by Practitioners, Not Marketers")

fc1, fc2 = st.columns(2)

fc1.markdown(
"""
### Praveen Kumar  
**Founder & Builder**

AI Engineer & systematic trader.  
Built VectorAlgoAI to solve one problem:

> Most traders never truly understand whether their strategy has an edge.
"""
)

fc2.markdown(
"""
### Sandhya Moni  
**Co-Founder & Strategy Lead**

Business & product strategy.  
Focused on clarity, usability, and long-term trader trust.
"""
)

st.caption("© VectorAlgoAI")
