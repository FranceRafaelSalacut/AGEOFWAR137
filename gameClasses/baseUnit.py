import pygame as pg

class baseUnit(pg.sprite.Sprite):
    def __init__(self, id, hp, mspd, aspd, arng, dmg, bounty):
        pg.sprite.Sprite.__init__(self)
        self.id = id
        self.hp = hp # Health points
        self.mspd = mspd # Movement speed
        self.aspd = aspd # Attack speed
        self.arng = arng # Attack range
        self.dmg = dmg # Damage
        self.bounty = bounty # Gold dropped when unit dies
        self.pos_x = 0
        self.pos_y = 0
    def attack(self):
        pass