def load_css():
    with open("assets/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

import streamlit as st
from ui.product_sections import render_product_sections

st.set_page_config(page_title="Product – VectorAlgoAI", layout="wide")

st.title("📦 Product")
render_product_sections()

