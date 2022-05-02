import random


class Character:
    def __init__(self, name, attacks, health):
        self.name = name
        self.attacks = attacks
        self.health = health

    def attack(self, enemy):
        enemy.health -= random.choice(self.attacks)["damage"]
        print(self.name + " goes for an attack! They're using " +
              random.choice(self.attacks)["name"])
        print(enemy.name + " took " + str(random.choice(self.attacks)
              ["damage"]) + " points of damage!")


class Battle:
    def __init__(self, char1, char2):
        self.char1 = char1
        self.char2 = char2

    def battle_start(self):
        print("Player 1 is " + self.char1.name,
              "Player 2 is " + self.char2.name)
        while self.char1.health > 0 and self.char2.health > 0:
            self.char1.attack(self.char2)
            self.char2.attack(self.char1)

            if self.char1.health < 0:
                print(self.char2.name + " Wins!")
            elif self.char2.health < 0:
                print(self.char1.name + " Wins!")
