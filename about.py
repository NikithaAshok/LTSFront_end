import streamlit as st
from streamlit_lottie import st_lottie
import requests

def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

def about():
    st.header("About")
    st.header("What is :violet[BriefLegal] :question:")
    # st.write(":wavy_dash::wavy_dash::wavy_dash::wavy_dash::wavy_dash::wavy_dash::wavy_dash::wavy_dash:")
    col1,col2 =st.columns([2,6])
    with col1: 
        animate1 = st_lottie(
        load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_6ljswtij.json"),
        speed=1,
        reverse=False,
        loop=True,
        quality="low", # medium ; high
        height=120,
        width=120,
        key=None,
    )
    with col2:
        st.subheader("Attorneys, judges, lawyers and others in the justice system are constantly surrounded by large amounts of the legal text, which can be difficult to manage across many cases.")
    st.write(":heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign:")
    st.subheader("To this day, they face the problem of organizing briefs, judgements and acts.")
    st.write(":heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign:")
    
    col1,col2=st.columns([2,1])
    with col1:
        st.subheader("Our application aims to build a medium where the synergy between law and technology will finally aid the litigators, solicitor or paralegals to smoothen their work system, improve efficiency and nimble their research.")
    with col2:
        animate2 = st_lottie(
        load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_jtvduiqm.json"),
        speed=1,
        reverse=False,
        loop=True,
        quality="low", # medium ; high
        height=200,
        width=200,
        key=None,
    )
       