import pygame
import threading
import time
from src.CONSTANTS import *
from mainClasses.screen import *
from mainClasses.button import *
from mainClasses.text import *
from mainClasses.gameclass import *
pygame.init


# Initializing Buttons
# parameters are text, color, pos_x, pos_y, width, height, font size, value

Button_trainUnit = Button("Unit", Light_Grey, GAME_SCREEN_WIDTH - 175, 50, 50, 50, 20,value = "train_unit")

# parameters are text, center x, center y, Fontsize
Display_Text = Text("test", GAME_SCREEN_WIDTH - 30, GAME_SCREEN_HEIGHT - 10, 20)

class GAME_SCREEN():
    def __init__(self) -> None:
        self.game = GameClass()
        self.to_display = [Display_Text, Button_trainUnit]
    
    def train_unit(self):
        return self.game.train_unit()
    
    def display(self):      
        return self.to_display