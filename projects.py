import streamlit as st

st.header("Projects")
st.divider()

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

st.info("1. I Care - Smart Doctor and Comprehensive Medical System (Graduation Project)")
st.write("""As a team leader i have distributed the tasks on the team members, i have decided to work with Agile methodology so i was making a meeting each one or two weeks with the team members to presenting the work done
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
applying anatomical recognition, disease evaluation, disease diagnosis, and also in tumor or bone fraction cases. It can locate the tumor or the fraction using image segmentation. It can predict 25 disease types such as (Bone Fracture, Brain Tumor, Covid 19, Breast Cancer, ...). It can read the Complete Blood Count (CBC) test images and evaluate overall health and diagnose conditions like anemia, infections, clotting disorders, and blood cancers by analyzing red and white blood cells, hemoglobin, hematocrit, and platelets. It also can recognize 101 food types from images and shows the approximate number of calories per gram.

* **Module 3:** An ensemble Machine Learning (Random Forest) Model for scan Electrocardiography ECG and diagnosis the heart diseases.

* In addition of making algorithm for MBTI personality analysis test.

* 🏆 Publication Achieved Winner of **Best Distinguished Applied Solution Showcase** at the **Computer Vision Projects Expo 2024** by Ready Tensor
""")
st.columns([1,8,1])[1].image("images/Logo.png")
st.link_button("GitHub Repository", "https://github.com/BeboFekry/I-Care-Smart-Doctor", use_container_width=1)
st.link_button("Publication Link", "https://app.readytensor.ai/publications/i_care_-_smart_doctor_-_comprehensive_medical_system_sZgWGLbCUMiS", use_container_width=1)
st.link_button("YouTube Demo Video", "https://youtu.be/_nqm8FuEdLA?si=c2eDVRqfAqKxlD__", use_container_width=1)
st.link_button("LinkedIn Demo Video", "https://www.linkedin.com/posts/abdallah-fekry_artificialintelliegence-ai-machinelearning-activity-7197120996053520384-NVmH?utm_source=share&utm_medium=member_desktop", use_container_width=1)
st.divider()

st.info("2. Smart ATS using Langchain and RAG")
st.write("""* Collected data from several resources as resume pdf documents using pdf plumber file scrappers, resume images using OCR model, text from CSV files using Pandas, then store all data into a Vector Database using Chroma DB.
* Built a retrieval system that retrieved most similar documents to the job description.
* Embedded an LLM model to collect and reformat the retrieved documents and the job description to recommend the best candidate fit the job.
* Designed a user friendly graphical interface using Streamlit with a integrated job description samples to try and testing the app.
Key Skills: LangChain · Retrieval-Augmented Generation (RAG) · Pandas (Software) · Python (Programming Language) · Optical Character Recognition (OCR) · ChromaDB · Streamlit""")
st.columns([1,1,1])[1].image("images/Chat bot-pana.png")
st.link_button("GitHub Repository To See Implementation Notebooks and Deployment Codes", "https://github.com/BeboFekry/Smart-ATS-System-using-RAG", use_container_width=1)
# st.link_button("Try Run The Project", "https://chatclub.streamlit.app/", use_container_width=1)
st.divider()

st.info("3. Smart Summarizer using Langchain and Web Scrapping")
st.write("""* Using LLM for Summarize text documents to focus only on the important topics and answer the questions about it. 
Scrapping and summaryzing text, pdf and text document files, web contents, LinkedIn posts, pdf, and YouTube videos content.
#### Key Points
* Scrapping web pages to get web content.
* Scrapping YouTube videos links to get text subtitles in Arabic or English languages.
* Scrapping text files (PDF & Text) to get text content.
* Summarizing the text contents using smart chatbot with message history based on LLM model (Google Gemini) using Langchain, focus on the important notes, and adding Q/A.
* Chatbot can talking to the users, summarizing text messages, answering questions on the summarized contents, and can help users to use the web page explaining step by step.
* Designed a user friendly graphical interface using Streamlit.""")
st.columns([1,1,1])[1].image("images/Chat bot-pana.png")
st.link_button("GitHub Repository To See Implementation Notebooks and Deployment Codes", "https://github.com/BeboFekry/Octobot-Smart-Summarizer", use_container_width=1)
st.link_button("Try Run The Project", "https://octobot.streamlit.app/", use_container_width=1)
st.divider()

st.info("4. ChatHub - Easy Auto Building Chatbots and Connect them with Social Media Accounts (Streamlit Project)")
# st.write("""Explaination""")
st.columns([1,1,1])[1].image("images/Chat bot-pana.png")
st.link_button("GitHub Repository To See Implementation Notebooks and Deployment Codes", "https://github.com/BeboFekry/ChatHub", use_container_width=1)
st.link_button("Try Run The Project", "https://chatclub.streamlit.app/", use_container_width=1)
st.divider()

st.info("5. Housing Price Prediction - Task 1 in Machine Learning internship at Prodigy InfoTech")
st.write("""The task is "Housing Price Prediction" 
I have used Multiple Linear Regression on "California Housing Prices" datasat, and trained the model after scaling the input data to take features about a house as input then predict the median house price.""")
st.columns([1,10,1])[1].image("images/istockphoto-153070435-612x612(1).jpg")
st.link_button("GitHub Repository To See Implementation Notebooks", "https://github.com/BeboFekry/Prodigy-Infotech-Internship/blob/main/Prodigy_ML_01_Housing_Price_Prediction.ipynb", use_container_width=1)
st.link_button("LinkedIn Video", "https://www.linkedin.com/posts/abdallah-fekry_prodigyinfotech-machinelearning-artificialintelliegence-activity-7166173820461027328-Mzgt?utm_source=share&utm_medium=member_desktop", use_container_width=1)
st.divider()

st.info("6. Customers of Retail Store - Task 2 in Machine Learning internship at Prodigy InfoTech")
st.write("""The task is "Customers of Retail Store" 
I have used K-Means clustering algorithm on "Customers Segmentation" datasat, and trained the model to clustering customers based on their purchase history.
""")
st.columns([1,8,1])[1].image("images/types-of-customers(1).png")
st.link_button("GitHub Repository To See Implementation Notebooks", "https://github.com/BeboFekry/Prodigy-Infotech-Internship/blob/main/Prodigy_ML_02_Retail_Store_Customers.ipynb", use_container_width=1)
st.link_button("LinkedIn Video", "https://www.linkedin.com/posts/abdallah-fekry_prodigyinfotech-machinelearning-artificialintelliegence-activity-7166461622331412480-DV98?utm_source=share&utm_medium=member_desktop", use_container_width=1)
st.divider()

st.info("7. Dogs vs Cats Classification using SVM - Task 3 in Machine Learning internship at Prodigy InfoTech")
st.write("""The task is "Dogs vs Cats Classification using SVM" 
I have used Support Vector Machine SVM Classifier algorithm on "dogs vs cats images" datasat, and trained the model to classify the input image is dog or cat.
""")
st.columns([1,8,1])[1].image("images/Introducing-a-cat-or-kitten-to-your-dog.png")
st.link_button("GitHub Repository To See Implementation Notebooks", "https://github.com/BeboFekry/Prodigy-Infotech-Internship/blob/main/Prodigy_ML_03_Dogs_and_Cats_Classification_SVM.ipynb", use_container_width=1)
st.link_button("LinkedIn Video", "https://www.linkedin.com/posts/abdallah-fekry_prodigyinfotech-machinelearning-artificialintelliegence-activity-7166859872779583489-3REC?utm_source=share&utm_medium=member_desktop", use_container_width=1)
st.divider()

st.info("8. Hand Gesture Classification - Task 4 in Machine Learning internship at Prodigy InfoTech")
st.write("""The task is "Hand Gesture Classification" 
I have used Deep Learning - Convolutional Neural Networks CNN Classification algorithm, use transfer learning of VGG16 model architecture and added two more hidden layers then the output layer. And use it on "Hand Gesture Recognition" datasat, and trained the model to classify the input image in which hand gestures class.""")
st.columns([1,8,1])[1].image(r"images/2106.i518.013.F.m005.c7.human hands background set.jpg")
st.link_button("GitHub Repository To See Implementation Notebooks", "https://github.com/BeboFekry/Prodigy-Infotech-Internship/blob/main/Prodigy_ML_04_Hand_Gesture_Classification_DL.ipynb", use_container_width=1)
st.link_button("LinkedIn Video", "https://www.linkedin.com/posts/abdallah-fekry_prodigyinfotech-machinelearning-artificialintelliegence-activity-7167385438230454273-ok0d?utm_source=share&utm_medium=member_desktop", use_container_width=1)
st.divider()

st.info("9. Food Types Classification & Calories Identification - Task 5 in Machine Learning internship at Prodigy InfoTech")
st.write("The Task is Classification the food types, I have use Deep Learning Computer Vision Inception V3 Architecture to classify the food types then identify their approximation number of calories per gram. The model can detect 101 types of food as 'Frensh fries', 'Pizza', 'Sushi', 'Pancakes', 'Chocolate cake', ...")
st.columns([1,8,1])[1].image("images/Wallpaper.jpg")
st.link_button("GitHub Repository To See Implementation Notebooks", "https://github.com/BeboFekry/Prodigy-Infotech-Internship/blob/main/Prodigy-ML-05_Food101_Classification_Calories_Identification_DL.ipynb", use_container_width=1)
# st.link_button("LinkedIn Video", "", use_container_width=1)
st.divider()

st.info("10. Titanic Classification - Task 1 in Data Science internship at Code Alpha")
st.write("""The task is "Titanic Classification", and i need to "Make a system which tells whether the person will be save from sinking. What factors were most likely lead to success-socio-economic status, age, gender and more"

Firstly i have start with data gathering and searching for a suitable dataset, start in read and explore it, i found null values, and some outliers and by using data analysis, visualisation and preprocessing techniques i solve these problems, then starting the modeling process starting with Logistic Regression model and increasing the model complicity till use ensemble learning Random Forest Classifier model architecture which given me the highest test accuracy score by using the Hold-Out cross validation or the train-test-split technique for the evaluation.""")
st.columns([1,8,1])[1].image("images/titanic.jpg")
st.link_button("GitHub Repository To See Implementation Notebooks", "https://github.com/BeboFekry/Code-Alpha---Task1---Titanic-Classification/blob/main/CdeAlpha-task1-titanic-classification.ipynb", use_container_width=1)
st.link_button("LinkedIn Video", "https://www.linkedin.com/posts/abdallah-fekry_codealpha-machinelearning-datascience-activity-7197434207025917952-DcXM?utm_source=share&utm_medium=member_desktop", use_container_width=1)
st.divider()

st.info("11. Stock Price Prediction - Task 1 in Machine Learning Internship at Code Casa")
st.write("""The task is "Stock Price Prediction" i have used Deep Learning LSTM model on AAPL data for the last 6 months from 20/4/2023 to 20/10/2023, and trained the model to take the last 30 days stock prices as input then predict the next price.""")
st.columns([1,5,1])[1].image("images/stock procesjpeg.jpeg")
st.link_button("GitHub Repository To See Implementation Notebooks", "https://github.com/BeboFekry/Code-Casa/blob/main/Stock_Price_Predection_CodeCasa.ipynb", use_container_width=1)
st.link_button("LinkedIn Video", "https://www.linkedin.com/posts/abdallah-fekry_codecasa-machinelearning-artificialintelligence-activity-7121041794896699393-U0eU?utm_source=share&utm_medium=member_desktop", use_container_width=1)
st.divider()

st.info("12. Housing Price Prediction - Task 2 in Machine Learning Internship at Code Casa")
st.write("""The task is "Housing Price Prediction" 
I have used Multiple Linear Regression model on Boston datasat, and trained the model to take features about a house as input then predict the house price.""")
st.columns([1,2,1])[1].image("images/House searching-amico.png")
st.link_button("GitHub Repository To See Implementation Notebooks", "https://github.com/BeboFekry/Code-Casa/blob/main/Housing_Price_Predection_CodeCasa.ipynb", use_container_width=1)
st.link_button("LinkedIn Video", "https://www.linkedin.com/posts/abdallah-fekry_codecasa-machinelearning-artificialintelligence-activity-7121063279963049985-mhQK?utm_source=share&utm_medium=member_desktop", use_container_width=1)
st.divider()

st.info("13. Prediction using Supervised Learning (Linear Regression) - Task 1 in Data Science Internship at The Sparks Foundation")
st.write("""The task is prediction using supervised learning, predict the percentage of an student based on the number of study hours.""")
st.columns([1,4,1])[1].image("images/IMSL What is Regression Model Blog Feature.jpeg")
st.link_button("GitHub Repository To See Implementation Notebooks", "https://github.com/BeboFekry/The-Sparks-Foundation/blob/main/task_1.ipynb", use_container_width=1)
st.link_button("LinkedIn Video", "https://www.linkedin.com/posts/activity-7108926955437109248-5QSd?utm_source=share&utm_medium=member_desktop", use_container_width=1)
st.divider()

st.info("14. Prediction using Unsupervised Learning (KMeans) - Task 2 in Data Science Internship at The Sparks Foundation")
st.write("""The task is prediction using unsupervised learning, 
by using "Iris" dataset, predict the number of clusters and represent it visually.""")
st.columns([1,2,1])[1].image("images/Spring flower-rafiki.png")
st.link_button("GitHub Repository To See Implementation Notebooks", "https://github.com/BeboFekry/The-Sparks-Foundation/blob/main/Task_2.ipynb", use_container_width=1)
st.link_button("LinkedIn Video", "https://www.linkedin.com/posts/abdallah-fekry_gripsept23-gripseptember23-machinelearning-activity-7115295868810870785-JGyR?utm_source=share&utm_medium=member_desktop", use_container_width=1)
st.divider()

st.info("15. Prediction using Decision Tree Algorithm - Task 3 in Data Science Internship at The Sparks Foundation")
st.write("The task is prediction using Decision Tree Algorithm.")
st.columns([1,2,1])[1].image("images/decision_tree.png")
st.link_button("GitHub Repository To See Implementation Notebooks", "https://github.com/BeboFekry/The-Sparks-Foundation/blob/main/task_6.ipynb", use_container_width=1)
st.link_button("LinkedIn Video", "https://www.linkedin.com/posts/abdallah-fekry_gripseptember23-gripsept23-machinelearning-activity-7110266401239515137-eyT7?utm_source=share&utm_medium=member_desktop", use_container_width=1)
st.divider()

st.info("16. ECG Classification with four Algorithms and identify the best practice - Task in NTI AI & IoT Training")
st.write("The task is applying 4 classification algorithms on ECG data and identify the better one from them")
st.columns([1,2,1])[1].image("images/medical.png")
st.link_button("GitHub Repository To See Implementation Notebooks", "https://github.com/BeboFekry/ECG-DataSet-NTI/blob/main/ECG_Task.ipynb", use_container_width=1)
st.link_button("LinkedIn Video", "https://www.linkedin.com/posts/activity-7108931390934573056-VMvc?utm_source=share&utm_medium=member_desktop", use_container_width=1)
st.divider()

st.info("17. NLP Sentiment Analysis - Task in NTI AI & IoT Training")
st.write("Classify humans' text to identify if their feelings is Positive, Negative or Neutral")
st.columns([1,8,1])[1].image("images/Sentiment-analysis-HUB-Final.jpg")
st.link_button("GitHub Repository To See Implementation Notebooks", "https://github.com/BeboFekry/Nationl-Telecommunication-Institute-NTI/blob/main/NLP_Sentiment_task_NTI.ipynb", use_container_width=1)
# st.link_button("LinkedIn Video", "", use_container_width=1)
st.divider()

st.info("18. Stock Price Prediction - Task in NTI AI & IoT Training")
st.write("Predict Stock Price for Apple Data using Deep Learning LSTM Architecture")
st.columns([1,5,1])[1].image("images/stock procesjpeg.jpeg")
st.link_button("GitHub Repository To See Implementation Notebooks", "https://github.com/BeboFekry/Nationl-Telecommunication-Institute-NTI/blob/main/Stock_Price_task_NTI.ipynb", use_container_width=1)
# st.link_button("LinkedIn Video", "", use_container_width=1)
st.divider()

st.info("19. Chest Xray Images Classification - Task in NTI AI & IoT Training")
st.write("Classify chest xray images by Deep Learning Computer Vision CNN Architecture to identify if there is Covid-19, Pneumonia, or Normal Chest X-ray")
st.columns([1,8,1])[1].image("images/download (1).png")
st.link_button("GitHub Repository To See Implementation Notebooks", "https://github.com/BeboFekry/Nationl-Telecommunication-Institute-NTI/blob/main/Task_2_NTI.ipynb", use_container_width=1)
# st.link_button("LinkedIn Video", "", use_container_width=1)
st.divider()

st.info("20. Hand written Numbers Classification - Task in NTI AI & IoT Training")
st.write("Hand written numbers images classification using Deep Learning CNN on Mnist Dataset")
st.columns([1,3,1])[1].image("images/handwritten-numbers-vector-260nw-333225059.jpg")
st.link_button("GitHub Repository To See Implementation Notebooks", "https://github.com/BeboFekry/Nationl-Telecommunication-Institute-NTI/blob/main/Task_NN2.ipynb", use_container_width=1)
# st.link_button("LinkedIn Video", "", use_container_width=1)
st.divider()

st.info("21. Used Cars Complete EDA - Task in Microsoft Learn Student Club Course")
st.write("""**Task**  \n
Deliverables:

Download the data from Kaggle using the given link  \n
Extract the data  \n
Assess the data and write down in the notebook as much as issues found as possible  \n
Clean the data  \n
Based on your findings and insights, write 6 to 12 business questions and answer them in code""")
st.columns([1,5,1])[1].image("images/360_F_576768135_pRj1DS7PMyzQRNCKHdxQq2uY2vWWPcrw.jpg")
st.link_button("GitHub Repository To See Implementation Notebooks", "https://github.com/BeboFekry/Microsoft-Learn-Student-Club/blob/main/MLSC-MidCourse-project-Used-Cars-Complete-EDA.ipynb", use_container_width=1)
# st.link_button("LinkedIn Video", "", use_container_width=1)
st.divider()

st.info("22. Images Gender Classification")
st.write("""Classify Mens and Womans images using Deep Learning - Computer Vision Convolutional Neural Networks CNN Techniques - VGG16 Architecture from data gathering process to deployment process""")
st.columns([1,5,1])[1].image("images/gender.png")
st.link_button("GitHub Repository To See Implementation Notebooks", "https://github.com/BeboFekry/Gender-Images-Classification/blob/main/gender-classification.ipynb", use_container_width=1)
st.link_button("Kaggle Notebook Link", "https://www.kaggle.com/code/bebofekry/gender-classification", use_container_width=1)
st.divider()

st.info("23. Nasa Hazardous Objects Detection ")
# st.write("""explain""")
st.columns([1,5,1])[1].image("images/Nasa-Hazardous-Objects-Detection.jpeg")
st.link_button("GitHub Repository To See Implementation Notebooks", "https://github.com/BeboFekry/Nasa-Hazardous-Objects-Detection/tree/main", use_container_width=1)
# st.link_button("Kaggle Notebook Link", "https://www.kaggle.com/code/bebofekry/gender-classification", use_container_width=1)
st.divider()
