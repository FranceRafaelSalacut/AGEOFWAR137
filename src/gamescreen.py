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



Button_trainTankUnit = Button("Tank", Light_Grey, GAME_SCREEN_WIDTH - 75, 50, 50, 50, 20,value = "train_tank_unit")
Button_trainRangeUnit = Button("Ranged", Light_Grey, Button_trainTankUnit.rect.left - 75, 50, 50, 50, 20,value = "train_ranged_unit")
Button_trainMeleeUnit = Button("Melee", Light_Grey, Button_trainRangeUnit.rect.left - 75, 50, 50, 50, 20,value = "train_melee_unit")

# parameters are text, center x, center y, Fontsize
Display_Text = Text("test", GAME_SCREEN_WIDTH - 30, GAME_SCREEN_HEIGHT - 10, 20)

class GAME_SCREEN():
    def __init__(self) -> None:
        self._game = GameClass()
        self.to_display = [Display_Text, Button_trainMeleeUnit, Button_trainRangeUnit, Button_trainTankUnit]

    def get_base(self):
        return self._game.get_base()
    
    def train_melee_unit(self):
        return self._game.train_melee_unit()
    
    def display(self):      
        return self.to_display