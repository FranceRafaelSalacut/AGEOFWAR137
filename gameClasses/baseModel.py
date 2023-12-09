import pygame as pg
from abc import abstractmethod

class baseModel(pg.sprite.Sprite):
    def __init__(self, id, x, y, width, height):
        # should only contain sprite stuff
        pg.sprite.Sprite.__init__(self)
        self.id = id
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.image = pg.Surface([width, height])
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

    @abstractmethod
    def die(self):
        pass