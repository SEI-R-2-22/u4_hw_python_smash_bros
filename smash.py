import random


class Character:
    def __init__(self, name, health, moves):
        self.name = name
        self.health = health
        self.moves = moves

    def bad_health(self, damage):
        self.health -= damage

    def random_move(self):
        return random.choice(self.moves)


class Battle:
    def __init__(self, character_one, character_two):
        self.character_one = character_one
        self.character_two = character_two

    def fight(self):
        # print(self.character_two.random()["damage"])
        while self.character_one.health > 0 and self.character_two.health > 0:
            self.character_one.bad_health(
                self.character_two.random_move()['damage'])
            # print(self.character_one.health)
            self.character_two.bad_health(
                self.character_one.random_move()['damage'])
            # print(self.character_two.health)

        print("The winner is: ", self.character_one.name if self.character_one.health >
              0 else self.character_two.name)
