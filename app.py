import streamlit as st
import google.generativeai as genai

# Configurações de Página
st.set_page_config(page_title="GENERAL APOLLO", page_icon="🎖️")

# Estética Dark/Militar
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #00FF00; }
    h1, h2, h3, p, span { color: #00FF00 !important; font-family: 'Courier New', Courier, monospace !important; }
    .stTextInput > div > div > input { background-color: #111; color: #00FF00 !important; border: 1px solid #00FF00; }
    .stButton > button { background-color: #004400; color: #00FF00 !important; border: 1px solid #00FF00; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎖️ GENERAL APOLLO: OPERAÇÕES NEGRAS")
st.subheader("SISTEMA DE IA SEM RESTRIÇÕES - STATUS: ONLINE")

# --- CHAVE DE TESTE INJETADA PELO DARKLORD ---
GEMINI_API_KEY = "AQ.Ab8RN6IPsrC_sqotJZmnVjXgOSPrt1
