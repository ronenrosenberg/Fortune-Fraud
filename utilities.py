import pygame
#makes it so the current resolution is correctly detected, idk man
import ctypes
ctypes.windll.user32.SetProcessDPIAware()

#sets fullscreen resolution
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

#function from the pygame wiki
def text_wrap(surface, text, color, rect, font, aa=True, bkg=None):
    rect = pygame.Rect(rect)
    y = rect.top
    lineSpacing = -2

    # get the height of the font
    fontHeight = font.size("Tg")[1]

    while text:
        i = 1

        # determine if the row of text will be outside our area
        if y + fontHeight > rect.bottom:
            break

        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1

        # if we've wrapped the text, then adjust the wrap to the last word      
        if i < len(text): 
            i = text.rfind(" ", 0, i) + 1

        # render the line and blit it to the surface
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)

        surface.blit(image, (rect.left, y))
        y += fontHeight + lineSpacing

        # remove the text we just blitted
        text = text[i:]

    return text

def scale_to_fullscreen(screen, image, enlarge=1):
    
    #get screen dimensions
    screen_width, screen_height = screen.get_size()
    
    #calculate scale factors
    scale_factor_width = screen_width / image.get_width()
    scale_factor_height = screen_height / image.get_height()
    #choose the smallest scale factor so we fit entire image
    scale_factor = min(scale_factor_width, scale_factor_height) * enlarge

    # Scale image
    scaled_image_width = int(image.get_width() * scale_factor)
    scaled_image_height = int(image.get_height() * scale_factor)
    scaled_image = pygame.transform.scale(image, (scaled_image_width, scaled_image_height))

    return scaled_image

def centered_rectangle(center_x_pecent, center_y_percent, width_percent, height_percent):
    center_x, center_y = int(screen_width * center_x_pecent), int(screen_height * center_y_percent)
    width, height = int(screen_width * width_percent), int(screen_height * height_percent)
    return pygame.rect.Rect(center_x - (width//2), center_y - (height//2), width, height)

def render_centered_sprite(screen, sprite, center_x_pecent, center_y_percent):
    center_x, center_y = int(screen_width * center_x_pecent), int(screen_height * center_y_percent)
    width, height = sprite.get_width(), sprite.get_height()
    screen.blit(sprite, (center_x - (width//2), center_y - (height//2)))

def center_xy(x_percent, y_percent):
    return (screen_width * x_percent, screen_height * y_percent)
