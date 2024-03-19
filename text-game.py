import random
import requests


class Player:

  def __init__(self):
    self.health = 100
    self.coins = 0
    self.inventory = []


class Enemy:

  def __init__(self, name, health, damage):
    self.name = name
    self.health = health
    self.damage = damage


class Location:

  def __init__(self, name, description, exits, items, enemies):
    self.name = name
    self.description = description
    self.exits = exits
    self.items = items
    self.enemies = enemies


def fight(player, enemy):
  while player.health > 0 and enemy.health > 0:
    print("You are fighting a", enemy.name)
    action = input("What do you want to do? (type 'attack' or 'run') ")
    if action == "attack":
      enemy.health -= 10
      print("You attack the", enemy.name, "for 10 damage.")
      if enemy.health > 0:
        player.health -= enemy.damage
        print("The", enemy.name, "attacks you for", enemy.damage, "damage.")
    elif action == "run":
      print("You run away from the", enemy.name)
      break
    else:
      print("Invalid action")
  if player.health > 0:
    print("You have defeated the", enemy.name)
  else:
    print("You have been defeated by the", enemy.name)


def main():
  OPENWEATHER_API_KEY = "YOUR KEY"
  player = Player()
  enemies = [
      Enemy("Goblin", 50, 5),
      Enemy("Ogre", 70, 7),
      Enemy("Dragon", 100, 10)
  ]
  locations = {
      "street":
      Location("Street",
               "You are standing in the middle of a deserted street.",
               ["alleyway", "building"], ["coin"], [enemies[0]]),
      "alleyway":
      Location("Alleyway", "You are in a dark and narrow alleyway.",
               ["street", "sewer"], ["sword"], [enemies[1]]),
      "building":
      Location("Building", "You are in an old abandoned building.",
               ["street", "roof"], ["shield"], [enemies[2]]),
      "sewer":
      Location("Sewer", "You are in a disgusting sewer tunnel.", ["alleyway"],
               ["key"], []),
      "roof":
      Location("Roof", "You are on the roof of the building.", ["building"],
               ["map"], []),
  }
  current_location = locations["street"]
  location_weather_cities = {
      "Street": ("Athens", "GR"),
      "Alleyway": ("London", "UK"),
      "Building": ("Doha", "QA"),
      "Sewer": ("Paris", "FR"),
      "Roof": ("Vienna", "AT")
  }
  current_location = locations["street"]

  while player.health > 0:
    try:
      print("You are currently at the", current_location.name)
      print(current_location.description)
      print("Exits:", current_location.exits)
      print("Items:", current_location.items)

      city, country_code = location_weather_cities[current_location.name]
      base_url = "http://api.openweathermap.org/data/2.5/weather?"
      complete_url = base_url + "appid=" + OPENWEATHER_API_KEY + "&q=" + city + "," + country_code
      response = requests.get(complete_url)

      if response.status_code == 200:
        data = response.json()
        weather_description = data['weather'][0]['description']
        print("The weather is:", weather_description)
      else:
        print("Error: Could not fetch weather data")

      if current_location.enemies:
        enemy = random.choice(current_location.enemies)
        fight(player, enemy)
      action = input("What do you want to do? (type 'exit' to quit) ")

      if action in current_location.exits:
        current_location = locations[action]
      elif action in current_location.items:
        player.inventory.append(action)
        current_location.items.remove(action)
        print("You picked up the", action)
      elif action == "exit":
        break
      else:
        print("Invalid action")
    except KeyError:
      print("That location doesn't exist.")
    except Exception as e:
      print("An error occurred:", str(e))

  if player.health > 0:
    print("Congratulations, you have escaped the city!")
  else:
    print("Game over. You died in the city.")


if __name__ == "__main__":
  main()
