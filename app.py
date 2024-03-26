import streamlit as st

st.set_page_config(
    page_title="Louisa Shi - Student at University of Washington",
    page_icon="",
    layout="centered",  # centered or wide
    initial_sidebar_state="auto",
)

col1, col2 = st.columns([0.3, 0.7])
with col1:
    st.image('leo.png', caption='Louisa Shi')
with col2:
    st.markdown(
        """
    # Louisa Shi    
    - Pronouns: She/Her
    - University of Washington, Master of Technology in Computer Science Innovation (2023 - 2025)
    - Tsinghua University, Master of Data Science & Information Technology (2022 - 2025)
    - Tsinghua University, Bachelor of Science in Computer Science (2018 - 2022)
    """
    )

st.markdown(
    """
# Work Experience

## APPLE, Cupertino, CA (Jun 2023 - Sep 2023)
### Software Engineer Intern

Vision-aided Spatial Interaction
- Worked within the Location Technologies team to innovate on spatial interactions between Apple devices, contributing
to the development of an app aimed at enhancing user experience through vision-aided technology.
- Leveraged Swift for app development, integrating Core Bluetooth and Multipeer Connectivity frameworks for seamless device communication, and implemented the YOLO real-time object detection model to enrich the interaction pipeline.

## Stanford University, Palo Alto, CA (Jun 2022 - Sep 2022)
### Research Assistant Intern

Adaptive Multimodal Assistants Through Automated State Tracking and User Model-Directed Guidance Planning
- Contributed to a project focused on redefining digital assistant usability with adaptive multimodal interfaces,
emphasizing practicality and user efficiency in the Human Computer Interaction Group
- Developed a Unity plugin using C# and the BepInEx framework for simulation purposes, and designed a Python-based
server and recipe data parser to support the architecture's backend.
- Our user study indicated a 22\% decrease in task completion time and a 40\% reduction in the need for manual
adjustments to communication modalities, showcasing the effectiveness of our adaptive interface.

## Tsinghua University, Beijing, China (Jun 2021 - Jun 2022) 
### Research Assistant Intern

One-Handed Operations on Smartphones through Front-Side Hybrid Interaction
- Collaborated on a project aimed at improving smartphone usability with one-handed operations in the Human
Computer Interaction Lab, introducing innovative interaction designs to enhance accessibility and efficiency.
- Created an Android application in Java to prototype BezelCursor and SwipeMenu, and executed four comprehensive
user studies to validate our designs.
- Demonstrated a 33\% decrease in touch attempt and a 15\% increase in performance for tasks involving hard-to-reach
targets, establishing BezelCursor and SwipeMenu as superior alternatives to traditional front-screen gestures.
"""
)

st.markdown(
    """
# Publication
Xin Yi, Shuning Zhang, Ziqi Pan, Louisa Shi, Fengyan Han, Yan Kong, Hewu Li, and Yuanchun Shi. 2023. Squeez’In: Private Authentication on Smartphones based on Squeezing Gestures. In Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems (CHI '23). https://doi.org/10.1145/3544548.3581419
""")

st.markdown(
    """
# Contact
louisams@uw.edu
""")
col1, col2, col3 = st.columns(3)

