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
        # pygame setup
        pygame.init()
        screen = pygame.display.set_mode([GAME_SCREEN_WIDTH, GAME_SCREEN_HEIGHT])
        clock = pygame.time.Clock()
        pygame.display.set_caption('TEST') # game/window title

        # loop
        TEST_timer = 0
        TEST_timerB = 0
        run = True
        all_units = pygame.sprite.Group()
        dead_units = pygame.sprite.Group()
        projectiles = pygame.sprite.Group()
        base = STATE.get_base()

        # music
        #pygame.mixer.music.load(MUSIC_GLORIOUS_MORNING)
        #pygame.mixer.music.play()

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
                STATE.update_state()

            for entity in all_units:
                STATE.update_unit_target(entity)
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
                        #print(entity_id)
                        #print(STATE.get_current_target_to_send())
                        message = entity_id.encode()
                        self.socket.sendto(message, (STATE.get_current_target_to_send()[1], 5555))
                        #print(STATE.get_current_target_to_send()[1])
                    dead_units.add(entity)

            for entity in dead_units:
                if entity.killer:
                    STATE.killed_unit(entity)
                    # TODO: pass to specific player this string
                    bounty = entity.get_bounty()
                    address = bounty.split("//")[0]
                    print(f"bounty: {bounty} -- address:{address}")
                    bounty = bounty.encode()
                    self.socket.sendto(bounty, (address, 5555))
                    print("sent")
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
                check = message.decode()
                check = check.split("//")
                print(f"checking attention please {check}")
                unit = STATE.spawn_enemy(message.decode())
                all_units.add(unit)
            except:
                pass

            '''
            # TEST
            TEST_timer += 1
            TEST_timerB += 1
            # if TEST_timer > 200:
            #     unit = STATE.spawn_enemy('192.168.68.103//51546//1//Slingshotter')
            #     all_units.add(unit)
            #     TEST_timer = 0 # reset timer to loop
            #     # print(enemy_units)

            if TEST_timerB > 300:
                unit = STATE.spawn_enemy('192.168.68.103//35939//2//DinoRider')
                all_units.add(unit)
                TEST_timerB = 0 # reset timer to loop
                # print(enemy_units)

            """
            TO SPAWN ENEMIES, do:
                unit = STATE.spawn_enemy('U)
                all_units.add(unit)
            """
            '''
    
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
            if value != getIPAdress()[0]:
                temp_list = (key,value,5555)
                targets.append(temp_list)
                print(f"key: {key}, value: {value}")
        
        print(targets)
        time.sleep(1)
        while True:
            try:
                temp_socket.sendto(temp.encode(), ('<broadcast>', 5555))
                message, address = temp_socket.recvfrom(1024)
                if message.decode() == "Ress":
                    print("Im dying")
                    break
            except:
                pass

        temp_socket.close()

        return targets
    else:
        print("No message passed")
        temp = ""
        for x in range(0,5):
            try: 
                message, address = temp_socket.recvfrom(1024)
                temp = message
                print("GGGGG")
                message = "Ress"
                temp_socket.sendto(message.encode(), address)
            except:
                print("tried")

        address_list = json.loads(temp)
        for key, value in address_list.items():
            if value != getIPAdress()[0]:
                temp_list = (key,value,5555)
                targets.append(temp_list)
                print(f"key: {key}, value: {value}")

        temp_socket.close()
        print(f"{targets}")
    
        return targets

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
    print("im in game")
    Game(players = targets)


