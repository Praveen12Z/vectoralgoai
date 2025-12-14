import streamlit as st

st.set_page_config(
    page_title="VectorAlgoAI",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.sidebar.title("VectorAlgoAI")
st.sidebar.markdown("Build. Crash-test. Understand.")

st.sidebar.page_link("Home", label="🏠 Home")
st.sidebar.page_link("Product", label="📦 Product")
st.sidebar.page_link("Dashboard", label="📊 Dashboard")

st.write("Select a page from the sidebar.")
