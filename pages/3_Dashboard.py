import streamlit as st
from pages_shared import load_css, top_nav

st.set_page_config(page_title="VectorAlgoAI — Dashboard", layout="wide")
load_css()
top_nav(active="Dashboard")

# If your existing MVP dashboard function exists, call it:
from mvp_dashboard import run_mvp_dashboard
run_mvp_dashboard()
