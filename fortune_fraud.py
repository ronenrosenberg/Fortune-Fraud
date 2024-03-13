#written by Ronen, Suri, Emma
import pygame
import random

#makes it so the current resolution is correctly detected, idk man
import ctypes
ctypes.windll.user32.SetProcessDPIAware()

from useful_functions import textWrap, scale_to_fullscreen
import character


# pygame setup
pygame.init()

#sets fullscreen resolution
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h
print(screen_height, screen_width)

#creates our "display surface" with some useful parameters
flags = pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF
screen = pygame.display.set_mode((screen_width, screen_height), flags)
pygame.display.set_caption("Fortune Fraud")

#rectangle object that covers the entire screen (for testing purposes)
screen_rect = screen.get_rect()
#defines where the text box should be relative to the size of the screen
text_center_x, text_center_y = int(screen_width * 0.5), int(screen_height * 0.95)
text_width, text_height = int(screen_width * 0.8), int(screen_height * 0.2)
text_rect = pygame.rect.Rect(text_center_x - (text_width//2), text_center_y - (text_height//2), text_width, text_height)

#pygame clock
clock = pygame.time.Clock()

#load image assets
background_image = pygame.image.load("assets/background.PNG") 
curtain_image = pygame.image.load("assets/curtain.PNG") 
crystal_ball_image = pygame.image.load("assets/crystal_ball.PNG") 
border_image = pygame.image.load("assets/border.PNG") 
text_box_image = pygame.image.load("assets/text_box.PNG") 

current_character = random.choice(character.character_list)

running = True
while running:
    # poll for events
    for event in pygame.event.get():
        #if click X on window, exit
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            #if hit escape, exit
            if event.key == pygame.K_ESCAPE:
                running = False


    #black background
    screen.fill(pygame.Color(0, 0, 0))

    #renders assets
    scale_to_fullscreen(screen, background_image)
    current_character.render(screen)
    scale_to_fullscreen(screen, curtain_image)
    scale_to_fullscreen(screen, crystal_ball_image)
    scale_to_fullscreen(screen, border_image)
    scale_to_fullscreen(screen, border_image)
    scale_to_fullscreen(screen, text_box_image)

    textWrap(screen, current_character.dialogue_location["question"], "black", text_rect, pygame.font.Font("Vollkorn.ttf", 40))
    
    
   

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()