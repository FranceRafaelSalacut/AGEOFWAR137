from __future__ import annotations
from .baseModel import baseModel
from .gameClassValues import UNITS
import pygame as pg
from math import sqrt

STATE_MOVING = 0
STATE_ATTACKING = 1
FACING_LEFT = 0
FACING_RIGHT = 1

def distance_to(P1, P2):
    return sqrt((P2[0]-P1[0])**2)
    return sqrt((P2[0] - P1[0])**2 + (P2[1] - P1[1])**2)

class baseUnit(baseModel):
    def __init__(self, id, x = 0, y = 0):
        super().__init__(id, x, y)
        self.movePattern = Movement_None(self)
        self.attackTarget:baseModel = None
        self.state = STATE_MOVING
        self.possibleTargets = pg.sprite.Group()
        self.isDead = False
        self.killer:baseModel = None
        self.owner = '//'.join(self.id.split('//')[:-1])
        self.isFacing = FACING_RIGHT
        self.position :list = [float(x),float(y)]
        self.direction = 0

    def fetchValues(self, unitType : str):
        val = UNITS[unitType]
        self.hp = val["hp"]
        self.mspd = val["mspd"]
        self.aspd = val["aspd"]
        self.attackTimer = 0
        self.dmg = val["dmg"]
        self.bounty = val["bounty"]
        self.exp = val["exp"]
        self.cost = val["cost"]
        self.range = val["range"]
        self.curhp = self.hp
        self.image = pg.image.load(val["img"]).convert_alpha()
        self.image = pg.transform.scale(self.image, val["imgScale"])
        self.imageNormal = self.image
        self.imageFlipped = pg.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()

    def addPossibleTarget(self, target: baseModel):
        if not self.possibleTargets.has(target):
            self.possibleTargets.add(target)


    def removePossibleTarget(self, target: baseModel):
        if self.possibleTargets.has(target):
            self.possibleTargets.remove(target)

    def setMovement(self, movePattern:Movement_None):
        self.movePattern = movePattern
        self.setDirection()

    def move(self):
        self.movePattern.move()

    def update_position(self):
         self.rect.centerx = round(self.position[0])

    def updateTarget(self):
        if self.possibleTargets:
            self.attackTarget = min(self.possibleTargets, key=lambda unit: distance_to(self.position, unit.position))
        self.movePattern.move()

    def die(self):
        #TODO: add death animation here (if we're gonna use em. Also prolly need to put a delay before calling self.kill())
        self.isDead = True

    def get_bounty(self):
        return f'{self.id}//GOLD:{self.bounty}//EXP:{self.exp}'

    def update(self, screen):
        self.updateTarget()
        if self.isFacing == FACING_RIGHT:
            self.image = self.imageNormal
        if self.isFacing == FACING_LEFT:
            self.image = self.imageFlipped

        if self.state == STATE_MOVING:
            self.move()
        elif self.state == STATE_ATTACKING:
            self.attack()
            if not self.attackTarget or self.attackTarget.isDead:
                self.state = STATE_MOVING
        self.update_healthBar(screen)
        self.update_position()
        if self.curhp <= 0:
            self.die()

    def attack(self):
        self.attackTimer += self.aspd
        if self.position[0] < self.attackTarget.position[0]:
            self.isFacing = FACING_RIGHT
        else:
            self.isFacing = FACING_LEFT
        if self.attackTimer > 500 and self.range > distance_to(self.position, self.attackTarget.position):
            self.attackTarget.curhp -= self.dmg
            self.attackTimer = 0
            print(f'{self.id} attacked {self.attackTarget.id} ({self.attackTarget.curhp})')
        if self.attackTarget.curhp <= 0:
            self.attackTarget.killer = self
            self.attackTarget = None
        
    def setDirection(self):
        if isinstance(self.movePattern, Movement_Friendly):
            self.direction = 1
        elif isinstance(self.movePattern, Movement_Enemy):
            self.direction = -1

class Movement_None():
    def __init__(self, unit:baseUnit) -> None:
        self.unit = unit
    def move(self):
        pass
    def goTowardsTarget(self):
        if distance_to(self.unit.position, self.unit.attackTarget.position) > self.unit.range - 30:
            if self.unit.position[0] > self.unit.attackTarget.position[0]:
                self.unit.position[0] -= self.unit.mspd
                self.unit.isFacing = FACING_LEFT
            else:
                self.unit.position[0] += self.unit.mspd
                self.unit.isFacing = FACING_RIGHT
        else:
            self.unit.state = STATE_ATTACKING
class Movement_Friendly(Movement_None):
    def move(self):
        if not self.unit.attackTarget:
            self.unit.position[0] += self.unit.mspd
            self.unit.isFacing = FACING_RIGHT
        else:
            self.goTowardsTarget()

class Movement_Enemy(Movement_None):
    def move(self):
        if not self.unit.attackTarget:
            print(self.unit.position)
            self.unit.position[0] -= self.unit.mspd
            self.isFacing = FACING_LEFT
        else:
            self.goTowardsTarget()