import pandas as pd
import streamlit as st
import plotly.express as px


# Add a title widget
st.title("In Search for Happiness")


# Add two selectbox widgets
option1 = st.selectbox(
    "Select the data for the X-axis",
    ("country", "happiness", "gdp", "corruption"),
    key="option1"
)
option2 = st.selectbox(
    "Select the data for the X-axis",
    ("country", "happiness", "gdp", "corruption"),
    key="option2"
)

# Load the dataframe
df = pd.read_csv("data/happy.csv")

# Match the value of the first option
match option1:
    case "country":
        opt_1 = df["country"]
    case "happiness":
        opt_1 = df["happiness"]
    case "gdp":
        opt_1 = df["gdp"]
    case "corruption":
        opt_1 = df["corruption"]

# Match the value of the second option
match option2:
    case "country":
        opt_2 = df["country"]
    case "happiness":
        opt_2 = df["happiness"]
    case "gdp":
        opt_2 = df["gdp"]
    case "corruption":
        opt_2 = df["corruption"]

# Add a subheader above the plot
st.subheader(f"{option1} and {option2}")

# Create and add the plot th the webpage
figure = px.scatter(x=opt_1, y=opt_2, labels={"x": option1, "y": option2})

st.plotly_chart(figure)
