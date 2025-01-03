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

# st.info("Certificates")
# # # # tabs = []
# # for i in range (29):
# #   st.write(f'"Certificate {i+1}", ')
# tabs = st.tabs(["Certificate 1","Certificate 2","Certificate 3","Certificate 4","Certificate 5","Certificate 6","Certificate 7","Certificate 8","Certificate 9","Certificate 10","Certificate 11","Certificate 12","Certificate 13","Certificate 14","Certificate 15","Certificate 16","Certificate 17","Certificate 18","Certificate 19","Certificate 20","Certificate 21","Certificate 22","Certificate 23","Certificate 24","Certificate 25","Certificate 26","Certificate 27","Certificate 28","Certificate 29","Certificate 30"])
# certificates = []
# certificates.append({"write":"Artificial Intelligence AI and Internet of Things IoT Training - National Telecommunication Institute NTI", "image":"images/NTI AI and IoT Training Certificate.jpg", "caption":"National Telecommunication Institute NTI"})
# certificates.append({"write":"Internet of Things Connecting Things IoT CT - Cisco Networking Academy","image":"images/AbdallahFekry Mohammed-IoT CT-certificate_page-0001.jpg","caption":"Cisco Networking Academy"})
# certificates.append({"write":"Big Data Essentials Training - National Telecommunication Institute NTI","image":"images/","caption":"National Telecommunication Institute NTI"})
# certificates.append({"write":"Huawei HCIA AI v3.5 - Huawei and the Egyptian Ministry of Youth and Sports","image":"images/","caption":"Huawei"})
# certificates.append({"write":"Data Science and Business Analytics Internship Offer Letter - The Sparks Foundation","image":"images/5VET2JCRLM.png","caption":"The Sparks Foundation"})
# certificates.append({"write":"Data Science and Business Analytics Internship - The Sparks Foundation","image":"images/MUHCQHJ8JR (1).png","caption":"The Sparks Foundation"})
# certificates.append({"write":"Machine Learning Internship Offer Letter - Code Casa","image":"images/Abdallah Fekry Mohammed Offer Letter_page-0001.jpg","caption":"Code Casa"})
# certificates.append({"write":"Machine Learning Internship - Code Casa","image":"images/Abdallah Fekry Mohammed Certificate_page-0001.jpg","caption":"Code Casa"})
# certificates.append({"write":"Machine Learning Internship Letter of Recommendation - Code Casa","image":"images/Letter of Recommendation (Code Casa).jpg","caption":"Code Casa"})
# certificates.append({"write":"Python Basic - Hacker Rank","image":"images/python basic.jpg","caption":"Hacker Rank"})
# certificates.append({"write":"Java Basic - Hacker Rank","image":"images/java basic.jpg","caption":"Hacker Rank"})
# certificates.append({"write":"SQL Basic - Hacker Rank","image":"images/sql basic.jpg","caption":"Hacker Rank"})
# certificates.append({"write":"Problem Solving Basic - Hacker Rank","image":"images/problem_solving_basic (Hacker Rank).png","caption":"Hacker Rank"})
# certificates.append({"write":"AI for Everyone - Maharatech","image":"images/AI for Everyone - ITI - maharatech en.jpg","caption":"Maharatech"})
# certificates.append({"write":"Python Programming Basics - Maharatech","image":"images/Course_Certificate_En (1).jpg","caption":"Maharatech"})
# certificates.append({"write":"Introduction to Java - Sololearn","image":"images/Introduction to Java_certificate.jpg","caption":"Sololearn"})
# certificates.append({"write":"Introduction to Python - Sololearn","image":"images/Introduction to Python_certificate.jpg","caption":"Sololearn"})
# certificates.append({"write":"Python Intermediate - Sololearn","image":"images/Python Intermediate_certificate.jpg","caption":"Sololearn"})
# certificates.append({"write":"Python Developer - Sololearn","image":"images/Python Developer_certificate.jpg","caption":"Sololearn"})
# certificates.append({"write":"Introduction to Programming using Python - Tawar We Ghayaer - Ministry of Youth and Sports - Ministry of Telecommunication - Microsoft","image":"images/python 1.jpg","caption":"Tawar We Ghayar"})
# certificates.append({"write":"Python Programming Language Intermediate Level - Tawar We Ghayaer - Ministry of Youth and Sports - Ministry of Telecommunication - Microsoft","image":"images/python 2.jpg","caption":"Tawar We Ghayar"})
# certificates.append({"write":"Introduction to Python Programming - Edraak","image":"images/download (4).jpg","caption":"Edraak"})
# certificates.append({"write":"Java Programming 1 - Edraak","image":"images/java 1.jpg","caption":"Edraak"})
# certificates.append({"write":"Java Programming 2 - Edraak","image":"images/java 2.jpg","caption":"Edraak"})
# certificates.append({"write":"Java Programming 3 - Edraak","image":"images/java 3.jpg","caption":"Edraak"})
# certificates.append({"write":"Python - Kaggle","image":"images/Abdallah Fekry Mohammed - Python.png","caption":"Kaggle"})
# certificates.append({"write":"Java Programming - Great Learning","image":"images/Abdallah_Fekry_Mohammed20221019-2047-1pathg3.jpg","caption":"Great Learning"})
# certificates.append({"write":"Digital Literacy Training Program - Egyptian Ministry of Youth and Sports","image":"images/","caption":""})
# certificates.append({"write":"Data Analysis & SQL Training Program - Egyptian Ministry of Youth and Sports","image":"images/", "caption":""})
# certificates.append({"write":"Freelancing Training Program - Egyptian Ministry of Youth and Sports","image":"images/","caption":""})

# for i in range(len(tabs)):
#   with tabs[i]:
#     st.write(certificates[i]["write"])
#     if certificates[i]["image"] != "images/":
#       st.image(certificates[i]["image"], caption = certificates[i]["caption"])
# st.write("---")

st.info("Certificates")

st.subheader("AI 2-months internship Completion Certificate - Electro Pi")
st.image("images/AI internship Certificate (Electro Pi).jpg", caption="Electro Pi")
st.write("---")

st.subheader("Artificial Intelligence AI and Internet of Things IoT Training - National Telecommunication Institute NTI")
st.image("images/NTI AI and IoT Training Certificate.jpg", caption="National Telecommunication Institute NTI")
st.write("---")

st.subheader("Big Data Essentials Training - National Telecommunication Institute NTI")
st.image("images/Big Data Essentials NTI.jpg", caption="National Telecommunication Institute NTI")
st.write("---")

st.subheader("Huawei HCIA AI v3.5 - Huawei and the Egyptian Ministry of Youth and Sports")
st.image("images/Huawei HCIA Certificate.jpg", caption="Huawei & Egyptian Ministry of Youth and Sports")
st.write("---")

st.subheader("Data Science & Machine Learning Course - Microsoft Learn Student Clubs MLSC")
st.image("images/Data Science & Machine Learning Course (Microsoft Learn Student Clubs MLSC) _page-0001.jpg", caption="Microsoft Learn Student Clubs MLSC")
st.write("---")

st.subheader("Internet of Things Connecting Things IoT CT - Cisco Networking Academy")
st.image("images/AbdallahFekry Mohammed-IoT CT-certificate_page-0001.jpg", caption="Cisco Networking Academy")
st.write("---")

st.subheader("Data Science and Business Analytics Internship Offer Letter - The Sparks Foundation")
st.image("images/5VET2JCRLM.png", caption="The Sparks Foundation")
st.write("---")

st.subheader("Data Science and Business Analytics Internship - The Sparks Foundation")
st.image("images/MUHCQHJ8JR (1).png", caption="The Sparks Foundation")
st.write("---")

st.subheader("Machine Learning Internship Offer Letter - Code Casa")
st.image("images/Abdallah Fekry Mohammed Offer Letter_page-0001.jpg", caption="Code Casa")
st.write("---")

st.subheader("Machine Learning Internship - Code Casa")
st.image("images/Abdallah Fekry Mohammed Certificate_page-0001.jpg", caption="Code Casa")
st.write("---")

st.subheader("Machine Learning Internship Letter of Recommendation - Code Casa")
st.image("images/Letter of Recommendation (Code Casa).jpg", caption="Code Casa")
st.write("---")

st.subheader("Python Basic - Hacker Rank")
st.image("images/python basic.jpg", caption="Hacker Rank")
st.write("---")

st.subheader("Java Basic - Hacker Rank")
st.image("images/java basic.jpg", caption="Hacker Rank")
st.write("---")

st.subheader("SQL Basic - Hacker Rank")
st.image("images/sql basic.jpg", caption="Hacker Rank")
st.write("---")

st.subheader("Problem Solving Basic - Hacker Rank")
st.image("images/problem_solving_basic (Hacker Rank).png", caption="Hacker Rank")
st.write("---")

st.subheader("Langchain Foundation - AlCamp - during Electro Pi Internship")
st.image("images/Langchain Foundation AlCamp Electro Pi Certificate.jpg", caption="AlCamp - Electro Pi")
st.write("---")

st.subheader("RAG Foundation - Alcamp - during Electro Pi Internship")
st.image("images/RAG Foundation AlCamp Electro Pi Certificate.jpg", caption="AlCamp - Electro Pi")
st.write("---")

st.subheader("Langchain with RAG Path - Alcamp - during Electro Pi Internship")
st.image("images/Langchain with RAG path AlCamp Electro Pi Certificate.jpg", caption="AlCamp - Electro Pi")
st.write("---")

st.subheader("AI for Everyone - Maharatech")
st.image("images/AI for Everyone - ITI - maharatech en.jpg", caption="Maharatech")
st.write("---")

st.subheader("Python Programming Basics - Maharatech")
st.image("images/Python Programming Basics Mahara Tech-1.jpg", caption="Maharatech")
st.write("---")

st.subheader("Introduction to Java - Sololearn")
st.image("images/Introduction to Java_certificate.jpg", caption="Sololearn")
st.write("---")

st.subheader("Introduction to Python - Sololearn")
st.image("images/Introduction to Python_certificate.jpg", caption="Sololearn")
st.write("---")

st.subheader("Python Intermediate - Sololearn")
st.image("images/Python Intermediate_certificate.jpg", caption="Sololearn")
st.write("---")

st.subheader("Python Developer - Sololearn")
st.image("images/Python Developer_certificate.jpg", caption="Sololearn")
st.write("---")

st.subheader("Introduction to Programming using Python - Tawar We Ghayaer - Ministry of Youth and Sports - Ministry of Telecommunication - Microsoft")
st.image("images/python 1.jpg", caption="Tawar We Ghayar")
st.write("---")

st.subheader("Python Programming Language Intermediate Level - Tawar We Ghayaer - Ministry of Youth and Sports - Ministry of Telecommunication - Microsoft")
st.image("images/python 2.jpg", caption="Tawar We Ghayar")
st.write("---")

st.subheader("Introduction to Python Programming - Edraak")
st.image("images/download (4).jpg", caption="Edraak")
st.write("---")

st.subheader("Java Programming 1 - Edraak")
st.image("images/java 1.jpg", caption="Edraak")
st.write("---")

st.subheader("Java Programming 2 - Edraak")
st.image("images/java 2.jpg", caption="Edraak")
st.write("---")

st.subheader("Java Programming 3 - Edraak")
st.image("images/java 3.jpg", caption="Edraak")
st.write("---")

st.subheader("Python - Kaggle")
st.image("images/Abdallah Fekry Mohammed - Python.png", caption="Kaggle")
st.write("---")

st.subheader("Java Programming - Great Learning")
st.image("images/Abdallah_Fekry_Mohammed20221019-2047-1pathg3.jpg", caption="Great Learning")
st.write("---")

st.subheader("Digital Literacy Training Program - Egyptian Ministry of Youth and Sports")
st.image("images/Digital Literacy Training Certificate.jpg")
st.write("---")

st.subheader("Data Analysis & SQL Training Program - Egyptian Ministry of Youth and Sports")
st.image("images/SQL & Data Analysis Training Certificate.jpg")
st.write("---")

st.subheader("Introductory Advanced Technologies Training Program - Egyptian Ministry of Youth and Sports")
st.image("images/Introductory Advanced Technologies Training Certificate.jpg")
st.write("---")
