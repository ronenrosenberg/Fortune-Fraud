#written by Ronen, Suri, Emma
import pygame
import random

#makes it so the current resolution is correctly detected, idk man
import ctypes
ctypes.windll.user32.SetProcessDPIAware()

# pygame setup
pygame.init()

#my libraries
import utilities
import character

#finds fullscreen resolution
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

#creates our "display surface" with some useful parameters
flags = pygame.FULLSCREEN
screen = pygame.display.set_mode((screen_width, screen_height), flags)
pygame.display.set_caption("Fortune Fraud")

#rectangle object that covers the entire screen (for testing purposes)
screen_rect = screen.get_rect()
#defines where the text box should be relative to the size of the screen
text_rect = utilities.centered_rectangle(0.5, 0.95, 0.84, 0.2)

#pygame clock
clock = pygame.time.Clock()

#load image assets
background_image = pygame.image.load("assets/background.PNG") 
curtain_image = pygame.image.load("assets/curtain.PNG") 
crystal_ball_image = pygame.image.load("assets/crystal_ball.PNG") 
border_image = pygame.image.load("assets/border.PNG") 
text_box_image = pygame.image.load("assets/text_box.PNG") 

background_image_scaled = utilities.scale_to_fullscreen(screen, background_image)
curtain_image_scaled = utilities.scale_to_fullscreen(screen, curtain_image)
crystal_ball_image_scaled = utilities.scale_to_fullscreen(screen, crystal_ball_image)
border_image_scaled = utilities.scale_to_fullscreen(screen, border_image)
text_box_image_scaled = utilities.scale_to_fullscreen(screen, text_box_image)

current_character = random.choice(character.character_list)

running = True
new_customer = True
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

    mouse_xy = pygame.mouse.get_pos()

    print(clock.get_fps())
    
    #renders assets
    if new_customer:
        screen.blit(background_image_scaled, (0,0))
        current_character.render_sprite(screen)
        screen.blit(curtain_image_scaled, (0,0))
        screen.blit(crystal_ball_image_scaled, (0,0))
        screen.blit(border_image_scaled, (0,0))
        screen.blit(text_box_image_scaled, (0,0))    
    
    #displays question/dialogue text
    utilities.text_wrap(screen, current_character.dialogue_location["question"], "black", text_rect, pygame.font.Font("Vollkorn.ttf", 36))
    
    #render text options (left and right)

    #highlights options
    left_option_rect, right_option_rect = utilities.centered_rectangle(0.12, 0.5, 0.2, 0.2), utilities.centered_rectangle(0.88, 0.5, 0.2, 0.2)
    unclicked_color, clicked_color = "orange", "yellow"
    left_color, right_color = unclicked_color, unclicked_color
    if left_option_rect.collidepoint(mouse_xy):
        left_color = clicked_color
    else:
        left_color = unclicked_color
    if right_option_rect.collidepoint(mouse_xy):
        right_color = clicked_color
    else:
        right_color = unclicked_color

    #draws everything
    pygame.draw.rect(screen, left_color, left_option_rect)
    pygame.draw.rect(screen, (0,0,0), left_option_rect, 7)
    pygame.draw.rect(screen, right_color, right_option_rect)
    pygame.draw.rect(screen, (0,0,0), right_option_rect, 7)

    utilities.text_wrap(screen, current_character.dialogue_location["reply"][0][0], "white", left_option_rect, pygame.font.Font("Vollkorn.ttf", 36), bkg="black")
    utilities.text_wrap(screen, current_character.dialogue_location["reply"][1][0], "white", right_option_rect, pygame.font.Font("Vollkorn.ttf", 36), bkg="black")
    """
    """
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(165)  # limits FPS to 60
    new_customer = False
pygame.quit()