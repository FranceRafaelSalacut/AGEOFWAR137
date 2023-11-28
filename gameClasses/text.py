import pygame
pygame.init()

class Text():
    def __init__(self, text, pos_x, pos_y) -> None:
        self.text = text
        self.x = pos_x
        self.y = pos_y

    def render(self):
        return pygame.font.SysFont('Corbel', 35).render(self.text, True, (0,0,0))
    
    def get_rect(self, r_text):
        return r_text.get_rect()
    
    def get_text(self):
        return self.text