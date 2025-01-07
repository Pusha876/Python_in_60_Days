import streamlit as st


st.header("Contact Us")
st.write("Please fill out the form below to contact us.")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message")
    button = st.form_submit_button("Submit")
    if button:
        print(button)
        print("I was clicked")
