import random

class Battle:
  def __init__(self, character1, character2):
    self.character1 = character1
    self.character2 = character2

  def run(self):
    self.character1.take_hit(self.character2.use_random_skill())
    self.character2.take_hit(self.character1.use_random_skill())
    print("\n")


class Character:
  def __init__(self, name, attacks):
    self.name = name
    self.health = 100
    self.attacks = attacks
      
  def take_hit(self, skill):
    self.health -= skill["damage"]
    print(self.name + " took " + str(skill["damage"]) + " damge and has remaining health: " + str(self.health))

  def use_random_skill(self):
    attack = random.choice(self.attacks)
    print(self.name + " uses " + attack["name"])
    return attack