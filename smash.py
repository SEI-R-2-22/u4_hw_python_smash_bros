import random


class Character:
    def __init__(self, name, attacks):
        self.name = name
        self.health = 100
        self.moves = attacks

    def decrement_health(self, damage):
        self.health = self.health - damage

    def random_attack(self):
        random_move = random.choice(self.moves)
        return random_move


class Battle:
    def __init__(self, character1, character2):
        self.character1 = character1
        self.character2 = character2
