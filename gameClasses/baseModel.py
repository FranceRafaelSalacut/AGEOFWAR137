import pygame as pg
from abc import abstractmethod

class baseModel(pg.sprite.Sprite):
    def __init__(self, id, x = 0, y = 0, width = 75, height = 75):
        # should only contain sprite stuff
        super(baseModel, self).__init__()
        self.id = id
        self.image = pg.Surface([width, height])
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

    @abstractmethod
    def die(self):
        pass