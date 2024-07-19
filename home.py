import streamlit as st

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
    st.write("**Data Scientist**")
st.write("---")

st.info("Overview")
st.write("""As a Computer Science enthusiast with an excellent academic background, I am determined to make a significant impact 
in the tech industry. I've had the privilege of gaining hands-on experience as an AI and IoT Trainee at NTI and Big Data 
Trainee at NTI. This experience has honed my skills and fueled my passion for innovation. I also have hands-on experience 
in real-world projects as a Data Science and Business Analytics intern at The Sparks Foundation, Machine Learning intern 
at Code Casa, and Machine Learning intern at Prodigy InfoTech.""")
st.write("---")

profile = st.Page("profile.py", title="Profile", icon=":material/person:")
# projects = st.Page("projects2.py", title="Projects", icon=":material/work:")

st.info("Education")
st.write("Bachelor’s degree in Computer Science - Culture and Science City C.S.C - 2020-2024  \nGrade: Excellent")
st.write("---")

st.info("Experience")
st.write("**Data Science & Machine Learning | Microsoft Student Clubs by EELU | March 2024 – Present**")
st.write("---")

st.write("**Data Science Intern | Code Alpha | May 2024 - Present**")
st.write("---")

st.write("""**Big Data Trainee | National Telecommunication Institute NTI | March 2024 – May 2024** 
  \n• I have learned the Networks & Linux essentials needed for Hadoop platforms. 
  \n• I learned Python programming, the basic syntax and advanced usage of Python as usage of 
Numpy, Pandas, Matplotlib, and OOP. 
  \n• It gives me a brief overview of how to process data using Structured Query Language (SQL). 
  \n• I have an introduction to Big Data and work on Hadoop platforms.""")
st.write("---")
st.write("""**Machine Learning Intern | Prodigy Infotech | February 2024 – March 2024** 
  \nDuring the internship, I have hands-on experience on five real-world projects:  
  \n• Housing price prediction using Multiple Linear Regression algorithm. 
  \n• Clustering using K-Means algorithm. 
  \n• Classification using Support Vector Machine SVM algorithm. 
  \n• Hand Gesture classification using Deep Learning. 
  \n• Food Classification and identify calories using Deep Learning – CNN. 
  \n• In addition to the part of Data Analysis, Preprocessing, Cleansing and Visualization.""")
st.write("---")
st.write("""**Machine Learning Intern | Code Casa | September 2023 – October 2023** 
  \nDuring the internship, I have hands-on experience on two real-world projects:  
  \n• Stock Price Prediction by LSTM model Architecture. 
  \n• Housing Price Prediction using Multiple Linear Regression Algorithm. 
  \n• In addition to the part of Data Analysis, Preprocessing, Cleansing and Visualization. 
  \n• In addition, I got a Letter of Recommendation for the hard work. """)
st.write("---")
st.write("""**Data Science and Business Analytics Intern | The Sparks Foundation | September 2023 – October 2023** 
  \nDuring the internship, I have hands-on experience on three real-world projects: 
  \n• Prediction using Supervised Learning using Regression Techniques. 
  \n• Prediction using Unsupervised Learning (I have used K-Means Algorithm). 
  \n• Prediction using Decision Tree Classifier. 
  \n• In addition to the part of Data Analysis, Preprocessing, Cleansing and Visualization""")
st.write("---")
st.write("""**Artificial Intelligence AI & Internet of Things IoT Trainee | National Telecommunication Institute NTI | September 2023 – October 2023** 
  \nDuring the 1-month (120 hours) Training Program, I had the opportunity to dive deep into AI world. 
  \n• Developing python codes from basic loops, condition statements to libraries as Numpy, 
Pandas, Matplotlib, Seaborn, Scikit-Learn, Keras, and TensorFlow. 
  \n• Learned Machine Learning techniques and developed projects as ECG classification, etc. 
  \n• Gained experience in AI techniques from data preprocessing, cleansing, analysis and 
visualization to machine learning and deep learning algorithms and predictive modelling. 
  \n• Learned Natural Language Processing basics and applying text preprocessing techniques as 
text padding and tokenization in projects as sentiment analysis, and on IMDB classification. 
  \n• Learned the Computer Vision basics and applying projects as chest x-ray diagnosis, 
handwritten numbers classification, object detection, etc.""")
st.write("---")

st.info("Certificates")
st.write("Artificial Intelligence AI and Internet of Things IoT Training - National Telecommunication Institute NTI")
# st.image("images/NTI AI and IoT Training Certificate.jpg", caption="National Telecommunication Institute NTI")
st.write("---")

st.write("Internet of Things Connecting Things IoT CT - Cisco Networking Academy")
# st.image("images/AbdallahFekry Mohammed-IoT CT-certificate_page-0001.jpg", caption="Cisco Networking Academy")
st.write("---")

st.write("Big Data Essentials Training - National Telecommunication Institute NTI")
# st.image("images/NTI AI and IoT Training Certificate.jpg", caption="National Telecommunication Institute NTI")
st.write("---")

st.write("Huawei HCIA AI v3.5 - Huawei and the Egyptian Ministry of Youth and Sports")
# st.image("images/", caption="")
st.write("---")

st.write("Data Science and Business Analytics Internship Offer Letter - The Sparks Foundation")
# st.image("images/5VET2JCRLM.png", caption="The Sparks Foundation")
st.write("---")

st.write("Data Science and Business Analytics Internship - The Sparks Foundation")
# st.image("images/MUHCQHJ8JR (1).png", caption="The Sparks Foundation")
st.write("---")

st.write("Machine Learning Internship Offer Letter - Code Casa")
# st.image("images/Abdallah Fekry Mohammed Offer Letter_page-0001.jpg", caption="Code Casa")
st.write("---")

st.write("Machine Learning Internship - Code Casa")
# st.image("images/Abdallah Fekry Mohammed Certificate_page-0001.jpg", caption="Code Casa")
st.write("---")

st.write("Machine Learning Internship Letter of Recommendation - Code Casa")
# st.image("images/Letter of Recommendation (Code Casa).jpg", caption="Code Casa")
st.write("---")

st.write("Python Basic - Hacker Rank")
# st.image("images/python basic.jpg", caption="Hacker Rank")
st.write("---")

st.write("Java Basic - Hacker Rank")
# st.image("images/java basic.jpg", caption="Hacker Rank")
st.write("---")

st.write("SQL Basic - Hacker Rank")
# st.image("images/sql basic.jpg", caption="Hacker Rank")
st.write("---")

st.write("Problem Solving Basic - Hacker Rank")
# st.image("images/problem_solving_basic (Hacker Rank).png", caption="Hacker Rank")
st.write("---")

st.write("AI for Everyone - Maharatech")
# st.image("images/AI for Everyone - ITI - maharatech en.jpg", caption="Maharatech")
st.write("---")

st.write("Python Programming Basics - Maharatech")
# st.image("images/Course_Certificate_En (1).jpg", caption="Maharatech")
st.write("---")

st.write("Introduction to Java - Sololearn")
# st.image("images/Introduction to Java_certificate.jpg", caption="Sololearn")
st.write("---")

st.write("Introduction to Python - Sololearn")
# st.image("images/Introduction to Python_certificate.jpg", caption="Sololearn")
st.write("---")

st.write("Python Intermediate - Sololearn")
# st.image("images/Python Intermediate_certificate.jpg", caption="Sololearn")
st.write("---")

st.write("Python Developer - Sololearn")
# st.image("images/Python Developer_certificate.jpg", caption="Sololearn")
st.write("---")

st.write("Introduction to Programming using Python - Tawar We Ghayaer - Ministry of Youth and Sports - Ministry of Telecommunication - Microsoft")
# st.image("images/python 1.jpg", caption="Tawar We Ghayar")
st.write("---")

st.write("Python Programming Language Intermediate Level - Tawar We Ghayaer - Ministry of Youth and Sports - Ministry of Telecommunication - Microsoft")
# st.image("images/python 2.jpg", caption="Tawar We Ghayar")
st.write("---")

st.write("Introduction to Python Programming - Edraak")
# st.image("images/download (4).jpg", caption="Edraak")
st.write("---")

st.write("Java Programming 1 - Edraak")
# st.image("images/java 1.jpg", caption="Edraak")
st.write("---")

st.write("Java Programming 2 - Edraak")
# st.image("images/java 2.jpg", caption="Edraak")
st.write("---")

st.write("Java Programming 3 - Edraak")
# st.image("images/java 3.jpg", caption="Edraak")
st.write("---")

st.write("Python - Kaggle")
# st.image("images/Abdallah Fekry Mohammed - Python.png", caption="Kaggle")
st.write("---")

st.write("Java Programming - Great Learning")
# st.image("images/Abdallah_Fekry_Mohammed20221019-2047-1pathg3.jpg", caption="Great Learning")
st.write("---")

st.write("Digital Literacy Training Program - Egyptian Ministry of Youth and Sports")
# st.image("images/Abdallah_Fekry_Mohammed20221019-2047-1pathg3.jpg", caption="Great Learning")
st.write("---")

st.write("Data Analysis & SQL Training Program - Egyptian Ministry of Youth and Sports")
# st.image("images/Abdallah_Fekry_Mohammed20221019-2047-1pathg3.jpg", caption="Great Learning")
st.write("---")

st.write("Freelancing Training Program - Egyptian Ministry of Youth and Sports")
# st.image("images/Abdallah_Fekry_Mohammed20221019-2047-1pathg3.jpg", caption="Great Learning")
st.write("---")

st.info("Languages")
st.write("Arabic (native)")
st.write("English (very good)")
st.write("---")

st.info("Graduation Project")
st.write("As a team leader i have distributed the tasks on the team, i choose to work with Agile methodology so i have made a meeting each one or two weeks with the team members to presenting the work done  \n i was responsible for the AI modules which are:")
st.write("""**My part in the project consists of three main modules:**

Module 1: An AI based smart chatbot called "Caroline" talking to the patient 
and taking its disease symptoms, then diagnosing the disease and 
recommend making some tests as x-ray, MRI ... in addition, given 
information about the predicted disease as an overview, symptoms, and 
treatments. 
It can predict 30 diseases such as (Breast Cancer, Influenza, Covid 19, Stroke, ...) 

Module 2: A sequence of 14 AI Computer Vision models for scanning medical 
imaging and tests it can scan (X-ray, MRI, CT, OCT, ECG, or Food image), 
detect the image type (Image Recognition), if it is medical imaging image, 
applying anatomical recognition, disease evaluation, disease diagnosis. It 
can predict 25 disease types such as (Bone Fracture, Brain Tumor, Covid 19, 
Breast Cancer, ...) 
It also can recognize 101 food types from images and shows the approximate number of calories per gram.

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
st.image("images/Banner.png", caption="Banner Design")

st.write("---")
st.write("I was responsible for these features")
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.image(r"images\chatbot.png", caption="Chatbot Diagnosis")
with col2:
    st.image(r"images\x-ray (4).png", caption="Medical Imaging Scan")
with col3:
    st.image(r"images\burger.png", caption="Food Calories Scan")
with col4:
    st.image(r"images\heart-rate (2).png", caption="ECG Scan")
with col5:
    st.image(r"images\puzzle.png", caption="MBTI Personality Analysis Test")
st.write("---")

# Chatbot feature
st.header("Chatbot Diagnosis")
col1, col2 = st.columns([1,3])
with col1:
    st.image(r"images\chatbot.png")
with col2:
    # st.title("Chatbot Diagnosis")
    st.info("An AI based smart chatbot called \"Caroline\" talking to the patient and taking its disease symptoms, then diagnosing the disease and recommend making some tests as x-ray, MRI ... in addition, given information about the predicted disease as an overview, symptoms, and treatments. It can predict 30 diseases such as (Breast Cancer, Influenza, Covid 19, Stroke, ...)")
st.write("---")

# Xrays feature
st.header("Medical Imaging Scan")
col1, col2 = st.columns([1,3])
with col1:
    st.image(r"images\x-ray (4).png")
with col2:
    st.info("A sequence of AI Computer Vision models for scanning medical imaging and tests it can scan (X-ray, MRI, CT, OCT, ECG, or Food image), detect the image type (Image Recognition), if it is medical imaging image, applying anatomical recognition, disease evaluation, disease diagnosis. It can predict 25 disease types such as (Bone Fracture, Brain Tumor, Covid 19, Breast Cancer, ...) It also can recognize 101 food types from images and shows the approximate number of calories per gram.")
st.write("---")

# Food scan feature
col1, col2 = st.columns([1,3])
with col1:
    st.image(r"images\burger.png")
with col2:
    st.header("Food Images Scan")
    st.info("It also can recognize 101 food types from images and shows the approximate number of calories per gram.")
st.write("---")

# ECG scan feature
col1, col2 = st.columns([1,3])
with col1:
    st.image(r"images\heart-rate (2).png")
with col2:
    st.header("ECG Scan")
    st.info("An ensemble Machine Learning (Random Forest) Model for scan Electrocardiography ECG and diagnosis the heart diseases.")
st.write("---")

# MBTI personality test feature
col1, col2 = st.columns([1,3])
with col1:
    st.image(r"images\puzzle.png")
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
st.image(r"images/test/AI Mindmap.jpg", caption="Scan Models Phases Mindmap")
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
st.image(r"D:\Downloads\brain.jpg", caption="Brain Tumor Detection")
st.write("---")

st.subheader("Bone Fracture Detection")
st.info("Can to detect bones fraction from x-rays and diagnosis their 10 types as 'Avulsion fracture', 'Comminuted fracture', 'Compression-Crush fracture', 'Fracture Dislocation', 'Greenstick fracture', 'Hairline Fracture', 'Impacted fracture', 'Intra-articular fracture', 'Longitudinal fracture', 'Oblique fracture', 'Pathological fracture', and 'Spiral Fracture'")
st.image(r"images\Fractures.jpeg", caption="Bone Fracture Detection")
st.write("---")

st.subheader("Breast Cancer Detection")
st.info("Can detect breast cancer from MRI and diagnosis its types 'Malignant' or 'Benign'")
st.image(r"images\3000-2000-2.75196496.jpg", caption="Breast Cancer Detection")
st.write("---")

st.subheader("Chest Diseases Detection")
st.info("Can detect chest diseases from x-rays and diagnosis if there is 'Covid 19' or 'Pneumonia'")
st.image(r"images\1000_F_757215169_shf3DYxchUW3uYxJ4320yPj9YyoYyq3G.jpg", caption="Chest Diseases Detection")
st.write("---")

st.subheader("Body Diseases Detection")
st.info("Can detect body diseases from CT scans and diagnosis if there is 'Cyst', 'Stones' or 'Tumors'")
st.image(r"images\resize-17111791171404206655GettyImages1185128095600x337.jpg", caption="Body Diseases Detection")
st.write("---")

st.subheader("ECG - Heart Diseases Detection")
st.info("Can detect heart diseases from Electrocardiography - ECG and diagnosis if there is 'Normal beat', 'Supraventricular premature beat', 'Premature ventricular contraction', 'Fusion of ventricular and normal beat', or 'Unclassifiable beat'")
st.image(r"images\Infinx-Blog-4-Ways-AI-Can-Help-Cardiology-Practices-Adapt-in-2020.jpg", caption="ECG Diseases Detection")
st.write("---")

st.subheader("Eyes Diseases Detection")
st.info("Can detect eyes diseases from OCT scans and diagnosis if there is 'CNV - Choroidal Neovascularization', 'DME - Diabetic Macular Edema' or 'Drusen'")
st.image(r"images\Screenshot 2024-07-16 154752.png", caption="Eyes Diseases Detection")
st.write("---")

st.subheader("Food Calories Detection")
st.info("Can detect food types from images and identify their approximation number of calories per gram. It can detect 101 types of food as 'Frensh fries', 'Pizza', 'Sushi', 'Pancakes', 'Chocolate cake', ...")
st.image(r"images/GENERAL GUIDELINES FOR EATING HEALTHY FOOD.png", caption="Food Calories Detection")
st.write("---")

st.subheader("Models Accuracy")
st.info("Models accuracy table contains model' input, output, functionality, training and testing accuracy, and recall")
st.image("images/test/Screenshot 2024-07-17 122050.png")
st.info("Models' training and testing accuracy graph")
st.image("images/test/output.2png.png")
st.write("---")

st.image("images/background.png", caption="Smart Comprehensive Medical System")
st.write("---")

# Footer
col1, col2, col3 = st.columns(3)
with col1:
    st.write("Social")
    col11, col22 = st.columns([1,4])
    with col11:
        st.image("images/702300.png")
    with col22:
        st.link_button("Linkedin", "http://www.linkedin.com/in/abdallah-fekry")
    col11, col22 = st.columns([1,4])
    with col11:
        st.image("images/25231.png")
    with col22:
        st.link_button("GitHub", "https://github.com/BeboFekry?tab=repositories")
    col11, col22 = st.columns([1,4])
    with col11:
        st.image("images/4844503.png")
    with col22:
        st.link_button("GitHub", "https://www.kaggle.com/bebofekry")
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

st.write("---")

col1, col2, col3 = st.columns([1,3,1])
with col1:
    st.caption("Copyright protected")
