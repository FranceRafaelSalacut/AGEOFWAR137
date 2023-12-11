from .baseUnit import baseUnit
from .projectile import Projectile

class rangedUnit(baseUnit):
    def __init__(self, id, x, y):
        super().__init__(id, x=x, y=y)
    def attack(self):
        self.attackTimer += self.aspd
        if self.attackTimer > 500:
            self.create_projectile()
            self.attackTarget.curhp -= self.dmg
            self.attackTimer = 0
            print(f'{self.id} attacked {self.attackTarget.id} ({self.attackTarget.curhp})')
            if self.attackTarget.curhp <= 0:
                self.attackTarget.killer = self
                self.attackTarget = None
    def create_projectile(self):
        print("HERES A STONE")
        return Projectile(id = 0, unit = self)
class Slingshotter(rangedUnit):
    def __init__(self, id, x=0, y=0):
        super().__init__(id, x=x, y=y)
        self.fetchValues('Slingshotter')
class Archer(rangedUnit):
    def __init__(self, id, x=0, y=0):
        super().__init__(id, x=x, y=y)
        self.fetchValues('Archer')
class Sniper(rangedUnit):
    def __init__(self, id, x=0, y=0):
        super().__init__(id, x=x, y=y)
        self.fetchValues('Sniper')
class Stormtrooper(rangedUnit):
    def __init__(self, id, x=0, y=0):
        super().__init__(id, x=x, y=y)
        self.fetchValues('Stormtrooper')

if __name__ == '__main__':
    test = Slingshotter(0,0,0)
    print(test.getListValues())
    test2 = Archer(0,0,0)
    print(test2.getListValues())
    test3 = Sniper(0,0,0)
    print(test3.getListValues())
    test4 = Stormtrooper(0,0,0)
    print(test4.getListValues())