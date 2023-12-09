from gameClasses.unitFactory import *
from gameClasses.baseUnit import *
from src.CONSTANTS import *
from src.get_ipaddress import *
class GameClass():
    def __init__(self) -> None:
        self.factory:UnitFactory = PrehistoricUnitFactory()
        self.unitNumber = 0
    def generateUnitID(self):
        id = '//'.join([str(x) for x in getIPAddressAndPort()])
        id += f'//{self.unitNumber}'
        self.unitNumber += 1
        return id

    def setUnitFactory(self, factoryClass):
        self.factory = factoryClass()

    def train_unit(self):
        unit = self.factory.create_melee_unit()(self.generateUnitID())
        unit.rect.center = (0, GAME_SCREEN_HEIGHT - unit.rect.height)
        return unit