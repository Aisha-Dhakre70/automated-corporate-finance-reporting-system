import streamlit as st

def apply_style():
    st.markdown("""
    <style>
    .main {
        background-color: #f7f9fc;
    }

    .kpi-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        text-align: center;
        border: 1px solid #e5e7eb;
    }

    .section-title {
        font-size: 22px;
        font-weight: 600;
        margin-top: 30px;
        margin-bottom: 10px;
    }

    hr {
        border: none;
        height: 1px;
        background-color: #e6e9ef;
        margin: 25px 0;
    }

    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)