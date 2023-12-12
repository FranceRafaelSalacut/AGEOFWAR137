import pygame
from mainClasses.text import *
from mainClasses.image import Image
pygame.init()


# start_server = Button("Start_Server", Light_Grey, 550, 150, 175, 50, 35)
class Button():
    def __init__(self, color, pos_x, pos_y, height, width, font_size, value = None, show = True, text = None, image:Image = None, textColor = None):
        self.color = color
        self.position = (pos_x, pos_y)
        self.size = (height, width)
        self.rect = pygame.Rect(self.position, self.size)
        if text:
            self.text = Text(text, self.rect.centerx, self.rect.centery, font_size, color=textColor)
        else:
            self.text = None
        self.value = value
        self.clicked = False
        self.show = show
        self.image = image
        
    def load_image(self):
        if self.image:
            print('what')
            self.image.load_image(self.rect, self.size)

    def draw(self, screen):
        action = False

        if self.show:
            #Drawing the colored rectangle on the screen
            if self.image:
                self.image.draw(screen)
            else:
                pygame.draw.rect(screen, self.color, self.rect)
            if self.text:
                #Drawing the text over the rectangle
                screen.blit(self.text.render(), self.text.rect)

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
        if self.text:
            return self.text.get_text()
        else:
            return "None"
    
    def getValue(self):
        return self.value
    
    def changeText(self, text):
        self.text = Text(text, 0, 0, 35)

