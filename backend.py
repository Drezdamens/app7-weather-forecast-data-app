import requests

API_KEY = "9f7f96d4c03e1d1a230f7a0f79ce3ffe"

def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    nr_values = 8 * forecast_days
    filtered_data = data["list"]
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__ == "__main__":
    print(get_data("Tokyo", forecast_days=3))

