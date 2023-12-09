import pygame
import threading
import time
from src.CONSTANTS import *
from mainClasses.screen import *
from mainClasses.button import *
from mainClasses.text import *
from mainClasses.serverclass import *
pygame.init


# Initializing Buttons
# parameters are text, color, pos_x, pos_y, width, height, font size
back = Button("Back", Light_Grey, 600, 50, 100, 50, 35)
start_server = Button("Start_Server", Light_Grey, 550, 150, 175, 50, 35)
stop_server = Button("Stop_Server", Light_Grey, 550, 250, 175, 50, 35)
start_game = Button("Start_Game", Light_Grey, 550, 350, 175, 50, 35)

# parameters are text, center x, center y, Fontsize
Display_Text = Text("", 100, 75, 20)

class SERVER_MENU():
    def __init__(self) -> None:
        self.server = Server()
        self.to_display = [back, Display_Text, start_server, stop_server, start_game]

    def screen_to_display(self):
        # Initializing Screen
        # parameters are height, width, color
        screen = Screen(SCREEN_WIDTH, SCREEN_HEIGHT, Baby_Blue)
        surface = screen.returnScreen()
        return surface
    
    def display(self):      
        return self.to_display
    
    def start(self):
        self.server.startServer(Display_Text)

    def stop(self):
        self.server.stopServer(Display_Text)
    
    def startGame(self):
        self.server.startGame()

        