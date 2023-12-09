import pygame as pg
from .baseModel import baseModel
from .gameClassValues import *

class baseBase(baseModel):
    def __init__(self, id, x = 0, y = 0):
        super().__init__(id)

    def fetchValues(self, baseType : str):
        val = BUILDINGS[baseType]
        self.hp = val["hp"]
        self.image = pg.image.load(val["img"]).convert_alpha()
        self.rect = self.image.get_rect()

class Cave(baseBase):
    def __init__(self, id):
        super().__init__(id)
        self.fetchValues('Cave')

class Castle(baseBase):
    def __init__(self, id):
        super().__init__(id)

class Camp(baseBase):
    def __init__(self, id):
        super().__init__(id)

class Citadel(baseBase):
    def __init__(self, id):
        super().__init__(id)
