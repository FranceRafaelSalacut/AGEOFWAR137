import pygame
from gameClasses.text import *
pygame.init()



class Button():
    def __init__(self, text, color, pos_x, pos_y, height, width, font_size):
        self.text = Text(text, 0, 0, font_size)
        self.color = color
        self.position = (pos_x, pos_y)
        self.size = (height, width)
        self.rect = pygame.Rect(self.position, self.size)
        self.clicked = False

    def draw(self, screen):
        action = False
        #Drawing the colored rectangle on the screen
        pygame.draw.rect(screen, self.color, self.rect )

        #Drawing the text over the rectangle
        screen.blit(self.text.render(), (self.position))

        #Tracking the mouse movement
        mouse = pygame.mouse.get_pos()

        #Setting up button if clicked functionality
        if self.rect.collidepoint(mouse): 
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        return action
    
    def getText(self):
        return self.text.get_text()
    
    def changeText(self, text):
        self.text = Text(text, 0, 0, 35)

