import pygame
import time
from src.CONSTANTS import *
from mainClasses.screen import *
from mainClasses.button import *
from mainClasses.clientclass import *
from mainClasses.image import *
pygame.init

# Initializing 
Server_text = Text("SERVERS", GAME_SCREEN_WIDTH//2, 30, 50)
ServerList = Image('graphics/gui/ServerList.png',250,Server_text.rect.bottom + 5,750,500)
Button_Generic_1 = Image('graphics/gui/Button_pickTarget.png',0,0,1,1)
Button_Generic_2 = Image('graphics/gui/Button_pickTarget.png',0,0,1,1)
Button_Generic_3 = Image('graphics/gui/Button_pickTarget.png',0,0,1,1)

# parameters are text, color, pos_x, pos_y, width, height
back = Button(Light_Grey, 50, 150, 100, 50, 35, text = "Back", value = "Back", image = Button_Generic_1, textColor=(100,100,100))
start_find = Button(Light_Grey, back.rect.left, back.rect.bottom + 10, 180, 50, 35, text = "Find Servers", value = "Find_Servers", image = Button_Generic_2, textColor=(100,100,100))
stop_find = Button(Light_Grey,  back.rect.left, start_find.rect.bottom + 10, 175, 50, 35, text = "Reset", value = "Reset", image = Button_Generic_3, textColor=(100,100,100))

Placeholder_text = Text("Cant find any Servers :(", Server_text.rect.centerx,ServerList.rect.top + 50, 20, show= False, color =(100,100,100))

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
            ServerList,
        ]
        self.to_display = [
            ServerList,
            back, 
            start_find, 
            stop_find,
            Server_text,
            Placeholder_text,
        ]
        self.buttonList :list[Button] = []
        self.textList : list[Text] = []
    def load_images(self):
        for i in self.images:
            i.load_image()
        for i in self.buttons:
            i.load_image()
    def load_extra(self):
        for i in self.buttonList:
            i.load_image()

    def screen_to_display(self):
        # Initializing Screen
        # parameters are height, width, color
        screen = Screen(SCREEN_WIDTH, SCREEN_HEIGHT, Baby_Blue)
        surface = screen.returnScreen()
        return surface

    def resetDisplay(self):
        self.buttonList = []
        self.textList = []

    def display(self):
        return self.to_display + self.buttonList + self.textList
    
    def start(self):
        self.resetDisplay()
        servers = self.client.startFinding()
        if servers:
            Placeholder_text.show = False
            for idx, address in enumerate(servers):
                if idx == 8:
                    break
                b = Button(Light_Grey, ServerList.rect.left + 50, ServerList.rect.top + 20 + (idx * 40), 75, 25, 20, text = "Connect", value = f"Connect//{str(address)}")
                t = Text(str(address), b.rect.right + 100, b.rect.centery, 20)
                self.buttonList.append(b)
                self.textList.append(t)
            self.load_extra()
        else:
            Placeholder_text.show = True

    def stop(self):
        self.resetDisplay()
        self.client.stopFinding()

    def connect(self,address : str):
        a = address.split('//')[1].replace("'",'').replace(')','').replace('(','').replace(' ','').split(',')
        a = (a[0],int(a[1]))
        return self.client.connect(a)

    def animate(self):
        pass