import sys
import pygame
import pygame.locals as gameVars

# This sets the size of the gameplay window
game_window = pygame.display.set_mode((400, 500))
pygame.init()  # This initialises the game and opens the window

# Colours are defined by RGB Values of 0 to 255
RPHColour = (255, 0, 0)

while True:
    # pygame includes commands that draw on the display window
    # The rectangle params are what to display it on, the colour and a tuple for position and size
    # Tuple params are (X coordinate, Y coordinate, width, height)
    pygame.draw.rect(game_window, RPHColour, (20, 20, 50, 100))
    pygame.display.update()  # This is needed to update the display with the image

    # This captures if the event has been to quit
    for event in pygame.event.get():
        print(str(event))  # added temporaraly to display events in the console
        if event.type == gameVars.QUIT:
            pygame.quit()
            sys.exit()

