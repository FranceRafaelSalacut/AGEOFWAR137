import pygame as pg
from .baseModel import baseModel

class baseBase(baseModel):
    def __init__(self, id,width, height, x, y):
        super().__init__(id,width, height, x, y)
        self.hp = 0