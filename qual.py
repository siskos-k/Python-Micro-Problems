import requests

def get_weather(city, country):
    api_key = ""
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": f"{city},{country}",
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    weather_data = response.json()
    return weather_data

def display_weather(weather_data):
    print(f"Weather in {weather_data['name']}:")
    print(f"Temperature: {weather_data['main']['temp']}°C")
    print(f"Humidity: {weather_data['main']['humidity']}%")
    print(f"Weather: {weather_data['weather'][0]['description']}")

def main():
    while True:
        print("Welcome to the Weather App!")
        print("Please select a city:")
        print("1. London, GB")
        print("2. Athens, GR")
        print("3. Tokyo, Japan")
        print("4. Doha, Qatar")
        print("5. Toronto, Canada")
        print("6. New York, USA")
        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            city = "London"
            country = "GB"
        elif choice == "2":
            city = "Athens"
            country = "GR"
        elif choice == "3":
            city = "Tokyo"
            country = "Japan"
        elif choice == "4":
            city = "Doha"
            country = "Qatar"
        elif choice == "5":
            city = "Toronto"
            country = "Canada"
        elif choice == "6":
            city = "New York"
            country = "USA"
        else:
            print("Invalid choice. Please try again.")
            continue
        try:
            weather_data = get_weather(city, country)
            display_weather(weather_data)
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            continue
        print("Do you want to continue? (y/n): ")
        response = input().lower()
        if response == "y":
            continue
        elif response == "n":
            break
        else:
            print("Invalid response. Please try again.")
            continue

if __name__ == "__main__":
    main()
