import pygame
import os
import json
from mainClasses.button import *
from src.CONSTANTS import *
from src.startmenu import *
from src.clientmenu import *
from src.servermenu import *
pygame.init()

run = True

STATE = START_MENU()
pygame.mixer.music.load(MUSIC_LAUNCHER)
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.5)
sound_effect = pygame.mixer.Sound(SOUND_INTRO)
sound_effect.play(-1)


screen_updated = False

while run:

    if not screen_updated:
        current_screen = STATE.screen_to_display()
        STATE.load_images()
        screen_updated = True
    
    STATE.animate()

    for index, display in enumerate(STATE.display()):
        if display.draw(current_screen):
            action = display.getValue()
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

            if action.startswith("Connect") :
                if STATE.connect(action):
                    print("here i error brycasda")
                    STATE.close()
                    os.system(f"python GAME.py")
                    run = False

            if action == "Start_Game":
                print("HERE")
                print(json.dumps(STATE.getList()))
                message = json.dumps(STATE.getList())
                STATE.stop()
                STATE.close()
                pygame.mixer.music.stop()
                sound_effect.stop()
                os.system(f"python GAME.py '{message}'")
                run = False

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