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
    # Louisa Shi (She/Her)
                
    - Student at University of Washington, Master of Technology in Computer Science Innovation
    - Bachelor of Science in Computer Science, Tsinghua University, Beijing, China
    """
    )

st.markdown(
    """
# Projects

- [Project 1](https://www.google.com)
- [Project 2](https://www.google.com)
- [Project 3](https://www.google.com)
"""
)

st.markdown(
    """
# Contact
louisams@uw.edu
""")
col1, col2, col3 = st.columns(3)

