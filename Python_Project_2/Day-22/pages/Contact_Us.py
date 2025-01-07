import streamlit as st
from send_email_exercise import send_email_exercise
import pandas

df = pandas.read_csv("topics.csv")

st.header("Contact Us")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    option = st.selectbox(
        "What topic do you want to discuss?",
        df["topic"],
        index=None,
        placeholder="Select contact method...",
    )
    st.write("You selected:", option)
    message = st.text_area("Text")
    message = (
        f"Subject: New email from {user_email}\n\n"
        f"From: {user_email}\n"
        f"Topic {option}\n"
        f"{message}"
    )

    button = st.form_submit_button("Submit")
    if button:
        send_email_exercise(message)
        st.info("Your email has been sent successfully.")
