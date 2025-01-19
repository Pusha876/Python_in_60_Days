import requests

API_key = "0d2413b4a3a8ed58b40ca80b0c435f89"


def get_data(place, forecast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"
    response = requests.get(url)
    data = response.json()
    num_values = 8 * forecast_days
    filtered_date = data["list"]
    filtered_date = filtered_date[:num_values]
    filtered_data = []
    if kind == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_date]
    if kind == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_date]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3, kind="Temperature"))
