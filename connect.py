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

# Step 1: Load the model from the saved pickle file
with open("C:/Users/Harsha Ashok/Downloads/bart_model.pkl", "rb") as f:
    bart_model = pickle.load(f)

def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()


#function for chunking
def split_text(text):
    words = word_tokenize(text)
    length = len(words)
        
    chunks = []
    current_chunk = words[0]
    for sentence in words[1:]:
        if len(current_chunk + " " + sentence) > (length/2):
            chunks.append(current_chunk)
            current_chunk = sentence
        
        else:
            current_chunk += " "+sentence
        
    chunks.append(current_chunk)
    return chunks

# Home page
def home():
    st.header("Home")
    st.subheader("Upload your .txt file")
    # Step 2: Create a file uploader using Streamlit's file_uploader widget
    uploaded_file = st.file_uploader("Choose a text file", type=["txt"])
    # Step 3: Generate a summary using the loaded model and uploaded file contents
    if st.button("Submit"):
        if uploaded_file is not None:
            input_text = uploaded_file.read().decode("utf-8")  # read and decode file contents
            bart_tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
            bart_model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
            final_summary = ""
            chunks = []
            chunks = split_text(input_text)
            for chunk in chunks:
                bart_inputs = bart_tokenizer.encode(chunk,return_tensors='pt', max_length=1024, truncation=True)
                bart_summary_ids = bart_model.generate(bart_inputs, num_beams=4, max_length=400, early_stopping=True)
                bart_summary = bart_tokenizer.decode(bart_summary_ids[0],skip_special_tokens=True)
                final_summary += bart_summary
                
        st.write("Output:")
        st.text_area("", value=final_summary)
       
# About page
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