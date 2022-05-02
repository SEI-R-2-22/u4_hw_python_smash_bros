import random


class Character:
    def __init__(self, name, attacks):
        self.name = name
        self.health = 100
        self.attacks = attacks

    def lose_health(self, damage):
        self.health -= damage

    def random_attack(self):
        return random.choice(self.attacks)


class Battle:
    def __init__(self, char_one, char_two):
        self.char_one = char_one
        self.char_two = char_two
