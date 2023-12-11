from gameClasses.unitFactory import *
from gameClasses.baseUnit import *
from gameClasses.baseBase import *
from src.CONSTANTS import *
from src.get_ipaddress import *
import math

# TODO: get targets from server
'''
targets = [
    ('GB','192.168.68.103',51546),
    ('Panpan','192.168.68.103',5922),
    ('Johannes','192.168.68.103',3159),
    ('Dustin','192.168.68.103',6490),
    ('Jav','192.168.68.103',8203)
]
'''

targets = [('TEST', 'dfsdf', 5555), ('T123123', 'TE12312SET', 5555)]
NONE = ('NONE','0',0)

class GameClass():
    def __init__(self, players) -> None:
        self.factory:UnitFactory = PrehistoricUnitFactory()
        self.unitNumber = 1
        self.techLevel = 1
        self.gold = 0
        self.exp = 0
        self.currentTarget = NONE
        self.players = players
        self.address = ('192.168.68.103',51546) # TODO: set this to client address
        self.fetchTargets()

    def addTargets(self, players: list):
        self.targets = players
    def fetchTargets(self):
        self.targets = self.players
        print(targets)
        print(self.targets)
    def selectTarget(self, target):
        for t in self.players:
            if target in t:
                self.currentTarget = t

    def generateUnitID(self):
        id = '//'.join([str(x) for x in self.address])
        id += f'//{self.unitNumber}'
        self.unitNumber += 1
        return id
    
    def get_base(self):
        base = Cave(0)
        print(self.techLevel)
        if self.techLevel == 2:
            base = Castle(0)
        if self.techLevel == 3:
            base = Camp(0)
        if self.techLevel == 4:
            base = Citadel(0)
        base.rect.bottomleft = (0, GAME_SCREEN_HEIGHT)
        return base
        
    def get_exp(self):
        return math.floor(self.exp)
    def get_gold(self):
        return math.floor(self.gold)
    def getTargets(self):
        return self.targets
    def get_currentTarget(self):
        return self.currentTarget[0]
    def get_target_to_send(self):
        return self.currentTarget

    def train_melee_unit(self):
        unit = self.factory.create_melee_unit()(self.generateUnitID())
        return self.train_unit(unit)
    
    def train_ranged_unit(self):
        unit = self.factory.create_ranged_unit()(self.generateUnitID())
        return self.train_unit(unit)
    
    def train_tank_unit(self):
        unit = self.factory.create_tank_unit()(self.generateUnitID())
        return self.train_unit(unit)
    
    def spawn_enemy_unit(self, ID:str):
        # NOTE: USE ENTITY ID, NOT UNIT ID; SEE GAME.py's StartGame function
        # ex. 192.168.68.103//51546//1//Slingshotter
        ID = ID.split('//')
        UnitID = '//'.join(ID[:-1])
        UnitType : type = self.get_unit_type(ID[-1])
        unit : baseUnit = UnitType(UnitID)
        unit.rect.bottomleft = (GAME_SCREEN_WIDTH, GAME_SCREEN_HEIGHT)
        unit.setMovement(Movement_Enemy(unit))
        print(f'spawning {unit.id}//{unit.__class__.__name__} at {unit.rect.center}')
        return unit
    
    @staticmethod
    def get_unit_type(unitType:str) -> type:
        types = {
            "Caveman" : Caveman,
            "Footman" : Footman,
            "Soldier" : Soldier,
            "Robot" : Robot,
            "Slingshotter" : Slingshotter,
            "Archer" : Archer,
            "Sniper" : Sniper,
            "Stormtrooper" : Stormtrooper,
            "DinoRider" : DinoRider,
            "Cavalier" : Cavalier,
            "Tank" : Tank,
            "Mecha" : Mecha,
        }
        if unitType in types:
            return types[unitType]
        else:
            return None


    def train_unit(self, unit:baseUnit):
        if self.currentTarget != NONE and self.get_gold() >= unit.cost:
            self.gold -= unit.cost
            unit.rect.bottomleft = (0, GAME_SCREEN_HEIGHT)
            unit.setMovement(Movement_Friendly(unit))
            return unit
        else:
            unit.kill()
            return None

    
    def upgrade(self):
        if self.get_exp() >= self.get_base().expCost:
            self.techLevel += 1
        return self.get_base()

    def passiveGain(self):
        self.gold += (1 / 60)