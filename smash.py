import random
import json
import time

class Battle:
  def __init__(self, Character1, Character2):
      self.Character1 = Character1
      self.Character2 = Character2

  def start_battle(self):
    random_player_attack = [self.Character1, self.Character2]
    attacking_player = ''
    defending_player = ''
    attack_move = ''

    print(f"***THE BATTLE BTW **{self.Character1.name}** AND **{self.Character2.name}** WILL BEGIN IN ")
    for i in range(1, 4):
      print(4 - i)
      time.sleep(1)
    
    while True:
      time.sleep(1)
      attacking_player = random.choice(random_player_attack)
      defending_player = self.Character1 if attacking_player != self.Character1 else self.Character2
      attack_move = attacking_player.random_attack()

      print(f"{attacking_player.name} attacks with {attack_move.get('name')}, {defending_player.name} took {attack_move.get('damage')} damage.")

      if defending_player == self.Character1:
        self.Character1.decrement_health(attack_move.get('damage'))
        print(f"{self.Character1.name}'s health is {self.Character1.health}")
        if self.Character1.health <= 0:
          print(f"{self.Character2.name} Wins!!!")
          break
      else:
        self.Character2.decrement_health(attack_move.get('damage'))
        print(f"{self.Character2.name}'s health is {self.Character2.health}")
        if self.Character2.health <= 0:
          print(f"{self.Character1.name} Wins!!!")
          break


class Character:
  def __init__(self, name, health, attacks):
      self.name = name
      self.health = health
      self.attacks = attacks

  def decrement_health(self, decrement):
    self.health -= decrement
  
  def random_attack(self):
    return random.choice(self.attacks)