import requests
from datetime import datetime, timedelta
from config import Config
from utils.converter import fahrenheit_to_celsius
from models.weather import WeatherData

class WeatherService:
    def __init__(self):
        self.base_url = Config.BASE_URL
        self.api_key = Config.API_KEY

    def get_weather(self, city, date_from=None, date_to=None):
        date_from = date_from or datetime.now().strftime("%Y-%m-%d")
        date_to = date_to or (datetime.now() + timedelta(1)).strftime("%Y-%m-%d")

        url = f"{self.base_url}{city}/{date_from}/{date_to}?key={self.api_key}"
        try:
            response = requests.get(url)
            response.raise_for_status()
        except Exception as e:
            raise Exception

        days = response.json()["days"]
        avg_temp = 0
        median = 0
        temp_arr = []

        for day in days:
            for hour in day["hours"]:
                temp_arr.append(hour["temp"])

        avg_temp = sum(temp_arr)/len(temp_arr)

        tempmin = min(temp_arr)
        tempmax = max(temp_arr)

        temp_arr.sort()
        if len(temp_arr) % 2 == 1:
            median = temp_arr[len(temp_arr) // 2]
        else:
            median = (temp_arr[len(temp_arr) // 2 - 1] + temp_arr[len(temp_arr) // 2]) / 2

        avg_temp = fahrenheit_to_celsius(avg_temp)
        median = fahrenheit_to_celsius(median)
        tempmin = fahrenheit_to_celsius(tempmin)
        tempmax = fahrenheit_to_celsius(tempmax)

        return WeatherData(avg_temp, median, tempmin, tempmax)
