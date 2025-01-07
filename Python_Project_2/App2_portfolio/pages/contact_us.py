import streamlit as st
from send_email import send_email

st.header("Contact Us")
st.write("Please fill out the form below to contact us.")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message")
    message = (
        f"Subject: New message from {user_email}\n\n"
        f"From: {user_email}\n"
        f"{message}"
    )
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email has been sent successfully.")
