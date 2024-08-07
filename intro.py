import streamlit as st

url = "https://github.com/BeboFekry/Personal-Website/blob/main/Blue%20Futuristic%20Technology%20Presentation%20(2).gif"
background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://github.com/BeboFekry/Personal-Website/blob/main/Blue%20Futuristic%20Technology%20Presentation.gif?raw=true");
    background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;  
    background-repeat: no-repeat;
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)

# home = st.Page("home.py", title="Home", icon=":material/home:")
# profile = st.Page("profile.py", title="Profile")
# certificates = st.Page("certificates.py", title="Certificates")
# projects = st.Page("projects.py", title="Projects")
#
# col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 6])
# with col1:
#     st.page_link(profile, use_container_width=1)
# with col2:
#     st.page_link(home, icon=":material/home:", use_container_width=1)
# with col3:
#     st.page_link(projects, use_container_width=1)
# with col4:
#     st.page_link(certificates, use_container_width=1)
#
# st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n")
# st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n")

# col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1,30])
# with col1:
#     st.markdown(
#         "[![FB](https://raw.githubusercontent.com/BeboFekry/ChatHub/main/images/702300.png)](http://www.linkedin.com/in/abdallah-fekry)")
# with col2:
#     st.markdown(
#         "[![FB](https://raw.githubusercontent.com/BeboFekry/ChatHub/main/images/25231.png)](https://github.com/BeboFekry?tab=repositories)")
# with col3:
#     st.markdown(
#         "[![FB](https://raw.githubusercontent.com/BeboFekry/ChatHub/main/images/4844503.png)](https://www.kaggle.com/bebofekry)")
# with col4:
#     st.markdown(
#         "[![FB](https://raw.githubusercontent.com/BeboFekry/ChatHub/main/images/streamlit-mark-color.png)](https://abdalleh-fekry.streamlit.app/)")
