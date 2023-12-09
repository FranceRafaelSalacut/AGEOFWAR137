from abc import ABC, abstractmethod
from .meleeUnit import meleeUnit, Caveman, Footman, Soldier, Robot
from .rangedUnit import rangedUnit, Slingshotter, Archer, Sniper, Stormtrooper
from .tankUnit import tankUnit, dinoRider, Cavalier, Tank, Mecha


class UnitFactory(ABC):

    @abstractmethod
    def create_melee_unit(self) -> type:
        pass

    @abstractmethod
    def create_ranged_unit(self) -> type:
        pass

    @abstractmethod
    def create_tank_unit(self) -> type:
        pass

class PrehistoricUnitFactory(UnitFactory):

    def create_melee_unit(self):
        return Caveman
    
    def create_ranged_unit(self):
        return Slingshotter

    def create_tank_unit(self):
        return dinoRider

class MedievalUnitFactory(UnitFactory):

    def create_melee_unit(self):
        return Footman
    
    def create_ranged_unit(self):
        return Archer

    def create_tank_unit(self):
        return Cavalier

class ModernUnitFactory(UnitFactory):
    
    def create_melee_unit(self):
        return Soldier
    
    def create_ranged_unit(self):
        return Sniper

    def create_tank_unit(self):
        return Tank

class ScifiUnitFactory(UnitFactory):

    def create_melee_unit(self):
        return Robot
    
    def create_ranged_unit(self):
        return Stormtrooper

    def create_tank_unit(self):
        return Mecha
