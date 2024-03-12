import pygame
import json

with open('dialogue.json') as f:
    dialogue = json.load(f)

#may be useful soon
class Character():
    def __init__(self, name):
        self.name = name
        dialogue_location = dialogue[self.name]
        answers = []

    def dialogue(self):
        pass