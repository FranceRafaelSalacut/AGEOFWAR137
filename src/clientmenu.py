import pygame
import time
from src.CONSTANTS import *
from mainClasses.screen import *
from mainClasses.button import *
from mainClasses.clientclass import *
from mainClasses.image import *
pygame.init

# Initializing Buttons
# parameters are text, color, pos_x, pos_y, width, height
back = Button(Light_Grey, 600, 50, 100, 50, 35, text = "Back")
start_find = Button(Light_Grey, 550, 150, 180, 50, 35, text = "Find_Servers")
stop_find = Button(Light_Grey, 550, 250, 175, 50, 35, text = "Reset")
connect = [
    Button(Light_Grey, 50, 50, 75, 25, 20, text = "Connect"),
    Button(Light_Grey, 50, 150, 75, 25, 20, text = "Connect"),
    Button(Light_Grey, 50, 250, 75, 25, 20, text = "Connect"),

    # parameters are text, center x, center y, Fontsize
    Text("Placeholder", 200, 60, 20),
]

class CLIENT_MENU():
    def __init__(self) -> None:
        self.client = Client()
        self.to_display = [back, start_find, stop_find#,
                           #connect[0], connect[1], connect[2],
                           #connect[3], connect[4], connect[5]
                           ]
        self.images = [
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
    
    def resetDisplay(self):
        self.to_display = [back, start_find, stop_find#,
                           #connect[0], connect[1], connect[2],
                           #connect[3], connect[4], connect[5]
                           ]
        for x in range(3, len(connect)):
            connect[x].changeText("")

    def display(self):      
        return self.to_display
    
    def start(self):
        self.resetDisplay()
        self.client.startFinding(self.to_display, connect)

    def stop(self):
        self.resetDisplay()
        self.client.stopFinding()

    def connect(self, index):
        return self.client.connect(index-3)