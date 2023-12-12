import pygame
import threading
import time
from src.CONSTANTS import *
from mainClasses.screen import *
from mainClasses.button import *
from mainClasses.text import *
from mainClasses.gameclass import *
pygame.init


# Initializing Buttons
# parameters are text, color, pos_x, pos_y, width, height, font size, value, show

Button_trainTankUnit = Button("Tank", Light_Grey, GAME_SCREEN_WIDTH - 75, 50, 50, 50, 20, value = "train_tank_unit")
Button_trainRangeUnit = Button("Ranged", Light_Grey, Button_trainTankUnit.rect.left - 75, 50, 50, 50, 20, value = "train_ranged_unit")
Button_trainMeleeUnit = Button("Melee", Light_Grey, Button_trainRangeUnit.rect.left - 75, 50, 50, 50, 20, value = "train_melee_unit")
Button_upgrade = Button("Upgrade", Light_Grey, Button_trainMeleeUnit.rect.left - 120, 50, 100, 50, 30, value = "upgrade")
Button_change = Button("CHANGE", Light_Grey, Button_upgrade.rect.left - 300, 30, 100, 30, 20, value = "change_target")

# parameters are text, center x, center y, Fontsize, value
Display_Text = Text("test", GAME_SCREEN_WIDTH - 30, GAME_SCREEN_HEIGHT - 10, 20)
Text_train = Text("Train",Button_trainMeleeUnit.rect.left, 20, 30)
Text_gold = Text("GOLD: 99999",Button_upgrade.rect.left - 100, Button_upgrade.rect.top, 20, 'text_gold')
Text_experience = Text("EXP: 99999",Text_gold.rect.centerx, Text_gold.rect.bottom + 20, 20, 'text_exp')
Text_currentTarget = Text("Current Target: NULL", Button_change.rect.left - 100, Button_change.rect.centery, 15)

Button_trainTankUnit_gold = Text("GOLD", Button_trainTankUnit.rect.centerx, Button_trainTankUnit.rect.bottom - 15, 10)
Button_trainRangeUnit_gold = Text("GOLD", Button_trainRangeUnit.rect.centerx, Button_trainRangeUnit.rect.bottom - 15, 10)
Button_trainMeleeUnit_gold = Text("GOLD", Button_trainMeleeUnit.rect.centerx, Button_trainMeleeUnit.rect.bottom - 15, 10)
Button_upgrade_exp = Text("EXP", Button_upgrade.rect.centerx, Button_upgrade.rect.bottom - 10, 10)

class GAME_SCREEN():
    def __init__(self) -> None:
        self._game = GameClass()
        self.to_display = [
            Display_Text,
            Text_train,
            Text_gold,
            Text_experience,
            Text_currentTarget,
            Button_trainMeleeUnit,
            Button_trainMeleeUnit_gold,
            Button_trainRangeUnit,
            Button_trainRangeUnit_gold,
            Button_trainTankUnit,
            Button_trainTankUnit_gold,
            Button_upgrade,
            Button_change,
            Button_upgrade_exp
        ]
        self.dropDownTargets : list[Button] = []
        self.get_targets()
        # self.initialize()

    def get_targets(self):
        for index, target in enumerate(self._game.getTargets()):
            button = Button(f"{target[0]}", Light_Grey, Button_change.rect.left, Button_change.rect.top + (30 * (index + 1)), 100, 30, 20, value = f"target_{target[0]}", show = False)
            self.to_display.append(button)
            self.dropDownTargets.append(button)
    def selectTarget(self, target):
        self._game.selectTarget(target)
    def initialize(self):
        self.get_unit_costs()


    def get_base(self):
        base = self._game.get_base()
        # Button_upgrade_exp.changeText(str(base.expCost))
        return base
    def get_exp(self):
        return self._game.get_exp()
    def get_currentTarget(self):
        return self._game.get_currentTarget()
    def get_unit_costs(self):
        costs = self._game.get_unit_costs()
        Button_trainMeleeUnit_gold.changeText(costs[0])
        Button_trainRangeUnit_gold.changeText(costs[1])
        Button_trainTankUnit_gold.changeText(costs[2])
    
    def train_melee_unit(self):
        return self._game.train_melee_unit()
    def train_ranged_unit(self):
        return self._game.train_ranged_unit()
    def train_tank_unit(self):
        return self._game.train_tank_unit()
    def upgrade(self):
        u = self._game.upgrade()
        self.get_unit_costs()
        return u
    def get_bg(self):
        return self._game.get_current_upgrade_bg()
    def change_target(self):
        for button in self.dropDownTargets:
            button.show = not button.show

    def killed_unit(self, unit:baseModel):
        self._game.killed_unit(unit)

    
    def update_state(self):
        self._game.passiveGain()
    def earn_bounty(self, bounty, exp):
        self._game.gold += bounty
        self._game.exp += exp
    def update_unit_target(self, unit:baseModel):
        self._game.update_unit_targets(unit)
    def spawn_enemy(self, ID:str):
        return self._game.spawn_enemy_unit(ID)
    
    def update_texts(self):
        exp_text = f'EXP: {str(self._game.get_exp())}'
        gold_text = f'GOLD: {str(self._game.get_gold())}'
        target_text = f'Current Target: {str(self._game.get_currentTarget())}'
        Text_experience.changeText(exp_text)
        Text_gold.changeText(gold_text)
        Text_currentTarget.changeText(target_text)

    def display(self):
        self.update_texts()
        return self.to_display