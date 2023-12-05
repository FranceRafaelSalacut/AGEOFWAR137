from baseUnit import baseUnit
from projectile import Projectile
import pygame as pg

class rangedUnit(baseUnit):
    def __init__(self, id, x, y, width, height):
        self.id = id
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def move(self):
        pass
    def attack(self):
        pass
    def die(self):
        pass
    
class Slingshotter(pg.sprite.Sprite, rangedUnit):
    def __init__(self, id, x, y, width, height):
        super(Slingshotter, self).__init__()
        self.image = pg.Surface([width, height])
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.hp = 0
        self.mspd = 0
        self.aspd = 0
        self.dmg = 0
        self.bounty = 0
        self.exp = 0
        
class Archer(pg.sprite.Sprite, rangedUnit):
    def __init__(self, id, x, y, width, height):
        super(Archer, self).__init__()
        self.image = pg.Surface([width, height])
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.hp = 0
        self.mspd = 0
        self.aspd = 0
        self.dmg = 0
        self.bounty = 0
        self.exp = 0

class Sniper(pg.sprite.Sprite, rangedUnit):
    def __init__(self, id, x, y, width, height):
        super(Sniper, self).__init__()
        self.image = pg.Surface([width, height])
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.hp = 0
        self.mspd = 0
        self.aspd = 0
        self.dmg = 0
        self.bounty = 0
        self.exp = 0
        
class Stormtrooper(pg.sprite.Sprite, rangedUnit):
    def __init__(self, id, x, y, width, height):
        super(Stormtrooper, self).__init__()
        self.image = pg.Surface([width, height])
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.hp = 0
        self.mspd = 0
        self.aspd = 0
        self.dmg = 0
        self.bounty = 0
        self.exp = 0