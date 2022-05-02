import random
import json
characters = []

with open('characters.json') as json_file:
    characters = json.load(json_file)


class Character:
    def __init__(self, name, health, moves):
        self.name = name
        self.health = health
        self.moves = []

    def new_attack(self, attack):
        self.moves.append(attack)

    def dec_health(self, dec):
        self.health -= dec

    def random_atk(self):
        return (random.choice(self.moves))


# rando = Character('Dan', 10, [])
# rando.new_attack('punch')
# rando.new_attack('kick')
# rando.dec_health(5)
# rando.random_atk()

# class Char1(Character):
#     def __init__(self, name, health, moves):
#         super().init(name, health, moves)


# class Char2(Character):
#     def __init__(self, name, health, moves):
#         super().init(name, health, moves)


class Battle:
    def __init__(self, char1, char2):
        self.char1 = char1
        self.char2 = char2

    def fight(self):
        while self.char1.health > 0 and self.char2.health > 0:
            self.char1.dec_health(self.char2.random_atk()["damage"])
            print(self.char2.name + ' attacks! ' + self.char1.name +
                  ' is now at ' + self.char1.health + ' health.')
            self.char2.dec_health(self.char1.random_atk()["damage"])
            print(self.char1.name + ' attacks! ' + self.char2.name +
                  ' is now at ' + self.char2.health + ' health.')
        print('Winner is ' + self.char1.name if self.char1.health else self.char2.name)
