import pygame
pygame.init()

class Image():
    def __init__(self, image:str, pos_x:int, pos_y:int, width:int, height:int, show = True):
        self.position = (pos_x, pos_y)
        self.dim = (width, height)
        self.show = show
        self.imgPath = image
        self.rect = pygame.Rect(self.position,self.dim)
        
    def load_image(self, rect:pygame.Rect = None, dim = None):
        self.image = pygame.image.load(self.imgPath).convert_alpha()
        if dim:
            self.image = pygame.transform.scale(self.image, dim)
        else:
            self.image = pygame.transform.scale(self.image, self.dim)
        
        if rect:
            coord = rect.topleft
            self.rect = pygame.Rect(coord,rect.size)
        else:
            self.rect = pygame.Rect(self.position,self.dim)
        

    def draw(self, screen):
        if self.show:
            #Drawing the colored rectangle on the screen
            screen.blit(self.image, self.rect)

