import tkinter as tk
from tkinter import ttk
import requests
import json
import time
import threading


# Constants
API_KEY = 'YOUR_api_key'
UPDATE_INTERVAL = 5

def get_weather_data(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data['main']['temp'], data['weather'][0]['description']

class WeatherApp(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        self.pack(padx=10, pady=10)

        self.athens_label = ttk.Label(self, text="Athens, Greece: ")
        self.athens_label.pack()
        self.athens_temp_label = ttk.Label(self)
        self.athens_temp_label.pack()
        self.athens_description_label = ttk.Label(self, wraplength=200)
        self.athens_description_label.pack()

        self.doha_label = ttk.Label(self, text="Doha, Qatar: ")
        self.doha_label.pack()
        self.doha_temp_label = ttk.Label(self)
        self.doha_temp_label.pack()
        self.doha_description_label = ttk.Label(self, wraplength=200)
        self.doha_description_label.pack()

        self.update_weather()
        self.update_thread = threading.Thread(target=self.update_weather_repeatedly)
        self.update_thread.start()

    def update_weather(self):
        # Get the current weather for Athens and Doha
        athens_temp, athens_description = get_weather_data("Athens")
        doha_temp, doha_description = get_weather_data("Doha")

        # Update the labels with the new weather data
        self.athens_temp_label.config(text=f"{athens_temp:.1f}°C")
        self.athens_description_label.config(text=athens_description)
        self.doha_temp_label.config(text=f"{doha_temp:.1f}°C")
        self.doha_description_label.config(text=doha_description)

    def update_weather_repeatedly(self):
        while True:
            time.sleep(UPDATE_INTERVAL)
            self.update_weather()

def main():
    root = tk.Tk()
    root.title("Weather App")
    app = WeatherApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
