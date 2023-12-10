from .baseUnit import baseUnit

class tankUnit(baseUnit):
    def __init__(self, id, x, y):
        super().__init__(id, x=x, y=y)
class DinoRider(tankUnit):
    def __init__(self, id, x=0, y=0):
        super().__init__(id, x=x, y=y)
        self.fetchValues('DinoRider')
class Cavalier(tankUnit):
    def __init__(self, id, x=0, y=0):
        super().__init__(id, x=x, y=y)
        self.fetchValues('Cavalier')
class Tank(tankUnit):
    def __init__(self, id, x=0, y=0):
        super().__init__(id, x=x, y=y)
        self.fetchValues('Tank')
class Mecha(tankUnit):
    def __init__(self, id, x=0, y=0):
        super().__init__(id, x=x, y=y)
        self.fetchValues('Mecha')

if __name__ == '__main__':
    test = DinoRider(0,0,0)
    print(test.getListValues())
    test2 = Cavalier(0,0,0)
    print(test2.getListValues())
    test3 = Tank(0,0,0)
    print(test3.getListValues())
    test4 = Mecha(0,0,0)
    print(test4.getListValues())