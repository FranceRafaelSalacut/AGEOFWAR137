import pygame
from src.CONSTANTS import *
pygame.init()

class Text():
    def __init__(self, text, pos_x, pos_y, font_size) -> None:
        self.text = text
        self.r_text = pygame.font.SysFont(FONT, font_size).render(self.text, True, (0,0,0))
        self.rect = self.r_text.get_rect()
        self.rect.center = (pos_x, pos_y)

    def render(self):
        return self.r_text
    
    def draw(self, screen):
        screen.blit(self.r_text, self.rect)

    def get_text(self):
        return self.text