import pygame
pygame.init()

class Image():
    def __init__(self, image:str, pos_x:int, pos_y:int, width:int, height:int, show = True):
        self.position = (pos_x, pos_y)
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, [width, height])
        self.rect = pygame.Rect(pos_x, pos_y, width, height)
        self.show = show

    def draw(self, screen):
        if self.show:
            #Drawing the colored rectangle on the screen
            screen.blit(self.image, self.rect)

