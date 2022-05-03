import random
import json
from smash import Character
from smash import Battle
characters = []

with open('characters.json') as json_file:
    characters = json.load(json_file)

def start_game(character1, character2):
    input('Would yoy like to be character1 or character2?')
    if input == character1: print("Great choice! You will be Mario.")
    else: print("Nice! You will be Luigi!")

def game(character1, character2, self):
    if Character.health == 100:
        print('Ready to fight?!')
    else: print('Play again later')

    if character1 == character1.moves:
        random.choice(self.moves)
        print('You injured your enemy!')
        character2.health - 25 
    else: print('Ouch!')
    character1.health - 25 

    if character1.health == 0:
        print('You lose, try again')
    else: print('Great job! You win!')