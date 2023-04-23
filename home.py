import streamlit as st
from trial import trial

def home():
    st.header("Home")
    st.subheader("Upload your .txt file below to summarize")
    trial()