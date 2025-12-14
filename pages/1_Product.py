import streamlit as st
from ui.product_sections import render_product_sections

st.set_page_config(page_title="Product – VectorAlgoAI", layout="wide")

st.title("📦 Product")
render_product_sections()

