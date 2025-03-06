import streamlit as st

def main():
    # Title
    st.title("My Digital Footprint – Showcasing My Journey")

    # Introduction
    st.header("About Me")
    st.write("Hello! I'm [IGISUBIZO Marie Promesse], a [Your Position/Field of Study] passionate about [Your Interests].")

    # Academic Journey
    st.header("Academic Journey")
    st.write("""
        - **BSc in Computer Science**, [INES Ruhengeli], [2025]
        - **MSc in Data Science**, [INES Ruhengeli], [2025]
    """)

    # Projects
    st.header("Projects")
    st.write("Here are some of my significant projects:")
    st.subheader("Project 1: [artifical intelligent]")
    st.write("""
        - Description: [Brief description of the project]
        - Technologies Used: [Python, Streamlit, etc.]
        - [Link to GitHub Repository](https://github.com/your-repo)
    """)
    
    st.subheader("Project 2: [my detail]")
    st.write("""
        - Description: [Brief description of the project]
        - Technologies Used: [Python, Streamlit, etc.]
        - [Link to GitHub Repository](https://github.com/your-repo)
    """)

    # Skills
    st.header("Skills")
    st.write("""
        - **Technical Skills**: Python, Java, Data Analysis, Machine Learning
        - **Soft Skills**: Communication, Teamwork, Problem Solving,collaboration
    """)

    # Achievements
    st.header("Achievements")
    st.write("""
        - [Award/Recognition 1]
        - [Award/Recognition 2]
    """)

    # Contact Information
    st.header("Contact Me")
    st.write("Feel free to reach out through:")
    st.write("- Email: [igisubizomariep50@gmail.com]")
    st.write("- LinkedIn: [Your LinkedIn Profile Link]")

if __name__ == "__main__":
    main()