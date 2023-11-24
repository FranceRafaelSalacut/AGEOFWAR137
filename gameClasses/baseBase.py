import pygame as pg

class baseBase(pg.sprite.Sprite):
    def __init__(self, id, hp):
        pg.sprite.Sprite.__init__(self)
        self.id = id
        self.hp = hp # Hit points
        