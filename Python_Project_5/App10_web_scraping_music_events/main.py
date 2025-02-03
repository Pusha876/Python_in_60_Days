import requests
import selectorlib
import smtplib
import ssl
import os


URL = "https://programmer100.pythonanywhere.com/tours/"
HEADERS = {
        'User-Agent': (
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/39.0.2171.95 Safari/537.36'
        )
    }


def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source


def extract(source):
    yaml_file = os.path.join(os.path.dirname(__file__), "extract.yaml")
    if not os.path.exists(yaml_file):
        print(f"Error: The file {yaml_file} does not exist.")
        return None

    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "jlovlov23@gmail.com"
    password = "vnixmtrtdvjyocrb"

    receiver = "jlovlov23@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

    print("Email was sent!")


def store(extracted):
    with open("data.txt", "a") as file:
        file.write(extracted + "\n")


def read(exrtracted):
    with open("data.txt", "r") as file:
        return file.read()


if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    print(extracted)

    content = read(extracted)
    if extracted != "No upcoming tours":
        if extracted not in content:
            store(extracted)
            send_email(message="Hey, there are new tours available!")
