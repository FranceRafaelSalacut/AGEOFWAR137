import pygame
pygame.init()

#Text Renderer
def render(text):
    return pygame.font.SysFont('Corbel', 35).render(text, True, (0,0,0))

class Button():
    def __init__(self, text, color, pos_x, pos_y, height, width):
        self.text = render(text)
        self.color = color
        self.position = (pos_x, pos_y)
        self.size = (height, width)
        self.rect = pygame.Rect(self.position, self.size)

    def draw(self, screen,  ):
        #Drawing the colored rectangle on the screen
        pygame.draw.rect(screen, self.color, self.rect )

        #Drawing the text over the rectangle
        screen.blit(self.text, (self.position))

        print(self.position[0])

