import streamlit as st
from pages_shared import load_css, top_nav

st.set_page_config(page_title="Dashboard — VectorAlgoAI", layout="wide")
load_css()
top_nav(active="Dashboard")

from mvp_dashboard import run_mvp_dashboard
run_mvp_dashboard()
