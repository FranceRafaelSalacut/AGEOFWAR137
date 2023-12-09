from gameClasses.unitFactory import *
from gameClasses.baseUnit import *
from gameClasses.baseBase import *
from src.CONSTANTS import *
from src.get_ipaddress import *

class GameClass():
    def __init__(self) -> None:
        self.factory:UnitFactory = PrehistoricUnitFactory()
        self.unitNumber = 1
        self.techLevel = 1

    def generateUnitID(self):
        id = '//'.join([str(x) for x in getIPAddressAndPort()])
        id += f'//{self.unitNumber}'
        self.unitNumber += 1
        return id
    
    def get_base(self):
        if self.techLevel == 1:
            base = Cave(0)
            base.rect.bottomleft = (0, GAME_SCREEN_HEIGHT)
            return base

    def train_melee_unit(self):
        unit = self.factory.create_melee_unit()(self.generateUnitID())
        unit.rect.bottomleft = (0, GAME_SCREEN_HEIGHT)
        return unit
    
    def train_ranged_unit(self):
        unit = self.factory.create_ranged_unit()(self.generateUnitID())
        unit.rect.bottomleft = (0, GAME_SCREEN_HEIGHT)
        return unit
    
    def train_tank_unit(self):
        unit = self.factory.create_tank_unit()(self.generateUnitID())
        unit.rect.bottomleft = (0, GAME_SCREEN_HEIGHT)
        return unit