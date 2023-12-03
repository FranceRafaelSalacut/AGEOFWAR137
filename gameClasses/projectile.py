import pygame as pg

class Projectile(pg.sprite.Sprite):
    def __init__(self, x, y, vel, direction):
        super().__init__()
        self.x = x
        self.y = y
        self.vel = vel
        self.direction = direction
    def draw(self):
        pass
    
"""
class Stone(Projectile):
    pass

class Arrow(Projectile):
    pass

class Bullet(Projectile):
    pass

class Laserbeam(Projectile):
    pass
"""