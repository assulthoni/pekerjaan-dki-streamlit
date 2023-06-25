import streamlit as st
import functions as f
import plotly.graph_objects as go

from millify import millify
from plotly.subplots import make_subplots


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
    ("All", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021")
)


def build_scorecard(year_choice):
    data = f.load_data(year_choice)
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


def build_plotly_graph(data):
    fig = make_subplots(
        rows=5, cols=3,
        specs=[
            [{"colspan": 2, "rowspan": 3}, {}, None],
            [None, {}, None],
            [None, {}, None],
            [{"colspan" : 3}, None, None],
            [{"colspan" : 3}, None, None]
        ],
        print_grid=True,
        subplot_titles=(
            "Total People in Each City",
            None,
            None,
            None,
            None,
            None
        )
    )
    fig.add_trace(go.Bar(
        x=data.groupby(["nama_kabupaten/kota"])[["jumlah"]].sum().reset_index().sort_values(
                            by="jumlah", ascending=False
                        )["nama_kabupaten/kota"].values,
        y=data.groupby(["nama_kabupaten/kota"])[["jumlah"]].sum().reset_index().sort_values(
                            by="jumlah", ascending=False
                        )["jumlah"].values,
        name="(1,1)"
    ), row=1, col=1)

    return fig


build_scorecard(year_choice)
st.plotly_chart(build_plotly_graph(data=f.load_data(year_choice)))
