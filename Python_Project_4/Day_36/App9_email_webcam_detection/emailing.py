import smtplib
from email.message import EmailMessage
import mimetypes

PASSWORD = "fhogzohnwwpsicat"
SENDER = "jlovlov23@gmail.com"
RECEIVER = "jlovlov23@gmail.com"


def send_email(image_path):
    print("clean_folder function started")
    email_message = EmailMessage()
    email_message["Subject"] = "New customer detected"
    email_message.set_content("A new customer has been detected in the store")

    try:
        with open(image_path, "rb") as file:
            content = file.read()
        mime_type, _ = mimetypes.guess_type(image_path)
        main_type, sub_type = mime_type.split('/')
        email_message.add_attachment(
            content, maintype=main_type, subtype=sub_type
        )
    except FileNotFoundError:
        print(f"Error: The file {image_path} does not exist.")
        return

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()
    print("send_email function ended")


if __name__ == "__main__":
    send_email(image_path="images/75.png")
