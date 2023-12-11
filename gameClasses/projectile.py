import pygame as pg
from gameClasses.baseModel import baseModel
from .gameClassValues import PROJECTILES

class Projectile(baseModel):
    def __init__(self, id, x = 0, y = 0):
        super().__init__(id, x, y)

    def fetchValues(self, unitType : str):
        val = PROJECTILES[unitType]
        # Get the damage value from the rannged unit
        self.image = pg.image.load(val["img"]).convert_alpha()
        self.image = pg.transform.scale(self.image, val["imgScale"])
        self.rect = self.image.get_rect()   
    def draw(self):
        pass
    def die(self):
        pass