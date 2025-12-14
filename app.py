import streamlit as st
from pages_shared import load_css, top_nav

st.set_page_config(page_title="VectorAlgoAI", layout="wide")

load_css()

# Top Navbar (works everywhere)
top_nav(active="Home")

st.title("🧪 VectorAlgoAI")

st.markdown(
    """
    <div class="container">
      <div class="notice">
        Use the top navigation to switch pages.
      </div>
    </div>
    """,
    unsafe_allow_html=True
)
