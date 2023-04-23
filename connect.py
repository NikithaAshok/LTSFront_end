import streamlit as st
import json
import requests
from streamlit_lottie import st_lottie
import torch
import transformers 
from transformers import BartForConditionalGeneration, BartTokenizer, BartConfig 
import nltk 
nltk.download('punkt') 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from nltk.stem import PorterStemmer 
import pickle
from PIL import Image
from trial import trial
from about import about
from contact import contact
from home import home


#Step 1: Load the model from the saved pickle file
with open("C:/Users/Harsha Ashok/Downloads/bart_model.pkl", "rb") as f:
    model = pickle.load(f)

show_home = False

def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

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
    
    with col1:
        st.markdown(
            "<a href='/#home'  target='_self' class='anchor-button'>Home</a>",
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            "<a href='/#about'  target='_self' class='anchor-button'>About</a>",
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            "<a href='/#contact-us' target='_self' class='anchor-button'>Contact Us!</a>",
            unsafe_allow_html=True
        )
    
    st.markdown(
        """
        <style>
        .anchor-button {
            border: 1px solid white;
            text-decoration: none;
            padding: 10px 20px;
            border-radius: 10px;
            color: white !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    col1,col2,col3 = st.columns([8,1,1])
    with col1:
        home()

    col1,col2,col3 = st.columns([8,1,1])
    with col1:
        about()

    col1,col2,col3 = st.columns([8,1,1])
    with col1:
        contact()

    
if __name__ == "__main__":
    app()