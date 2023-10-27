from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title = "My Portfolio", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#css for contact form
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
local_css("style/style.css")

lottie_coding = load_lottieurl("https://lottie.host/9ce0d5ad-92e8-418c-9624-d3961bc3affb/OSrBmfC7u6.json")
Sales_insight_image = Image.open("image/salesinsight.png")
cricket_data_analysis = Image.open("image/cricket.jpg")
OEE_of_3DPrinter = Image.open("image/3DPrinter.jpg")

with st.container():
    st.subheader("Hi, I am Narendra Kumar B N :wave:")
    st.title("A Data Analyst")
    st.write("I can give a voice to your data, making it speak for itself.")
    st.write("[Resume >](https://drive.google.com/file/d/1Y1BgU7VEDY3xEC5i-wn-VH_wGE_YCsk8/view?usp=drive_link)")



with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header('About Me')
        st.write("##")
        st.write(
            """
            As a final year mechanical engineering student at NIE Mysore, I've embarked on a journey fueled by an unwavering passion for Artificial Intelligence and Machine Learning (AI/ML). 
            This fascination with AI's potential has driven me to dive headfirst into the world of data analysis and machine learning. 
            My quest has been marked by continuous learning, hands-on experimentation, and an unyielding commitment to remain at the forefront of this dynamic field. 
            While I've honed my skills in data analysis, I'm also actively upgrading my knowledge in machine learning, exploring the synergies between the two domains. 
            From studying cutting-edge research to building and refining AI models, I've dedicated myself to pushing the boundaries of what AI and ML can achieve. 
            As I continue on this path, I'm eager to contribute to the transformative power of AI/ML in shaping the future.

            """
        )

with right_column:
    st_lottie(lottie_coding, height=300, key='coding')


#---Projects---
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    
    with image_column:
        st.image(Sales_insight_image,width=500)
    
    with text_column:
            st.subheader("Sales Insights Data Analysis Project")
            st.write(
                """
                In the Sales Insights Data Analysis Project, I've orchestrated a harmonious synergy between SQL queries and Power BI dashboards. 
                SQL served as my analytical backbone, enabling rigorous data validation and cross-referencing to ensure the utmost precision in results. 
                The Power BI dashboards I crafted were not mere data representations; they were gateways to transformative insights. 
                This project is a testament to my skill in data validation, analysis, and visualization, exemplifying my steadfast commitment to decision-making driven by data and analytics. 
                It vividly showcases my ability to bridge the gap between raw data and strategic business decisions, making complex data accessible and actionable
                """
            )
            st.markdown("[Github Link....](link)")

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(cricket_data_analysis,width=500)
    with text_column:
            st.subheader("Cricket Data Analytics Project")
            st.write(
                """
                For my Cricket Data Analytics Project, 
                I combined my Python skills with Power BI to uncover actionable insights. Using Python, 
                I scraped and processed data from Cricbuzz, focusing on the Asia Cup. After rigorous data cleaning, 
                I imported the dataset into Power BI for analysis. The project's core objective was to determine the ideal 11 players for the Indian cricket team in the World Cup. 
                To achieve this, I classified players into categories such as batsmen, bowlers, and all-rounders and handpicked the top 5 players in each category. 
                This project not only demonstrates my technical prowess but also my knack for utilizing data-driven solutions in the world of cricket.
                """
            )
            st.markdown("[Github Link....](https://github.com/Narendra-18/Cricket_Data_analysis_Project)")

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(OEE_of_3DPrinter,width=500)
    with text_column:
            st.subheader("Predicting And Improving OEE of Additive Manufacturing Machine")
            st.write(
                """
                The ongoing project, titled "Improving Overall Equipment Effectiveness (OEE) of Additive Manufacturing Machine," is a focused endeavor aimed at addressing critical challenges within the realm of additive manufacturing. 
                This project recognizes the paramount importance of enhancing the Overall Equipment Effectiveness (OEE) of a specific additive manufacturing machine. Through a systematic, data-driven, and iterative approach, we are committed to achieving substantial OEE gains and ensuring long-term operational excellence. 
                The project's methodology encompasses data collection, root cause analysis, implementation of corrective measures, performance monitoring, before-and-after comparisons, feedback collection, and comprehensive documentation. 
                This project is characterized by its dedication to fine-tuning strategies and consistently monitoring the machine's performance to maintain optimal efficiency and reliability. 
                It is an ongoing initiative, and we remain committed to delivering tangible improvements in additive manufacturing efficiency. Stay tuned for further updates on the project's progress and its ongoing impact in the manufacturing sector.
                """
            )
            st.markdown("[Github Link....](link)")


with st.container():
    st.write("---")
    st.header('Get In Touch With Me!')
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/nkbn1905@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder = "Your Name" required>
     <input type="email" name="email" placeholder = "Your email"" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
    
        
        
