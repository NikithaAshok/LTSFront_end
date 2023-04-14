import streamlit as st

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
    st.header("About")
    st.write("This is the about page. Here, you can display information about how text summarization works.")

# Contact page
def contact():
    st.header("Contact")
    st.write("This is the contact page. Here, you can display social media icons and links, and a comment box with an email.")

# App
def app():
    st.set_page_config(page_title="BriefLegal")
    st.title("BriefLegal")
    menu = ["Home", "About", "Contact"]
    choice = st.sidebar.selectbox("Select a page", menu)
    if choice == "Home":
        home()
    elif choice == "About":
        about()
    else:
        contact()

if __name__ == "__main__":
    app()
