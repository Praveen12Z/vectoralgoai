import streamlit as st
from pages_shared import load_css, top_nav

st.set_page_config(page_title="VectorAlgoAI", layout="wide")

load_css()
top_nav(active="Home")

st.switch_page("pages/1_Home.py")
