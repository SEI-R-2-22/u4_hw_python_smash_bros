import random
import json
characters = []
from smash import Character
from smash import Battle

with open('characters.json') as json_file:
    characters = json.load(json_file)

 ############ I AM SO SORRY! I REALLY STRUGGLE WITH THIS ONE :-( ##########


def game():
   game_character = input("Please select your character")
 
   character_info = [x for x in characters if x['name'] == game_character]
   player_character = Character(game_character, 100, character_info[0]['attacks'])
   if not player_character or character_info is None:
           game_character = random.choice(characters)
   else:
       print("The player has selected: " + player_character ) 


for character in characters:
    comp_index = random.randint(0, len(characters)-1)
computer = Character(characters[comp_index]["name"], 100, characters[comp_index]["attacks"])
print("Computer has selected: " + computer["name"])
   
start = input("Press s to start the battle!")
begin = str(start)
if begin == 's':
    Battle.fight(player_character, computer)
    Character.decrement_health()
    Character.select_attack()

game() 

play_again = input("Would you like to play again y/n?")
play = str(play_again)  
if play == 'y': 
    game()   







