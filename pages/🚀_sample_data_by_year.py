import streamlit as st
import functions as f

st.set_page_config(page_title="Sample Data by Year", page_icon="🚀")

st.markdown("# Sample Data by Year")

st.sidebar.header("Sample Data by Year")

st.write(
    """This page will show a some sample data that can show you the occupation in DKI Jakarta in yearly basis
    You can select specific year to show the visualization.
    Enjoy!"""
)

year_choice = st.sidebar.selectbox(
    "Select Year in This Filter",
    ("2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021")
)


@st.cache_data
def read_sample(year_choice):
    df_sample = f.read_data(year_choice)
    return df_sample.head(10)


st.write(read_sample(year_choice))