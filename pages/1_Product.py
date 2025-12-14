import streamlit as st
from ui.shared import load_css

st.set_page_config(layout="wide")
load_css()

st.title("📦 Product")

st.markdown("""
### What makes VectorAlgoAI different?

- We **don’t predict price blindly**
- We **stress-test ideas**
- We **explain why strategies fail**
- We prepare traders for **prop-firm reality**

### Machine Learning (Next Phase)
- Per-instrument ML models
- Confidence scoring, not predictions
- XAI: *why this signal, why now, when it fails*
""")
