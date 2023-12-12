import pygame as pg
from gameClasses.baseModel import baseModel
from gameClasses.baseUnit import *
from .gameClassValues import PROJECTILES

class Projectile(baseModel):
    def __init__(self, id, unit, x = 0, y = 0):
        super().__init__(id, x, y)
        self.unit = unit
        self.x = self.unit.rect.centerx
        self.y = self.unit.rect.centery
        self.fetchValues('Stone')
        self.dmg = self.unit.dmg
        
    def fetchValues(self, unitType : str):
        val = PROJECTILES[unitType]
        self.image = pg.image.load(val["img"]).convert_alpha()
        self.image = pg.transform.scale(self.image, val["imgScale"])
        self.rect = self.image.get_rect()
            
    def goTowardsTarget(self):
        self.rect.centerx += 2

    def check_collision(self):
        # unit.Rect.collidepoint
        pass
    def deal_damage(self, unit):
        unit.curhp -= self.dmg