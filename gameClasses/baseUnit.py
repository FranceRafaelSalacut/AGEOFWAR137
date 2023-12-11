from __future__ import annotations
from abc import abstractmethod
from .baseModel import baseModel
from .gameClassValues import UNITS
import pygame as pg

class baseUnit(baseModel):
    def __init__(self, id, x = 0, y = 0):
        super().__init__(id, x, y)
        self.movePattern = Movement_None(self)
        self.attackTarget:baseModel = None
    def fetchValues(self, unitType : str):
        val = UNITS[unitType]
        self.hp = val["hp"]
        self.mspd = val["mspd"]
        self.aspd = val["aspd"]
        self.dmg = val["dmg"]
        self.bounty = val["bounty"]
        self.exp = val["exp"]
        self.cost = val["cost"]
        self.curhp = self.hp
        self.image = pg.image.load(val["img"]).convert_alpha()
        self.image = pg.transform.scale(self.image, val["imgScale"])
        self.rect = self.image.get_rect()

    def setMovement(self, movePattern:Movement_None):
        self.movePattern = movePattern
        
    def move(self):
        self.movePattern.move()
        
    def die(self):
        #TODO: add death animation here (if we're gonna use em. Also prolly need to put a delay before calling self.kill())
        self.kill()
    
    def update(self, screen):
        self.curhp -= 0.01 #-> Comment out to test sprite dying
        self.hpratio = self.curhp/self.hp       
        pg.draw.rect(screen, (255,0,0), (self.rect.left, self.rect.top - 20, self.rect.width, 10))
        pg.draw.rect(screen, (0,128,0), (self.rect.left, self.rect.top - 20, self.rect.width * self.hpratio, 10))
        if self.curhp <= 0:
            self.die()

    @abstractmethod
    def attack(self):
        pass
class Movement_None():
    def __init__(self, unit:baseUnit) -> None:
        self.unit = unit
    def move(self):
        pass
class Movement_Friendly(Movement_None):
    def move(self):
        self.unit.rect.centerx += self.unit.mspd

class Movement_Enemy(Movement_None):
    def move(self):
        self.unit.rect.centerx -= self.unit.mspd