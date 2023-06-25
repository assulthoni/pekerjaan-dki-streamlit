import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Data Visualization Project! 👋")

st.sidebar.success("Select a menu above.")

st.markdown(
    """
    # Data Visualization of occupation data in DKI province using Streamlit

    This project uses Streamlit to visualize occupation data in DKI province. Streamlit is a Python library that makes it easy to create interactive web apps. The project uses data from the Badan Pusat Statistik (BPS) to create visualizations of the occupation distribution in DKI province. The visualizations show the top occupations in DKI province, the distribution of occupations by gender, and the distribution of occupations by age group.

    The project is designed to be used by policymakers, researchers, and anyone else who is interested in understanding the occupation distribution in DKI province. The visualizations can be used to identify trends in the occupation distribution, to compare the occupation distribution across different groups, and to explore the relationship between occupation and other factors such as gender and age.

    Here are some of the benefits of using Streamlit to visualize occupation data in DKI province:

    - Streamlit is easy to use. Even if you don't have any experience with Python or web development, you can use Streamlit to create interactive visualizations.
    - Streamlit is interactive. The visualizations created by Streamlit are interactive, which means that users can interact with them to explore the data.
    - Streamlit is portable. Streamlit apps can be run on any device that has a web browser.

    --A.S. Sulthoni--
    """
)