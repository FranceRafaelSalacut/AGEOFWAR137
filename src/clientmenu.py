import pygame
from src.CONSTANTS import *
from gameClasses.screen import *
from gameClasses.button import *
pygame.init

# Initializing Buttons
# parameters are text, color, pos_x, pos_y, height, width
back = Button("Back", Light_Grey, 150, 50, 100, 50)

class CLIENT_MENU():
    def __init__(self) -> None:
        pass

    def screen_to_display(self):
        # Initializing Screen
        # parameters are height, width, color
        screen = Screen(SCREEN_HEIGHT, SCREEN_WIDTH, Baby_Blue)
        surface = screen.returnScreen()
        return surface
    
    def display(self):      
        return [back]