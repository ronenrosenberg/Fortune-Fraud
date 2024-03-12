#written by Ronen, Suri, Emma
import pygame
from useful_functions import textWrap

# pygame setup
pygame.init()

#sets fullscreen resolution
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

#creates our "display surface" with some useful parameters
flags = pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF
screen = pygame.display.set_mode((screen_width, screen_height), flags)

#rectangle object that covers the entire screen (for testing purposes)
screen_rect = pygame.rect.Rect(0, 0, screen_width, screen_height)

#pygame clock
clock = pygame.time.Clock()


running = True
while running:
    # poll for events
    for event in pygame.event.get():
        #if click X on window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    #returns if 
    mouse_click_location = pygame.mouse.get_pressed()


    # fill the screen with a color to wipe away anything from last frame
    screen.fill(pygame.Color(32, 80, 255))
    
    test_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer a facilisis velit. Donec placerat et neque et feugiat. Praesent metus nisl, maximus non vulputate in, rutrum sit amet elit. Duis at mauris viverra, euismod justo ut, aliquet ipsum. Phasellus congue nibh eleifend mauris condimentum tempus. Mauris malesuada lobortis dui, in viverra dui ornare quis. Fusce mollis bibendum ultrices. Integer in vestibulum dui. Sed nec rutrum felis. Maecenas dolor enim, efficitur at dui et, finibus porta lacus. Nulla malesuada dui dui, non vehicula purus dictum in."
    textWrap(screen, test_text, "black", screen_rect, pygame.font.Font("Poppins-Regular.ttf", 24))
    


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()