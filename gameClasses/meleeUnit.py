from gameClasses.baseUnit import baseUnit
import pygame as pg


class meleeUnit(baseUnit):
    def __init__(self, id, x, y, width, height):
        super().__init__(id, x, y, width, height)
    def move(self):
        pass
    def attack(self):
        pass
    def die(self):
        pass

class Caveman(meleeUnit):
    def __init__(self, id, x, y, width, height):
        super().__init__(id, x, y, width, height)
        self.getValues('Caveman')
class Footman(meleeUnit):
    def __init__(self, id, x, y, width, height):
        super().__init__(id, x, y, width, height)
        self.getValues('Footman')
class Soldier(meleeUnit):
    def __init__(self, id, x, y, width, height):
        super().__init__(id, x, y, width, height)
        self.getValues('Soldier')
class Robot(meleeUnit):
    def __init__(self, id, x, y, width, height):
        super().__init__(id, x, y, width, height)
        self.getValues('Robot')