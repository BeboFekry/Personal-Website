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

if st.session_state.first_time:
    st.toast("Rotate your mobile screen", icon=":material/sync:")
    st.session_state.first_time = False

col1, col2, col3, col4 = st.columns([1,2,3,1])
with col2:
    st.image(r"images/Picsart_24-07-16_16-37-19-394.png")
with col3:
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.subheader("Eng. Abdallah Fekry")
    st.write("**AI Engineer**")
st.write("---")

st.info("Overview")
st.write("""As a computer science enthusiast with a great academic background with grade very good with honors, 
    I am determined to make a significant impact in the tech industry. 
    I've had the privilege of gaining hands-on experience as an AI Engineer in internship opportunity at Electro Pi working on variety of real-world projects, 
    Artificial Intelligence (AI) and Internet of Things (IoT) trainee and Big Data treinee at National Telecommunication Institute NTI. 
    This experience has honed my skills and fueled my passion for innovation. I also have hands-on experience in real-world projects as i was 
    Data Science and Business Analytics intern at The Sparks Foundation, Machine Learning intern at Code Casa, and finally, Machine Learning intern at Prodigy InfoTech.""")
st.write("---")

profile = st.Page("profile.py", title="Profile", icon=":material/person:")
# projects = st.Page("projects2.py", title="Projects", icon=":material/work:")

st.info("Education")
st.write("**Bachelor’s degree BSc in Computer Science - Culture and Science City C.S.C - 2020-2024**  \n**Cumulative Grade:** Very Good with Honors  \n**Final year Grade:** Excellent  \n**Graduation Project Grade:** Excellent")
st.write("---")

st.info("Experience")
st.write("""**Ai Engineer | Electro Pi | internship | August 2024 – October 2024**
      \n• Developed more than 8 AI projects in NLP, LLM, Computer Vision, and Speech Recognition. 
      \n• Developed NLP Techniques as LLM using LangChain and RAG for making customized chatbots to answer business questions. 
      \n• Applied the Computer Vision Techniques as OCR for using in invoicing systems and connect it with LLM to extract the data and add it to a database for the system. 
      \n• Working with other techniques as Speech Recognition (voice to text) and (text to voice), Wav2Lip for Lip Syncing for making human like chatbots.
      \n• Working individually and as a part of a team using Agile methodology.""")
st.write("---")

st.write("**Data Science & Machine Learning | Microsoft Student Clubs by EELU | March 2024 – Present**")
st.write("---")

st.write("**Data Science Intern | Code Alpha | May 2024 - Present**")
st.write("---")

st.write("""**Big Data Trainee | National Telecommunication Institute NTI | March 2024 – May 2024** 
  \n• Got the foundation of 2 essentials needed for Hadoop platforms Networks & Linux. 
  \n• Developed an interactive Python programming codes and integrating practical exercises on 5 advanced topics 
    like OOP, Numpy, Pandas, Matplotlib and Seaborn and improving data handling efficiency. 
  \n• Develop a completed database, analyze data, apply EDA and ask business questions in a reports using Structured Query Language SQL. 
  \n• Had the opportunity to start with Big Data tools and techniques and work on Hadoop platforms.""")
st.write("---")

st.write("""**Machine Learning Intern | Prodigy Infotech | February 2024 – March 2024** 
  \nDuring the internship, I have hands-on experience on 5 real-world projects:
  \n• Developed 3 Machine Learning projects such as House Price Prediction using Multiple Linear Regression Customer Clustering using K-Means, Dogs and Cats 
    Classification using Support Vector Machine SVM. 
  \n• Architected 2 Deep Learning projects such as Hand Gesture classification using Deep Learning, Food Type 
    Classification and identify calories using Deep Learning CNN. 
  \n• In addition, the data analysis, cleansing, preprocessing and visualization parts for 5 projects.""")
st.write("---")

st.write("""**Machine Learning Intern | Code Casa | September 2023 – October 2023** 
  \n• During the internship, I have hands-on experience on 2 real-world projects as Stock Price Prediction using LSTM model architecture and 
    Housing Price Prediction using Multiple Linear Regression Algorithm.
  \n• Collect, analyze, preprocess and clean data from 2 datasets then visualize the results for 2 projects. 
  \n• Received a Letter of Recommendation after the 1-month internship for responsibility and professional work.""")
st.write("---")

st.write("""**Data Science and Business Analytics Intern | The Sparks Foundation | September 2023 – October 2023** 
  \nDuring the internship, I have hands-on experience on three real-world projects: 
  \n• Prediction using Supervised Learning using Regression Techniques. 
  \n• Prediction using Unsupervised Learning (I have used K-Means Algorithm). 
  \n• Prediction using Decision Tree Classifier. 
  \n• In addition to the part of Data Analysis, Preprocessing, Cleansing and Visualization""")
st.write("---")

st.write("""**Artificial Intelligence AI & Internet of Things IoT Trainee | National Telecommunication Institute NTI | September 2023 – October 2023** 
  \nDuring the 1-month (120 hours) Training Program, had the opportunity to dive deep into the AI world. 
  \n• Developed python codes hands-on experience with Artificial Intelligence tools such as Numpy, Pandas, 
    Matplotlib, Seaborn, Scikit-Learn, Keras, and TensorFlow. 
  \n• Mastered AI techniques including mathematics, data preprocessing, cleansing, and visualization while 
    implementing machine learning and deep learning algorithms, this knowledge enabled the successful 
    completion of 10 predictive modeling projects. 
  \n• Experienced in Natural Language Processing NLP techniques and applying text preprocessing as text 
    stemming, padding and tokenization in 2 projects as sentiment analysis, and on IMDB classification. 
  \n• Experienced in Computer Vision techniques as CNN, RNN, LSTM, etc. and applying 5 projects as chest 
    Xray diagnosis, handwritten numbers classification, object detection, face recognition, etc. """)
st.write("---")

st.info("Skills")
st.write("""**Mathematics**  \n• Probability  \n• Statistics  \n• Linear Algebra  \n• Calculus  
**Data Analysis & Visualization**  \n• Numpy  \n• Pandas  \n• Matplotlib  \n• Seaborn  \n• Microsoft Power BI  
**Programming**  \n• Python  \n• Java  \n• OOP  \n• SQL  \n• Data Structures & Algorithms  \n• Machine Learning with Scikit-Learn  \n• Deep Learning with Tensorflow & Keras  
**Generative Modeling**  \n• Langchain  \n• RAG  
**Deployment**  \n• Flask  \n• Streamlit
\n""")
st.write("---")

st.info("Certificates")
# # # tabs = []
# for i in range (29):
#   st.write(f'"Certificate {i+1}", ')
tabs = st.tabs(["Certificate 1","Certificate 2","Certificate 3","Certificate 4","Certificate 5","Certificate 6","Certificate 7","Certificate 8","Certificate 9","Certificate 10","Certificate 11","Certificate 12","Certificate 13","Certificate 14","Certificate 15","Certificate 16","Certificate 17","Certificate 18","Certificate 19","Certificate 20","Certificate 21","Certificate 22","Certificate 23","Certificate 24","Certificate 25","Certificate 26","Certificate 27","Certificate 28","Certificate 29","Certificate 30","Certificate 31","Certificate 32","Certificate 33","Certificate 34","Certificate 35"])
certificates = []
certificates.append({"write":"AI 2-months internship Completion Certificate - Electro P", "image":"images/AI internship Certificate (Electro Pi).jpg", "caption":"Electro Pi"})
certificates.append({"write":"Artificial Intelligence AI and Internet of Things IoT Training - National Telecommunication Institute NTI", "image":"images/NTI AI and IoT Training Certificate.jpg", "caption":"National Telecommunication Institute NTI"})
certificates.append({"write":"Big Data Essentials Training - National Telecommunication Institute NTI","image":"images/Big Data Essentials NTI.jpg","caption":"National Telecommunication Institute NTI"})
certificates.append({"write":"Huawei HCIA AI v3.5 - Huawei and the Egyptian Ministry of Youth and Sports","image":"images/Huawei HCIA Certificate.jpg","caption":"Huawei & Egyptian Ministry of Youth and Sports"})
certificates.append({"write":"Data Science & Machine Learning Course - Microsoft Learn Student Clubs MLSC","image":"images/Data Science & Machine Learning Course (Microsoft Learn Student Clubs MLSC) _page-0001.jpg","caption":"Microsoft Learn Student Clubs MLSC"})
certificates.append({"write":"Internet of Things Connecting Things IoT CT - Cisco Networking Academy","image":"images/AbdallahFekry Mohammed-IoT CT-certificate_page-0001.jpg","caption":"Cisco Networking Academy"})
certificates.append({"write":"Data Science and Business Analytics Internship Offer Letter - The Sparks Foundation","image":"images/5VET2JCRLM.png","caption":"The Sparks Foundation"})
certificates.append({"write":"Data Science and Business Analytics Internship - The Sparks Foundation","image":"images/MUHCQHJ8JR (1).png","caption":"The Sparks Foundation"})
certificates.append({"write":"Machine Learning Internship Offer Letter - Code Casa","image":"images/Abdallah Fekry Mohammed Offer Letter_page-0001.jpg","caption":"Code Casa"})
certificates.append({"write":"Machine Learning Internship - Code Casa","image":"images/Abdallah Fekry Mohammed Certificate_page-0001.jpg","caption":"Code Casa"})
certificates.append({"write":"Machine Learning Internship Letter of Recommendation - Code Casa","image":"images/Letter of Recommendation (Code Casa).jpg","caption":"Code Casa"})
certificates.append({"write":"Python Basic - Hacker Rank","image":"images/python basic.jpg","caption":"Hacker Rank"})
certificates.append({"write":"Java Basic - Hacker Rank","image":"images/java basic.jpg","caption":"Hacker Rank"})
certificates.append({"write":"SQL Basic - Hacker Rank","image":"images/sql basic.jpg","caption":"Hacker Rank"})
certificates.append({"write":"Langchain Foundation - AlCamp - during Electro Pi Internship","image":"images/Langchain Foundation AlCamp Electro Pi Certificate.jpg","caption":"AlCamp - Electro Pi"})
certificates.append({"write":"RAG Foundation - AlCamp - during Electro Pi Internship","image":"images/RAG Foundation AlCamp Electro Pi Certificate.jpg","caption":"AlCamp - Electro Pi"})
certificates.append({"write":"Langchain with RAG Path - AlCamp - during Electro Pi Internship","image":"images/Langchain with RAG path AlCamp Electro Pi Certificate.jpg","caption":"AlCamp - Electro Pi"})
certificates.append({"write":"Problem Solving Basic - Hacker Rank","image":"images/problem_solving_basic (Hacker Rank).png","caption":"Hacker Rank"})
certificates.append({"write":"AI for Everyone - Maharatech","image":"images/AI for Everyone - ITI - maharatech en.jpg","caption":"Maharatech"})
certificates.append({"write":"Python Programming Basics - Maharatech","image":"images/Python Programming Basics Mahara Tech-1.jpg","caption":"Maharatech"})
certificates.append({"write":"Introduction to Java - Sololearn","image":"images/Introduction to Java_certificate.jpg","caption":"Sololearn"})
certificates.append({"write":"Introduction to Python - Sololearn","image":"images/Introduction to Python_certificate.jpg","caption":"Sololearn"})
certificates.append({"write":"Python Intermediate - Sololearn","image":"images/Python Intermediate_certificate.jpg","caption":"Sololearn"})
certificates.append({"write":"Python Developer - Sololearn","image":"images/Python Developer_certificate.jpg","caption":"Sololearn"})
certificates.append({"write":"Introduction to Programming using Python - Tawar We Ghayaer - Ministry of Youth and Sports - Ministry of Telecommunication - Microsoft","image":"images/python 1.jpg","caption":"Tawar We Ghayar"})
certificates.append({"write":"Python Programming Language Intermediate Level - Tawar We Ghayaer - Ministry of Youth and Sports - Ministry of Telecommunication - Microsoft","image":"images/python 2.jpg","caption":"Tawar We Ghayar"})
certificates.append({"write":"Introduction to Python Programming - Edraak","image":"images/download (4).jpg","caption":"Edraak"})
certificates.append({"write":"Java Programming 1 - Edraak","image":"images/java 1.jpg","caption":"Edraak"})
certificates.append({"write":"Java Programming 2 - Edraak","image":"images/java 2.jpg","caption":"Edraak"})
certificates.append({"write":"Java Programming 3 - Edraak","image":"images/java 3.jpg","caption":"Edraak"})
certificates.append({"write":"Python - Kaggle","image":"images/Abdallah Fekry Mohammed - Python.png","caption":"Kaggle"})
certificates.append({"write":"Java Programming - Great Learning","image":"images/Abdallah_Fekry_Mohammed20221019-2047-1pathg3.jpg","caption":"Great Learning"})
certificates.append({"write":"Digital Literacy Training Program - Egyptian Ministry of Youth and Sports","image":"images/Digital Literacy Training Certificate.jpg","caption":""})
certificates.append({"write":"SQL & Data Analysis Training Program - Egyptian Ministry of Youth and Sports","image":"images/SQL & Data Analysis Training Certificate.jpg", "caption":""})
certificates.append({"write":"Introductory Advanced Technologies Training Program - Egyptian Ministry of Youth and Sports","image":"images/Introductory Advanced Technologies Training Certificate.jpg", "caption":""})
for i in range(len(tabs)):
  with tabs[i]:
    st.write(certificates[i]["write"])
    if certificates[i]["image"] != "images/":
      st.image(certificates[i]["image"], caption = certificates[i]["caption"])
certificates_page = st.Page("certificates.py")
st.write("  \n")
st.write("  \n")
if st.button("View All Certificates", use_container_width=1):
    st.switch_page(certificates_page)
st.write("---")
st.info("Languages")
st.write("Arabic (native)")
st.write("English (very good)")
st.write("---")

st.info("Projects")
projects = st.Page("projects.py")
if st.button("View All Projects", use_container_width=1):
    st.switch_page(projects)
st.subheader("Graduation Project")
st.write("As a team leader i have distributed the tasks on the team members, i have decided to work with Agile methodology so i was making a meeting each one or two weeks with the team members to presenting the work done  \n i was responsible for the AI modules which are:")
st.write("""**My part in the project consists of three main modules:**

Module 1: An AI based smart chatbot called "Caroline" talking to the patient 
and taking its disease symptoms, then diagnosing the disease and 
recommend making some tests as x-ray, MRI ...  \nin addition, given 
information about the predicted disease as an overview, symptoms, and 
treatments.  \nIt can predict 30 diseases such as (Breast Cancer, Influenza, Covid 19, Stroke, ...) 

Module 2: A sequence of 14 AI Computer Vision models for scanning medical 
imaging and tests it can scan (X-ray, MRI, CT, OCT, ECG, or Food image), 
detect the image type (Image Recognition), if it is medical imaging image, 
applying anatomical recognition, disease evaluation, disease diagnosis.  \nIt 
can predict 25 disease types such as (Bone Fracture, Brain Tumor, Covid 19, 
Breast Cancer, ...)  \nIt also can recognize 101 food types from images and shows the approximate number of calories per gram.

Module 3: An ensemble Machine Learning (Random Forest) Model for scan Electrocardiography ECG and diagnosis the heart diseases.

In addition i have made some graphic designs as the Logo and the Banner,

Creating the Software Requirements Specification SRS and the proposal and give them to the other team members to working on them

Collecting the other' work and combining them, making documentation and the presentation

Making algorithm for MBTI personality analysis test
""")
st.write("---")

st.subheader("Logo Design")
st.image("images/Logo.png", caption="Logo Design")
st.write("---")
st.subheader("Poster Design")
st.write("  \n")
st.image("images/Banner.svg", caption="Banner Design")

st.write("---")
st.write("I was responsible for these features")
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.image(r"images/chatbot.png", caption="Chatbot Diagnosis")
with col2:
    st.image(r"images/x-ray (4).png", caption="Medical Imaging Scan")
with col3:
    st.image(r"images/burger.png", caption="Food Calories Scan")
with col4:
    st.image(r"images/heart-rate (2).png", caption="ECG Scan")
with col5:
    st.image(r"images/puzzle.png", caption="MBTI Personality Analysis Test")
st.write("---")

# Chatbot feature
st.header("Chatbot Diagnosis")
col1, col2 = st.columns([1,3])
with col1:
    st.image(r"images/chatbot.png")
with col2:
    # st.title("Chatbot Diagnosis")
    st.info("An AI based smart chatbot called \"Caroline\" talking to the patient and taking its disease symptoms, then diagnosing the disease and recommend making some tests as x-ray, MRI ... in addition, given information about the predicted disease as an overview, symptoms, and treatments. It can predict 30 diseases such as (Breast Cancer, Influenza, Covid 19, Stroke, ...)")
st.write("---")

# Xrays feature
st.header("Medical Imaging Scan")
col1, col2 = st.columns([1,3])
with col1:
    st.image(r"images/x-ray (4).png")
with col2:
    st.info("A sequence of AI Computer Vision models for scanning medical imaging and tests it can scan (X-ray, MRI, CT, OCT, ECG, or Food image), detect the image type (Image Recognition), if it is medical imaging image, applying anatomical recognition, disease evaluation, disease diagnosis. It can predict 25 disease types such as (Bone Fracture, Brain Tumor, Covid 19, Breast Cancer, ...)")
st.write("---")

# Food scan feature
col1, col2 = st.columns([1,3])
with col1:
    st.image(r"images/burger.png")
with col2:
    st.header("Food Images Scan")
    st.info("It also can recognize 101 food types from images and shows the approximate number of calories per gram.")
st.write("---")

# ECG scan feature
col1, col2 = st.columns([1,3])
with col1:
    st.image(r"images/heart-rate (2).png")
with col2:
    st.header("ECG Scan")
    st.info("An ensemble Machine Learning (Random Forest) Model for scan Electrocardiography ECG and diagnosis the heart diseases.")
st.write("---")

# MBTI personality test feature
col1, col2 = st.columns([1,3])
with col1:
    st.image(r"images/puzzle.png")
with col2:
    st.header("MBTI Personality Test")
    st.info("MBTI personality analysis test that consists of only 20 questions, after answering them you get your personality type and information about it that can help you to take better decision as choosing a school department or career work")
st.write("---")

# Diseases
st.title("Diseases Detection")
st.info("The AI doctor can detect many diseases")
st.image(r"images/fig1-1024x576.png")
st.write("---")

st.subheader("AI Scan Phases")
st.image(r"images/AI Mindmap.svg", caption="Scan Models Phases Mindmap")
st.write("---")

st.subheader("Medical Imaging Scan Diseases")
st.image(r"images/Diseases Mindmap.jpg", caption="Diseases Mindmap")
st.write("---")

st.subheader("Object Recognition")
st.info("Identify the medical imaging scan and food from images")
st.image(r"images/7-Best-Image-Recognition-APIs-e1587080882739.jpg", caption="Object Detection")
st.write("---")

st.subheader("Imaging Scan Type Detection")
st.info("Identifying the medical imaging scan type of 4 main types which are 'Electromagnetic Variations - Xray', 'Magnetic Resonance Imaging - MRI', 'Computerized Tomography - CT', or 'Optical Coherence Tomography - OCT'")
st.image(r"images/158096096_m.jpeg", caption="Medical Imaging Scan Type Detection")
st.write("---")

st.subheader("Anatomical Recognition")
st.info("Applying anatomical recognition on all imaging types to identify the body parts")
st.image(r"images/various-x-ray-images-of-human-body-parts-vector.jpg", caption="Anatomical Recognition")
st.write("---")

st.subheader("Brain Tumor Detection")
st.info("Can to detect brain tumor from MRI and diagnosis their types as 'Glioma_tumor', 'Meningioma_tumor', and 'Pituitary_tumor'")
st.image(r"images/brain.jpg", caption="Brain Tumor Detection")
st.write("---")

st.subheader("Bone Fracture Detection")
st.info("Can to detect bones fraction from x-rays and diagnosis their 10 types as 'Avulsion fracture', 'Comminuted fracture', 'Compression-Crush fracture', 'Fracture Dislocation', 'Greenstick fracture', 'Hairline Fracture', 'Impacted fracture', 'Intra-articular fracture', 'Longitudinal fracture', 'Oblique fracture', 'Pathological fracture', and 'Spiral Fracture'")
st.image(r"images/Fractures.jpeg", caption="Bone Fracture Detection")
st.write("---")

st.subheader("Breast Cancer Detection")
st.info("Can detect breast cancer from MRI and diagnosis its types 'Malignant' or 'Benign'")
st.image(r"images/3000-2000-2.75196496.jpg", caption="Breast Cancer Detection")
st.write("---")

st.subheader("Chest Diseases Detection")
st.info("Can detect chest diseases from x-rays and diagnosis if there is 'Covid 19' or 'Pneumonia'")
st.image(r"images/1e04_gefk_220113.jpg", caption="Chest Diseases Detection")
st.write("---")

st.subheader("Body Diseases Detection")
st.info("Can detect body diseases from CT scans and diagnosis if there is 'Cyst', 'Stones' or 'Tumors'")
st.image(r"images/resize-17111791171404206655GettyImages1185128095600x337.jpg", caption="Body Diseases Detection")
st.write("---")

st.subheader("ECG - Heart Diseases Detection")
st.info("Can detect heart diseases from Electrocardiography - ECG and diagnosis if there is 'Normal beat', 'Supraventricular premature beat', 'Premature ventricular contraction', 'Fusion of ventricular and normal beat', or 'Unclassifiable beat'")
st.image(r"images/Infinx-Blog-4-Ways-AI-Can-Help-Cardiology-Practices-Adapt-in-2020.jpg", caption="ECG Diseases Detection")
st.write("---")

st.subheader("Eyes Diseases Detection")
st.info("Can detect eyes diseases from OCT scans and diagnosis if there is 'CNV - Choroidal Neovascularization', 'DME - Diabetic Macular Edema' or 'Drusen'")
st.image(r"images/Screenshot 2024-07-16 154752.png", caption="Eyes Diseases Detection")
st.write("---")

st.subheader("Food Calories Detection")
st.info("Can detect food types from images and identify their approximation number of calories per gram. It can detect 101 types of food as 'Frensh fries', 'Pizza', 'Sushi', 'Pancakes', 'Chocolate cake', ...")
st.image(r"images/GENERAL GUIDELINES FOR EATING HEALTHY FOOD.png", caption="Food Calories Detection")
st.write("---")

st.subheader("Models Accuracy")
st.info("Models accuracy table contains model' input, output, functionality, training and testing accuracy, and recall")
st.image("images/Screenshot 2024-07-17 122050.png")
st.info("Models' training and testing accuracy graph")
st.image("images/output.2png.png")
st.write("---")

st.image("images/background.png", caption="Smart Comprehensive Medical System")
st.write("---")

# Footer
footer = st.container(border=True) 
with footer:
    st.columns([1,1,1])[1].image("images/Picsart_24-07-24_23-25-40-729.png")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("Services")
        st.caption("Data Science")
        st.caption("Machine Learning")
        st.write("Social")
        col11, col22, col33, col44, col5 = st.columns([1,1,1,1,3])
        with col11:
            st.markdown("[![FB](https://raw.githubusercontent.com/BeboFekry/ChatHub/main/images/702300.png)](http://www.linkedin.com/in/abdallah-fekry)")
        with col22:
            st.markdown("[![FB](https://raw.githubusercontent.com/BeboFekry/ChatHub/main/images/25231.png)](https://github.com/BeboFekry?tab=repositories)")
        with col33:
            st.markdown("[![FB](https://raw.githubusercontent.com/BeboFekry/ChatHub/main/images/4844503.png)](https://www.kaggle.com/bebofekry)")
        with col44:
            st.markdown("[![FB](https://raw.githubusercontent.com/BeboFekry/ChatHub/main/images/streamlit-mark-color.png)](https://abdalleh-fekry.streamlit.app/)")
    with col2:
        st.write("Contact")
        st.caption("Eng. Abdallah Fekry")
        st.caption("Egypt, Cairo")
        st.caption("+20 111 9499 384")
        st.caption("abdallahfekry95@gmail.com")
    with col3:
        st.write("About")
        st.caption("Smart Doctor")
        st.caption("Intelligent Comprehensive Medical System")
        st.caption("NLP + Computer Vision models that mimic a doctor")

col1, col2, col3 = st.columns([1,3,1])
with col1:
    st.caption("  \tCopyright protected")
