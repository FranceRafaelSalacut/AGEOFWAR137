from abc import abstractmethod
from .baseModel import baseModel
from .gameClassValues import UNITS
import pygame as pg

class baseUnit(baseModel):
    def __init__(self, id, x = 0, y = 0):
        super().__init__(id, x, y)
    def fetchValues(self, unitType : str):
        val = UNITS[unitType]
        self.hp = val["hp"]
        self.mspd = val["mspd"]
        self.aspd = val["aspd"]
        self.dmg = val["dmg"]
        self.bounty = val["bounty"]
        self.exp = val["exp"]
        self.image = pg.image.load(val["img"]).convert_alpha()
        self.image = pg.transform.scale(self.image, (75,75))
        self.rect = self.image.get_rect()
    def getListValues(self):
        return [self.hp, self.mspd, self.aspd, self.dmg, self.bounty, self.exp]

    def move(self):
        self.rect.centerx += self.mspd
    @abstractmethod
    def attack(self):
        pass

if __name__ == "__main__":
    test = baseUnit(1)
    test.fetchValues('Caveman')

    print(test.hp)