import streamlit as st

st.logo("images/Picsart_24-07-24_23-25-40-729.png")

intro = st.Page("intro.py", title="Preview", icon=":material/slideshow:")
home = st.Page("home.py", title="Home", icon=":material/home:", default=True)
profile = st.Page("profile.py", title="Profile", icon=":material/person:")
certificates = st.Page("certificates.py", title="Certificates", icon=":material/workspace_premium:")
projects = st.Page("projects.py", title="Projects", icon=':material/share:')

pg = st.navigation([intro, profile, home, certificates, projects])
pg.run()
