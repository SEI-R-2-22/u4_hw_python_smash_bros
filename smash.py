import random
import random
import json

character_file = open('characters.json')
characters = json.load(character_file)


class Character:
    def __init__(self, name, attacks):
        self.name = name
        self.health = 50
        self.moves = attacks

    def attack(self, enemy):
        attack = random.choice(self.moves)
        enemy.health = enemy.health - attack["damage"]
        print(self.name + " has hit " + enemy.name + " with " + attack["name"])
        print(enemy.name + " health is now " + str(enemy.health))


class Battle:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def runit(self):
        while (self.player.health > 0 and self.computer.health > 0):
            self.player.attack(self.computer)
            self.computer.attack(self.player)
        if self.player.health <= 0:
            print(self.player.name + " is the winner!")
        elif self.computer.health <= 0:
            print(self.computer.name + " has won!")
