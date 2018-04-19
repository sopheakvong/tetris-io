import pygame
import sys
from game import *
from globalvars import *

# initialize screen
pygame.init()
# create screen
screen = pygame.display.set_mode((W,H))
pygame.display.set_caption("Tetris")

# set up game engine
game = Engine(screen, Container())


#################### MAIN LOOP ####################
while True:
    # fetches any user action
    for event in pygame.event.get():
        # if "X" button is clicked on window, exit program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # check for key presses
        elif event.type == pygame.KEYDOWN:
            # if escape key is pressed, exit program
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    # set background
    screen.fill(BLACK)

    # draw game to screen
    game.draw(screen)

    # redraw the screen
    pygame.display.flip()
