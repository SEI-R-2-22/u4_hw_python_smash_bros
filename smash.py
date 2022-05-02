import random
import json


class Character:
    def __init__(self, name, health, moves):
        self.name = name
        self.health = health
        self.moves = moves

    def decrement_health(self, damage):
        self.health -= damage

    def random_move(self):
        return random.choice(self.moves)


class Battle:
    def __init__(self, character_one, character_two):
        self.character_one = character_one
        self.character_two = character_two

    def battling(self):
        while self.character_one.health > 0 and self.character_two.health > 0:
            self.character_one.decrement_health(
                self.character_two.random_move()['damage'])
            print(self.character_one.health)
            self.character_two.decrement_health(
                self.character_one.random_move()['damage'])
            print(self.character_two.health)

        print("Winner is " + self.character_one.name if self.character_one.health >
              0 else "Winner is " + self.character_two.name)
