import pygame
from mainClasses.button import *
from src.CONSTANTS import *
from src.gamescreen import *
from gameClasses.unitFactory import *
from src.get_ipaddress import *
from mainClasses.gameclass import *
import sys
import json
import socket
import time

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
        self.running = False
        self.ip_address = getIPAdress()[0]
        self.port = 5555
        self.address = (self.ip_address, self.port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.socket.settimeout(0.0001)
        self.socket.bind(self.address)
        self.startGame()

    def startGame(self):
        STATE = GAME_SCREEN(self.players)
        STATE.addTargets(self.players)
        # pygame setup
        pygame.init()
        screen = pygame.display.set_mode([GAME_SCREEN_WIDTH, GAME_SCREEN_HEIGHT])
        clock = pygame.time.Clock()
        pygame.display.set_caption('TEST') # game/window title

        # loop
        TEST_timer = 0
        run = True
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
                
                if type(entity.movePattern) == Movement_Friendly and entity.rect.left >= GAME_SCREEN_WIDTH:
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
                    print(STATE.get_current_target_to_send())
                    message = entity_id.encode()
                    #self.socket.sendto(message, STATE.get_current_target_to_send()[1], 5555)
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
            try:
                message, address = self.socket.recvfrom(1024)
                unit = STATE.spawn_enemy(message.decode())
                all_units.add(unit)
            except:
                pass

            '''
            # TEST
            TEST_timer += 1
            if TEST_timer > 100:
                unit = STATE.spawn_enemy('192.168.68.103//51546//1//Slingshotter')
                all_units.add(unit)
                TEST_timer = 0 # reset timer to loop
            '''

            """
            TO SPAWN ENEMIES, do:
                unit = STATE.spawn_enemy('U)
                all_units.add(unit)
            """

            # ^^===========================================^^
            # flip() the display to put your work on screen
            pygame.display.flip()
            clock.tick(60)
        
        self.socket.close()
        pygame.quit()

def makeSocket():
    ip_address = getIPAdress()[0]
    port = 5555
    address = (ip_address, port)
    temp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    temp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    temp_socket.settimeout(1)
    temp_socket.bind(address)

    return temp_socket


def getArgs():
    targets = []
    temp_socket = makeSocket()
    print("In here boyoyoyoy")
    if len(sys.argv) > 1:
        temp = sys.argv[1:]
        print(temp)

        temp = ''.join(temp).replace("'","").replace('{', '{"').replace(':','": "').replace(',','", "').replace('}','"}')
        print(json.loads(temp))

        address_list = json.loads(temp)
        for key, value in address_list.items():
            temp_list = (key,value,5555)
            targets.append(temp_list)
            print(f"key: {key}, value: {value}")
        
        print(targets)
        temp = sys.argv[1].encode()
        time.sleep(1)
        while True:
            temp_socket.sendto(temp, ('<broadcast>', 5555))
            message, address = temp_socket.recvfrom(1024)
            if message.decode == "Ress":
                print("Im dying")
                break

        temp_socket.close()

        return targets
    else:
        print("No message passed")
        for x in range(0,5):
            try: 
                message, address = temp_socket.recvfrom(1024)
                print("GGGGG")
                temp_socket.sendto("Ress".encode(), address)
            except:
                print("tried")

        temp_socket.close()
        print(f"{message.decode()}")
    
        #return message.decode()

if __name__ == "__main__":
    '''
    targets = [
        ('GB','192.168.68.103',51546),
        ('Panpan','192.168.68.103',5922),
        ('Johannes','192.168.68.103',3159),
        ('Dustin','192.168.68.103',6490),
        ('Jav','192.168.68.103',8203)
    ]
    '''
    targets = getArgs()
    
    Game(players = targets)





