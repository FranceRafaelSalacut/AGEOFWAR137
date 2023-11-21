import pygame
from gameClasses.button import *
from src.CONSTANTS import *
from src.startmenu import *

pygame.init()

# screen = Screen(SCREEN_HEIGHT, SCREEN_WIDTH, Baby_Blue)
# surface = screen.returnScreen()

run = True

STATE = START_MENU()

screen_updated = False

while run:

    if not screen_updated:
        current_screen = STATE.screen_to_display()
        screen_updated = True

    for display in STATE.display():
        if display.draw(current_screen):
            print(display.getText())
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
        
pygame.quit()