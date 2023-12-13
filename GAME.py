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
from mainClasses.image import *
from gameClasses.rangedUnit import *

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
        pygame.mixer.music.set_volume(0.5)

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
                if isinstance(entity, rangedUnit):
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
                        #print(entity_id)
                        #print(STATE.get_current_target_to_send())
                        message = entity_id.encode()
                        self.socket.sendto(message, (STATE.get_current_target_to_send()[1], 5555))
                        #print(STATE.get_current_target_to_send()[1])
                    dead_units.add(entity)
            for entity in projectiles:
                screen.blit(entity.image, entity.rect)
                for unit in all_units:
                    entity.check_collision(unit)
                entity.check_collision(base)
                
                entity.goTowardsTarget() # Update the movement of the projectiles' rect
                # If bullet leaves screen, kill its sprite
            for entity in dead_units:
                if entity.killer:
                    STATE.killed_unit(entity)
                    # TODO: pass to specific player this string
                    killer_id = entity.killer.get_bounty()
                    killer_id = killer_id.split("//")
                    killer_id = killer_id[0]
                    print(f"killer id = {killer_id}")


                    bounty = entity.get_bounty()
                    bounty = bounty.split("//")
                    bounty.pop(0)

                    new_bounty = "//".join(bounty)
                    new_bounty = killer_id + "//" + new_bounty
                    print(f"old bounty {entity.get_bounty()}")
                    print(f"bounty: {new_bounty}")

                    message = new_bounty.encode()
                    self.socket.sendto(message, (killer_id, 5555))
                    print("sent")
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
                m = f"DIED//{self.ip_address}"
                for p in self.players:
                    self.socket.sendto(m, (p, 5555))
            
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
            try:
                message, address = self.socket.recvfrom(1024)
                check = message.decode()
                if "DIED" in check:
                    toRemove = message.decode()
                    toRemove = toRemove.split("//")[1]
                    self.players.remove(toRemove)
                    print(self.players)
                elif "EXP" in check:
                    print("Im the exp man")
                    bounty = message.decode()
                    bounty = bounty.split("//")
                    gold = bounty[3].split(":")
                    gold = int(gold[1])
                    print(f"gold = {gold}")
                    exp = bounty[4].split(":")
                    exp = int(exp[1])
                    print(f"exp = {exp}")

                    STATE.earn_bounty(gold,exp)
                else:
                    print("Enemy units ahead")
                    unit = STATE.spawn_enemy(message.decode())
                    all_units.add(unit)
            except:
                pass
            # TEST

            # TEST_timerB += 1
            # if TEST_timerB > 100:
            #     unit = STATE.spawn_enemy('192.168.68.103//35939//2//Stormtrooper')
            #     all_units.add(unit)
            #     TEST_timerB = 0 # reset timer to loop
            #     # print(enemy_units)
            # TEST_timer += 1
            # if TEST_timer > 200:
            #     unit = STATE.spawn_enemy('192.168.68.103//51546//1//Slingshotter')
            #     all_units.add(unit)
            #     TEST_timer = 0 # reset timer to loop
            #     # print(enemy_units)

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
        running = True
        while running:
            try:
                temp_socket.sendto(temp.encode(), ('<broadcast>', 5555))
                message, address = temp_socket.recvfrom(1024)
                if message.decode() == "Ress":
                    print("Im dying")
                    running = False
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


