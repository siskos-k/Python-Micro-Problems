import json
import random

def load_legends(file_path):
    with open(file_path) as f:
        return json.load(f)["legends"]

def compare_players(player_a, player_b):
    print(f"Is {player_a['name']} better than {player_b['name']}? (y/n)")
    choice = input("> ")
    if choice.lower() == 'y':
        return player_a
    else:
        return player_b

def play_game(legends):
    current_player = random.choice(legends)
    for _ in range(3):
        next_player = random.choice(legends)
        current_player = compare_players(current_player, next_player)

    print(f"{current_player['name']} is the GOAT!")

if __name__ == "__main__":
    legends = load_legends("football_legends.json")
    play_game(legends)
