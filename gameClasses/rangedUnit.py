from baseUnit import baseUnit
from projectile import Projectile
import pygame as pg

class rangedUnit(baseUnit):
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
    def move(self):
        pass
    def attack(self):
        pass
    def die(self):
        pass
    
class Slingshotter(pg.sprite.Sprit, rangedUnit):
    def __init__(self):
        super().__init__()
        self.hp = 0
        self.mspd = 0
        self.aspd = 0
        self.dmg = 0
        self.bounty = 0
        self.exp = 0
        
class Archer(pg.sprite.Sprit, rangedUnit):
    def __init__(self):
        super().__init__()
        self.hp = 0
        self.mspd = 0
        self.aspd = 0
        self.dmg = 0
        self.bounty = 0
        self.exp = 0

class Sniper(pg.sprite.Sprit, rangedUnit):
    def __init__(self):
        super().__init__()
        self.hp = 0
        self.mspd = 0
        self.aspd = 0
        self.dmg = 0
        self.bounty = 0
        self.exp = 0
        
class Stormtrooper(pg.sprite.Sprit, rangedUnit):
    def __init__(self):
        super().__init__()
        self.hp = 0
        self.mspd = 0
        self.aspd = 0
        self.dmg = 0
        self.bounty = 0
        self.exp = 0