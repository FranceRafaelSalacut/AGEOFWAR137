import pygame
from mainClasses.button import *
from src.CONSTANTS import *
from src.gamescreen import *
from gameClasses.unitFactory import *

class Game():
    def __init__(self, players: list) -> None:
        """
        MAKE SURE THAT THE PLAYERS LIST FOLLOWS
            (NAME, IP ADDRESS, PORT)
        
        NOTE: Name can just be randomly generated if we dont have time
        
        example:
        players = [
            ('GB','192.168.68.103',51546),
            ('Panpan','192.168.68.103',5922),
            ('Johannes','192.168.68.103',3159),
            ('Dustin','192.168.68.103',6490),
            ('Jav','192.168.68.103',8203)
        ]
        """
        self.players = players
        self.startGame()

    def startGame(self):
        STATE = GAME_SCREEN()
        STATE.addTargets(self.players)
        # pygame setup
        pygame.init()
        screen = pygame.display.set_mode([GAME_SCREEN_WIDTH, GAME_SCREEN_HEIGHT])
        clock = pygame.time.Clock()
        pygame.display.set_caption('TEST') # game/window title

        # loop
        dt = 0 # deltaTime
        run = True
        screen_updated = False
        all_units = pygame.sprite.Group()
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
                screen.blit(base.image, base.rect)
                STATE.passiveGain()

            for entity in all_units:
                entity.move()
                screen.blit(entity.image, entity.rect)
                
                if entity.rect.left >= GAME_SCREEN_WIDTH:
                    # TODO: put something here to send entity over to server
                    # current IDs are {IP ADDRESS}//{PORT}//{UNIQUE NUMBER}//{UNIT CLASS}
                    # Ex. 192.168.68.103//51546//1//Slingshotter
                    entity_id = f'{entity.id}//{type(entity).__name__}'
                    print(entity_id)
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

                        if action == 'upgrade':
                            base = STATE.upgrade()

                    if action == "Exit":
                        run = False

                    print(action)

            # ^^===========================================^^
            # flip() the display to put your work on screen
            pygame.display.flip()

            dt = clock.tick(60) / 1000 # limits FPS to 60

        pygame.quit()


if __name__ == "__main__":
    targets = [
        ('GB','192.168.68.103',51546),
        ('Panpan','192.168.68.103',5922),
        ('Johannes','192.168.68.103',3159),
        ('Dustin','192.168.68.103',6490),
        ('Jav','192.168.68.103',8203)
    ]
    Game(playimport sys
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
