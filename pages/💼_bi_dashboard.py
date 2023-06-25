import streamlit as st
import functions as f
from millify import millify

st.set_page_config(page_title="Dashboard by Year", page_icon="🚀")

st.markdown("# Dashboard by Year")

st.sidebar.header("Dashboard by Year")

st.write(
    """This page will show a some charts that can show you information of occupation in DKI Jakarta in yearly basis
    You can select specific filter to show the visualization.
    Enjoy!"""
)

year_choice = st.sidebar.selectbox(
    "Select Year in This Filter",
    ("2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021")
)


def build_scorecard(year_choice):
    data = f.read_data(year_choice)
    count_occupation, count_kecamatan, count_kelurahan, count_people = st.columns(4)
    count_occupation = count_occupation.metric(
        "Count Distinct Occupation",
        data['jenis_pekerjaan'].nunique()
    )
    count_kecamatan = count_kecamatan.metric("Count Distinct District", data['nama_kecamatan'].nunique())
    count_kelurahan = count_kelurahan.metric(
        "Count Distinct Village",
        data['nama_kelurahan'].nunique()
    )
    count_people = count_people.metric(
        "Sum of People",
        millify(data['jumlah'].sum(), precision=4)
    )
    return count_occupation, count_kecamatan, count_kelurahan, count_people


build_scorecard(year_choice)
