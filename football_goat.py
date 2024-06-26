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

def get_valid_rounds():
    while True:
        try:
            rounds = int(input("How many rounds of comparisons (between 2 and 5)? "))
            if 2 <= rounds <= 5:
                return rounds
            else:
                print("Invalid input. Please enter a number between 2 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    players = load_players()
    rounds = get_valid_rounds()

    # Initialize win tracker
    win_tracker = {player['name']: 0 for player in players}

    # Create a copy of the players list for tracking
    remaining_players = players.copy()

    current_player = random.choice(remaining_players)
    remaining_players.remove(current_player)  # Remove from the pool

    for _ in range(rounds):
        opponent = random.choice(remaining_players)
        remaining_players.remove(opponent)  # Remove from the pool

        winner = compare_players(current_player, opponent)
        win_tracker[winner['name']] += 1  # Increment the win count

        current_player = winner

    print(f"\n{current_player['name']} is the GOAT!")

    # Display the win counts
    print("\nWin counts:")
    for player, wins in win_tracker.items():
        print(f"{player}: {wins} wins")

if __name__ == "__main__":
    main()
