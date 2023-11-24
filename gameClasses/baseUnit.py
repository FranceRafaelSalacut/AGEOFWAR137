import pygame as pg
vec = pg.math.Vector2

# TODO: Add image and rect attributes (different per unit)

class baseUnit(pg.sprite.Sprite):
    def __init__(self, id, hp, mspd, aspd, arng, dmg, cost, bounty):
        pg.sprite.Sprite.__init__(self)
        self.id = id
        self.hp = hp # Hit points
        self.mspd = mspd # Movement speed
        self.aspd = aspd # Attack speed
        self.arng = arng # Attack range
        self.dmg = dmg # Damage
        self.cost = cost # Gold required to purchase the unit
        self.bounty = bounty # Gold dropped when unit dies
        self.pos = vec(0,0) # Unit position
    def attack(self):
        pass
    def die(self):
        pass