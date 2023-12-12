import pygame as pg
from gameClasses.baseModel import baseModel
from gameClasses.baseUnit import *
from .gameClassValues import PROJECTILES

class Projectile(baseModel):
    def __init__(self, id, unit, x = 0, y = 0):
        super().__init__(id, x, y)
        self.unit = unit
        self.fetchValues('Stone')
        self.dmg = self.unit.dmg
        self.direction = self.unit.direction
        self.rect.x = self.unit.rect.x
        self.rect.y = self.unit.rect.y
        
    def fetchValues(self, unitType : str):
        val = PROJECTILES[unitType]
        self.image = pg.image.load(val["img"]).convert_alpha()
        self.image = pg.transform.scale(self.image, val["imgScale"])
        self.rect = self.image.get_rect()
        
    def goTowardsTarget(self):
        if self.direction == 1: 
            self.rect.centerx += 2
        elif self.direction == -1:
            self.rect.centerx -= 2

    def check_collision(self, unit):
        if self.rect.colliderect(unit.rect) and self.direction != unit.direction:    
            self.deal_damage(unit)
            self.kill()
    def deal_damage(self, unit):
        unit.curhp -= self.dmg