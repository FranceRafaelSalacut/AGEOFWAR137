import pygame as pg
from gameClasses.meleeUnit import *

# Class for buttons used by players ingame
class playerButton(pg.sprite.Sprite):
    def __init__(self, x, y, enabled, scale, image):
        super().__init__()
        self.image = pg.image.load(image).convert_alpha()
        self.image = pg.transform.scale(self.image, (int(self.image.get_width() * scale), int(self.image.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.mouse_pos = pg.mouse.get_pos()
        self.enabled = enabled
        #self.rect.center = (x,y)
        self.rect.topleft = (x,y)
        self.clicked = False
    
    # Sprite group calls this method for all buttons constantly in game loop
    def update(self):
        # When mouse hovers over button
        if self.rect.collidepoint(self.mouse_pos):
            # When button gets left-clicked
            if pg.mouse.get_pressed()[0]:
                # Implement behavior here
                pass
            

class trainButton(playerButton):
    def __init__(self, x, y, enabled, scale, image, factory, era):
        super(playerButton, self).__init__()
        self.image = pg.image.load(image).convert_alpha()
        self.image = pg.transform.scale(self.image, (int(self.image.get_width() * scale), int(self.image.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.mouse_pos = pg.mouse.get_pos()
        self.factory = factory
        self.enabled = enabled
        #self.rect.center = (x,y)
        self.rect.topleft = (x,y)
        self.type = era
        self.clicked = False
    
    def update(self):
        if self.rect.collidepoint(self.mouse_pos):
            # Maybe show unit descriptions here when player hovers mouse over button(?)
            if pg.mouse.get_pressed()[0]:
                # Train units here
                if self.clicked != True:
                    if self.type == 1:
                        self.factory.create_melee_unit()
                    elif self.type == 2:
                        self.factory.create_ranged_unit()
                    if self.type == 3:
                        self.factory.create_tank_unit()