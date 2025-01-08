import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.title("Best Company")
company_info = """
    “We can’t all have the cheapest prices, but you can surely emphasize other
    aspects of benefit,” Elmardi added.“From engaging industry experts to add
    to your customer service, to [finding] unique goods/offerings, to executing
    loyalty programs, there are countless ways to make your business distinct
    from your competitor.”
"""
st.info(company_info)

st.header("Our Team")

col1, col2, col3 = st.columns([1, 1, 1])

df = pandas.read_csv("data.csv", sep=",")
df["full_name"] = df["first name"] + " " + df["last name"]
with col1:
    for index, row in df[:4].iterrows():
        st.header(row["full_name"])
        st.write(row["role"])
        st.image("images/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.header(row["full_name"])
        st.write(row["role"])
        st.image("images/" + row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.header(row["full_name"])
        st.write(row["role"])
        st.image("images/" + row["image"])
