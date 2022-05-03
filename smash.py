import random

class Battle:
    def __init__(self, char1, char2):
        self.char1 = char1
        self.char2 = char2
        self.start = True

class Character:
    def __init__(self, name, moves):
        self.name = name
        self.health = 100
        self.moves = moves

    def decrease_health(self, damage):
        self.health -= damage

    def select_move(self):
        return random.choice(self.moves)