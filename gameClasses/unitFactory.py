from abc import ABC, abstractmethod
from meleeUnit import Caveman, Footman, Soldier, Robot
from rangedUnit import Slingshotter, Archer, Sniper, Stormtrooper
from tankUnit import dinoRider, Cavalier, Tank, Mecha


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

class PrehistoricUnitFactory(UnitFactory):

    def create_melee_unit(self) -> Caveman:
        return Caveman()
    
    def create_ranged_unit(self) -> Slingshotter:
        return Slingshotter()

    def create_tank_unit(self) -> dinoRider:
        return dinoRider() 

class MedievalUnitFactory(UnitFactory):

    def create_melee_unit(self) -> Footman:
        return Footman()
    
    def create_ranged_unit(self) -> Archer:
        return Archer()

    def create_tank_unit(self) -> Cavalier:
        return Cavalier()

class ModernUnitFactory(UnitFactory):
    
    def create_melee_unit(self) -> Soldier:
        return Soldier()
    
    def create_ranged_unit(self) -> Sniper:
        return Sniper()

    def create_tank_unit(self) -> Tank:
        return Tank()

class ScifiUnitFactory(UnitFactory):

    def create_melee_unit(self) -> Robot:
        return Robot()
    
    def create_ranged_unit(self) -> Stormtrooper:
        return Stormtrooper()

    def create_tank_unit(self) -> Mecha:
        return Mecha()

 
