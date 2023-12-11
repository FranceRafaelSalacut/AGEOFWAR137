import pygame as pg
from src.CONSTANTS import *

class UnitQueue:
    def __init__(self, groups):
        self.queue = [] # Queue of units
        self.groups = groups 

    def add_unit(self, unit, queue_time):
        self.queue.append((unit, queue_time))

    def update_queue(self, dt):
        if self.queue:
            unit, queue_time = self.queue[0]
            queue_time -= dt

            if queue_time <= 0:
                self.queue.pop(0)
                self.groups.add(unit)
            else:
                self.queue[0] = (unit, queue_time)

    def draw(self, screen):
        font_header = pg.font.SysFont(FONT, 24) 
        font = pg.font.SysFont(FONT, 20)
        color = (0, 0, 35)

        training_text_render = font_header.render("Training: ", True, color)
        screen.blit(training_text_render, (GAME_SCREEN_WIDTH - 200, 130))

        for i, (unit, queue_time) in enumerate(self.queue): 
            y_coord_units = 160 + (i * 30)   
            queue_time_str = f"{unit.__class__.__name__}: {queue_time:.2f} s"
            text = font.render(queue_time_str, True, color)
            screen.blit(text, (GAME_SCREEN_WIDTH - 200, y_coord_units))  
            
        pg.display.update()