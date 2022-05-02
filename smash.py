import random


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
            attack1 = self.character_one.random_move()
            self.character_two.decrement_health(attack1["damage"])
            print("{} is using {}, and damages {} {} health, remaining {} hp".format(
                self.character_one.name, attack1["name"], self.character_two.name, attack1["damage"], self.character_two.health))
            if self.character_two.health <= 0:
                return print("The winner is: {}".format(self.character_one.name))
            attack2 = self.character_two.random_move()
            self.character_one.decrement_health(attack2["damage"])
            print("{} is using {}, and damages {} {} health,  remaining {} hp".format(
                self.character_two.name, attack2["name"], self.character_one.name, attack1["damage"], self.character_one.health))
            if self.character_one.health <= 0:
                return print("The winner is: {}".format(self.character_two.name))
