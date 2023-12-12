import pygame
pygame.init()

class Image():
    def __init__(self, image:str, pos_x:int, pos_y:int, width:int, height:int, show = True):
        self.position = (pos_x, pos_y)
        self.dim = (width, height)
        self.show = show
        self.imgPath = image
        
    def load_image(self):
        self.image = pygame.image.load(self.imgPath).convert_alpha()
        self.image = pygame.transform.scale(self.image, self.dim)
        self.rect = pygame.Rect(self.position[0],self.position[1], self.dim[0], self.dim[1])

    def draw(self, screen):
        if self.show:
            #Drawing the colored rectangle on the screen
            screen.blit(self.image, self.rect)

