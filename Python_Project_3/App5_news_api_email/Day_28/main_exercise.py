import streamlit as st
import requests

api_key = "EhHsc6xjU7yofHeCEuUIZs7sKQUV3YnCouDSI7Ad"
url = "https://api.nasa.gov/planetary/apod?"f"api_key={api_key}"

response1 = requests.get(url, timeout=10)
data = response1.json()

title = data["title"]
image_url = data["url"]
explanation = data["explanation"]

image_filepath = "image.jpg"
response2 = requests.get(image_url, timeout=10)
with open(image_filepath, 'wb') as file:
    file.write(response2.content)

st.title(title)
st.image(image_filepath)
st.write(explanation)
