import pygame
import json

#loads the dialogue json file
with open('dialogue.json') as f:
    dialogue = json.load(f)

#class that represents each character
#
class Character():
    def __init__(self, animal_name, sprite):
        #name of the animal
        self.animal_name = animal_name
        #contains the question/answer
        self.dialogue_location = dialogue["characters"][self.animal_name]
        #Meyer-Briggs Info (assigned after )
        self.answers = []
        #Sprite that represents the character
        self.sprite = pygame.image.load(sprite)

    def dialogue(self):
        pass

    def render(self, screen):
        screen.blit(self.sprite, (1000, 600))

character_list = []

#generates each character, loading their dialogue, and adding them the list of characters
for k, v in dialogue["characters"].items():
    character_list.append(Character(k, "assets/ghost.png"))

for thing in character_list:
    print(thing.dialogue_location)

