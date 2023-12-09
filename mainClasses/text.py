import pygame
from src.CONSTANTS import *
pygame.init()

class Text():
    def __init__(self, text, pos_x, pos_y, font_size, value = None) -> None:
        self.text = text
        self.font_size = font_size
        self.r_text = pygame.font.SysFont(FONT, self.font_size).render(self.text, True, (0,0,0))
        self.rect = self.r_text.get_rect()
        self.rect.center = (pos_x, pos_y)
        self.value = value

    def render(self):
        return self.r_text
    
    def draw(self, screen):
        screen.blit(self.r_text, self.rect)

    def get_text(self):
        return self.text
    
    def getValue(self):
        return self.value
    
    def changeText(self, text):
        self.text = text
        self.r_text = pygame.font.SysFont(FONT, self.font_size).render(self.text, True, (0,0,0))