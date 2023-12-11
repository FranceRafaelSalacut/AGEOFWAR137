import pygame
pygame.init()


# start_server = Button("Start_Server", Light_Grey, 550, 150, 175, 50, 35)
class Image():
    def __init__(self, color, pos_x, pos_y, height, width, show = True):
        self.color = color
        self.position = (pos_x, pos_y)
        self.size = (height, width)
        self.rect = pygame.Rect(self.position, self.size)
        self.show = show

    def draw(self, screen):
        if self.show:
            #Drawing the colored rectangle on the screen
            pygame.draw.rect(screen, self.color, self.rect)

            #Drawing the text over the rectangle
            screen.blit(self.text.render(), self.rect.topleft)

