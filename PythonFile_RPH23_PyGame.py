import sys
import pygame
import pygame.locals as gameVars

# This sets the size of the gameplay window
game_window = pygame.display.set_mode((400, 500))
pygame.display.set_caption('RPH First Pygame File')
pygame.init()  # This initialises the game and opens the window

# Colours are defined by RGB Values of 0 to 255
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Black = (0, 0, 0)
XPosition = 100
YPosition = 100


GameOver = False
while not GameOver:
    # pygame includes commands that draw on the display window
    # The rectangle params are what to display it on, the colour and a tuple for position and size
    # List or Tuple params are (X coordinate, Y coordinate, width, height)
    pygame.draw.rect(game_window, Black, [0, 0, 400, 500])
    player1 = pygame.draw.circle(game_window, Blue, [YPosition, XPosition], 10)
    # pygame.display.update()  # This is needed to update the display with the image
    pygame.display.flip()

    # This captures if the event has been to quit
    for event in pygame.event.get():
        # print(str(event))  # added temporaraly to display events in the console

        # Movements
        keys = pygame.key.get_pressed()
        if keys[gameVars.K_LEFT]:
            # print('The Left Arrow has been Pressed')
            YPosition = YPosition - 10

        if keys[gameVars.K_RIGHT]:
            # print('The Right Arrow has been Pressed')
            YPosition = YPosition + 10

        if keys[gameVars.K_UP]:
            # print('The Up Arrow has been Pressed')
            XPosition = XPosition - 10

        if keys[gameVars.K_DOWN]:
            # print('The Down Arrow has been Pressed')
            XPosition = XPosition + 10

        # This closes the game when quit
        if event.type == gameVars.QUIT:
            GameOver = True
            print('Game Over')
            pygame.quit()
            sys.exit()

