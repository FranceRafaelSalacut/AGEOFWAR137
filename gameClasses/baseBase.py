import pygame as pg
from .baseModel import baseModel
from .gameClassValues import *

class baseBase(baseModel):
    def __init__(self, id, x = 0, y = 0):
        super().__init__(id)

    def fetchValues(self, baseType : str):
        val = BUILDINGS[baseType]
        self.hp = val["hp"]
        self.expCost = val["expCost"]
        self.image = pg.image.load(val["img"]).convert_alpha()
        self.image = pg.transform.scale(self.image, val["imgScale"])
        self.rect = self.image.get_rect()
        self.curhp = self.hp

class Cave(baseBase):
    def __init__(self, id):
        super().__init__(id)
        self.fetchValues('Cave')

class Castle(baseBase):
    def __init__(self, id):
        super().__init__(id)
        self.fetchValues('Castle')

class Camp(baseBase):
    def __init__(self, id):
        super().__init__(id)
        self.fetchValues('Camp')

class Citadel(baseBase):
    def __init__(self, id):
        super().__init__(id)
        self.fetchValues('Citadel')
