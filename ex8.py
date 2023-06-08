import streamlit as st
from pathlib import Path
from PIL import Image

#  Setting up the path for the root files
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir/ "assets" / "aadesh_resume.pdf"
profile_pic = current_dir/"assets"/ "Aadesh Motghare.jpg"

# General Details of Person
PAGE_TITLE = "Digital CV | Aadesh Motghare"
PAGE_ICON = ":wave:"
NAME = "Aadesh Motghare"
DESCRIPTION = """
Python Developer  
"""
# Email
EMAIL = "motghareaadeshrajkumar@gmail.com"

# Social Handles Stored in Dictionary
SOCIAL_MEDIA = {
    "github" : "github.com/AaadeshMotghare/",
    "linkedin" : "",
    "twitter" : "",
    "leetcode" : ""
}

# Project Stored in Set data structure
PROJECTS = {
    " Image to Sketch Converter : An application Use to Convert a given image into corresponding pencil sketch without any additional input from the user.",
    " Exploratory Data Analysis(EDA) on cereals : Use to visualize the statistical data of cereals in different data visualization graphs using R tools.",
    " Personal Assistant + Chatbot GUI : Use to operate the laptop and pc using voice commands with UI and to perform tasks which the user ask to do.",
    " Histogram Analysis of Image : A C++ Application To analyze the histogram of the particular image by plotting the histogram of original image and histogram of its equalized image"
}

#  Setting the page configuration of the default streamlit page
st.set_page_config(page_title=PAGE_TITLE,page_icon=PAGE_ICON)

# Loading the CSS files
with open(css_file) as FILE_CSS :
    st.markdown("<style>{}</style>".format(FILE_CSS.read()),unsafe_allow_html=True)

# Loading the resume file in binary format
with open(resume_file,"rb") as PDF_FILE :
    PDF_BYTE = PDF_FILE.read()

# Loading the profile picture
PROFILE_PIC = Image.open(profile_pic)

col1, col2 = st.columns(2,gap="small")

with col1:
    st.image(PROFILE_PIC)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="Download Resume",
        data=PDF_BYTE,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )

st.write("Email",EMAIL)

# Social Links
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))

for index, (platform,link) in enumerate(SOCIAL_MEDIA.items()) :
    cols[index].write(f"[{platform}]({link})")

# Skills
st.markdown("---")
st.write("#")
st.subheader("Hard Skills")
st.write("""
    - C/C++ Programming
    - Java Programming
    - Python Programming
    - MySQL
    - Full Stack
 """)

 # Projects and Accomplolishments
st.write("#")
st.subheader("Projects")
st.markdown("---")
for PROJECT in PROJECTS :
    st.write(PROJECT)

# Work History
st.write("#")
st.subheader("Work History")
st.write("---")
st.write("")