import random
import json
from smash import Character, Battle
characters = []

with open('characters.json') as json_file:
    characters = json.load(json_file)


def game():
    print("Choose you're character!")
    champion = input()

    person = {}
    computer = {}

    for character in characters:
        if character["name"] == champion or character["name"].lower() == champion:
            person = character

    computer = random.choice(characters)

    player = Character(person["name"], person["attacks"])
    comp = Character(computer["name"], computer["attacks"])

    print("You have chosen " + person["name"] +
          " and you will be fighting " + computer["name"])

    battle = Battle(player, comp)
    battle.fight()


game()
