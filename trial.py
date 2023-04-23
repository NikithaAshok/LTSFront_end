import streamlit as st
#import json
#import requests
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


def trial():
    with st.form("my_form"):
        #st.write("Inside the form")
        uploaded_file = st.file_uploader("Choose a text file", type=["txt"])
        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
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
            st.text_area("", value=final_summary, height=100)
                

