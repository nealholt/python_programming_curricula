import pygame, diep_sprite
from constants import *

pygame.init()

class Powerup(diep_sprite.DiepSprite):

    def __init__(self, screen, x, y, color):
        super().__init__(screen, x, y, color, 0, 0,
                        100000, #hp
                        sprite_type=TYPE_ANIMATION,
                        draw_healthbar=False)
        #Create a font
        font = pygame.font.SysFont("colonna", 72)
        self.text = font.render("Powerup", True, white)

    def draw(self, povx, povy, center_on_screen=False):
        self.screen.blit(self.text,(0,0))
