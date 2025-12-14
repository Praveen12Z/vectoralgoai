import streamlit as st
from pathlib import Path

def load_css():
    css_file = Path("ui/styles.css")
    if css_file.exists():
        st.markdown(f"<style>{css_file.read_text()}</style>", unsafe_allow_html=True)
    else:
        st.error(f"CSS not found: {css_file}")

def top_nav(active=None):
    col1, col2, col3, col4 = st.columns([2,1,1,1])

    with col1:
        st.markdown(
            """
            <div class='topbar-brand'>
                <span class='brand-dot'></span>
                <span class='brand-text'>VectorAlgoAI</span>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        if st.button("🏠 Home", use_container_width=True, disabled=(active=="Home")):
            st.switch_page("pages/1_Home.py")

    with col3:
        if st.button("📦 Product", use_container_width=True, disabled=(active=="Product")):
            st.switch_page("pages/2_Product.py")

    with col4:
        if st.button("📊 Dashboard", use_container_width=True, disabled=(active=="Dashboard")):
            st.switch_page("pages/3_Dashboard.py")

    st.markdown("<div class='topbar-divider'></div>", unsafe_allow_html=True)
