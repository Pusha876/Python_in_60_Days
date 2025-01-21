import requests

API_key = "0d2413b4a3a8ed58b40ca80b0c435f89"


def get_data(place, forecast_days=None):
    url = (
        f"http://api.openweathermap.org/data/2.5/forecast?q={place}"
        f"&appid={API_key}"
    )
    response = requests.get(url, timeout=10)
    data = response.json()
    filtered_date = data["list"]
    num_values = 8 * forecast_days
    filtered_date = filtered_date[:num_values]
    return filtered_date


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3))
