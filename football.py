import random
players_data =[
  {
    "name": "Lionel Messi",
    "position": "Forward",
    "jersey_number": 10,
    "rating": 99
  },
  {
    "name": "Cristiano Ronaldo",
    "position": "Forward",
    "jersey_number": 7,
    "rating": 98
  },
  {
    "name": "Diego Maradona",
    "position": "Forward",
    "jersey_number": 10,
    "rating": 97
  },
  {
    "name": "Pele",
    "position": "Forward",
    "jersey_number": 10,
    "rating": 97
  },
  {
    "name": "Johan Cruyff",
    "position": "Forward",
    "jersey_number": 14,
    "rating": 96
  },
  {
    "name": "Zinedine Zidane",
    "position": "Midfielder",
    "jersey_number": 5,
    "rating": 95
  },
  {
    "name": "Franz Beckenbauer",
    "position": "Defender",
    "jersey_number": 5,
    "rating": 95
  },
  {
    "name": "Paolo Maldini",
    "position": "Defender",
    "jersey_number": 3,
    "rating": 94
  },
  {
    "name": "Bobby Moore",
    "position": "Defender",
    "jersey_number": 6,
    "rating": 94
  },
  {
    "name": "Ronaldinho",
    "position": "Midfielder",
    "jersey_number": 10,
    "rating": 94
  },
  {
    "name": "Michel Platini",
    "position": "Midfielder",
    "jersey_number": 10,
    "rating": 94
  },
  {
    "name": "Lev Yashin",
    "position": "Goalkeeper",
    "jersey_number": 1,
    "rating": 93
  },
  {
    "name": "Alfredo Di Stefano",
    "position": "Forward",
    "jersey_number": 9,
    "rating": 93
  },
  {
    "name": "Ronaldo Nazario",
    "position": "Forward",
    "jersey_number": 9,
    "rating": 93
  },
  {
    "name": "Ferenc Puskas",
    "position": "Forward",
    "jersey_number": 10,
    "rating": 92
  },
  {
    "name": "Marco van Basten",
    "position": "Forward",
    "jersey_number": 9,
    "rating": 92
  },
  {
    "name": "George Best",
    "position": "Forward",
    "jersey_number": 7,
    "rating": 91
  },
  {
    "name": "Eusebio",
    "position": "Forward",
    "jersey_number": 10,
    "rating": 91
  }
]

def display_player_options(position):
    players = [player for player in players_data if player['position'] == position]
    print(f'Choose {position} (Enter the jersey number):')
    for index, player in enumerate(players, start=1):
        print(f'{index}. {player["name"]} (Jersey Number: {player["jersey_number"]})')
def print_team_lineup(team_name, players):
    print(f'{team_name}:')
    for player in players:
        print(f'{player["name"]} ({player["position"]}, Jersey Number: {player["jersey_number"]})')
def select_player(position):
    display_player_options(position)
    choice = int(input('Enter your choice: '))
    players = [player for player in players_data if player['position'] == position]
    return players[choice - 1]

team_a_goalkeeper = select_player('Goalkeeper')
team_a_defender = select_player('Defender')
team_a_forward = select_player('Forward')

team_b_goalkeeper = select_player('Goalkeeper')
team_b_defender = select_player('Defender')
team_b_forward = select_player('Forward')

print_team_lineup('Team A', [team_a_goalkeeper, team_a_defender, team_a_forward])
print_team_lineup('Team B', [team_b_goalkeeper, team_b_defender, team_b_forward])
