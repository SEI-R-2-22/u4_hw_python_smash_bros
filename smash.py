import random


class Character:
    def __init__(self, name, attacks):
        self.name = name
        self.health = 50
        self.attacks = attacks

    def decrement_health(self, damage):
        self.health -= damage

    def random_attack(self):
        return random.choice(self.attacks)

class Battle:
    def __init__(self, character_one, character_two):
        self.character_one = character_one
        self.character_two = character_two