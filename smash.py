import random


class Battle:
    def __init__(self, character1, character2):
        self.character1 = character1
        self.character2 = character2


class Character:
    def __init__(self, name, attacks):
        self.name = name
        self.health = 100
        self.attacks = attacks

    def decrement_health(self, damage):
        self.health -= damage

    def random_attack(self):
        return random.choice(self.attacks)
