import pygame
from src.CONSTANTS import *
from mainClasses.screen import *
from mainClasses.button import *
pygame.init

# Initializing Buttons
# parameters are text, color, pos_x, pos_y, width, 
Background = Image('graphics/main_menu.png',0,0,SCREEN_WIDTH,SCREEN_HEIGHT)

Menu = Image('graphics/gui/Training_board.png',SCREEN_WIDTH - 210,10,200,300)
Button_Generic_1 = Image('graphics/gui/Button_pickTarget.png',0,0,1,1)
Button_Generic_2 = Image('graphics/gui/Button_pickTarget.png',0,0,1,1)
Button_Generic_3 = Image('graphics/gui/Button_pickTarget.png',0,0,1,1)


host = Button(Light_Grey, Menu.rect.centerx - 50, Menu.rect.top + 45, 100, 42, 35, value = "Host", text = "Host", image=Button_Generic_1, textColor=(100,100,100))
client = Button(Light_Grey, host.rect.left, host.rect.bottom + 10, 100, 50, 35, value = "Client", text ="Client", image=Button_Generic_2, textColor=(100,100,100))
exit = Button(Light_Grey, host.rect.left, client.rect.bottom + 10, 100, 50, 35, value = "Exit", text = "Exit", image=Button_Generic_3, textColor=(100,100,100))

class START_MENU():
    def __init__(self) -> None:
        self.images = [
            Background,
            Menu,
            Button_Generic_1,
            Button_Generic_2,
            Button_Generic_3,
        ]
        self.buttons = [
            host,
            client,
            exit
        ]
        self.toDisplay = [
            Background,
            Menu,
            host,
            client, 
            exit, 
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
    
    def display(self):
        return self.toDisplay
    def animate(self):
        pass