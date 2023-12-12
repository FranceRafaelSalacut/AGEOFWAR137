import pygame
import time
from src.CONSTANTS import *
from mainClasses.screen import *
from mainClasses.button import *
from mainClasses.clientclass import *
from mainClasses.image import *
pygame.init

# Initializing Buttons
Button_Generic_1 = Image('graphics/gui/Button_pickTarget.png',0,0,1,1)
Button_Generic_2 = Image('graphics/gui/Button_pickTarget.png',0,0,1,1)
Button_Generic_3 = Image('graphics/gui/Button_pickTarget.png',0,0,1,1)

# parameters are text, color, pos_x, pos_y, width, height
back = Button(Light_Grey, 50, 50, 100, 50, 35, text = "Back", value = "Back", image = Button_Generic_1, textColor=(100,100,100))
start_find = Button(Light_Grey, back.rect.left, back.rect.bottom + 10, 180, 50, 35, text = "Find Servers", value = "Find_Servers", image = Button_Generic_2, textColor=(100,100,100))
stop_find = Button(Light_Grey,  back.rect.left, start_find.rect.bottom + 10, 175, 50, 35, text = "Reset", value = "Reset", image = Button_Generic_3, textColor=(100,100,100))
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
        self.buttons = [
            back,
            start_find,
            stop_find
        ]
        self.images = [
            Button_Generic_1,
            Button_Generic_2,
            Button_Generic_3,
        ]
        self.to_display = [
            back, 
            start_find, 
            stop_find
        ]
    def load_images(self):
        for i in self.images:
            i.load_image()
        for i in self.buttons:
            i.load_image()

    def screen_to_display(self):
        # Initializing Screen
        # parameters are height, width, color
        screen = Screen(SCREEN_WIDTH, SCREEN_HEIGHT, Baby_Blue)
        surface = screen.returnScreen()
        return surface
    
    def resetDisplay(self):
        self.to_display = [
            back, 
            start_find, 
            stop_find
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

    def animate(self):
        pass