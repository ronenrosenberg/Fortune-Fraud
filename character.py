import pygame
import json
import utilities

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
        #Sprite that represents the character
        self.sprite = pygame.image.load(sprite).convert_alpha()
    def render_sprite(self, screen):
        utilities.render_centered_sprite(screen, self.sprite, 0.5, 0.55)
    def render_options(self, screen):
        pass



character_list = []

#generates each character, loading their dialogue/sprite, and adding them the list of characters
for k, v in dialogue["characters"].items():
    character_list.append(Character(k, v["sprite"]))


