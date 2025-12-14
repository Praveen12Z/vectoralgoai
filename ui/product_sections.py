import streamlit as st

def render_product_sections():
    st.markdown("## Why VectorAlgoAI?")

    st.markdown("""
    **Most platforms focus on signals.  
    Institutions focus on structure.**

    VectorAlgoAI evaluates:
    - Risk asymmetry
    - Regime sensitivity
    - Edge durability
    - Decision quality
    """)

    st.markdown("## What makes us different?")

    c1, c2 = st.columns(2)

    with c1:
        st.subheader("❌ ChatGPT / Indicators")
        st.write("""
        - Generic probabilities  
        - No accountability  
        - No backtesting  
        - No risk structure  
        """)

    with c2:
        st.subheader("✅ VectorAlgoAI")
        st.write("""
        - Strategy-specific analysis  
        - Real backtest metrics  
        - Risk & RR diagnostics  
        - Explainable AI (coming)  
        """)
