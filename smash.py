import random
import json
characters = []

with open('characters.json') as json_file:
    characters = json.load(json_file)
    #print(characters)
    
class Character:
    def __init__(self, name, health, moves):
        self.name = name
        self.health = health
        self.moves = moves
        
        
        def decremet_health(self):
             self.health = int(self.health - 1)
        
        def select_attack(self):
            index =random.randint(0, len(self.moves))
            return self.moves[index]


class Battle:
    def __init__(self, char1, char2):
        self.char1 = char1
        self.char2 = char2
        
    def fight(self):
        if self.char2.health <= 0:
            print("The winner is: {}".format(self.char1.name))
        elif self.char1.health <= 0:
            print("The winner is: {}".format(self.char2.name))
        else:
            print("It's a draw!")
        
        
     
