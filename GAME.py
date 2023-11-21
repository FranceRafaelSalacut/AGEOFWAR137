import pygame
from gameClasses.button import *
from src.CONSTANTS import *
from src.startmenu import *
from src.clientmenu import *
from src.servermenu import *
pygame.init()

run = True

STATE = START_MENU()

screen_updated = False

while run:

    if not screen_updated:
        current_screen = STATE.screen_to_display()
        screen_updated = True

    for display in STATE.display():
        if display.draw(current_screen):
            if display.getText() == "Client":
                STATE = CLIENT_MENU() 

            if display.getText() == "Host":
                STATE = SERVER_MENU()

            if display.getText() == "Back":
                STATE = START_MENU()

            if display.getText() == "Exit":
                run = False

            print(display.getText())
            screen_updated = False
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
        
pygame.quit()