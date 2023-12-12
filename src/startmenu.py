import pygame
from src.CONSTANTS import *
from mainClasses.screen import *
from mainClasses.button import *
pygame.init

# Initializing Buttons
# parameters are text, color, pos_x, pos_y, width, height
host = Button(Light_Grey, 350, 50, 100, 50, 35, text = "Host")
client = Button(Light_Grey, 350, 150, 100, 50, 35, text ="Client")
exit = Button(Light_Grey, 350, 250, 100, 50, 35, text = "Exit")

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