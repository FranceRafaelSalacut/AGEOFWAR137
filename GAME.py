import pygame
from mainClasses.button import *
from src.CONSTANTS import *
from src.gamescreen import *
from gameClasses.unitFactory import *


STATE = GAME_SCREEN()


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

# music
pygame.mixer.music.load(MUSIC_GLORIOUS_MORNING)
pygame.mixer.music.play()


while run:
    # polling for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # filling the screen with a color to wipe away everything from the last frame
    screen.fill('white')

    # Render game here
    # vv===========================================vv

    for entity in all_units:
        entity.move()
        screen.blit(entity.image, entity.rect)
        
        if entity.rect.left >= GAME_SCREEN_WIDTH:
            del entity
    
    # GUI
    for index, display in enumerate(STATE.display()):
        if display.draw(screen):
            action = display.getValue()

            if type(STATE) == GAME_SCREEN:
                if action == 'train_unit':
                    unit = STATE.train_unit()
                    all_units.add(unit)

            if action == "Exit":
                run = False

            print(action)


    # ^^===========================================^^
    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60) / 1000 # limits FPS to 60

pygame.quit()