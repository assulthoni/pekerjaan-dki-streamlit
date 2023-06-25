import streamlit as st
import functions as f
import plotly.graph_objects as go

from millify import millify
from plotly.subplots import make_subplots


st.set_page_config(page_title="Dashboard by Year", page_icon="🚀", layout="wide")

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
        rows=2, cols=3,
        specs=[
            [{"colspan": 2, "rowspan": 1}, None, {"rowspan": 1, "colspan" : 1, "type": "pie"}],
            [{"colspan": 3, "rowspan": 1, "secondary_y": True}, None, None],
        ],
        subplot_titles=(
            "Total People in Each City",
            "Employment Type Distribution",
            "Employment Rate by Year"
        ),
        # shared_xaxes=True,
        # shared_yaxes=True
    )
    data["status_pekerjaan"] = data["jenis_pekerjaan"].apply(lambda x: "Work" if "belum" not in x.lower() else "Unemployment")
    grouped_data = data.groupby(["nama_kabupaten/kota", "status_pekerjaan"])[["jumlah"]].sum().reset_index()
    fig.add_trace(go.Bar(
        x=grouped_data.loc[grouped_data["status_pekerjaan"] == "Work"]["nama_kabupaten/kota"].values,
        y=grouped_data.loc[grouped_data["status_pekerjaan"] == "Work"]["jumlah"].values,
        offsetgroup=0,
        showlegend=False,
        marker_color="#1C4E80",
        name="Work"
    ), row=1, col=1)
    fig.add_trace(go.Bar(
        x=grouped_data.loc[grouped_data["status_pekerjaan"] == "Unemployment"]["nama_kabupaten/kota"].values,
        y=grouped_data.loc[grouped_data["status_pekerjaan"] == "Unemployment"]["jumlah"].values,
        offsetgroup=1,
        name="Unemployment",
        marker_color="#EA6A47",
        showlegend=False
    ), row=1, col=1)
    pie_data = data.groupby(['status_pekerjaan'])[['jumlah']].sum().reset_index().sort_values(by='status_pekerjaan')
    fig.add_trace(
        go.Pie(
            labels=pie_data['status_pekerjaan'],
            values=pie_data['jumlah'],
            showlegend=True,
            marker=dict(colors=['#EA6A47','#1C4E80']),
            name="type"
        ),
        row=1, col=3
    )
    yearly_work_sum = data.groupby(["tahun", "status_pekerjaan"])[['jumlah']].sum().reset_index().pivot(columns="status_pekerjaan", index="tahun", values="jumlah").reset_index()
    yearly_work_sum["Employment_rate"] = yearly_work_sum["Work"] / (yearly_work_sum["Work"] + yearly_work_sum["Unemployment"])
    fig.add_trace(go.Bar(
        x=yearly_work_sum["tahun"].values,
        y=yearly_work_sum["Work"].values,
        offsetgroup=0,
        showlegend=False,
        marker_color="#1C4E80",
        name="Work"
    ), row=2, col=1)
    fig.add_trace(go.Bar(
        x=yearly_work_sum["tahun"].values,
        y=yearly_work_sum["Unemployment"].values,
        offsetgroup=0,
        base=yearly_work_sum["tahun"],
        marker_color="#EA6A47",
        showlegend=False,
        name="Unemployment"
    ), row=2, col=1)
    fig.add_trace(go.Scatter(
        x=yearly_work_sum["tahun"].values,
        y=yearly_work_sum["Employment_rate"].values,
        offsetgroup=1,
        showlegend=False,
        name="Employment Rate",
        mode="lines+markers+text",
        marker_color="#A5D8DD",
        
    ), row=2, col=1, secondary_y=True)
    fig.update_traces(selector=dict(type='scatter'), textposition='top center')
    fig.update_layout(height=900)
    # fig.update_layout(yaxis2=dict(tickvals=[0.1,0.2,0.7], tickformat='.1%', title_text='Secondary y-axis percentage'))
    return fig


build_scorecard(year_choice)
st.plotly_chart(build_plotly_graph(data=f.load_data(year_choice)), use_container_width=True)
