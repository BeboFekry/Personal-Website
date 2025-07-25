import streamlit as st

# Function to display the image on hover
def display_image_on_hover(image_url, i):
    # Generate unique class names for each image
    hover_class = f'hoverable_{i}'
    tooltip_class = f'tooltip_{i}'
    image_popup_class = f'image-popup_{i}'

    # Define the unique CSS for each image
    hover_css = f'''
        .{hover_class} {{
            position: relative;
            display: inline-block;
            cursor: pointer;
        }}
        .{hover_class} .{tooltip_class} {{
            opacity: 0;
            position: absolute;
            bottom: 100%;
            left: 50%;
            transform: translateX(-50%);
            transition: opacity 0.5s;
            background-color: rgba(0, 0, 0, 0.8);
            color: #fff;
            padding: 4px;
            border-radius: 4px;
            text-align: center;
            white-space: nowrap;
        }}
        .{hover_class}:hover .{tooltip_class} {{
            opacity: 1;
        }}
        .{image_popup_class} {{
            position: absolute;
            display: none;
            background-image: none;
            width: 200px;
            height: 200px;
        }}
        .{hover_class}:hover .{image_popup_class} {{
            display: block;
            background-image: url({image_url});
            background-size: cover;
            z-index: 999;
        }}
    '''
    tooltip_css = f"<style>{hover_css}</style>"

    # Define the html for each image
    image_hover = f'''
        <div class="{hover_class}">
            <a href="{image_url}">{image_url}</a>
            <div class="{tooltip_class}">Image {i}</div>
            <div class="{image_popup_class}"></div>
        </div>
    '''
    
    # Write the dynamic HTML and CSS to the content container
    st.markdown(f'<p>{image_hover}{tooltip_css}</p>', unsafe_allow_html=True)

# Initialize Streamlit app
st.title("Floating Image Tooltips on MouseOver")

# A list of image urls
url_list = [
    "https://everydayswag.org/images/misc/ableton-sampler-vol-env.png",
    "https://everydayswag.org/images/email.png"
]

# Create a container for the content that triggers the tooltip on mouseover
with st.expander("⛓", expanded=True):
    # Generate the dynamic HTML and CSS for each URL in the list
    for i, url in enumerate(url_list):
        display_image_on_hover(url, i)


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
    st.markdown(
        ":blue-badge[:material/check: ML Engineer] :blue-badge[:material/check: AI Engineer] :blue-badge[:material/check: Data Scientist]"
    )
    # st.write("**AI Engineer**")
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
