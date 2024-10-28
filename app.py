import streamlit as st

st.logo("images/Picsart_24-07-24_23-25-40-729.png")

st.set_page_config(page_title="Abdallah", page_icon='images/ai (2).png')

if "first_time" not in st.session_state:
  st.session_state.first_time = True

# intro = st.Page("intro.py", title="Preview", icon=":material/slideshow:", default=True)
home = st.Page("home.py", title="Home", icon=":material/home:", default=True)
profile = st.Page("profile.py", title="Profile", icon=":material/person:")
certificates = st.Page("certificates.py", title="Certificates", icon=":material/workspace_premium:")
projects = st.Page("projects.py", title="Projects", icon=':material/share:')

pg = st.navigation([profile, home, certificates, projects])
pg.run()
