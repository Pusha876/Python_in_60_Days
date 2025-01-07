# Day 23 Student Exercise

## Overview

On Day 23, we built upon yesterday's `main_exercise.py` program. We added additional functionality by creating a home page and a contact page. The contact page includes a web form that allows users to send emails. Additionally, we made the password secure by storing it in an environment variable.

## Features

- **Home Page**: A welcoming page for users.
- **Contact Page**: A page with a web form where users can send emails.
- **Secure Password**: The email password is stored securely in an environment variable.

## Files

- `main_exercise.py`: The main program file.
- `send_email.py`: Contains the function to send emails.
- `pages/home.py`: The home page.
- `pages/contact_us.py`: The contact page with the email form.

## Usage

1. **Set Up Environment Variable**:
   - Store your email password in an environment variable named `EMAIL_PASSWORD`.
   - On Windows, you can set an environment variable using the command:
     ```sh
     setx EMAIL_PASSWORD "your_password"
     ```

2. **Run the Program**:
   - Ensure you have all the necessary dependencies installed.
   - Run the main program:
     ```sh
     python main_exercise.py
     ```

3. **Navigate the Pages**:
   - Use the home page to navigate through the application.
   - Use the contact page to send an email via the web form.

## Example

```python
import streamlit as st
from send_email import send_email

st.header("Contact Us")
st.write("Please fill out the form below to contact us.")

with st.form(key="contact_form"):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message")
    message = (
        f"Subject: New message from {user_email}\n\n"
        f"From: {user_email}\n"
        f"{message}"
    )
    submit_button = st.form_submit_button(label="Submit")
    if submit_button:
        send_email(message)
        st.write("Thank you for your message.")