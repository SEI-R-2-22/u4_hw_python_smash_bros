import random
import json

file = open('characters.json')
characters = json.load(file)


class Character:
    def __init__(self, name, attacks):
        self.name = name
        self.health = 100
        self.attacks = attacks

    def attack(self, enemy):
        move = random.choice(self.attacks)
        enemy.health = enemy.health - move["damage"]
        print(self.name + " has hit " +
              enemy.name + " with " + move["name"])
        print(enemy.name + " health is now " + str(enemy.health))


class Battle:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def fight(self):
        while (self.player.health > 0 and self.computer.health > 0):
            self.player.attack(self.computer)
            self.computer.attack(self.player)
        if self.player.health <= 0:
            print(self.player.name + " wins!")
        elif self.computer.health <= 0:
            print(self.computer.name + " wins!")
