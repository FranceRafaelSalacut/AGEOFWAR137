from abc import ABC, abstractmethod

class baseUnit(ABC):
    @abstractmethod
    def move(self):
        pass
    @abstractmethod
    def attack(self):
        pass
    @abstractmethod
    def die(self):
        pass