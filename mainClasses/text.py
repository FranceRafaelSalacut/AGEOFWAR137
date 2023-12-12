import pygame
from src.CONSTANTS import *
pygame.init()

class Text():
    def __init__(self, text, pos_x, pos_y, font_size, value = None, color = None, show = True) -> None:
        self.text = text
        self.font_size = font_size
        if color:
            self.color = color
        else:
            self.color = (255,255,255)
        self.r_text = pygame.font.SysFont(FONT, self.font_size).render(self.text, True, self.color)
        self.rect = self.r_text.get_rect()
        self.rect.center = (pos_x, pos_y)
        self.value = value
        self.show = show

    def render(self):
        return self.r_text
    
    def draw(self, screen):
        if self.show:
            screen.blit(self.r_text, self.rect)

    def get_text(self):
        return self.text
    
    def getValue(self):
        return self.value
    
    def changeText(self, text):
        self.text = text
        self.r_text = pygame.font.SysFont(FONT, self.font_size).render(self.text, True, self.color)