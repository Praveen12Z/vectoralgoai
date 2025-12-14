import streamlit as st

def render_hero():
    st.markdown(
        """
        <h1 style="text-align:center;">VectorAlgoAI</h1>
        <h3 style="text-align:center;color:#9ca3af;">
        AI-powered strategy evaluation for serious traders
        </h3>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <p style="text-align:center;font-size:18px;">
        We don’t predict markets.<br>
        We expose <b>weak strategies</b>, <b>fragile edges</b>, and <b>false confidence</b>
        <br>before real money is deployed.
        </p>
        """,
        unsafe_allow_html=True,
    )
