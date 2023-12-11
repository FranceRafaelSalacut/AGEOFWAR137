import pygame as pg
from gameClasses.baseModel import baseModel

class Projectile(baseModel):
    def __init__(self, id, x = 0, y = 0):
        super().__init__(id, x, y)
    def draw(self):
        pass
    def die(self):
        pass
    