import pygame
from src.CONSTANTS import *
from mainClasses.screen import *
from mainClasses.button import *
from mainClasses.text import *
from mainClasses.serverclass import *
from mainClasses.image import *
pygame.init


# Initializing Buttons
# parameters are text, color, pos_x, pos_y, width, height, font size
back = Button(Light_Grey, 600, 50, 100, 50, 35, text = "Back")
start_server = Button(Light_Grey, 550, 150, 175, 50, 35, text = "Start_Server")
stop_server = Button(Light_Grey, 550, 250, 175, 50, 35, text = "Stop_Server")
start_game = Button(Light_Grey, 550, 350, 175, 50, 35, text = "Start_Game")

# parameters are text, center x, center y, Fontsize
Display_Text = Text("", 100, 75, 20)

class SERVER_MENU():
    def __init__(self) -> None:
        self.server = Server()
        self.to_display = [back, Display_Text, start_server, stop_server, start_game]
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
    
    def display(self):      
        return self.to_display
    
    def start(self):
        self.server.startServer(Display_Text)

    def stop(self):
        self.server.stopServer(Display_Text)

    def getList(self):
        return self.server.getAdress_list()
    
    def close(self):
        self.server.close()
    
    def startGame(self):
        self.server.startGame()

        