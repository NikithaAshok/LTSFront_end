import streamlit as st
#streamlit code



# Home page
def home():
    st.title("Home Page")
    st.write("Enter your text below:")
    text = st.text_area("Input Text")
    if st.button("Submit"):
        # Perform some processing here (e.g. summarization) and save output to pickle file
        output = "This is the output."
        # Display output
        st.write("Output:")
        st.text_area("", value=output)

# About page
def about():
    st.title("About Page")
    st.write("This is a brief explanation of how text summarization works.")

# Contact page
def contact():
    st.title("Contact Page")
    st.write("Follow us on social media:")
    st.write("[Facebook](https://www.facebook.com)")
    st.write("[Twitter](https://www.twitter.com)")
    st.write("Leave us a comment:")
    email = st.text_input("Email")
    comment = st.text_area("Comment")
    if st.button("Submit"):
        # Save comment to database or send email
        st.write("Comment submitted.")

# Navigation bar
menu = ["Home", "About", "Contact"]
choice = st.sidebar.selectbox("Select a page", menu)

# Display selected page
if choice == "Home":
    home()
elif choice == "About":
    about()
elif choice == "Contact":
    contact()
