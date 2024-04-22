import json

def search_weapon_by_name(weapons_json, name_to_search):
    name_to_search = name_to_search.lower()
    matched_weapons = []
    for weapon in weapons_json:
        if name_to_search in weapon['name'].lower():
            matched_weapons.append(weapon)
    return matched_weapons

# Load the weapons.json file
with open('weapons.json', 'r') as f:
    weapons_data = json.load(f)

# Get the weapon name to search from the user
weapon_name = input("Enter the name of the weapon you are looking for: ")

# Search for the weapon by name
matched_weapons = search_weapon_by_name(weapons_data, weapon_name)

# If matches are found, display the weapon details
if matched_weapons:
    print(f"Weapons Found:")
    for weapon in matched_weapons:
        print(f"Name: {weapon['name']}")
        print(f"Description: {weapon['description']}")
        print(f"Age: {weapon['age']}")
        print("-" * 30)
else:
    print("No weapons found.")
