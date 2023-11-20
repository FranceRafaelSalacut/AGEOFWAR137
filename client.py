import pygame
from CONSTANTS import *


# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('TEST') # game/window title
dt = 0 # deltaTime
run = True

while run:
    # polling for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # filling the screen with a color to wipe away everything from the last frame
    screen.fill('white')

    # Render game here
    # vv===========================================vv



    # ^^===========================================^^
    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60) / 1000 # limits FPS to 60

pygame.quit()