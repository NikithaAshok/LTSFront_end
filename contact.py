import streamlit as st
from PIL import Image

def contact():
    st.header('Contact Us! ')
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
