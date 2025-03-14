import matplotlib.pyplot as plt
import streamlit as st
from streamlit import multiselect

from penguins import Penguins

def _define_slider(data, col_name, k):
    col_min = int(data[col_name].min()//1)
    col_max = int(data[col_name].max()//1 + 1)
    return st.sidebar.slider(k, col_min, col_max, [col_min, col_max])

if __name__ == "__main__":
    st.set_page_config(layout="wide")
    st.title("Penguin Analysis Dashboard")
    penguins = Penguins()

    st.sidebar.header("Penguin Settings")

    bill_length = _define_slider(penguins.data, "bill_length_mm", "Bill Length [mm]")
    bill_depth = _define_slider(penguins.data, "bill_depth_mm", "Bill Depth [mm]")
    flipper_length = _define_slider(penguins.data, "flipper_length_mm", "Flipper Length [mm]")

    cols = st.columns(2)
    species = cols[0].selectbox("Species", penguins.species)
    spec_data = penguins.data[penguins.data["species"] == species]
    islands = cols[1].pills("Islands", list(spec_data["island"].unique()), selection_mode="multi")

    island_data = spec_data[spec_data["island"].isin(islands)]
    filtered_data = island_data[(bill_length[0] < island_data["bill_length_mm"])]
    filtered_data = filtered_data[(island_data["bill_length_mm"] < bill_length[1])]
    filtered_data = filtered_data[(bill_depth[0] < island_data["bill_depth_mm"])]
    filtered_data = filtered_data[(island_data["bill_depth_mm"] < bill_depth[1])]
    filtered_data = filtered_data[(flipper_length[0] < island_data["flipper_length_mm"])]
    filtered_data = filtered_data[(island_data["flipper_length_mm"] < flipper_length[1])]

    features = ["Gender", "Mass"]
    tabs = st.tabs(features)

    with tabs[0]:
        gender_data = filtered_data.groupby("sex")["id"].count()
        cols = st.columns([1, 3, 5])
        for gender in gender_data.index:
            cols[0].metric(gender, gender_data.loc[gender])

        fig, ax = plt.subplots()
        gender_data.plot(kind="pie", ax=ax)
        cols[1].pyplot(fig)
        year_gender_data = filtered_data.groupby(["sex", "year"])["id"].count().reset_index()
        cols[2].line_chart(year_gender_data, x="year", y="id", color="sex")

    with tabs[1]:
        cols = st.columns(3)
        for i, x_value in enumerate(["bill_length_mm", "bill_depth_mm", "flipper_length_mm"]):
            cols[i].header(x_value)
            for gender in ["male", "female"]:
                cols[i].subheader(gender)
                fig, ax = plt.subplots()
                filtered_data[filtered_data["sex"]==gender].plot.scatter(x=x_value, y="body_mass_g", ax=ax)
                cols[i].pyplot(fig)
