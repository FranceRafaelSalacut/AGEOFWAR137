import pygame as pg

class baseUnit(pg.sprite.Sprite):
    def __init__(self, id, hp, mspd, aspd, dmg):
        pg.sprite.Sprite.__init__(self)
        self.id = id
        self.hp = hp # Health points
        self.mspd = mspd # Movement speed
        self.aspd = aspd # Attack speed
        self.dmg = dmg # Damage