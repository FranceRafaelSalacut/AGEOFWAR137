import pygame as pg
from gameClasses.baseModel import baseModel
from gameClasses.baseUnit import *
from .gameClassValues import PROJECTILES

class Projectile(baseModel):
    def __init__(self, id, unit, x = 0, y = 0):
        super().__init__(id, x, y)
        self.fetchValues('Stone')
        self.unit = unit
        self.movePattern = Movement_None(self)
        self.damage = self.unit.damage

    def fetchValues(self, unitType : str):
        val = PROJECTILES[unitType]
        self.image = pg.image.load(val["img"]).convert_alpha()
        self.image = pg.transform.scale(self.image, val["imgScale"])
        self.rect = self.image.get_rect()
            
    def goTowardsTarget(self):
        if distance_to(self.unit.rect.center, self.unit.attackTarget.rect.center) > 80:
            if self.unit.rect.centerx > self.unit.attackTarget.rect.centerx:
                self.unit.rect.centerx -= self.unit.mspd
            else:
                self.unit.rect.centerx += self.unit.mspd

    def check_collision(self):
        # unit.Rect.collidepoint
        pass
    def deal_damage(self, unit):
        unit.curhp -= self.damage