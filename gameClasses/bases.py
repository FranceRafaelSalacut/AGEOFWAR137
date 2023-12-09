import pygame as pg
from gameClasses.baseBase import baseBase

class prehistoricBase(baseBase):
    def __init__(self, id, x, y, height, width):
        super().__init__()
        self.id = id
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def die(self):
        pass
