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
    def __init__(self, id, x, y, width, height, direction, groups, screen):
        super(Caveman, self).__init__()
        pg.sprite.Sprite.__init__(self, groups) # Init the sprit within this group
        self.groups = groups
        self.image = pg.Surface([width, height])
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.width = width
        self.height = height
        self.direction = direction
        self.maxhp = 10
        self.hp = 10
        self.hpratio = self.hp/self.maxhp
        self.mspd = 2
        self.aspd = 0
        self.dmg = 0
        self.bounty = 0
        self.exp = 0
        self.screen = screen
        # Health bar    
    def update(self):
        self.rect.centerx += self.mspd
        self.hp-=0.05 # Comment out/remove. This is just to test if hp bar decrements
        # Kill sprite if it leaves screen
        self.hpratio = self.hp/self.maxhp        
        pg.draw.rect(self.screen, (255,0,0), (self.rect.left, self.rect.top - 20, self.width, 10))
        pg.draw.rect(self.screen, (0,128,0), (self.rect.left, self.rect.top - 20, self.width * self.hpratio, 10))
        if self.rect.left > SCREEN_WIDTH + 100 or self.hp < 0:
            self.die()
    def die(self):
        self.kill()
        
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
        # Kill sprite if it leaves screen
        if self.rect.left > SCREEN_WIDTH + 100:
            self.kill()

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
        # Kill sprite if it leaves screen 
        if self.rect.left > SCREEN_WIDTH + 100:
            self.kill()

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
        # Kill sprite if it leaves screen
        if self.rect.left > SCREEN_WIDTH + 100:
            self.kill()