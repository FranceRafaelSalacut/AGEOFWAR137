import pygame
from gameClasses.button import *

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('AGE_OF_WAR')

run = True

#Light Grey Color
Light_Grey = (170,170,170)

# Initializing Buttons
# parameters are text, color, pos_x, pos_y, height, width
host = Button("Host", Light_Grey, 50, 50, 100, 50)
client = Button("Client", Light_Grey, 50, 150, 100, 50)


while run:
    screen.fill((202, 228, 241))    

    #See Button.py for documentation
    host.draw(screen)
    client.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()