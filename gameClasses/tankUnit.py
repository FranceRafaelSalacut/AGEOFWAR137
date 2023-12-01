from baseUnit import baseUnit
import pygame as pg

class tankUnit(baseUnit):
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
    
class dinoRider(pg.sprite.Sprite, tankUnit):
    def __init__(self, id, x, y, width, height):
        super(dinoRider, self).__init__()
        self.hp = 0
        self.mspd = 0
        self.aspd = 0
        self.dmg = 0
        self.bounty = 0
        self.exp = 0
        
class Cavalier(pg.sprite.Sprite, tankUnit):
    def __init__(self, id, x, y, width, height):
        super(Cavalier, self).__init__()
        self.hp = 0
        self.mspd = 0
        self.aspd = 0
        self.dmg = 0
        self.bounty = 0
        self.exp = 0

class Tank(pg.sprite.Sprite, tankUnit):
    def __init__(self, id, x, y, width, height):
        super(Tank, self).__init__()
        self.hp = 0
        self.mspd = 0
        self.aspd = 0
        self.dmg = 0
        self.bounty = 0
        self.exp = 0

class Mecha(pg.sprite.Sprite, tankUnit):
    def __init__(self, id, x, y, width, height):
        super(Mecha, self).__init__()
        self.hp = 0
        self.mspd = 0
        self.aspd = 0
        self.dmg = 0
        self.bounty = 0
        self.exp = 0