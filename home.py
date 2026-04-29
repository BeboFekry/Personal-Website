import streamlit as st
import streamlit.components.v1 as components

if st.session_state.first_time:
    st.toast("Rotate your mobile screen", icon=":material/sync:")
    st.session_state.first_time = False

# Header
c1, c2 = st.columns([1,2.5])
with c1:
    st.write("")
    st.header("Abdallah Fekry", divider='blue')
    st.markdown(
    ":blue-badge[:material/robot_2: AI] " \
    ":blue-badge[:material/automation: Machine Learning]" \
    ":blue-badge[:material/share: Deep Learning]" \
    ":blue-badge[:material/robot_2: NLP] " \
    ":blue-badge[:material/scan: Computer Vision] " \
    ":blue-badge[:material/bar_chart_4_bars: Data Analytics] " \
    )
    st.write("##### AI/ML Engineer - Data Scientist")
    st.write(":material/distance: Cairo, Egypt")
    st.write(":material/email: abdallahfekry95@gmail.com")
    st.write(":material/phone: +20 111 94 99 384")
    # Social
    col11, col22, col33, col44, col55, space = st.columns([1,1,1,1,1.15,5], vertical_alignment='bottom')
    with col11:
        st.markdown("[![G](https://raw.githubusercontent.com/BeboFekry/Personal-Website/main/images/gmail.png)](mailto:abdallahfekry95@gmail.com)")
    with col22:
        st.markdown("[![LI](https://raw.githubusercontent.com/BeboFekry/Personal-Website/main/images/702300.png)](http://www.linkedin.com/in/abdallah-fekry)")
    with col33:
        st.markdown("[![GH](https://raw.githubusercontent.com/BeboFekry/Personal-Website/main/images/25231.png)](https://github.com/BeboFekry?tab=repositories)")
    with col44:
        st.markdown("[![Kg](https://raw.githubusercontent.com/BeboFekry/Personal-Website/main/images/4844503.png)](https://www.kaggle.com/bebofekry)")
    with col55:
        st.markdown("[![ST](https://raw.githubusercontent.com/BeboFekry/ChatHub/main/images/streamlit-mark-color.png)](https://abdalleh-fekry.streamlit.app/)")
        
with c2:
    # Black Shape
    with open("html.txt", 'r') as f:
        particles_js = f.read(  )
    components.html(particles_js, height=370, scrolling=False)
st.divider()
# ________________________________________________________________________________________________

# Overview
st.header(":material/overview: Overview", divider='blue')
text_to_justify = """As a computer science enthusiast with a great academic background with grade very good with honors, 
    I am determined to make a significant impact in the tech industry. 
    I've had the privilege of gaining hands-on experience as an AI Engineer in internship opportunity at Electro Pi working on variety of real-world projects, 
    Artificial Intelligence (AI) and Internet of Things (IoT) trainee and Big Data treinee at National Telecommunication Institute NTI. 
    This experience has honed my skills and fueled my passion for innovation. I also have hands-on experience in real-world projects as i was 
    Data Science and Business Analytics intern at The Sparks Foundation, Machine Learning intern at Code Casa, and finally, Machine Learning intern at Prodigy InfoTech."""
st.markdown(
f"""
<div style='text-align: justify; 
            background-color: #ffffff; 
            padding: 15px; 
            border-radius: 10px; 
            font-size: 16px; 
            line-height: 1.6;
            color: #333;'>
        {text_to_justify}
        </div>
""",
unsafe_allow_html=True
)
st.divider()

profile = st.Page("profile.py", title="Profile", icon=":material/person:")
# ________________________________________________________________________________________________

# Education
st.header(":material/school: Education", divider='blue')
col1, col2 = st.columns([3,1])
with col1:
    st.write("**Bachelor's degree BSc in Computer Science - Culture and Science City C.S.C**  \n**Department:** Computer Science CS  \n**Cumulative Grade:** Very Good with Honors  \n**Graduation Project Grade:** Excellent")
with col2:
    st.markdown(f"""<div style='text-align: justify;font-size: 16px;line-height: 1.6;color: #333;direction: rtl;'>
        (October 2020 - June 2024)</div>""",unsafe_allow_html=True)
st.write("🏆 Graduation Project Publication Achieved Winner of **Best Distinguished Applied Solution Showcase** in **Computer Vision Projects Expo 2024** Competition by Ready Tensor")
st.write("**Course work:**")
st.markdown(
":grey-badge[:material/code: Programming]" \
":grey-badge[:material/data_object: Object Oriented Programming OOP]" \
":grey-badge[:material/share: Data Structures & Algorithms] " \
":grey-badge[:material/percent: Probability & Statistics] " \
":grey-badge[:material/function: Calculus] " \
":grey-badge[:material/database: Advanced Database] " \
":grey-badge[:material/robot_2: Artificatial Intelligence] " \
":grey-badge[:material/bar_chart_4_bars: Data Science and Machine Learning] " \
":grey-badge[:material/code: Pattern Recognition] " \
":grey-badge[:material/computer: Operating Systems OS] " \
":grey-badge[:material/computer: Computer Architicture] " \
":grey-badge[:material/developer_mode_tv: Software Engineering] " \
":grey-badge[:material/developer_mode_tv: System Analysis and Design] " \
":grey-badge[:material/scan: Image Processing] " \
":grey-badge[:material/share: Computer Networks] " \
)

if 'g' not in st.session_state:
    st.session_state.g = False
if 'c' not in st.session_state:
    st.session_state.c = False
col1, col2, col3, col4 = st.columns([1,1,1,3])
with col1:
    if st.button(":material/license: Graduation Certificate", type='tertiary'):
        st.session_state.g = not st.session_state.g
with col2:
    if st.button("🏆 Competition Certificate", type='tertiary'):
        st.session_state.c = not st.session_state.c
with col3:
    st.link_button(":material/link: Publication Link",url='https://app.readytensor.ai/publications/i_care_-_smart_doctor_-_comprehensive_medical_system_sZgWGLbCUMiS', type='tertiary')
if st.session_state.g:
    st.columns([1,1,1])[1].image("images\Abdallah Fekry Graduation Certificate.jpg")
if st.session_state.c:
    st.columns([1,2,1])[1].image("images\Distinguished Applied Solution Showcase in CV Projects Expo 2024 Competition (Ready Tensor).jpg")
st.divider()
# ______________________________________________________________________________

# Skills
st.header(":material/person_celebrate: Skills", divider='blue')
st.markdown(
    ":material/calculate: **Mathematics:** " \
    ":blue-badge[:material/percent: Probability] " \
    ":blue-badge[:material/percent: Statistics]" \
    ":blue-badge[:material/function: Calculus]" \
    ":blue-badge[:material/square_foot: Linear Algebra] " \
    ":blue-badge[:material/functions: Optimization] " \
)
st.markdown(
    ":material/bar_chart_4_bars: **Data Analysis & Visualization:** " \
    ":blue-badge[:material/deployed_code: Numpy] " \
    ":blue-badge[:material/table: Pandas]" \
    ":blue-badge[:material/bar_chart_4_bars: Matplotlib]" \
    ":blue-badge[:material/bar_chart: Seaborn] " \
    ":blue-badge[:material/table_chart_view: MS Power BI] " \
)
st.markdown(
    ":material/code: **Programming:** " \
    ":blue-badge[:material/code: Python] " \
    ":blue-badge[:material/coffee: Java]" \
    ":blue-badge[:material/data_object: Oblect Oriented Programming - OOP]" \
    ":blue-badge[:material/database: SQL] " \
    ":blue-badge[:material/share: Data Structures & Algorithms] " \
)
st.markdown(
    ":material/network_intel_node: **Machine Learning ML/Deep Learning DL:** " \
    ":blue-badge[:material/network_intel_node: Scikit-learn] " \
    ":blue-badge[:material/share: TensorFlow]" \
    ":blue-badge[:material/share: Keras]" \
)
st.markdown(
    ":material/robot_2: **Natural Language processing NLP:** " \
    ":blue-badge[:material/text_compare: LSTM] " \
    ":blue-badge[:material/robot_2: LangChain]" \
    ":blue-badge[:material/search: RAG]" \
    ":blue-badge[:material/database: Chroma DB]" \
)
st.markdown(
    ":material/code: **Dev Tools:** " \
    ":blue-badge[:material/code: Git] " \
    ":blue-badge[:material/api: REST APIs by Flask]" \
    ":blue-badge[:material/bar_chart: MS Power BI]" \
    ":blue-badge[:material/developer_mode_tv: Streamlit]" \
)
st.markdown(
    ":material/list: **Methodologies:** " \
    ":blue-badge[:material/format_line_spacing: Agile] " \
    ":blue-badge[:material/water: Waterfall]" \
)
st.divider()
# _________________________________________________________________________________________


# Experience
st.header(":material/work: Experience", divider='blue')
st.write("")
col1, col2 = st.columns([3,1])
with col1:
    st.markdown(f"""<div style='font-size: 18px;font-weight: bold;color: #333;'>
        Ai Engineer | Electro Pi | internship
        </div>""",unsafe_allow_html=True)
with col2:
    st.markdown("(August 2024 - October 2024)",text_alignment='right')
st.write("")
st.write("""  \n• Developed more than 8 AI projects in NLP, LLM, Computer Vision, and Speech Recognition. 
      \n• Developed NLP Techniques as LLM using LangChain and RAG for making customized chatbots to answer business questions. 
      \n• Applied the Computer Vision Techniques as OCR for using in invoicing systems and connect it with LLM to extract the data and add it to a database for the system. 
      \n• Working with other techniques as Speech Recognition (voice to text) and (text to voice), Wav2Lip for Lip Syncing for making human like chatbots.
      \n• Working individually and as a part of a team using Agile methodology.""")
st.divider()

col1, col2 = st.columns([3,1])
with col1:
    st.markdown(f"""<div style='font-size: 18px;font-weight: bold;color: #333;'>
        Data Science & Machine Learning | Microsoft Student Clubs by EELU
        </div>""",unsafe_allow_html=True)
with col2:
    st.markdown("(March 2024 - September 2024)""",text_alignment='right')
st.write("")
st.write("")
st.divider()


col1, col2 = st.columns([3,1])
with col1:
    st.markdown(f"""<div style='font-size: 18px;font-weight: bold;color: #333;'>
        Big Data Trainee | National Telecommunication Institute NTI
        </div>""",unsafe_allow_html=True)
with col2:
    st.markdown("(March 2024 - May 2024)",text_alignment='right')
st.write("")
st.write("""\n• Got the foundation of 2 essentials needed for Hadoop platforms Networks & Linux. 
  \n• Developed an interactive Python programming codes and integrating practical exercises on 5 advanced topics 
    like OOP, Numpy, Pandas, Matplotlib and Seaborn and improving data handling efficiency. 
  \n• Develop a completed database, analyze data, apply EDA and ask business questions in a reports using Structured Query Language SQL. 
  \n• Had the opportunity to start with Big Data tools and techniques and work on Hadoop platforms.""")
st.divider()


col1, col2 = st.columns([3,1])
with col1:
    st.markdown(f"""<div style='font-size: 18px;font-weight: bold;color: #333;'>
        Machine Learning Intern | Prodigy Infotech
        </div>""",unsafe_allow_html=True)
with col2:
    st.markdown("(February 2024 - March 2024)",text_alignment='right')
st.write("")
st.write("""\nDuring the internship, I have hands-on experience on 5 real-world projects:
  \n• Developed 3 Machine Learning projects such as House Price Prediction using Multiple Linear Regression Customer Clustering using K-Means, Dogs and Cats 
    Classification using Support Vector Machine SVM. 
  \n• Architected 2 Deep Learning projects such as Hand Gesture classification using Deep Learning, Food Type 
    Classification and identify calories using Deep Learning CNN. 
  \n• In addition, the data analysis, cleansing, preprocessing and visualization parts for 5 projects.""")
st.divider()

col1, col2 = st.columns([3,1])
with col1:
    st.markdown(f"""<div style='font-size: 18px;font-weight: bold;color: #333;'>
        Machine Learning Intern | Code Casa
        </div>""",unsafe_allow_html=True)
with col2:
    st.markdown("(September 2023 - October 2023)",text_alignment='right')
st.write("")
st.write("""\n• During the internship, I have hands-on experience on 2 real-world projects as Stock Price Prediction using LSTM model architecture and 
    Housing Price Prediction using Multiple Linear Regression Algorithm.
  \n• Collect, analyze, preprocess and clean data from 2 datasets then visualize the results for 2 projects. 
  \n• Received a Letter of Recommendation after the 1-month internship for responsibility and professional work.""")
st.divider()

col1, col2 = st.columns([3,1])
with col1:
    st.markdown(f"""<div style='font-size: 18px;font-weight: bold;color: #333;'>
        Data Science and Business Analytics Intern | The Sparks Foundation
        </div>""",unsafe_allow_html=True)
with col2:
    st.markdown("(September 2023 - October 2023)",text_alignment='right')
st.write("")
st.write("""\nDuring the internship, I have hands-on experience on three real-world projects: 
  \n• Prediction using Supervised Learning using Regression Techniques. 
  \n• Prediction using Unsupervised Learning (I have used K-Means Algorithm). 
  \n• Prediction using Decision Tree Classifier. 
  \n• In addition to the part of Data Analysis, Preprocessing, Cleansing and Visualization""")
st.divider()

col1, col2 = st.columns([3,1])
with col1:
    st.markdown(f"""<div style='font-size: 18px;font-weight: bold;color: #333;'>
        Artificial Intelligence AI & Internet of Things IoT Trainee | National Telecommunication Institute NTI
        </div>""",unsafe_allow_html=True)
with col2:
    st.markdown("(September 2023 - October 2023)",text_alignment='right')
st.write("")
text_to_justify = """\nDuring the 1-month (120 hours) Training Program, had the opportunity to dive deep into the AI world. 
  \n• Developed python codes hands-on experience with Artificial Intelligence tools such as Numpy, Pandas, 
    Matplotlib, Seaborn, Scikit-Learn, Keras, and TensorFlow. 
  \n• Mastered AI techniques including mathematics, data preprocessing, cleansing, and visualization while 
    implementing machine learning and deep learning algorithms, this knowledge enabled the successful 
    completion of 10 predictive modeling projects. 
  \n• Experienced in Natural Language Processing NLP techniques and applying text preprocessing as text 
    stemming, padding and tokenization in 2 projects as sentiment analysis, and on IMDB classification. 
  \n• Experienced in Computer Vision techniques as CNN, RNN, LSTM, etc. and applying 5 projects as chest 
    Xray diagnosis, handwritten numbers classification, object detection, face recognition, etc."""
st.markdown(f"""<div style='text-align: justify;font-size: 16px;line-height: 1.6;color: #333;'>
        {text_to_justify}
        </div>""",unsafe_allow_html=True)
st.divider()
# __________________________________________________________________________________________

# Projects
st.header(":material/share: Projects", divider='blue')

projects = []

def add_project(data):
    projects.append(
        {
            "title": data['title'],
            "images": data['images'],
            "video": data['video'],
            "description": data['description'],
            "tools": data['tools'],
            "links": data['links'],
            "achivements":data['achivements']
        }
    )
def add_tools(tools_list, color = "blue"):
    # global skills
    tools = ""
    for tool in tools_list:
        tools = tools + f""":{color}-badge[:material/code: {tool}] """
    return tools


# project 1
p = {
    "title":"The Voices of History - Interactive Smart Digital Museum",
    "video":'https://youtu.be/GdaU0RYDoDw?si=zGzj4kTkSuckBJLu',
    "images":["images/image.jpg", 
              "https://d112y698adiu2z.cloudfront.net/photos/production/software_photos/004/450/766/datas/original.jpg",
              "https://d112y698adiu2z.cloudfront.net/photos/production/software_photos/004/450/785/datas/original.jpg",
              "https://d112y698adiu2z.cloudfront.net/photos/production/software_photos/004/450/768/datas/original.jpg",
              "https://d112y698adiu2z.cloudfront.net/photos/production/software_photos/004/450/769/datas/original.jpg",
              "https://d112y698adiu2z.cloudfront.net/photos/production/software_photos/004/450/770/datas/original.jpg",
              "https://d112y698adiu2z.cloudfront.net/photos/production/software_photos/004/450/772/datas/original.jpg",
              "https://d112y698adiu2z.cloudfront.net/photos/production/software_photos/004/450/831/datas/original.jpg"
              ],
    "description":"""
    The Voices of History is an interactive digital museum AI-powered web application that allows users to communicate with historical characters inside a virtual museum environment. 

    The system combines conversational AI, voice interaction, visual animations, and computer vision to create an immersive educational experience.

    Users can interact using text, voice, or images, and the system responds with spoken explanations with animation in real time.

    Users can speak or type to famous personalities such as:

        o Tour Guide (default virtual character works as the tour guide for the digital museum)

            •   Karim (tour guide)
        
        o Historical Characters

            •   Tut Ankh Amun

            •   Nefertiti
        
        o Scientific Characters
            
            •   Isaac Newton
        
        o Artistic Characters
            
            •   Leonardo da Vinci
    
    Each character responds using a personalized prompt that reflects their historical identity and communication style.
    
    The system also supports image recognition, allowing users to upload an image of an antiquities, archaeological sites, and tourist attractions, or object. 
    
    The AI analyzes the image and provides a description, simulating a museum guide explaining the item.
    
    The application is implemented as a real-time multimodal AI interface using large language models, speech technologies, and visual processing to replicate a digital museum tour.

    Goal: The goal of the project is to transform the traditional museum experience and educational experience into an interactive AI-driven learning environment.""",

    "tools":['Python', 'Large Language Model LLM', 'Langgraph', 'Gemini API', 'Google Cloud Service', 'Open-CV', 'Speech-Recognition', 'SoundFile', 'Streamlit'],

    "links":[
        {'type':'youtube','url':'https://youtu.be/GdaU0RYDoDw?si=zGzj4kTkSuckBJLu'},
        {'type':'linkedin','url':'https://www.linkedin.com/posts/abdallah-fekry_geminiliveagentchallenge-google-artificialintelligence-ugcPost-7439144965978537984-UbMJ?utm_source=share&utm_medium=member_desktop&rcm=ACoAADix1d8B0P4_8e5-In9xO-53B4KwXOzAKpY'},
        {'type':'github','url':'https://github.com/Abdallah-Fekry/Interactive-Digital-Museum'},
        {'type':'app','url':'https://interactive-digital-museum-614445730433.europe-west1.run.app/'}
            ],
    "achivements":""
}
add_project(p)

# project 2
p = {
    "title":"I Care - Smart Doctor & Comprehensive Medical System",
    "video":'https://youtu.be/_nqm8FuEdLA?si=dfecR4FjO0gU8Im3',
    "images":[r"images/Logo.png"],
    "description":"""As a team leader i have distributed the tasks on the team members, i have decided to work with Agile methodology so i was making a meeting each one or two weeks with the team members to presenting the work done
    i was responsible for the AI modules which are:

    ### My part in the project consists of three main modules:

    * **Module 1:** An AI based smart chatbot called "Caroline" talking to the patient 
    and taking its disease symptoms by text or voice messages, then diagnosing the disease and 
    recommend making some tests or medical imaging scans to do as x-ray, MRI, Complete Blood Count CBC, ... in addition, given 
    information about the predicted disease as an overview, symptoms, and 
    treatments. It can predict 30 diseases such as (Breast Cancer, Influenza, Covid 19, Stroke, ...) 

    * **Module 2:** A sequence of AI Computer Vision models for scanning medical 
    imaging scans and medical tests it can scan (X-ray, MRI, CT, OCT, CBC, or Food images), 
    detect the image type (Image Recognition), if it is medical imaging image, 
    applying anatomical recognition, disease evaluation, disease diagnosis, and also in tumor or bone fraction cases. It can locate the tumor or the fraction using image segmentation. 
    It can predict 25 disease types such as (Bone Fracture, Brain Tumor, Covid 19, Breast Cancer, ...). 
    It can read the Complete Blood Count (CBC) test images and evaluate overall health and diagnose conditions like anemia, infections, clotting disorders, and blood cancers by analyzing red and white blood cells, hemoglobin, hematocrit, and platelets. 
    It also can recognize 101 food types from images and shows the approximate number of calories per gram.

    * **Module 3:** An ensemble Machine Learning (Random Forest) Model for scan Electrocardiography ECG and diagnosis the heart diseases.

    * In addition of making algorithm for MBTI personality analysis test.
    """,

    "tools":['Python', 'Machine Learning', 'Deep Learning', 'Transfere Learning', 'CNN', 'Natural Language Processing NLP', 'Pattern Recognition', 'Flask API',
            'Langchain', 'Large Language Model LLM', 'Gemini API', 'Optical Character Recognition OCR', 'Speech-Recognition', 'Streamlit'],

    "links":[
        {'type':'youtube','url':'https://youtu.be/_nqm8FuEdLA?si=dfecR4FjO0gU8Im3'},
        {'type':'linkedin','url':'https://www.linkedin.com/posts/abdallah-fekry_artificialintelliegence-ai-machinelearning-activity-7197120996053520384-NVmH?utm_source=share&utm_medium=member_desktop'},
        {'type':'github','url':'https://github.com/BeboFekry/I-Care-Smart-Doctor'},
        {'type':'app','url':''},
        {'type':'publication', 'url':'https://app.readytensor.ai/publications/i_care_-_smart_doctor_-_comprehensive_medical_system_sZgWGLbCUMiS'}
            ],
    "achivements":"* 🏆 Publication Achieved Winner of **Best Distinguished Applied Solution Showcase** at the **Computer Vision Projects Expo 2024** by Ready Tensor"
    }
add_project(p)

# project 3
p = {
    "title":"Findora - Smart AI Product Assistant",
    "video":'https://youtu.be/1qybCcar-vE?si=9Bb-BMCFvd_Rrqx9',
    "images":[r"images/Findora_Home_-_Google_Chrome_2026-04-16_03-04-30.jpg",
              r"images/Findora_Home_-_Google_Chrome_2026-04-16_03-04-30(1).jpg",
              r"images/Otcobot_-_Google_Chrome_2026-04-16_03-53-43.jpg",
              r"images/Findora_Home_-_Google_Chrome_2026-04-16_03-04-30(2).jpg",
              r"images/Findora_Home_-_Google_Chrome_2026-04-16_03-04-30(4).jpg",
              r"images/Findora_Home_-_Google_Chrome_2026-04-16_03-04-30(3).jpg"],
    "description":"""
    #### Findora - AI-Powered Product Assistant

    > Smarter Shopping Starts Here.

    Findora is an intelligent AI-powered assistant designed to help users find, compare, and purchase products.
    It combines **AI decision-making**, **structured datasets**, and **real-time web data** to deliver the best product recommendations in seconds.

    #### Overview

    Finding the best product online is frustrating.
    Too many options, inconsistent prices, and time-consuming comparisons.

    **Findora solves this problem by:**

    * Searching internal product databases
    * Using AI to analyze and compare products
    * Selecting the best option based on value
    * Fetching real-time deals from Amazon & eBay

    All in one seamless experience.

    ---

    #### Features

    * **AI Decision Making** (LLM-powered recommendations)
    * **Top 3 Product Comparison**
    * **Best Product Selection**
    * **Real-Time Price Search (Amazon + eBay)**
    * **Voice Input Support**
    * **Interactive Chat UI**
    * **Multiple Categories** (Phones, Laptops, Cars)
    * **User Feedback System**

    ---

    #### Architecture

    ```
    User → Streamlit UI
            ↓
    Chat Interface
            ↓
    AI Agent (LangGraph + Gemini)
            ↓
    ┌───────────────┬───────────────┐
    │ Internal DB   │ External APIs │
    │ (CSV files)   │ (Amazon/eBay) │
    └───────────────┴───────────────┘
            ↓
    Final Recommendation + UI
    ```

    #### How It Works

    1. User enters a query (e.g., "Best phone under $500")
    2. AI agent understands the request
    3. Internal database is searched
    4. Top 3 products are selected
    5. Best product is chosen
    6. Amazon & eBay APIs fetch live deals
    7. Results are displayed with links and UI cards

    ---

    #### Tech Stack

    ##### Core

    * Python
    * Streamlit

    ##### AI & Agents

    * LangChain
    * LangGraph
    * Google Gemini API

    ##### Data Processing

    * Pandas

    ##### APIs

    * SerpAPI (Amazon Search)
    * eBay API

    ##### Speech Processing

    * SpeechRecognition (Voice input)

    ---

    #### Example Queries

    * "Best iPhone under $800"
    * "Laptop for programming with 16GB RAM"
    * "Car under $20,000 with good fuel efficiency"

    ---
    #### Final Note

    Findora is more than just a chatbot…
    It's a **smart decision-making system** designed to make online shopping faster, easier, and more intelligent.
    
    ---
    """,

    "tools":['Python', 'Langchain','Langgraph', 'Large Language Model LLM', 'Gemini API', 'Pandas', 'Speech-Recognition', 'Streamlit', 'SerpAPI', 'EbayAPI', 'Web Screpping'],

    "links":[
        {'type':'youtube','url':'https://youtu.be/1qybCcar-vE?si=9Bb-BMCFvd_Rrqx9'},
        {'type':'linkedin','url':''},
        {'type':'github','url':'https://github.com/Abdallah-Fekry/Findora---Smart-AI-Product-Assistant/tree/main'},
        {'type':'app','url':'https://findora-ai-assistant.streamlit.app/'},
        {'type':'publication', 'url':''}
            ],
    "achivements":""
    }
add_project(p)
# ______________________________________________________________________________________________________________________________
# project 4
p = {
    "title":"Smart Summarizer using Langchain and Web Scrapping",
    "video":'',
    "images":["images/Chat bot-pana.png"],
    "description":"""* Using LLM for Summarize text documents to focus only on the important topics and answer the questions about it. 
    Scrapping and summaryzing text, pdf and text document files, web contents, LinkedIn posts, pdf, and YouTube videos content.
    #### Key Points
    * Scrapping web pages to get web content.
    * Scrapping YouTube videos links to get text subtitles in Arabic or English languages.
    * Scrapping text files (PDF & Text) to get text content.
    * Summarizing the text contents using smart chatbot with message history based on LLM model (Google Gemini) using Langchain, focus on the important notes, and adding Q/A.
    * Chatbot can talking to the users, summarizing text messages, answering questions on the summarized contents, and can help users to use the web page explaining step by step.
    * Designed a user friendly graphical interface using Streamlit.
    """,

    "tools":['Python', 'Large Language Model LLM', 'Langchain', 'Gemini API', 'PDF and Files Scrapping','Web Scrapping','OCR', 'Speech-Recognition', 'Streamlit'],

    "links":[
        {'type':'youtube','url':''},
        {'type':'linkedin','url':''},
        {'type':'github','url':'https://github.com/BeboFekry/Octobot-Smart-Summarizer'},
        {'type':'app','url':'https://octobot.streamlit.app/'}
            ],
    "achivements":""
}
add_project(p)

# project 5
p = {
    "title":"Smart ATS using Langchain and RAG",
    "video":'',
    "images":["images/Chat bot-pana.png"],
    "description":"""* Collected data from several resources as resume pdf documents using pdf plumber file scrappers, resume images using OCR model, text from CSV files using Pandas, then store all data into a Vector Database using Chroma DB.
* Built a retrieval system that retrieved most similar documents to the job description.
* Embedded an LLM model to collect and reformat the retrieved documents and the job description to recommend the best candidate fit the job.
* Designed a user friendly graphical interface using Streamlit with a integrated job description samples to try and testing the app.""",

    "tools":['Python', 'Large Language Model LLM', 'Langchain','Retrieval-Augmented Generation (RAG)', 'Gemini API', 'Chroma DB','Pandas','OCR', 'Streamlit'],

    "links":[
        {'type':'youtube','url':''},
        {'type':'linkedin','url':''},
        {'type':'github','url':'https://github.com/BeboFekry/Smart-ATS-System-using-RAG'},
        {'type':'app','url':''}
            ],
    "achivements":""
}
add_project(p)

# project 6
p = {
    "title":"Food Types Classification & Calories Identification - Task 5 in Machine Learning internship at Prodigy InfoTech",
    "video":'',
    "images":["images/Wallpaper.jpg"],
    "description":"""The Task is Classification the food types, I have use Deep Learning Computer Vision Inception V3 Architecture to classify the food types then identify their approximation number of calories per gram. The model can detect 101 types of food as 'Frensh fries', 'Pizza', 'Sushi', 'Pancakes', 'Chocolate cake', ...""",

    "tools":['Python', 'Deep Learning', 'Transfere Learning', 'CNN', 'Pattern Recognition'],

    "links":[
        {'type':'youtube','url':''},
        {'type':'linkedin','url':''},
        {'type':'github','url':'https://github.com/BeboFekry/Prodigy-Infotech-Internship/blob/main/Prodigy-ML-05_Food101_Classification_Calories_Identification_DL.ipynb'},
        {'type':'app','url':''}
            ],
    "achivements":""
}
add_project(p)


# project 7
p = {
    "title":"Stock Price Prediction - Task 1 in Machine Learning Internship at Code Casa",
    "video":'',
    "images":[r"images/698d3b14c355bd5a24407495ab3703c8f0f2392881442ac30547c9d1.jpg"],
    "description":"""The task is "Stock Price Prediction" i have used Deep Learning LSTM model on Apple stock prices data for the last 6 months from 20/4/2023 to 20/10/2023, and trained the model to take the last 30 days stock prices as input then predict the next price""",

    "tools":['Python', 'Deep Learning', 'Transfere Learning', 'LSTM', 'Time Series Data', 'Regression'],

    "links":[
        {'type':'youtube','url':''},
        {'type':'linkedin','url':'https://www.linkedin.com/posts/abdallah-fekry_codecasa-machinelearning-artificialintelligence-activity-7121041794896699393-U0eU?utm_source=share&utm_medium=member_desktop'},
        {'type':'github','url':'https://github.com/BeboFekry/Code-Casa/blob/main/Stock_Price_Predection_CodeCasa.ipynb'},
        {'type':'app','url':''}
            ],
    "achivements":""
}
add_project(p)

n = 1
for p in projects:
    with st.expander(f":blue[Project {n}]: {p['title']}"):
        st.subheader(p['title'], divider='blue')
        # images
        if len(p['images'])>1 or p['video']:
            test = list(range(1,len(p['images'])+1))
            for i in range(len(test)):
                test[i] = "Image " + str(test[i])
            if p['video']:
                tabs = st.tabs(["Video"] + test)
            else:
                tabs = st.tabs(test)
            del test
            i = 0
            for t in range(len(tabs)):
                if t==0 and p['video']:
                    with tabs[t]:
                        st.columns([1,3,1])[1].video(p['video'])
                        continue
                with tabs[t]:
                    st.columns([1,3,1])[1].image(p['images'][i], caption='project image')
                    i+=1
        else: # onlu one image
            st.columns([1,3,1])[1].image(p['images'][0], caption='project image')
        
        # info
        st.markdown(p['description'], text_alignment='justify')
        if p['achivements']:
            st.warning(p['achivements'])

        # tools
        st.subheader(":material/add_circle: Key tools:")
        tools = add_tools(p['tools'])
        st.markdown(tools)

        # links
        st.subheader(":material/link: Links")
        columns = st.columns(4)
        c = 0
        for i in p['links']:
            if i['type']=='youtube':
                if i['url']:
                    with columns[c]:
                        st.link_button(":primary[:material/link:] Youtube demo video link", i['url'], type='tertiary')
                else:
                    continue
            elif i['type']=='linkedin':
                if i['url']:
                    with columns[c]:
                        st.link_button(":primary[:material/link:] LinkedIn demo video link", i['url'], type='tertiary')
                else:
                    continue
            elif i['type']=='github':
                if i['url']:
                    with columns[c]:
                        st.link_button(":primary[:material/link:] Github repository link", i['url'], type='tertiary')
                else:
                    continue
            elif i['type']=='app':
                if i['url']:
                    with columns[c]:
                        st.link_button(":primary[:material/link:] Try the Project link", i['url'], type='tertiary')
                else:
                    continue
            elif i['type']=='publication':
                if i['url']:
                    with columns[c]:
                        st.link_button(":primary[:material/link:] Publication link", i['url'], type='tertiary')
                else:
                    continue
            c += 1
            c %= 4
    
    n+=1
projects = st.Page("projects.py", title="Projects", icon=':material/share:')
if st.columns([1,1,1])[1].button("Show all projects...", icon=':material/share:', type='tertiary', use_container_width=1):
    st.switch_page(projects)
st.divider()
# ______________________________________________________________________________________________

# Certificates
st.header(":material/license: Certificates", divider='blue')
tabs = st.tabs(["Certificate 1","Certificate 2","Certificate 3","Certificate 4","Certificate 5","Certificate 6","Certificate 7","Certificate 8","Certificate 9","Certificate 10","Certificate 11","Certificate 12","Certificate 13","Certificate 14","Certificate 15","Certificate 16","Certificate 17","Certificate 18","Certificate 19","Certificate 20","Certificate 21","Certificate 22","Certificate 23","Certificate 24","Certificate 25","Certificate 26","Certificate 27","Certificate 28","Certificate 29","Certificate 30","Certificate 31","Certificate 32","Certificate 33","Certificate 34"])
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
certificates.append({"write":"Langchain with RAG Path - AlCamp - during Electro Pi Internship","image":"images/Langchain with RAG Path Electro Pi & Alcamp.png","caption":"AlCamp - Electro Pi"})
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
# certificates.append({"write":"Digital Literacy Training Program - Egyptian Ministry of Youth and Sports","image":"images/Digital Literacy Training Certificate.jpg","caption":""})
certificates.append({"write":"SQL & Data Analysis Training Program - Egyptian Ministry of Youth and Sports","image":"images/SQL & Data Analysis Training Certificate.jpg", "caption":""})
certificates.append({"write":"Introductory Advanced Technologies Training Program - Egyptian Ministry of Youth and Sports","image":"images/Introductory Advanced Technologies Training Certificate.jpg", "caption":""})
for i in range(len(tabs)):
  with tabs[i]:
    with st.columns([1,3,1])[1]:
        st.write(certificates[i]["write"])
        if certificates[i]["image"] != "images/":
            st.image(certificates[i]["image"], caption = certificates[i]["caption"])
certificates_page = st.Page("certificates.py")
st.write("")
# st.write("")
if st.columns([1,3,1])[1].button("Show all certificates...", use_container_width=1, type='tertiary'):
    st.switch_page(certificates_page)
st.divider()
# __________________________________________________________________________________

# Publications
st.header(":material/menu_book: Publications", divider='blue')
text_to_justify = """
#### I Care - Smart Doctor & Comprehensive Medical System
**The project consists of three main modules:**

**Module 1:** An AI based smart chatbot called "Caroline" talking to the patient and taking its disease symptoms by text or voice messages, then diagnosing the disease and recommend making some tests or medical imaging scans to do as x-ray, MRI, Complete Blood Count CBC, ... in addition, given information about the predicted disease as an overview, symptoms, and treatments. 
It can predict 30 diseases such as (Breast Cancer, Influenza, Covid 19, Stroke, ...) 

**Module 2:** A sequence of AI Computer Vision models for scanning medical imaging scans and medical tests it can scan (X-ray, MRI, CT, OCT, CBC, or Food images), detect the image type (Image Recognition), if it is medical imaging image, applying anatomical recognition, disease evaluation, disease diagnosis, and also in tumor or bone fraction cases it can segmentate the tumor or the fraction using image segmentation. 
It can predict 25 disease types such as (Bone Fracture, Brain Tumor, Covid 19, Breast Cancer, ...) 
It can read the Complete Blood Count (CBC) test images and evaluate overall health and diagnose conditions like anemia, infections, clotting disorders, and blood cancers by analyzing red and white blood cells, hemoglobin, hematocrit, and platelets. 
It also can recognize 101 food types from images and shows the approximate number of calories per gram. 

**Module 3:** An ensemble Machine Learning (Random Forest) Model for scan Electrocardiography ECG and diagnosis the heart diseases. 

**Conclusion:** 
The AI module is designed in different parts. There are a Natural Language Processing NLP, Deep Learning Computer Vision Classification Models, Image Segmentation, Optical Character Recognition OCR, Large Language Model LLM, Speech Recognition, and Machine Learning Models all are combined together to mimic a doctor for all specialties."""
st.markdown(f"""<div style='text-align: justify;font-size: 16px;line-height: 1.6;color: #333;'>
        {text_to_justify}</div>""",unsafe_allow_html=True)
st.warning("🏆 Achieved Winner of **Best Distinguished Applied Solution Showcase** in **Computer Vision Projects Expo 2024** Competition by Ready Tensor")
st.columns([1,2,1])[1].image('images/Distinguished Applied Solution Showcase in CV Projects Expo 2024 Competition (Ready Tensor).jpg')
st.write("")
# with st.columns([1,1,1])[1]:
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.link_button("GitHub Repository", "https://github.com/BeboFekry/I-Care-Smart-Doctor", use_container_width=1, icon=':material/link:', type='tertiary')
with col2:
    st.link_button("Publication Link", "https://app.readytensor.ai/publications/i_care_-_smart_doctor_-_comprehensive_medical_system_sZgWGLbCUMiS", use_container_width=1, icon=':material/link:', type='tertiary')
with col3:
    st.link_button("YouTube Demo Video", "https://youtu.be/_nqm8FuEdLA?si=c2eDVRqfAqKxlD__", use_container_width=1, icon=':material/link:', type='tertiary')
with col4:
    st.link_button("LinkedIn Demo Video", "https://www.linkedin.com/posts/abdallah-fekry_artificialintelliegence-ai-machinelearning-activity-7197120996053520384-NVmH?utm_source=share&utm_medium=member_desktop", use_container_width=1, icon=':material/link:', type='tertiary')
st.divider()
# ______________________________________________________________________________________________


st.subheader(":material/language: Languages", divider='blue')
st.write("**Arabic** (native)")
st.write("**English** (very good)")
# ___________________________________________________________________________________

# Footer
st.write("");st.write("");st.write("")
footer = st.container(border=True) 
with footer:
    st.columns([1,1,1])[1].image("images/Picsart_24-07-24_23-25-40-729.png")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("Services")
        st.caption("Data Science")
        st.caption("Machine Learning")
        st.write("Social")
        col11, col22, col33, col44, col55, space = st.columns([1,1,1,1,1.15,6], vertical_alignment='bottom')
        with col11: #https://github.com/BeboFekry/Personal-Website/blob/main/images/gmail.png
            st.markdown("[![G](https://raw.githubusercontent.com/BeboFekry/Personal-Website/main/images/gmail.png)](mailto:abdallahfekry95@gmail.com)")
        with col22:
            st.markdown("[![LI](https://raw.githubusercontent.com/BeboFekry/Personal-Website/main/images/702300.png)](http://www.linkedin.com/in/abdallah-fekry)")
        with col33:
            st.markdown("[![GH](https://raw.githubusercontent.com/BeboFekry/Personal-Website/main/images/25231.png)](https://github.com/BeboFekry?tab=repositories)")
        with col44:
            st.markdown("[![Kg](https://raw.githubusercontent.com/BeboFekry/Personal-Website/main/images/4844503.png)](https://www.kaggle.com/bebofekry)")
        with col55:
            st.markdown("[![ST](https://raw.githubusercontent.com/BeboFekry/ChatHub/main/images/streamlit-mark-color.png)](https://abdalleh-fekry.streamlit.app/)")
    with col2:
        st.write("Contact")
        st.caption(":material/person: Abdallah Fekry")
        st.caption(":material/distance: Cairo, Egypt")
        st.caption(":material/phone: +20 111 9499 384")
        st.caption(":material/email: abdallahfekry95@gmail.com")
    with col3:
        st.write("About")
        st.caption("Data and Applied Scientist")
        st.caption("Artificial Intelligence Engineer")
        st.caption("Natural Language Processing NLP")
        st.caption("Large Language Models (LLM) and Agents")

col1, col2, col3 = st.columns([1,3,1])
with col1:
    st.caption("  \tCopyright protected")
