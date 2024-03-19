import requests
import os

def get_weather(city_name, units="metric"):
    api_key = "YOUR KEY"
    if not api_key:
        print("Error: API Key not found.")
        return

    base_url = "http://api.openweathermap.org/data/2.5/weather"

    response = requests.get(base_url, params={"q": city_name, "appid": api_key, "units": units})

    if response.status_code == 200:
        weather_data = response.json()
        print(f"Weather in {city_name} ({weather_data['sys']['country']}):")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Weather: {weather_data['weather'][0]['description']}")
        print(f"Wind: {weather_data['wind']['speed']} m/s {weather_data['wind']['deg']}°")
    else:
        print(f"Error: Unable to get weather data. Status code: {response.status_code}")

city_name = input("Enter the city name: ")
units = input("Enter the units (metric/imperial): ")
get_weather(city_name, units)
