import streamlit as st
import torch
import transformers 
from transformers import BartForConditionalGeneration, BartTokenizer, BartConfig 
import nltk 
nltk.download('punkt') 
from nltk.corpus import stopwords 
from nltk.tokenize import sent_tokenize,word_tokenize 
from nltk.stem import PorterStemmer 
import string 
import pickle

# Step 1: Load the model from the saved pickle file
with open("C:/Users/Harsha Ashok/Downloads/bart_model.pkl", "rb") as f:
    model = pickle.load(f)


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
def about():
    st.header("About")
    st.write("This is the about page. Here, you can display information about how text summarization works.")

if __name__ == "__main__":
    home()