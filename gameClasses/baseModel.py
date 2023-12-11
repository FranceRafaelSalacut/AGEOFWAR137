import pygame as pg
from abc import abstractmethod

class baseModel(pg.sprite.Sprite):
    def __init__(self, id, x = 0, y = 0, width = 75, height = 75):
        # should only contain sprite stuff
        super(baseModel, self).__init__()
        self.id:str = id
        self.image = pg.Surface([width, height])
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

        # dont mind this
        self.hp = 0
        self.curhp = self.hp
        self.isDead = False
    
    def die(self):
        #TODO: add death animation here (if we're gonna use em. Also prolly need to put a delay before calling self.kill())
        self.kill()

    def getCenter(self):
        return self.rect.center
    
    def update(self, screen):
        self.update_healthBar(screen)

    def update_healthBar(self, screen):
        hpratio = self.curhp/self.hp
        pg.draw.rect(screen, (255,0,0), (self.rect.left, self.rect.top - 20, self.rect.width, 10))
        pg.draw.rect(screen, (0,128,0), (self.rect.left, self.rect.top - 20, self.rect.width * hpratio, 10))
        if self.curhp <= 0:
            self.die()

    @abstractmethod
    def die(self):
        pass