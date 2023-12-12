import pygame
from src.CONSTANTS import *
from mainClasses.screen import *
from mainClasses.button import *
from mainClasses.text import *
from mainClasses.serverclass import *
from mainClasses.image import *
pygame.init


ServerBoard = Image('graphics/gui/GUI_player_board.png',0,0,SCREEN_WIDTH//2 + 250,SCREEN_HEIGHT-10)
Button_Generic_1 = Image('graphics/gui/Button_pickTarget.png',0,0,1,1)
Button_Generic_2 = Image('graphics/gui/Button_pickTarget.png',0,0,1,1)
Button_Generic_3 = Image('graphics/gui/Button_pickTarget.png',0,0,1,1)
Button_Generic_4 = Image('graphics/gui/Button_pickTarget.png',0,0,1,1)
# Initializing Buttons
# parameters are text, color, pos_x, pos_y, width, height, font size
back = Button(Light_Grey, SCREEN_WIDTH - 200, 150, 100, 50, 35, text = "Back", image=Button_Generic_1, textColor=(100,100,100))
start_server = Button(Light_Grey, back.rect.left, back.rect.bottom + 20, 175, 50, 35, text = "Start_Server", image=Button_Generic_2, textColor=(100,100,100))
stop_server = Button(Light_Grey, back.rect.left, start_server.rect.bottom + 20, 175, 50, 35, text = "Stop_Server", image=Button_Generic_3, textColor=(100,100,100))
start_game = Button(Light_Grey, back.rect.left, stop_server.rect.bottom + 20, 175, 50, 35, text = "Start_Game", image=Button_Generic_4, textColor=(100,100,100))

# parameters are text, center x, center y, Fontsize
Display_Text = Text("SERVERS", 150, 150, 20)

class SERVER_MENU():
    def __init__(self) -> None:
        self.server = Server()
        self.images = [
            ServerBoard,
        ]
        self.buttons = [
            back,
            start_server,
            stop_server,
            start_game,
        ]
        self.to_display = [
            ServerBoard,
            back,
            Display_Text,
            start_server,
            stop_server,
            start_game]
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

    def animate(self):
        pass

        