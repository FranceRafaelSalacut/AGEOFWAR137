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

    for index, display in enumerate(STATE.display()):
        if display.draw(current_screen):
            action = display.getText()
            if action == "Client":
                STATE = CLIENT_MENU() 

            if action == "Host":
                STATE = SERVER_MENU()

            if action == "Back":
                STATE.stop()
                STATE = START_MENU()

            if action == "Start_Server":
                STATE.start()

            if action == "Stop_Server":
                STATE.stop()

            if action == "Find_Servers":
                STATE.start()

            if action == "Reset":
                STATE.stop()

            if action == "Connect":
                STATE.connect(index)

            if action == "Start_Game":
                print("HERE")
                STATE.getList()

            if action == "Exit":
                run = False

            print(action)
            screen_updated = False
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            try : STATE.stop()
            except:
                print("HEHEHE")
                pass
            run = False

    pygame.display.update()
        
pygame.quit()