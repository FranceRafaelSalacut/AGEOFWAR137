import pygame
from src.CONSTANTS import *
from gameClasses.screen import *
from gameClasses.button import *
pygame.init

# Initializing Buttons
# parameters are text, color, pos_x, pos_y, height, width
host = Button("Host", Light_Grey, 350, 50, 100, 50)
client = Button("Client", Light_Grey, 350, 150, 100, 50)
exit = Button("Exit", Light_Grey, 350, 250, 100, 50)

class START_MENU():
    def __init__(self) -> None:
        pass

    def screen_to_display(self):
        # Initializing Screen
        # parameters are height, width, color
        screen = Screen(SCREEN_WIDTH, SCREEN_HEIGHT, Baby_Blue)
        surface = screen.returnScreen()
        return surface
    
    def display(self):      
        return [host, client, exit]