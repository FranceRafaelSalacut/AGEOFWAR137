import pygame
from mainClasses.button import *
from src.CONSTANTS import *
from src.gamescreen import *
from gameClasses.unitFactory import *
from mainClasses.image import *
from gameClasses.rangedUnit import *
from gameClasses.baseUnit import *

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
        TEST_timerB = 0
        hasLost = False
        hasWon = False
        yes = False
        run = True
        all_units = pygame.sprite.Group()
        dead_units = pygame.sprite.Group()
        projectiles = pygame.sprite.Group()
        STATE.initialize()
        base = STATE.get_base()
        STATE.load_images()


        # GAME STUFF
        # music
        pygame.mixer.music.load(MUSIC_GLORIOUS_MORNING)
        pygame.mixer.music.play(loops=-1)

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
            STATE.backGround.draw(screen)
            base.update(screen)
            screen.blit(base.image, base.rect)
            STATE.update_state()

            sorted_sprites = sorted(all_units.sprites(), key=lambda sprite: sprite.rect.bottomleft[1])
            all_units.empty()
            all_units.add(sorted_sprites)

            for entity in all_units:
                if not hasLost and not hasWon:
                    STATE.update_unit_target(entity)
                    entity.update(screen)
                if isinstance(entity, rangedUnit) and entity.state == STATE_ATTACKING:
                    # Call a method that returns some value here
                    if entity.hasShot:
                        projectiles.add(entity.create_projectile())
                if entity.isDead:
                    dead_units.add(entity)
                screen.blit(entity.image, entity.rect)
        
                # remove entity if they get out of the screen
                if entity.rect.left >= GAME_SCREEN_WIDTH + 20 or entity.rect.right <= 0:
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
            for entity in projectiles:
                screen.blit(entity.image, entity.rect)
                for unit in all_units:
                    entity.check_collision(unit)
                entity.check_collision(base)
                
                entity.goTowardsTarget() # Update the movement of the projectiles' rect
                # If bullet leaves screen, kill its sprite
                if (entity.rect.left >= GAME_SCREEN_WIDTH + 20 or entity.rect.right <= 0) or (entity.rect.right <= GAME_SCREEN_WIDTH + 20 or entity.rect.left >= 0):
                    entity.kill()
            for entity in dead_units:
                if entity.killer:
                    STATE.killed_unit(entity)
                    # TODO: pass to specific player this string
                    entity.get_bounty()

                entity.kill()

            if STATE.is_base_dead() and not hasLost:
                hasLost = True
                pygame.mixer.music.stop()
                sf = pygame.mixer.Sound(SOUND_GAME_OVER)
                sf.play()
                time.sleep(2)
                pygame.mixer.music.load(MUSIC_GAME_OVER)
                pygame.mixer.music.play(loops=-1)
                # TODO: SEND SOMETHING TO OTHER PLAYERS THAT THIS PLAYER HAS LOST
            
            if not hasWon and yes: # TODO: CHANGE YES TO SOME FUNCTION THAT DETECTS THAT PLAYER IS THE ONLY ONE LEFT
                hasWon = True
                STATE.show_win_screen()
                pygame.mixer.music.stop()
                sf = pygame.mixer.Sound(SOUND_GAME_OVER_WIN)
                sf.play()
                time.sleep(2)
                pygame.mixer.music.load(MUSIC_GAME_OVER_WIN)
                pygame.mixer.music.play(loops=-1)


            # GUI
            for index, display in enumerate(STATE.display()):
                if display.draw(screen):
                    action = display.getValue()

                    if type(STATE) == GAME_SCREEN:
                        # BUTTONS
                        if not hasLost and not hasWon:
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
                            if action == 'upgrade':
                                upgraded_base = STATE.upgrade()
                                if upgraded_base:
                                    base = upgraded_base

                    if action == "Exit":
                        run = False

                    print(action)

            # TEST

            TEST_timerB += 1
            if TEST_timerB > 800:
                unit = STATE.spawn_enemy('192.168.68.103//35939//2//DinoRider')
                all_units.add(unit)
                TEST_timerB = 0 # reset timer to loop
                # print(enemy_units)

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
