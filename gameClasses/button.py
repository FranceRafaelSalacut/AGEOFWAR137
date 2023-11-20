import pygame
pygame.init()

#Text Renderer
def render(text):
    return pygame.font.SysFont('Corbel', 35).render(text, True, (0,0,0))

class Button():
    def __init__(self, text, color, pos_x, pos_y, height, width):
        self.text = text
        self.color = color
        self.position = (pos_x, pos_y)
        self.size = (height, width)
        self.rect = pygame.Rect(self.position, self.size)
        self.clicked = False

    def draw(self, screen):
        on_top = False
        #Drawing the colored rectangle on the screen
        pygame.draw.rect(screen, self.color, self.rect )

        #Drawing the text over the rectangle
        screen.blit(render(self.text), (self.position))

        #Tracking the mouse movement
        mouse = pygame.mouse.get_pos()

        #Setting up button if clicked functionality
        if self.rect.collidepoint(mouse): 
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                print("Here on " + str(self.text))

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
