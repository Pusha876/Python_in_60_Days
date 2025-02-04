import requests
import selectorlib
import smtplib
import ssl
import os
import time
import sqlite3

"INSERT INTO events VALUES ('Tigers', 'Tokyo City', '2025.10.14')"
"SELECT*FROM events WHERE date='2025.10.15'"


URL = "https://programmer100.pythonanywhere.com/tours/"
HEADERS = {
        'User-Agent': (
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/39.0.2171.95 Safari/537.36'
        )
    }

connection = sqlite3.connect("data.db")


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
    row = extracted.split(",")
    row = [item.strip() for item in row]
    cursor = connection.cursor()
    cursor.execute("INSERT INTO events VALUES(?, ?, ?)", row)
    connection.commit()


def read(exrtracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    band, city, date = row
    cursor = connection.cursor()
    cursor.execute(
        "SELECT band, date FROM events WHERE band=? AND city=? AND date=?",
        (band, city, date)
    )
    rows = cursor.fetchall()
    print(rows)
    return rows


if __name__ == "__main__":
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)

        if extracted != "No upcoming tours":
            row = read(extracted)
            if not row:
                store(extracted)
                send_email(message="Hey, there are new tours available!")
            time.sleep(3)
