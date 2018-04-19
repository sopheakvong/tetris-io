import pygame

# initialize screen
pygame.init()
# create screen
W = 800
H = 600
screen = pygame.display.set_mode((W,H))
pygame.display.set_caption("Tetris")

# Color constants in RGB
WHITE = (255,255,255)
BLACK = (  0,  0,  0)


#################### MAIN LOOP ####################
while True:
    # fetches any user action
    for event in pygame.event.get():
        # if "X" button is clicked on window, exit program
        if event.type == pygame.QUIT:
            pygame.quit()
        # check for key presses
        elif event.type == pygame.KEYDOWN:
            # if escape key is pressed, exit program
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

    # set background
    screen.fill((255, 255, 255))

    # redraw the screen
    pygame.display.flip()
