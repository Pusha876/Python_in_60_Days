import streamlit as st
import pandas


st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/profile_pic.jpg", width=400)

with col2:
    st.title("Jamie B. Pryce")
    content = """
    I’m currently on an exciting journey of growth and learning as I dive
    deeper into Python programming and explore new opportunities in technology.
    Outside of coding, I’m passionate about Reggae music, which fuels my
    creativity, and enjoy the strategic challenge of Poker. Recently, I’ve
    taken up shadow boxing as a new hobby, combining focus and fitness, while
    also training for my first half marathon—a goal that reflects my
    determination and drive
    both in and out of the tech world.
    """
    st.info(content)

content2 = """
    Below you can find some of the apps I have built in Python.
    Feel free to contact me!!!
    """
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"], width=400)
        st.write(f"[Source code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"], width=400)
        st.write(f"[Source code]({row['url']})")
