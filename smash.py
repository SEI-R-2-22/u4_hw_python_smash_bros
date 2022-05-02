import random
import json
characters = []

with open('characters.json') as json_file:
    characters = json.load(json_file)
name = characters[1]
damage = characters[0]
print(name)

class Character:
    def __init__(self, name, health, list_moves):
        self.name = name
        self.health = health
        self.list_moves = [list_moves]
    def choose_move(self):
        rand_move = random.choice(self.list_moves)
        print("{name} attacks with {rand_move}".format(name=self.name, rand_move=rand_move))
    def take_damage(self):
        self.health = self.health - 5

class Battle:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

# for character in enumerate(characters[1]):
#     character = Character(character["name"], 100, character["damage"])
#     print(character[i])