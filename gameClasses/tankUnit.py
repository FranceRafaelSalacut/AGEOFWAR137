from baseUnit import baseUnit

class tankUnit(baseUnit):
    def __init__(self, id, x, y):
        super().__init__(id, x, y)
    def attack(self):
        pass
class dinoRider(tankUnit):
    def __init__(self, id, x, y):
        super().__init__(id, x, y)
        self.fetchValues('DinoRider')
class Cavalier(tankUnit):
    def __init__(self, id, x, y):
        super().__init__(id, x, y)
        self.fetchValues('Cavalier')
class Tank(tankUnit):
    def __init__(self, id, x, y):
        super().__init__(id, x, y)
        self.fetchValues('Tank')
class Mecha(tankUnit):
    def __init__(self, id, x, y):
        super().__init__(id, x, y)
        self.fetchValues('Mecha')

if __name__ == '__main__':
    test = dinoRider(0,0,0)
    print(test.getListValues())
    test2 = Cavalier(0,0,0)
    print(test2.getListValues())
    test3 = Tank(0,0,0)
    print(test3.getListValues())
    test4 = Mecha(0,0,0)
    print(test4.getListValues())