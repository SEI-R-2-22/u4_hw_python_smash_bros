import random
import json
from smash import Character, Battle
from threading import Timer

characters = []

def ask_for_input(user_input):
    while True:
        # try:
        user_input = input('Select a player from above by enter their number: ')
        if user_input == '':
            user_input = random.randrange(0, 57)
            print(f"random character is {characters[user_input].get('name')}")
            return user_input
        elif int(user_input) >= 0 and int(user_input) <= 57:
            return int(user_input)
        else:
            ask_for_input(user_input)


def random_computer():
    random_computer = random.randrange(0, 57)
    computer = Character(characters[random_computer].get("name"), 100, characters[random_computer].get("attacks"))
    return computer

def restart_game():
    while True:
        res = input('Do you want to play again? y/n ')

        if res.upper() == 'Y':
            main()
        elif res.upper() == 'N':
            break

with open('characters.json') as json_file:
    characters = json.load(json_file)

def main():
    player = ''
    computer = ''
    user_input = -1
    
    for char in enumerate(characters):
        print((str(char[0]) + " " + char[1].get('name')))
    print("Press enter for Random character")

    user_input = ask_for_input(user_input)
    
    player = Character(characters[user_input].get("name"), 100, characters[user_input].get("attacks"))

    computer = random_computer()

    battle = Battle(player, computer)

    battle.start_battle()

    restart_game()

main()