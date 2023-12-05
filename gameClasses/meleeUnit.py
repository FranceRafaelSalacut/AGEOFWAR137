from gameClasses.baseUnit import baseUnit
import pygame as pg
from CONSTANTS import *


class MeleeUnit(baseUnit):
    def __init__(self, id, x, y, width, height):
        self.id = id
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def move(self):
        pass
    def attack(self):
        pass
    def die(self):
        pass

class Caveman(pg.sprite.Sprite, MeleeUnit):
    def __init__(self, id, x, y, width, height, direction, groups):
        super(Caveman, self).__init__()
        pg.sprite.Sprite.__init__(self, groups) # Init the sprit within this group
        self.groups = groups
        self.image = pg.Surface([width, height])
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.direction = direction
        self.hp = 0
        self.mspd = 2
        self.aspd = 0
        self.dmg = 0
        self.bounty = 0
        self.exp = 0

    def update(self):
        self.rect.centerx += self.mspd
        # 
        if self.rect.left > SCREEN_WIDTH + 100:
            self.kill()
        else:
            print(self.rect.centerx)

class Footman(pg.sprite.Sprite, MeleeUnit):
    def __init__(self, id, x, y, width, height, direction, groups):
        super(Footman, self).__init__()
        pg.sprite.Sprite.__init__(self, groups) # Init the sprit within this group
        self.groups = groups
        self.image = pg.Surface([width, height])
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.hp = 0
        self.mspd = 2
        self.aspd = 0
        self.dmg = 0
        self.bounty = 0
        self.exp = 0
        
    def update(self):
        self.rect.centerx += self.mspd
        # 
        if self.rect.left > SCREEN_WIDTH + 100:
            self.kill()
        else:
            print(self.rect.centerx)

class Soldier(pg.sprite.Sprite, MeleeUnit):
    def __init__(self, id, x, y, width, height, direction, groups):
        super(Soldier, self).__init__()
        pg.sprite.Sprite.__init__(self, groups) # Init the sprit within this group
        self.groups = groups
        self.image = pg.Surface([width, height])
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.hp = 0
        self.mspd = 2
        self.aspd = 0
        self.dmg = 0
        self.bounty = 0
        self.exp = 0
        
    def update(self):
        self.rect.centerx += self.mspd
        # 
        if self.rect.left > SCREEN_WIDTH + 100:
            self.kill()
        else:
            print(self.rect.centerx)

class Robot(pg.sprite.Sprite, MeleeUnit):
    def __init__(self, id, x, y, width, height, direction, groups):
        super(Robot, self).__init__()
        pg.sprite.Sprite.__init__(self, groups) # Init the sprit within this group
        self.groups = groups
        self.image = pg.Surface([width, height])
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.hp = 0
        self.mspd = 2
        self.aspd = 0
        self.dmg = 0
        self.bounty = 0
        self.exp = 0
        
    def update(self):
        self.rect.centerx += self.mspd
        # 
        if self.rect.left > SCREEN_WIDTH + 100:
            self.kill()
        else:
            print(self.rect.centerx)