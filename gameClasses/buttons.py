import pygame as pg

class Button(pg.sprite.Sprite):
    def __init__(self, x, y, enabled, scale, image):
        super().__init__()
        self.image = pg.image.load(image).convert_alpha()
        self.image = pg.transform.scale(self.image, (int(self.image.get_width() * scale), int(self.image.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.mouse_pos = pg.mouse.get_pos()
        self.enabled = enabled
        #self.rect.center = (x,y)
        self.rect.topleft = (x,y)
        self.clicked = False
    
    # Sprite group calls this method for all buttons constantly in game loop
    def update(self):
        # When mouse hovers over button
        if self.rect.collidepoint(self.mouse_pos):
            # When button gets left-clicked
            if pg.mouse.get_pressed()[0]:
                # Implement behavior here
                print("Click")
