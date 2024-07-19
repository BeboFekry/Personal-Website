import streamlit as st

st.logo("images/Logo.png")

home = st.Page("home.py", title="Home", icon=":material/home:", default=True)
profile = st.Page("profile.py", title="Profile", icon=":material/person:")
certificates = st.Page("certificates.py", title="Certificates", icon=":material/list:")

pg = st.navigation([profile,home,certificates])
pg.run()