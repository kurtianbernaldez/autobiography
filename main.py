import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="Autobiography & Portfolio",
    page_icon="🎓",
    layout="centered",
)

st.title("Autobiography & Portfolio")
st.image("796.jpg", width=200)  # Replace with your image path
st.markdown("""
### Welcome to my journey as a 4th-year IT student!
I'm currently studying at Cebu Institute of Technology-University, where I have developed strong skills in programming languages and web development. Below is a summary of my journey, skills, and some of my favorite work.
""")

# About Me Section
st.header("About Me")
st.markdown("""
I am an IT student with interest in software development and web technologies. Throughout my academic journey, I have gained knowledge in various programming languages including C, C++, Java, Python, HTML, and JavaScript.

What got me interested in this field is that whenever I look at something in my computer, I always try to figure out how these things work. I find it amusing that so many things can fit in just a very compact device. 

Talking about my personal life, I'm into motorcycles, cars, basketball, and pretty much everything related to that. I am 184cm, so it's pretty much a given that I have to play sports. Filipino parents, ehem...  
""")

# Columns for Education and Career
col1, col2 = st.columns(2)

with col1:
    st.header("Education")
    st.markdown("""
    - **Cebu Institute of Technology-University**: 4th Year IT Student
    - **Relevant Courses**: Software Engineering, Web Development, Data Structures, Algorithms
    """)

with col2:
    st.header("Skills")
    st.markdown("""
    - **Programming Languages**: C, C++, Java, Python
    - **Web Development**: HTML, JavaScript, CSS
    - **Tools & Technologies**: Git, SQL, Linux, VS Code
    """)

# Portfolio Section
st.header("Portfolio")
st.markdown("Here is a selection of my projects:")

# Use tabs to display different portfolio items
tab1, tab2 = st.tabs(["Project 1", "Project 2"])

with tab1:
    st.subheader("Project 1: [Web Development Project]")
    st.image("project1.jpg", width=500)
    st.markdown("A fully responsive website built using HTML, CSS, and JavaScript.")

with tab2:
    st.subheader("Project 2: [NLP Project]")
    st.image("project2.jpg", width=500)
    st.markdown("A streamlit application developed in Python for searching recommendations for recipes.")


st.header("Skills Proficiency")
st.markdown("A visual representation of my proficiency in various skills:")

skills = {
    "C": 70,
    "C++": 85,
    "Java": 85,
    "Python": 70,
    "HTML": 90,
    "JavaScript": 70
}

skills_df = pd.DataFrame(list(skills.items()), columns=["Skill", "Proficiency"])
skills_df = skills_df.set_index("Skill")

st.bar_chart(skills_df)

st.header("My Favorite Song")
st.markdown("""
Listening to music is one of my favorite whenever I'm doing something, whether it be working out, studying, or just starting blankly. I'm into a pretty diverse genre of songs such as pop, k-pop, j-pop, classical, jazz, r&b, k r&b.

This is one of my favorite songs right now. I like the songs vibe, it makes me feel groovy.
""")

st.video("https://www.youtube.com/watch?v=-s7TCuCpB5c")

st.markdown("### Thank you for exploring my autobiography and portfolio!")
