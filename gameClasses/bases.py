import pygame as pg
from gameClasses.baseBase import baseBase

class prehistoricBase(pg.sprite.Sprite, baseBase):
    def __init__(self, id, x, y, height, width, groups, screen):
        super().__init__(groups)
        self.id = id
        self.x = x
        self.y = y
        self.groups = groups
        self.screen = screen
        self.image = pg.Surface([width, height])
        self.image.fill((0,0,255))
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]        
        self.width = width
        self.height = height
        self.hp = 10
    def update(self):
        pg.draw.rect(self.screen, (255,0,0), (self.rect.left, self.rect.top - 20, self.width, 10))
        pg.draw.rect(self.screen, (0,128,0), (self.rect.left, self.rect.top - 20, self.width - (5 * (10 - self.hp)), 10))
    def die(self):
        pass
