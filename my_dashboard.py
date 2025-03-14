import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


if __name__ == "__main__":
    st.set_page_config(layout="wide")
    st.title("My First Dashboard")

    st.divider()
    st.write("Hello **World!**")

    name = st.text_input("What's your name?")

    if name:
        st.write(f"Hello **{name}**")

        age = st.slider("How old are you?", 0, 100)

        is_programmer = st.toggle("Are you a programmer?")

        if is_programmer:
            favourite_language = st.selectbox("What's your favourite language?", ["Python", "Javascipt", "Java", "C++", "Other"])


        if st.button("Let's Party"):
            st.balloons()
            st.toast("Hurray!")


        st.sidebar.write("This ist the **sidebar**!")

    st.divider()

    st.subheader("Data Time!")

    cols = st.columns([2, 3, 2])
    cols[0].write("first column")
    cols[1].write("second column")
    cols[2].write("third column")

    data = pd.DataFrame({"idx": [1, 2, 3, 4, 5], "A": [5, 1, 7, 3, 4], "B": [10, 3, 6, 2, 6]}).set_index("idx")

    cols[0].dataframe(data)

    cols[1].line_chart(data)

    fig, ax = plt.subplots()
    data.plot(kind="bar", ax=ax)
    cols[2].pyplot(fig)

    cols = st.columns([1, 2])

    my_form = cols[0].form("slider")
    slider_a = my_form.slider("A", 0, 50, [0, 50])
    slider_b = my_form.slider("B", 0, 50, [0, 50])
    color = my_form.color_picker("Color")

    if my_form.form_submit_button("Generate Data"):

        more_data = pd.DataFrame({"A": np.random.randint(slider_a[0], slider_a[1], 100),
                                  "B": np.random.randint(slider_b[0], slider_b[1], 100)})

        fig2, ax2 = plt.subplots()
        more_data.plot.scatter("A", "B", ax=ax2, color=color)
        plt.xlim((0, 50))
        plt.ylim((0, 50))
        cols[1].pyplot(fig2)

