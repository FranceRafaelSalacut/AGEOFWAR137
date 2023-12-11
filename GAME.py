import pygame
from mainClasses.button import *
from src.CONSTANTS import *
from src.gamescreen import *
from gameClasses.unitFactory import *

class Game():
    def __init__(self) -> None:
        self.startGame()

    def startGame(self):
        STATE = GAME_SCREEN()
        # pygame setup
        pygame.init()
        screen = pygame.display.set_mode([GAME_SCREEN_WIDTH, GAME_SCREEN_HEIGHT])
        clock = pygame.time.Clock()
        pygame.display.set_caption('TEST') # game/window title

        # loop
        TEST_timer = 0
        run = True
        all_units = pygame.sprite.Group()
        dead_units = pygame.sprite.Group()
        enemy_units = pygame.sprite.Group()
        friendly_units = pygame.sprite.Group()
        base = STATE.get_base()

        # music
        pygame.mixer.music.load(MUSIC_GLORIOUS_MORNING)
        pygame.mixer.music.play()

        # TODO: get targets from server

        while run:
            # polling for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            # filling the screen with a color to wipe away everything from the last frame
            screen.fill('white')

            # Render game here
            # vv===========================================vv
            if type(STATE) == GAME_SCREEN:
                base.update(screen)
                screen.blit(base.image, base.rect)
                STATE.passiveGain()

            for entity in all_units:
                entity.update(screen)
                if entity.isDead:
                    dead_units.add(entity)
                screen.blit(entity.image, entity.rect)

                # remove entity if they get out of the screen
                if entity.rect.left >= GAME_SCREEN_WIDTH or entity.rect.right <= 0:
                    if type(entity.movePattern) == Movement_Friendly:
                        # TODO: put something here to send entity over to server
                        # current entity IDs are {IP ADDRESS}//{PORT}//{UNIQUE NUMBER}//{UNIT CLASS}
                        # NOTE: entity IDs are the ones to be passed, IDs inside unit classes are similar but do not have Unit Class appended
                        # Ex.
                        #   Entity ID (the one to be passed through network)
                        #       -> 192.168.68.103//51546//1//Slingshotter
                        #   Unit ID
                        #       -> 192.168.68.103//51546//1

                        entity_id = f'{entity.id}//{type(entity).__name__}'
                        print(entity_id)
                    dead_units.add(entity)

            for entity in dead_units:
                if entity.killer:
                    STATE.killed_unit(entity)
                entity.kill()
            # GUI
            for index, display in enumerate(STATE.display()):
                if display.draw(screen):
                    action = display.getValue()

                    if type(STATE) == GAME_SCREEN:
                        # BUTTONS
                        if action == 'change_target':
                            STATE.change_target()
                        if action.startswith('target_'):
                            STATE.selectTarget(action.split('_')[1])
                            STATE.change_target()

                        unit = None
                        if action == 'train_melee_unit':
                            unit = STATE.train_melee_unit()
                        elif action == 'train_ranged_unit':
                            unit = STATE.train_ranged_unit()
                        elif action == 'train_tank_unit':
                            unit = STATE.train_tank_unit()
                        if unit:
                            all_units.add(unit)
                            friendly_units.add(unit)
                            for e in enemy_units:
                                e.addPossibleTarget(unit)
                                unit.addPossibleTarget(e)

                        if action == 'upgrade':
                            base = STATE.upgrade()

                    if action == "Exit":
                        run = False

                    print(action)

            # TEST
            TEST_timer += 1
            if TEST_timer > 200:
                unit = STATE.spawn_enemy('192.168.68.103//51546//1//Slingshotter')
                all_units.add(unit)
                enemy_units.add(unit)
                for e in friendly_units:
                    e.addPossibleTarget(unit)
                    unit.addPossibleTarget(e)
                TEST_timer = 0 # reset timer to loop

            """
            TO SPAWN ENEMIES, do:
                unit = STATE.spawn_enemy('U)
                all_units.add(unit)
            """

            # ^^===========================================^^
            # flip() the display to put your work on screen
            pygame.display.flip()
            clock.tick(60)

        pygame.quit()


if __name__ == "__main__":
    Game()

import sys
import json

def getArgs():
    print("In here boyoyoyoy")
    if len(sys.argv) > 1:
        temp = sys.argv[1:]
        print(temp)

        temp = ''.join(temp).replace("'","").replace('{', '{"').replace(':','": "').replace(',','", "').replace('}','"}')
        print(json.loads(temp))

        address_list = json.loads(temp)
        for key, value in address_list.items():
            print(f"key: {key}, value: {value}")

        print("watatata")
    else:
        print("No message passed")

getArgs()
