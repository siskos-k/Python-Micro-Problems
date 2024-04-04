import requests
import random

# API endpoint for Athens weather
athens_api_url = "http://api.openweathermap.org/data/2.5/weather?q=Athens,gr&units=metric&appid=YOURAPI"

# API endpoint for Thessaloniki weather
thessaloniki_api_url = "http://api.openweathermap.org/data/2.5/weather?q=Thessaloniki,gr&units=metric&appid=YOURAPI"

# Function to fetch the current temperature for a city
def get_temperature(city_url):
    response = requests.get(city_url)
    if response.status_code == 200:
        data = response.json()
        return data['main']['temp']
    else:
        print(f"Error fetching data for {city_url}")
        return None

# Function to compare the temperatures and determine the winner
def compare_temperatures(athens_temp, thessaloniki_temp):
    if athens_temp > thessaloniki_temp:
        return "Athens is hotter!"
    elif athens_temp < thessaloniki_temp:
        return "Thessaloniki is hotter!"
    else:
        return "It's a tie!"

# Function to play the game
def play_game():
    print("Welcome to the Weather API Game!")

    athens_temp = get_temperature(athens_api_url)
    thessaloniki_temp = get_temperature(thessaloniki_api_url)

    if athens_temp is not None and thessaloniki_temp is not None:
        user_input = input("Which city is hotter? (Athens/Thessaloniki): ")
        while user_input not in ["Athens", "Thessaloniki"]:
            user_input = input("Please enter either 'Athens' or 'Thessaloniki': ")

        winner = compare_temperatures(athens_temp, thessaloniki_temp)
        print(f"The winner is: {winner}")
        print(f"Current temperature in Athens: {athens_temp} degrees Celsius")
        print(f"Current temperature in Thessaloniki: {thessaloniki_temp} degrees Celsius")


        if user_input.lower() == winner.split()[0].lower():
            print("You guessed correctly! You win!")
        else:
            print("You guessed incorrectly. You lose!")
    else:
        print("Error fetching temperature data. Please try again later.")

# Main function to run the game
if __name__ == "__main__":
    play_game()
