import requests
import random

# API endpoint for OpenWeatherMap
api_key = ""
base_url = "http://api.openweathermap.org/data/2.5/weather"

# Function to fetch the temperature of a city
def get_temperature(city, units):
    url = f"{base_url}?q={city}&units={units}&appid={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data['main']['temp']
    else:
        print(f"Failed to fetch temperature for {city}.")
        return None

# Function to play the game
def play_game():
    score = 0

    cities = ['London', 'Doha', 'Athens', 'Berlin, Germany', 'Paris, France']
    random.shuffle(cities)

    units = input("Enter 'c' for Celsius or 'f' for Fahrenheit: ")
    if units.lower() == 'c':
        units = 'metric'
    elif units.lower() == 'f':
        units = 'imperial'
    else:
        print("Invalid input. Defaulting to Celsius.")
        units = 'metric'

    for city in cities:
        temperature = get_temperature(city, units)

        if temperature is not None:
            random_number = random.randint(int(temperature) - 10, int(temperature) + 10)
            print(f"The temperature in {city} is higher or lower than: {random_number}")

            user_input = input("Enter 'h' if it is higher or 'l' if it is lower: ")

            if user_input.lower() == 'h' and random_number < temperature:
                score += 1
                print("Correct! Your score is +1.")
            elif user_input.lower() == 'l' and random_number > temperature:
                score += 1
                print("Correct! Your score is +1.")
            else:
                print("Incorrect! You lose.")
                break

    if score == 5:
        print("Game Over! You WIN!")
    else:
        print("Game Over! You LOSE!")

play_game()
