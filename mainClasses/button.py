import pygame
from mainClasses.text import *
pygame.init()


# start_server = Button("Start_Server", Light_Grey, 550, 150, 175, 50, 35)
class Button():
    def __init__(self, text, color, pos_x, pos_y, height, width, font_size, value = None, show = True):
        self.text = Text(text, pos_x, pos_y, font_size)
        self.color = color
        self.position = (pos_x, pos_y)
        self.size = (height, width)
        self.rect = pygame.Rect(self.position, self.size)
        self.value = value
        self.clicked = False
        self.show = show

    def draw(self, screen):
        action = False

        if self.show:
            #Drawing the colored rectangle on the screen
            pygame.draw.rect(screen, self.color, self.rect)

            #Drawing the text over the rectangle
            screen.blit(self.text.render(), self.rect.topleft)

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
    
    def getValue(self):
        return self.value
    
    def changeText(self, text):
        self.text = Text(text, 0, 0, 35)

