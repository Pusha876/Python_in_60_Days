import requests
import selectorlib
import sqlite3

from datetime import datetime

connection = sqlite3.connect("data3.db")

URL = "https://programmer100.pythonanywhere.com/"
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
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value


def store(extracted):
    now = datetime.now() .strftime("%y-%m-%d-%H-%M-%S")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO events VALUES(?, ?)", (now, extracted))
    connection.commit()


if __name__ == "__main__":
    scraped = scrape(URL)
    if scraped:
        extracted = extract(scraped)
        if extracted:
            store(extracted)
            print(extracted)
