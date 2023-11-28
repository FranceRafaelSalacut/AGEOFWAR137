import pygame
from src.CONSTANTS import *
from gameClasses.screen import *
from gameClasses.button import *
from gameClasses.clientclass import *
pygame.init

# Initializing Buttons
# parameters are text, color, pos_x, pos_y, height, width
back = Button("Back", Light_Grey, 600, 50, 100, 50)
start_find = Button("Find_Servers", Light_Grey, 550, 150, 175, 50)
stop_find = Button("Stop_Find", Light_Grey, 550, 250, 175, 50)

class CLIENT_MENU():
    def __init__(self) -> None:
        self.client = Client()

    def screen_to_display(self):
        # Initializing Screen
        # parameters are height, width, color
        screen = Screen(SCREEN_WIDTH, SCREEN_HEIGHT, Baby_Blue)
        surface = screen.returnScreen()
        return surface
    
    def display(self):      
        return [back, start_find, stop_find]
    
    def find_start(self):
        self.client.startFinding()

    def find_stop(self):
        self.client.stopFinding()