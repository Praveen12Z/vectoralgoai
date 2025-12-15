import streamlit as st
import os
from mvp_dashboard import run_mvp_dashboard

st.set_page_config(layout="wide")

def load_css():
    css_path = "assets/styles.css"
    if os.path.exists(css_path):
        with open(css_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
load_css()

# Navbar
st.markdown("""
<div class="navbar">
    <div class="nav-left">VectorAlgoAI</div>
    <div class="nav-right">
        <a href="/" class="nav-item">Home</a>
        <a href="/Product" class="nav-item">Product</a>
        <a href="/Dashboard" class="nav-item nav-cta active">Dashboard</a>
    </div>
</div>
""", unsafe_allow_html=True)

run_mvp_dashboard()
