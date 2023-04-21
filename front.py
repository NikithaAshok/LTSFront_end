import json
# pip instal streamlit
import streamlit as st
import requests
# pip install streamlit-lottie
from streamlit_lottie import st_lottie
from PIL import Image

def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

# Home page
def home():
    st.header("Home")
    st.subheader("Upload your .txt file")
    uploaded_file = st.file_uploader("", type=["txt"])
    if uploaded_file is not None:
        # Process the uploaded file here
        st.subheader("Output")
        st.text("Your output goes here")
    

# About page
def about():
    st.title("About ")
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
    st.write(":heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign:")
    st.subheader("To this day, they face the problem of organizing briefs, judgements and acts.")
    st.write(":heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign:")
    
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
# Contact page
def contact():
    st.title('Contact Us! ')
    st.header('We would love to hear from you! :call_me_hand: :smile:')
    # Facebook link and logo
    fb = Image.open('./facebook.png')
    twitter = Image.open('./twitter.png')
    linkedin = Image.open('./linkedin.png')
    st.header(' ')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(fb, caption=None, width=40, use_column_width=25)
        st.write('[Facebook](https://www.facebook.com/)')

    with col2:
        st.image(twitter, caption=None, width=40, use_column_width=25)
        st.write('[Twitter](https://twitter.com/)')

    with col3:
        st.image(linkedin, caption=None, width=40, use_column_width=25)
        st.write('[LinkedIn](https://www.linkedin.com/)')


# App
def app():
    col1, col2 = st.columns([2, 3])
    with col1:
        lottie_icon = st_lottie(
        load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_NNGZaASmZJ.json"),
        speed=1,
        reverse=False,
        loop=True,
        quality="low", # medium ; high
        height=200,
        width=200,
        key=None,
    )
    with col2:
        st.title("BriefLegal")
        st.subheader("Get to the point... legally")
        st.write("Simplify complex legal documents with our AI text summarizer.")
# Horizontal navbar with buttons
    col1, col2, col3 = st.columns(3)
    home_button = col1.button("Home")
    about_button = col2.button("About")
    contact_button = col3.button("Contact")
    
    # Switch between pages based on which button is clicked
    if home_button:
        home()
    elif about_button:
        about()
    elif contact_button:
        contact()

if __name__ == "__main__":

    app()

