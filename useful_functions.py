import pygame

#function from the pygame wiki
def textWrap(surface, text, color, rect, font, aa=True, bkg=None):
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

#this is kind of slow to call each frame but Imma worry about that later
def scale_to_fullscreen(screen, image):
    
    # Get screen dimensions
    screen_width, screen_height = screen.get_size()
    
    # Calculate scale factors
    scale_factor_width = screen_width / image.get_width()
    scale_factor_height = screen_height / image.get_height()
    # Choose the smallest scale factor to ensure the image fits within the screen
    scale_factor = min(scale_factor_width, scale_factor_height)

    # Scale image
    scaled_image_width = int(image.get_width() * scale_factor)
    scaled_image_height = int(image.get_height() * scale_factor)
    scaled_image = pygame.transform.scale(image, (scaled_image_width, scaled_image_height))

    # Blit the scaled image onto the screen
    screen.blit(scaled_image, ((screen_width - scaled_image_width) // 2, (screen_height - scaled_image_height) // 2))
