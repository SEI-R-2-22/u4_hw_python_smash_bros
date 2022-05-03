import random

class Battle:
    def __init__(self, char1, char2):
        self.char1 = char1
        self.char2 = char2

class Character:
    def __init__(self, name, attacks):
        self.name = name
        self.health = 100
        self.attacks = attacks
        self.new_attack = []

    def lose_health(self, damage):
        self.health -= damage

    def attack(self):
        self.new_attack = random.choice(self.attacks)
