import pygame, diep_sprite
from constants import *

class Sparkle(diep_sprite.DiepSprite):
    def __init__(self, screen, x, y, color):
        super().__init__(screen, x, y, color, 0, 0,
                        sprite_type=TYPE_ANIMATION,
                        draw_healthbar=False)
        #Use hp as timeout
        self.xs[HP_INDEX] = 15

    #Override super class's update function
    def update(self):
        #Use hp as timeout
        self.xs[HP_INDEX] -= 1

    def draw(self, povx, povy, center_on_screen=False):
        #Get coordinate adjustments
        x_adjust = self.screen.get_width()/2 - povx
        y_adjust = self.screen.get_height()/2 - povy
        x = self.x + x_adjust
        y = self.y + y_adjust
        #If this sprite is not on screen, don't draw it
        if self.isOffScreen(x, y):
            return
        length = 5
        pygame.draw.line(self.screen, self.color,
            (x-length,y-length), (x+length,y+length), 1) #1 is width
        pygame.draw.line(self.screen, self.color,
            (x-length,y+length), (x+length,y-length), 1) #1 is width