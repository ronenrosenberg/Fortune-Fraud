#sloppily coded by Ronen (mostly), Suri, Emma w/use of one pygame wiki function and a lot of hints from chatgpt
#credit for assets: Emma
#credit for script/json file: Suri
#credit for concept/ideas: Emma, Suri
import pygame
import random
import math

#makes it so the current resolution is correctly detected, idk man
import ctypes
ctypes.windll.user32.SetProcessDPIAware()

# pygame setup
pygame.init()
#finds fullscreen resolution
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h
#creates our "display surface" with some useful parameters
flags = pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.HWACCEL
screen = pygame.display.set_mode((screen_width, screen_height), flags)
pygame.display.set_caption("Fortune Fraud")
pygame.display.set_icon(pygame.image.load("assets/icon.png"))

#my libraries
import utilities
import character

#rectangle object that covers the entire screen (for testing purposes)
screen_rect = screen.get_rect()
#defines where the text box should be relative to the size of the screen
text_rect = utilities.centered_rectangle(0.5, 0.95, 0.86, 0.2)

#pygame clock
clock = pygame.time.Clock()

#load image assets
background_image = pygame.image.load("assets/background.PNG") 
curtain_image = pygame.image.load("assets/curtain.PNG") 
crystal_ball_image = pygame.image.load("assets/crystal_ball.PNG") 
border_image = pygame.image.load("assets/border.PNG") 
text_box_image = pygame.image.load("assets/text_box.PNG") 
#using convert_alpha() speeds up the game's performance a fuck ton
background_image_scaled = utilities.scale_to_fullscreen(screen, background_image).convert_alpha()
curtain_image_scaled = utilities.scale_to_fullscreen(screen, curtain_image, 1.05).convert_alpha()
crystal_ball_image_scaled = utilities.scale_to_fullscreen(screen, crystal_ball_image, 1.05).convert_alpha()
border_image_scaled = utilities.scale_to_fullscreen(screen, border_image, 1.05).convert_alpha()
text_box_image_scaled = utilities.scale_to_fullscreen(screen, text_box_image).convert_alpha()



#experimental (bobbing animation stuff)
class BobbingSprite(pygame.sprite.Sprite):
    def __init__(self, image, center_x_percent=0.5, center_y_percent=0.5):
        super().__init__()
        self.image = image.convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.centerx = center_x_percent * screen_width
        self.rect.centery = center_y_percent * screen_height

        self.original_y = self.rect.y
        self.amplitude = 5 + (random.random() * 10) # Amplitude of the bobbing motion in pixels (varies slightly)
        self.speed = 0.0018  #how fast we bob
        self.phase_shift = random.random() #starts at random location
        
        
    def update(self):
        #bobs sprite up and down
        self.rect.y = self.original_y + (self.amplitude * math.sin(pygame.time.get_ticks() * self.speed + self.phase_shift)) #outputs a value from -amplitude to amplitude and adds to original_y

curtain_image_scaled_bob = BobbingSprite(curtain_image_scaled)
crystal_ball_image_scaled_bob = BobbingSprite(crystal_ball_image_scaled)
border_image_scaled_bob = BobbingSprite(border_image_scaled)

foreground_sprite_group = pygame.sprite.Group(curtain_image_scaled_bob, crystal_ball_image_scaled_bob, border_image_scaled_bob)
#text_sprite_group = pygame.sprite.Group(crystal_ball_image_scaled_bob, pygame.sprite.Sprite())

#variables for drawing replies
left_option_rect, right_option_rect = utilities.centered_rectangle(0.12, 0.5, 0.2, 0.2), utilities.centered_rectangle(0.88, 0.5, 0.2, 0.2)
left_option_rect_padded, right_option_rect_padded = utilities.centered_rectangle(0.12, 0.5, 0.22, 0.22), utilities.centered_rectangle(0.88, 0.5, 0.22, 0.22)
unclicked_color, clicked_color = "orange", "yellow"

running = True

#manage current state
state_list = ["initiation" ,"customer_message", "interstitial_message", "end"]
state_index = 0

replies = []

current_character = random.choice(character.character_list)

while running:
    #empty unless there's a mouse click
    mouse_click_xy = None

    #sets the current state
    if state_index == len(state_list) - 1:
        state_index = 1
        character.character_list.remove(current_character)

        if len(character.character_list) != 0:
            current_character = random.choice(character.character_list)
        else:
            state_index = -1
    current_state = state_list[state_index]

    # poll for events
    for event in pygame.event.get():
        #if click X on window, exit
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            #if hit escape, exit
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #left click
            if event.button == 1:
                mouse_click_xy = event.pos
    
    #always has some value
    mouse_xy = pygame.mouse.get_pos()

    #background image
    screen.blit(background_image_scaled, (0,0))
    #renders character
    if current_state == "customer_message":
        screen.blit(current_character.image, current_character.rect)
        current_character.update()
    if current_state == "interstitial_message":
        screen.blit(current_character.image, current_character.rect)
        current_character.update()
        current_character.fade()
    #bobbing foreground
    foreground_sprite_group.draw(screen)
    foreground_sprite_group.update()
    #text box
    screen.blit(text_box_image_scaled, (0,0))

    #displays question/dialogue text
    if current_state == "initiation":
        utilities.text_wrap(screen, "You are a fraudulent fortune teller who is trying to trick your customers into believing in the strength of your mystical powers. Good luck!", "black", text_rect, pygame.font.Font("Vollkorn.ttf", 36))
        if mouse_click_xy != None and text_rect.collidepoint(mouse_click_xy):
            state_index += 1
    
    if current_state == "interstitial_message":
        utilities.text_wrap(screen, "a message that goes in between", "black", text_rect, pygame.font.Font("Vollkorn.ttf", 36))
        if mouse_click_xy != None and text_rect.collidepoint(mouse_click_xy):
            state_index += 1
            
    if current_state == "customer_message":
        current_character.fade(-30)
        utilities.text_wrap(screen, current_character.animal_name + ": " + current_character.dialogue_location["question"], "black", text_rect, pygame.font.Font("Vollkorn.ttf", 36))
        if mouse_click_xy != None and left_option_rect_padded.collidepoint(mouse_click_xy):
            replies.append(current_character.dialogue_location["reply"][0][1:3])
            state_index += 1
        elif mouse_click_xy != None and right_option_rect_padded.collidepoint(mouse_click_xy):
            replies.append(current_character.dialogue_location["reply"][1][1:3])
            state_index += 1

        #text options with highlighting
        left_color, right_color = unclicked_color, unclicked_color
        if left_option_rect.collidepoint(mouse_xy) :
            left_color = clicked_color
        else:
            left_color = unclicked_color
        if right_option_rect.collidepoint(mouse_xy):
            right_color = clicked_color
        else:
            right_color = unclicked_color

        #draws everything
        pygame.draw.rect(screen, left_color, left_option_rect_padded)
        pygame.draw.rect(screen, (0,0,0), left_option_rect_padded, 7)
        pygame.draw.rect(screen, right_color, right_option_rect_padded)
        pygame.draw.rect(screen, (0,0,0), right_option_rect_padded, 7)
        
        #causes lag spike
        utilities.text_wrap(screen, current_character.dialogue_location["reply"][0][0], "white", left_option_rect, pygame.font.Font("Vollkorn.ttf", 36), bkg="black")
        utilities.text_wrap(screen, current_character.dialogue_location["reply"][1][0], "white", right_option_rect, pygame.font.Font("Vollkorn.ttf", 36), bkg="black")
        
    

    #updates display
    pygame.display.flip()
pygame.quit()