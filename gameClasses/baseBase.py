import pygame as pg
from .baseModel import baseModel

class baseBase(baseModel):
    def __init__(self, id, x, y, width, height):
        super().__init__(id, x, y, width, height)
        self.hp = 0