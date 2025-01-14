import requests
from pathlib import Path

url = (
    'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/'
    'Nikos_Christodoulides_meets_with_Joseph_Aoun_%28cropped%29.jpg/'
    '180px-Nikos_Christodoulides_meets_with_Joseph_Aoun_%28cropped%29.jpg'
    )

response = requests.get(url)

# Specify the file location
file_location = Path(
    "c:/WORKSPACE/Python_in_60_Days/Python_Project_3/App5_news_api_email/"
    "Day-28/images/image.jpg"
)
# Create directories if they don't exist
file_location.parent.mkdir(parents=True, exist_ok=True)


with open(file_location, "wb") as file:
    file.write(response.content)

print(f"Image downloaded to {file_location}")
