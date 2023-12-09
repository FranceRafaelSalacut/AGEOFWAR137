from abc import ABC, abstractmethod
from gameClasses.baseUnit import baseUnit
from gameClasses.meleeUnit import MeleeUnit, Caveman, Footman, Soldier, Robot
from gameClasses.rangedUnit import Slingshotter, Archer, Sniper, Stormtrooper
from gameClasses.tankUnit import dinoRider, Cavalier, Tank, Mecha
import pygame as pg

from CONSTANTS import *

# TODO: Find a better way of assigning the group/s to the units (Not sure, but I think this should not be one of the factories' responsibilities(?))

class UnitFactory(ABC):

    @abstractmethod
    def create_melee_unit(self):
        pass

    @abstractmethod
    def create_ranged_unit(self):
        pass

    @abstractmethod
    def create_tank_unit(self):
        pass

class PrehistoricUnitFactory(pg.sprite.Sprite, UnitFactory):
    def __init__(self, groups, screen):
        super().__init__()
        self.x = 0
        self.y = SCREEN_HEIGHT
        self.hp = 0
        self.groups = groups
        self.screen = screen

    def create_melee_unit(self):
        Caveman(1, (self.x + 20), (self.y - 10), 100, 100, 1, self.groups, self.screen)
        
    def create_ranged_unit(self) -> Slingshotter:
        return Slingshotter(1, (self.x + 20), (self.y - 10), 100, 100, 1, self.groups, self.screen)

    def create_tank_unit(self) -> dinoRider:
        return dinoRider() 

class MedievalUnitFactory(UnitFactory):

    def create_melee_unit(self) -> Footman:
        Footman(1, (self.x + 20), (self.y - 10), 100, 100, 1, self.groups)
    
    def create_ranged_unit(self) -> Archer:
        return Archer()

    def create_tank_unit(self) -> Cavalier:
        return Cavalier()

class ModernUnitFactory(UnitFactory):
    
    def create_melee_unit(self) -> Soldier:
        Soldier(1, (self.x + 20), (self.y - 10), 100, 100, 1, self.groups)
    
    def create_ranged_unit(self) -> Sniper:
        return Sniper()

    def create_tank_unit(self) -> Tank:
        return Tank()

class ScifiUnitFactory(UnitFactory):

    def create_melee_unit(self) -> Robot:
        Robot(1, (self.x + 20), (self.y - 10), 100, 100, 1, self.groups)
    
    def create_ranged_unit(self) -> Stormtrooper:
        return Stormtrooper()

    def create_tank_unit(self) -> Mecha:
        return Mecha()

 
