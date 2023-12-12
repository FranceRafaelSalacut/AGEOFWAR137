import pygame
from src.CONSTANTS import *
from mainClasses.screen import *
from mainClasses.button import *
pygame.init

# Initializing Buttons
# parameters are text, color, pos_x, pos_y, width, 
Background = Image('graphics/main_menu.png',0,0,SCREEN_WIDTH,SCREEN_HEIGHT)
Menu = Image('graphics/gui/Training_board.png',0,0,100,100)
host = Button(Light_Grey, SCREEN_WIDTH - 200, 50, 100, 50, 35, text = "Host")
client = Button(Light_Grey, host.rect.left, 150, 100, 50, 35, text ="Client")
exit = Button(Light_Grey, host.rect.left, 250, 100, 50, 35, text = "Exit")

class START_MENU():
    def __init__(self) -> None:
        self.images = [
            Background,
            Menu
        ]
    def load_images(self):
        for i in self.images:
            i.load_image()
    def screen_to_display(self):
        # Initializing Screen
        # parameters are height, width, color
        screen = Screen(SCREEN_WIDTH, SCREEN_HEIGHT, Baby_Blue)
        surface = screen.returnScreen()
        return surface
    
    def display(self):
        return [
            Menu,
            Background,
            host, 
            client, 
            exit, 
            ]