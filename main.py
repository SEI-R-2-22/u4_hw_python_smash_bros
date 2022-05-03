import random
import json
from smash import Character, Battle
from threading import Timer

characters = []

def ask_for_input(user_input):
    while not (int(user_input) >= 0 and int(user_input) <= 58):
        try:
        
            user_input = int(input('Select a player from above: '))
        except ValueError:
            print('Integer only')
    return user_input if user_input != 58 else random.randrange(0, 57)

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
    print("58 Random character")
    print('You have 10 second to choose a character')

    user_input = ask_for_input(user_input)
    
    player = Character(characters[user_input].get("name"), 100, characters[user_input].get("attacks"))

    computer = random_computer()

    battle = Battle(player, computer)

    battle.start_battle()

    restart_game()

main()