import pygame
import threading
import time
from src.CONSTANTS import *
from mainClasses.screen import *
from mainClasses.button import *
from mainClasses.text import *
from mainClasses.gameclass import *
from mainClasses.image import Image
pygame.init


# Initializing GUI
Background = Image('graphics/backgrounds/background_prehistoric.png',0,0,GAME_SCREEN_WIDTH,GAME_SCREEN_HEIGHT)
Player_board = Image('graphics/gui/GUI_player_board.png', GAME_SCREEN_WIDTH - 300, 0, 400, 120)
Button_generic_0 = Image('graphics/gui/Button.png', 0, 0, 1, 1)
Button_generic_1 = Image('graphics/gui/Button.png', 0, 0, 1, 1)
Button_generic_2 = Image('graphics/gui/Button.png', 0, 0, 1, 1)
Button_upgrade_icon = Image('graphics/gui/Button_upgrade.png', 0, 0, 1, 1)


Button_trainTankUnit = Button(Light_Grey, GAME_SCREEN_WIDTH - 75, 30, 50, 50, 15, value = "train_tank_unit", text = "Tank", image= Button_generic_0)
Button_trainRangeUnit = Button(Light_Grey, Button_trainTankUnit.rect.left - 75, 30, 50, 50, 15, value = "train_ranged_unit", text = "Ranged", image = Button_generic_1)
Button_trainMeleeUnit = Button(Light_Grey, Button_trainRangeUnit.rect.left - 75, 30, 50, 50, 15, value = "train_melee_unit", text = "Melee", image = Button_generic_2)
Button_upgrade = Button(Light_Grey, 20 , 10, 80, 80, 60, value = "upgrade", image = Button_upgrade_icon)
Button_change = Button(Light_Grey, Player_board.rect.left - 300, 30, 100, 30, 20, text = "CHANGE", value = "change_target")

Display_Text = Text("created by the boys", GAME_SCREEN_WIDTH - 30, GAME_SCREEN_HEIGHT - 10, 20)
GUI_gold_count = Image('graphics/gui/Gold_count.png', Button_upgrade.rect.right, 15, 110, 34)
GUI_exp_count = Image('graphics/gui/Exp_count.png', Button_upgrade.rect.right,GUI_gold_count.rect.bottom, 110, 34)
Text_gold = Text("GOLD: 99999",0, GUI_gold_count.rect.top + 20, 20, 'text_gold')
Text_gold.rect.left = (Button_upgrade.rect.right + 35)
Text_experience = Text("EXP: 99999",0, Text_gold.rect.bottom + 20, 20, 'text_exp')
Text_experience.rect.left = (Button_upgrade.rect.right + 35)
Text_currentTarget = Text("Current Target: NULL", Button_change.rect.left - 100, Button_change.rect.centery, 15)
Text_currentTarget_Warning = Text("Warning: Cannot train units until target is set", 0, Button_change.rect.centery + 20, 15, color=(255,0,0))
Text_currentTarget_Warning.rect.left = Text_currentTarget.rect.left

Text_trainTankUnit_gold = Text("GOLD", Button_trainTankUnit.rect.centerx + 15, Button_trainTankUnit.rect.bottom + 10, 20, color=(255,255,0))
Gold_icon_tank = Image('graphics/gold_icon.png',Text_trainTankUnit_gold.rect.centerx - 5,Text_trainTankUnit_gold.rect.centery-5,10,12)
Text_trainRangeUnit_gold = Text("GOLD", Button_trainRangeUnit.rect.centerx + 15, Button_trainRangeUnit.rect.bottom + 10, 20, color=(255,255,0))
Gold_icon_range = Image('graphics/gold_icon.png',Text_trainRangeUnit_gold.rect.centerx - 5,Text_trainRangeUnit_gold.rect.centery-5,10,12)
Text_trainMeleeUnit_gold = Text("GOLD", Button_trainMeleeUnit.rect.centerx + 15, Button_trainMeleeUnit.rect.bottom + 10, 20, color=(255,255,0))
Gold_icon_melee = Image('graphics/gold_icon.png',Text_trainMeleeUnit_gold.rect.centerx - 5,Text_trainMeleeUnit_gold.rect.centery-5,10,12)
Text_upgrade_exp = Text("EXP", Button_upgrade.rect.centerx, Button_upgrade.rect.bottom + 20, 30)

class GAME_SCREEN():
    def __init__(self) -> None:
        self._game = GameClass()
        self.images = [
            Background,
            Player_board,
            Button_generic_0,
            Button_generic_1,
            Button_generic_2,
            Gold_icon_tank,
            Gold_icon_range,
            Gold_icon_melee,
            GUI_gold_count,
            GUI_exp_count,
            ]
        self.buttons = [
            Button_trainMeleeUnit,
            Button_trainRangeUnit,
            Button_trainTankUnit,
            Button_upgrade,
            Button_change,
        ]
        self.backGround = Background
        self.to_display = [
            Player_board,
            Display_Text,
            GUI_gold_count,
            GUI_exp_count,
            Text_gold,
            Text_experience,
            Text_currentTarget,
            Button_trainMeleeUnit,
            Text_trainMeleeUnit_gold,
            Button_trainRangeUnit,
            Text_trainRangeUnit_gold,
            Button_trainTankUnit,
            Text_trainTankUnit_gold,
            Button_upgrade,
            Button_change,
            Text_upgrade_exp,
            Gold_icon_tank,
            Gold_icon_range,
            Gold_icon_melee,
            Text_currentTarget_Warning,
        ]

        self.dropDownTargets : list[Button] = []
        self.get_targets()

    def get_targets(self):
        for index, target in enumerate(self._game.getTargets()):
            button = Button(Light_Grey, Button_change.rect.left, Button_change.rect.top + (30 * (index + 1)), 100, 30, 20, value = f"target_{target[0]}", show = False, text = f"{target[0]}")
            self.to_display.append(button)
            self.dropDownTargets.append(button)
    def selectTarget(self, target):
        Text_currentTarget_Warning.show = False
        self._game.selectTarget(target)
    def initialize(self):
        self.get_unit_costs()
    def load_images(self):
        for i in self.images:
            i.load_image()
        for i in self.buttons:
            i.load_image()

    def get_base(self):
        base = self._game.get_base()
        return base
    def get_exp(self):
        return self._game.get_exp()
    def get_currentTarget(self):
        return self._game.get_currentTarget()
    def get_unit_costs(self):
        costs = self._game.get_unit_costs()
        Text_upgrade_exp.changeText(str(self._game.get_required_upgrade_exp()))
        Text_trainMeleeUnit_gold.changeText(costs[0])
        Text_trainRangeUnit_gold.changeText(costs[1])
        Text_trainTankUnit_gold.changeText(costs[2])
    
    def train_melee_unit(self):
        return self._game.train_melee_unit()
    def train_ranged_unit(self):
        return self._game.train_ranged_unit()
    def train_tank_unit(self):
        return self._game.train_tank_unit()
    def upgrade(self):
        u = self._game.upgrade()
        self.get_unit_costs()
        self.get_bg()
        return u
    def get_bg(self):
        self.backGround = self._game.get_current_upgrade_bg()
        self.backGround.load_image()
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
        exp_text = f'{str(self._game.get_exp())}'
        gold_text = f'{str(self._game.get_gold())}'
        target_text = f'Current Target: {str(self._game.get_currentTarget())}'
        Text_experience.changeText(exp_text)
        Text_gold.changeText(gold_text)
        Text_currentTarget.changeText(target_text)

    def display(self):
        self.update_texts()
        return self.to_display