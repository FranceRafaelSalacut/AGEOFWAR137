import pygame as pg
from abc import abstractmethod

class baseModel(pg.sprite.Sprite):
    def __init__(self, id, width = 0, height = 0, x = 0, y = 0):
        # should only contain sprite stuff
        pg.sprite.Sprite.__init__(self)
        self.id = id

        self.image = pg.Surface([width, height])
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

    @abstractmethod
    def die(self):
        pass