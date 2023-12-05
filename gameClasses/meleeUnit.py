from gameClasses.baseUnit import baseUnit
import pygame as pg


class meleeUnit(baseUnit):
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

class Caveman(pg.sprite.Sprite, meleeUnit):
    def __init__(self, id, x, y, width, height):
        super(Caveman, self).__init__()
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

class Footman(pg.sprite.Sprite, meleeUnit):
    def __init__(self, id, x, y, width, height):
        super(Footman, self).__init__()
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

class Soldier(pg.sprite.Sprite, meleeUnit):
    def __init__(self, id, x, y, width, height):
        super(Soldier, self).__init__()
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

class Robot(pg.sprite.Sprite, meleeUnit):
    def __init__(self, id, x, y, width, height):
        super(Robot, self).__init__()
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