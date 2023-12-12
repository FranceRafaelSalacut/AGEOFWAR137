from gameClasses.unitFactory import *
from gameClasses.baseUnit import *
from gameClasses.baseBase import *
from mainClasses.image import Image
from src.CONSTANTS import *
from src.get_ipaddress import *
import random
import math

# TODO: get targets from server
targets = [
    ('GB','192.168.68.103',51546),
    ('Panpan','192.168.68.103',5922),
    ('Johannes','192.168.68.103',3159),
    ('Dustin','192.168.68.103',6490),
    ('Jav','192.168.68.103',8203)
]
NONE = ('NONE','0',0)

class GameClass():
    def __init__(self) -> None:
        self.factory:UnitFactory = PrehistoricUnitFactory()
        self.unitNumber = 1
        self.techLevel = 1
        self.gold = 0
        self.exp = 9999
        self.currentTarget = NONE
        self.address = ('192.168.68.103',9999) # TODO: set this to client address
        self.base = None
        self.fetchTargets()

    def fetchTargets(self):
        self.targets = targets
        self.unitLists : list[tuple[str,pg.sprite.Group]] = [('//'.join([str(z) for z in x[1:]]),pg.sprite.Group()) for x in self.targets]
        self.unitLists.append((self.getStringAddress(),pg.sprite.Group()))
        print(self.unitLists)

    def initialize(self):
        self.base = self.get_base()

    def selectTarget(self, target):
        for t in targets:
            if target in t:
                self.currentTarget = t

    def getStringAddress(self):
        return '//'.join([str(x) for x in self.address])

    def generateUnitID(self):
        id = self.getStringAddress()
        id += f'//{self.unitNumber}'
        self.unitNumber += 1
        return id
    
    def get_base(self):
        base = Cave(self.generateUnitID())
        self.factory = PrehistoricUnitFactory()
        print(self.techLevel)
        if self.techLevel == 2:
            base = Castle(self.generateUnitID())
            self.factory = MedievalUnitFactory()
        if self.techLevel == 3:
            base = Camp(self.generateUnitID())
            self.factory = ModernUnitFactory()
        if self.techLevel == 4:
            base = Citadel(self.generateUnitID())
            self.factory = ScifiUnitFactory()
        base.rect.bottomleft = (0, GAME_SCREEN_HEIGHT-50)
        return base
    def get_required_upgrade_exp(self):
        if self.base:
            return self.base.expCost
        else:
            return 0
        
    def get_exp(self):
        return math.floor(self.exp)
    def get_gold(self):
        return math.floor(self.gold)
    def getTargets(self):
        return self.targets
    def get_currentTarget(self):
        return self.currentTarget[0]
    def get_unit_costs(self):
        a = str(self.factory.create_melee_unit()('0').cost)
        b = str(self.factory.create_ranged_unit()('0').cost)
        c = str(self.factory.create_tank_unit()('0').cost)
        return (a,b,c)


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
        unit.rect.bottomleft = (GAME_SCREEN_WIDTH, GAME_SCREEN_HEIGHT - random.randint(5,15)*6)
        unit.setMovement(Movement_Enemy(unit))
        unit.addPossibleTarget(self.base)
        self.set_team(unit)
        
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

    def train_unit(self, unit:baseUnit):
        if self.currentTarget != NONE and self.get_gold() >= unit.cost:
            self.gold -= unit.cost
            unit.rect.bottomleft = (self.base.rect.centerx, GAME_SCREEN_HEIGHT - random.randint(5,15)*6)
            unit.setMovement(Movement_Friendly(unit))
            self.set_team(unit)
            return unit
        else:
            unit.kill()
            return None

    def set_team(self, unit:baseUnit):
        for g in self.unitLists:
            if unit.owner == g[0]:
                g[1].add(unit)
            else:
                for e in g[1]:
                    unit.addPossibleTarget(e)
                    e.addPossibleTarget(unit)
    
    def set_enemies_target(self, target:baseModel):
        print(target.owner)
        for g in self.unitLists:
            if target.owner != g[0]:
                for e in g[1]:
                    e.addPossibleTarget(target)
    def remove_enemies_target(self, target:baseModel):
        print(target.owner)
        for g in self.unitLists:
            if target.owner != g[0]:
                for e in g[1]:
                    e.removePossibleTarget(target)

    def killed_unit(self, unit:baseUnit):
        if unit.killer.owner == self.getStringAddress():
            self.exp += unit.exp
            self.gold += unit.bounty
    
    def upgrade(self):
        if self.isUpgradeable():
            self.exp -= self.base.expCost
            if self.techLevel < 4:
                self.techLevel += 1
            base = self.get_base()
            self.remove_enemies_target(self.base)
            self.base = base
            self.set_enemies_target(base)
            return base
        return None
    
    def isUpgradeable(self):
        return self.get_exp() >= self.base.expCost
    def get_current_upgrade_bg(self):
        if self.techLevel == 1:
            return Image('graphics/backgrounds/background_prehistoric.png',0,0,GAME_SCREEN_WIDTH,GAME_SCREEN_HEIGHT)
        if self.techLevel == 2:
            return Image('graphics/backgrounds/background_medieval.png',0,0,GAME_SCREEN_WIDTH,GAME_SCREEN_HEIGHT)
        if self.techLevel == 3:
            return Image('graphics/backgrounds/background_modern.png',0,0,GAME_SCREEN_WIDTH,GAME_SCREEN_HEIGHT)
        if self.techLevel == 4:
            return Image('graphics/backgrounds/background_scifi.png',0,0,GAME_SCREEN_WIDTH,GAME_SCREEN_HEIGHT)

    def passiveGain(self):
        self.gold += (1 / 60)

    def update_unit_targets(self, unit:baseUnit):
        self.set_team(unit)