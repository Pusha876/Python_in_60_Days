import requests
from send_email import send_email

topic = "Apple"
api_key = "3c5a6e842906490dbb3124af1f01f10e"
url = "https://newsapi.org/v2/everything?" \
    f"q={topic}&" \
    "from=2025-01-12&to=2025-01-12&sortBy=popularity&apiKey=" \
    "3c5a6e842906490dbb3124af1f01f10e&language=en"

# Make request to the API
request = requests.get(url, timeout=10)

# Get a dictionary of the JSON response
content = request.json()

# Access the article titles and descriptions
body = ""
for article in content["articles"][0:20]:
    title = article["title"] if article["title"] else "No title"
    description = (
        article["description"] if article["description"] 
        else "No description"
    )
    body = "Subject: Today's news\n"
    for article in content["articles"][0:20]:
        title = article["title"] if article["title"] else "No title"
        description = (
            article["description"] if article["description"]
            else "No description"
        )
        body += f"{title}\n{description}\n{article['url']}\n\n"

send_email(message=body)
