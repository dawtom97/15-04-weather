import requests
from datetime import datetime
from config import Config
from common.functions import kelvin_to_celsius, ms_to_kmh


def get_weather():
    api_key = Config.api_key
    city = Config.api_city
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    try:
        response = requests.get(url)
        data = response.json()

        weather = {
            "temp": kelvin_to_celsius(data.get("main").get("temp")),
            "feels_like": kelvin_to_celsius(data.get("main").get("feels_like")),
            "name": data.get("name"),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "humidity": data.get("main").get("humidity"),
            "pressure": data.get("main").get("pressure"),
            "description": data.get("weather")[0].get("description"),
            "wind_speed": ms_to_kmh(data.get("wind").get("speed")),
        }

        return weather
    except Exception as e:
        print(e)



