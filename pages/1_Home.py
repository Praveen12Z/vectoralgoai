import streamlit as st
from ui.hero import render_hero
from ui.features import render_features

st.set_page_config(page_title="VectorAlgoAI", layout="wide")

render_hero()
st.markdown("---")
render_features()

st.markdown("---")
st.markdown("### 🚀 Ready to test your strategy?")
st.page_link("pages/3_Dashboard.py", label="Open Strategy Dashboard →")
