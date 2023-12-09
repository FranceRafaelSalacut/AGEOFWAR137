from abc import abstractmethod
from baseModel import baseModel
from gameClassValues import UNITS

class baseUnit(baseModel):
    def __init__(self, id, x = 0, y = 0, width = 0, height = 0):
        super().__init__(id, x, y, width, height)
    def getValues(self, unitType : str):
        val = UNITS[unitType]
        self.hp = val["hp"]
        self.mspd = val["mspd"]
        self.aspd = val["aspd"]
        self.dmg = val["dmg"]
        self.bounty = val["bounty"]
        self.exp = val["exp"]

    @abstractmethod
    def move(self):
        pass
    @abstractmethod
    def attack(self):
        pass

if __name__ == "__main__":
    test = baseUnit(1)
    test.getValues('Caveman')

    print(test.hp)