import smtplib
import ssl
import os


# This function sends an email to the user
def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "jlovlov23@gmail.com"
    password = os.getenv("PASSWORD")

    receiver = "jlovlov23@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message.encode('utf-8'))
