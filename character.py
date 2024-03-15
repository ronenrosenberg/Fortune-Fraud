import pygame
import json
import utilities
import random
import math


#loads the dialogue json file
with open('dialogue.json') as f:
    dialogue = json.load(f)

#class that represents each character
#
class Character(pygame.sprite.Sprite):
    def __init__(self, animal_name, image_dir):
        super().__init__()
        #name of the animal
        self.animal_name = animal_name
        #contains the question/answer
        self.dialogue_location = dialogue["characters"][self.animal_name]
        #sprite that represents the character
        self.image = pygame.image.load(image_dir).convert_alpha()
        self.image.set_alpha(0)
        self.rect = self.image.get_rect()
        (self.rect.centerx, self.rect.centery) = utilities.center_xy(0.5, 0.65)

        self.original_y = self.rect.y
        self.amplitude = 15 + (random.random() * 10) # Amplitude of the bobbing motion in pixels (varies slightly)
        self.speed = 0.003  #how fast we bob
        self.phase_shift = random.random() #starts at random location
        

    def update(self):
        #bobs sprite up and down
        self.rect.y = self.original_y + (self.amplitude * math.sin(pygame.time.get_ticks() * self.speed + self.phase_shift))
    
    def fade(self, speed=30):
        alpha = self.image.get_alpha()
        if alpha >= 0 and alpha <= 255:
            new_alpha = alpha - speed
            if new_alpha < 0:
                new_alpha = 0
            elif new_alpha > 255:
                new_alpha = 255
            self.image.set_alpha(new_alpha)
        

class BobbingSprite(pygame.sprite.Sprite):
    def __init__(self, image, center_x_percent=0.5, center_y_percent=0.5):
        super().__init__()
        self.image = image.convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.centerx = center_x_percent * screen_width
        self.rect.centery = center_y_percent * screen_height

        
        
        
    


character_list = []

#generates each character, loading their dialogue/sprite, and adding them the list of characters
for k, v in dialogue["characters"].items():
    character_list.append(Character(k, v["sprite"]))


