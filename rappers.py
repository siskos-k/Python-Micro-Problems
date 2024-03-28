import random
import json

# Load the JSON data
with open('rappers.json', 'r') as f:
    data = json.load(f)

rappers = data['rappers']

def select_random_rapper():
    return random.choice(rappers)

def compare_rappers(rapper1, rapper2):
    print(f"Who is better: {rapper1['name']} or {rapper2['name']}?")
    choice = input(f"Enter 'A' for {rapper1['name']} or 'B' for {rapper2['name']}: ")
    while choice not in ['A', 'B']:
        print("Invalid choice. Please enter 'A' or 'B'.")
        choice = input(f"Enter 'A' for {rapper1['name']} or 'B' for {rapper2['name']}: ")
    return choice == 'A'

def main():
    selected_rapper = None
    for round_ in range(3):
        rapper1 = select_random_rapper()
        rapper2 = select_random_rapper()

        if selected_rapper is None:
            winner = compare_rappers(rapper1, rapper2)
            selected_rapper = rapper1 if winner else rapper2
        else:
            winner = compare_rappers(selected_rapper, rapper2)
            selected_rapper = selected_rapper if winner else rapper2

    print(f"The winner is {selected_rapper['name']}!")

if __name__ == '__main__':
    main()
