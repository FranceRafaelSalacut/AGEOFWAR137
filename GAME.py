import pygame
from mainClasses.button import *
from src.CONSTANTS import *
pygame.init()

run = True


screen_updated = False

while run:

    if not screen_updated:
        current_screen = STATE.screen_to_display()
        screen_updated = True

    for index, display in enumerate(STATE.display()):
        if display.draw(current_screen):

            screen_updated = False
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            try : STATE.stop()
            except:
                print("Game Stopped")
                pass
            run = False

    pygame.display.update()
        
pygame.quit()