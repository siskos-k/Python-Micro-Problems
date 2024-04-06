
import json
import random

def load_players():
    with open('football_legends.json') as f:
        data = json.load(f)
        return data['players']

def compare_players(player1, player2):
    print(f"\nIs {player1['name']} a better player than {player2['name']}? (y/n)")
    choice = input("> ").lower()
    return player1 if choice == 'y' else player2

def main():
    players = load_players()

    current_player = random.choice(players)
    for _ in range(2):  # Two rounds of comparison
        opponent = random.choice(players)
        while opponent == current_player:  # Ensure they're not the same player
            opponent = random.choice(players)
        current_player = compare_players(current_player, opponent)

    print(f"\n{current_player['name']} is the GOAT!")

if __name__ == "__main__":
    main()
