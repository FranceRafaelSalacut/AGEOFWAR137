import pygame
import threading
import time
from src.CONSTANTS import *
from mainClasses.screen import *
from mainClasses.button import *
from mainClasses.text import *
from mainClasses.gameclass import *
pygame.init


# GRAPHICS

# UI

Display_Text = Text("GAME STARTED", 100, 75, 20)

class GAME_SCREEN():
    def __init__(self) -> None:
        self.to_display = [Display_Text]

    def screen_to_display(self):
        # Initializing Screen
        # parameters are height, width, color
        screen = Screen(GAME_SCREEN_WIDTH, GAME_SCREEN_HEIGHT, Baby_Blue)
        surface = screen.returnScreen()
        return surface
    
    def display(self):      
        return self.to_display
