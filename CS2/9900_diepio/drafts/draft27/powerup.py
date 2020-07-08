import pygame, diep_sprite
from constants import *

pygame.init()

#Center the powerup hitbox better in the center of the word
powerup_x_shift = -40

class Powerup(diep_sprite.DiepSprite):

    def __init__(self, screen, x, y, color):
        super().__init__(screen, x, y, color, 0, 0,
                        100000, #hp
                        sprite_type=TYPE_POWERUP,
                        draw_healthbar=False)
        self.collision_damage=0
        #Create a font
        font = pygame.font.SysFont("colonna", 32)
        self.text = font.render("Powerup", True, white)

    def draw(self, povx, povy, center_on_screen=False):
        #Get coordinate adjustments
        x_adjust = self.screen.get_width()/2 - povx
        y_adjust = self.screen.get_height()/2 - povy
        x = self.x + x_adjust + powerup_x_shift
        y = self.y + y_adjust
        #If this sprite is not on screen, don't draw it
        if self.isOffScreen(x, y):
            return
        self.screen.blit(self.text,(x,y))
