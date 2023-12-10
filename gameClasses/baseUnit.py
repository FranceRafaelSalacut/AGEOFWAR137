from __future__ import annotations
from abc import abstractmethod
from .baseModel import baseModel
from .gameClassValues import UNITS
import pygame as pg
from math import sqrt

def distance_to(P1, P2):
    return sqrt((P2[0] - P1[0])**2 + (P2[1] - P1[1])**2)
class baseUnit(baseModel):
    def __init__(self, id, x = 0, y = 0):
        super().__init__(id, x, y)
        self.movePattern = Movement_None(self)
        self.attackTarget:baseModel = None
        self.possibleTargets = pg.sprite.Group()

    def fetchValues(self, unitType : str):
        val = UNITS[unitType]
        self.hp = val["hp"]
        self.mspd = val["mspd"]
        self.aspd = val["aspd"]
        self.dmg = val["dmg"]
        self.bounty = val["bounty"]
        self.exp = val["exp"]
        self.cost = val["cost"]
        self.image = pg.image.load(val["img"]).convert_alpha()
        self.image = pg.transform.scale(self.image, val["imgScale"])
        self.rect = self.image.get_rect()

    def addPossibleTarget(self, target: baseModel):
        if not self.possibleTargets.has(target):
            self.possibleTargets.add(target)

    def setMovement(self, movePattern:Movement_None):
        self.movePattern = movePattern

    def move(self):
        self.movePattern.move()

    def updateTarget(self):
        if self.possibleTargets:
            self.attackTarget = min(self.possibleTargets, key=lambda rect: distance_to(self.rect.center, rect.rect.center))

    @abstractmethod
    def attack(self):
        pass
class Movement_None():
    def __init__(self, unit:baseUnit) -> None:
        self.unit = unit
    def move(self):
        pass
    def goTowardsTarget(self):
        if distance_to(self.unit.rect.center, self.unit.attackTarget.rect.center) > 80:
            if self.unit.rect.centerx > self.unit.attackTarget.rect.centerx:
                self.unit.rect.centerx -= self.unit.mspd
            else:
                self.unit.rect.centerx += self.unit.mspd
class Movement_Friendly(Movement_None):
    def move(self):
        if not self.unit.attackTarget:
            self.unit.rect.centerx += self.unit.mspd
        else:
            self.goTowardsTarget()

class Movement_Enemy(Movement_None):
    def move(self):
        if not self.unit.attackTarget:
            self.unit.rect.centerx -= self.unit.mspd
        else:
            self.goTowardsTarget()