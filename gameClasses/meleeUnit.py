from baseUnit import baseUnit
import pygame as pg

class meleeUnit(baseUnit):
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

class Caveman(pg.sprite.Sprite, meleeUnit):
    def __init__(self):
        super().__init__()
        self.image = pg.image.surface()
        self.hp = 0
        self.mspd = 0
        self.aspd = 0
        self.dmg = 0
        self.bounty = 0
        self.exp = 0

class Footman(pg.sprite.Sprite, meleeUnit):
    def __init__(self):
        super().__init__()
        self.hp = 0
        self.mspd = 0
        self.aspd = 0
        self.dmg = 0
        self.bounty = 0
        self.exp = 0

class Soldier(pg.sprite.Sprite, meleeUnit):
    def __init__(self):
        super().__init__()
        self.hp = 0
        self.mspd = 0
        self.aspd = 0
        self.dmg = 0
        self.bounty = 0
        self.exp = 0

class Robot(pg.sprite.Sprite, meleeUnit):
    def __init__(self):
        super().__init__()
        self.hp = 0
        self.mspd = 0
        self.aspd = 0
        self.dmg = 0
        self.bounty = 0
        self.exp = 0