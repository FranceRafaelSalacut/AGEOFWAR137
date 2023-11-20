import pygame
from src.CONSTANTS import *
from gameClasses.screen import *
pygame.init


screen = Screen(SCREEN_HEIGHT, SCREEN_WIDTH, Baby_Blue)
screen.createScreen()
surface = screen.returnScreen()
print(surface)
