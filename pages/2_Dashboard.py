import streamlit as st
from ui.shared import load_css
from mvp_dashboard import run_mvp_dashboard

st.set_page_config(page_title="Dashboard", layout="wide")
load_css()

run_mvp_dashboard()
