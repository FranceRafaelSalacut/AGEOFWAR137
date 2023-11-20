import pygame
from gameClasses.button import *
from src.CONSTANTS import *
import src.startmenu as START_MENU

pygame.init()

run = True

# Initializing Buttons
# parameters are text, color, pos_x, pos_y, height, width
host = Button("Host", Light_Grey, 50, 50, 100, 50)
client = Button("Client", Light_Grey, 50, 150, 100, 50)


while run:
    current_screen = START_MENU.screen.returnScreen()

    #See Button.py for documentation
    host.draw(current_screen)
    client.draw(current_screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()