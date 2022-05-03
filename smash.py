import random


class Battle:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


class Character:
    def __init__(self, name, health, moves):
        self.name = name
        self.health = health
        self.moves = []

    def decrement_health(self, damage):
        print.random.choice(self.moves)
        self.health -= damage
        # print('{name} lost health'.format(name=self.name))

    def random_move(self):
        return random.choice(self.moves)
