import streamlit as st
import pickle

# Step 1: Load the model from the saved pickle file
with open("C:/Users/krithika/Downloads/bart_model.pkl", "rb") as f:
    model = pickle.load(f)

# Step 2: Create a file uploader using Streamlit's file_uploader widget
uploaded_file = st.file_uploader("Choose a text file", type=["txt"])

# Step 3: Generate a summary using the loaded model and uploaded file contents
if uploaded_file is not None:
    input_text = uploaded_file.read().decode("utf-8")  # read and decode file contents
    summary = model.generate(input_text)  # generate summary using BART model

    # Step 4: Display the generated summary on the Streamlit app
    st.write("Generated Summary:")
    st.write(summary)
