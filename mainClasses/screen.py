import pygame
pygame.init()

class Screen():
    def __init__(self, height, width, color) -> None:
        self.title = 'AGE_OF_WAR'
        self.size = (height, width)
        self.color = color
        pygame.display.set_caption(self.title)
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill(self.color)

    def returnScreen(self):
        return self.screen
    