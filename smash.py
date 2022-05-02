import random


class Character:
    def __init__(self, name, health, moves, damage_dealt):
        self.name = name
        self.health = 100
        self.moves = moves
        damage_dealt = 0

    def attack(self):
        random_move = random.choice(self.moves)
        print(self.name + " uses " + random_move["name"])
        self.damage_dealt = random_move["damage"]
        print("It does " + str(self.damage_dealt) + " damage.")

    def take_damage(self, damage):
        self.health = self.health - damage
        print(self.name + "'s health is now " + str(self.health) + "!")


class Battle:
    def __init__(self, character1, character2, winner_declared):
        self.character1 = character1
        self.character2 = character2
        self.winner_declared = False

    def start_battle(self):

        while self.winner_declared == False:
            self.character1.attack()
            self.character2.take_damage(self.character1.damage_dealt)

            if self.character2.health <= 0:
                print(self.character1.name + " is the winner!")
                self.winner_declared = True
                return
            else:
                self.character2.attack()
                self.character1.take_damage(self.character2.damage_dealt)

            if self.character2.health <= 0:
                print(self.character1.name + " is the winner!")
                self.winner_declared = True
                return
