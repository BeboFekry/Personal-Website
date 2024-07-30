import streamlit as st

background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://raw.githubusercontent.com/BeboFekry/ChatHub/main/images/background.jpg");
    background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;  
    background-repeat: no-repeat;
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)

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

with open ("DS Resume.pdf", "rb") as file:
    btn = st.download_button(
            label="⬇️ Download Resume",
            data=file,
            file_name="Abdallah_Fekry_Data_Science_Resume.pdf",
            mime="text/pdf"
          )
# st.download_button("")

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
        st.link_button("Kaggle", "https://www.kaggle.com/bebofekry")
