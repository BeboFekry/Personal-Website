import streamlit as st

st.write("---")
col1, col2 = st.columns([1,3])
with col1:
    st.image(r"images/Picsart_24-07-17_12-32-08-644.png")
with col2:
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.subheader("Abdallah Fekry")
    st.write("**Data Scientist**")
st.write("---")

st.info("**Name:** Abdallah Fekry Mohammed")
st.info("**Email:** abdallahfekry95@gmail.com")
st.info("**Phone:** +20 111 9499 384")
st.info("**Location:** Egypt, Cairo")
st.info("**Age:** 24")

st.write("---")
st.write("Social")
col1, col2, col3 = st.columns(3)
with col1:
    col11, col22 = st.columns([1,4])
    with col11:
        st.image("images/702300.png")
    with col22:
        st.link_button("Linkedin", "http://www.linkedin.com/in/abdallah-fekry")
with col2:
    col11, col22 = st.columns([1,4])
    with col11:
        st.image("images/25231.png")
    with col22:
        st.link_button("GitHub", "https://github.com/BeboFekry?tab=repositories")
st.write("---")
with col3:
    col11, col22 = st.columns([1,4])
    with col11:
        st.image("images/4844503.png")
    with col22:
        st.link_button("GitHub", "https://www.kaggle.com/bebofekry")
