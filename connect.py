import streamlit as st
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
    st.title("About")
    st.subheader(":wavy_dash::wavy_dash::wavy_dash::wavy_dash::wavy_dash::wavy_dash::wavy_dash::wavy_dash:")
    st.header("What is :violet[BriefLegal] :question:")
    st.subheader("Attorneys, judges, lawyers and others in the justice system are constantly surrounded by large amounts of the legal text, which can be difficult to manage across many cases.")
    st.subheader(":heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign:")
    st.subheader("To this day, they face the problem of organizing briefs, judgements and acts.")
    st.subheader(":heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign::heavy_minus_sign:")
    st.subheader("Our application aims to build a medium where the synergy between law and technology will finally aid the litigators, solicitor or paralegals to smoothen their work system, improve efficiency and nimble their research.")

def contact():
    st.title('Contact Us! ')
    st.header('We would love to hear from you! :call_me_hand: :smile:')
    
    # Facebook link and logo
    fb = Image.open('./facebook.png')
    st.image(fb, caption=None, width=40, use_column_width=25)
    st.write('[Facebook](https://www.facebook.com/)')
    
    # Twitter link and logo
    twitter = Image.open('./twitter.png')
    st.image(twitter, caption=None, width=40, use_column_width=25)
    st.write('[Twitter](https://twitter.com/)')
    
    # LinkedIn link and logo
    linkedin = Image.open('./linkedin.png')
    st.image(linkedin, caption=None, width=40, use_column_width=25)
    st.write('[LinkedIn](https://www.linkedin.com/)')
    
if __name__ == "__main__":
    contact()