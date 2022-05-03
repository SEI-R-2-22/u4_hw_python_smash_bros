import random

class Character:

    def __init__(self, name, health, moves):
        self.name = name
        self.health = health
        self.moves = moves

    def health_depleted(self, damage):
        self.health -= damage

    def rand_battle_move(self):
        return random.choice(self.moves)


class Battle:
    def __init__(self, player_one, player_two):
        self.player_one = player_one
        self.player_two = player_two

    def fighting(self):
        while self.player_one.health > 0 and self.player_two.health > 0:

            player_attack = self.player_one.rand_battle_move()
            self.player_two.health_depleted(player_attack["damage"])
            print("{} uses the move {} on {} which deals {} damage! {}'s remaining health is {}".format(
                self.player_one.name, player_attack["name"], self.player_two.name,
                 player_attack["damage"], self.player_two.name, self.player_two.health))
            if self.player_two.health <= 0:
                return print("The winner is: {}".format(self.player_one.name))

            cpu_attack = self.player_two.rand_battle_move()
            self.player_one.health_depleted(cpu_attack["damage"])
            print("{} uses the move {} on {} which deals {} damage! {}'s remaining health is {}".format(
                self.player_two.name, cpu_attack["name"], self.player_one.name,
                 player_attack["damage"], self.player_one.name, self.player_one.health))
            if self.player_one.health <= 0:
                return print("The winner is: {}".format(self.player_two.name))