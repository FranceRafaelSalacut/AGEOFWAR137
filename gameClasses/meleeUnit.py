from baseUnit import baseUnit
import pygame as pg


class meleeUnit(baseUnit):
    def __init__(self, id, x, y):
        super().__init__(id, x, y)
    def attack(self):
        pass

class Caveman(meleeUnit):
    def __init__(self, id, x, y):
        super().__init__(id, x, y)
        self.fetchValues('Caveman')
class Footman(meleeUnit):
    def __init__(self, id, x, y):
        super().__init__(id, x, y)
        self.fetchValues('Footman')
class Soldier(meleeUnit):
    def __init__(self, id, x, y):
        super().__init__(id, x, y)
        self.fetchValues('Soldier')
class Robot(meleeUnit):
    def __init__(self, id, x, y):
        super().__init__(id, x, y)
        self.fetchValues('Robot')


if __name__ == '__main__':
    test = Caveman(0,0,0)
    print(test.getListValues())
    test2 = Footman(0,0,0)
    print(test2.getListValues())
    test3 = Soldier(0,0,0)
    print(test3.getListValues())
    test4 = Robot(0,0,0)
    print(test4.getListValues())