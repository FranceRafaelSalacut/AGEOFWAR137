from abc import abstractmethod
from baseModel import baseModel
from gameClassValues import UNITS

class baseUnit(baseModel):
    def __init__(self, id, width = 0, height = 0, x = 0, y = 0):
        super().__init__(id,width, height, x, y)
    def fetchValues(self, unitType : str):
        val = UNITS[unitType]
        self.hp = val["hp"]
        self.mspd = val["mspd"]
        self.aspd = val["aspd"]
        self.dmg = val["dmg"]
        self.bounty = val["bounty"]
        self.exp = val["exp"]
    def getListValues(self):
        return [self.hp, self.mspd, self.aspd, self.dmg, self.bounty, self.exp]

    def move(self):
        pass
    @abstractmethod
    def attack(self):
        pass

if __name__ == "__main__":
    test = baseUnit(1)
    test.fetchValues('Caveman')

    print(test.hp)