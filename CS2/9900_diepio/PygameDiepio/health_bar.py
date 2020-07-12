import pygame
from constants import *

class HealthBar:
    def __init__(self, surface, x,y,width,height,hp_total):
        self.surface = surface
        self.total_width = width
        self.green_rect = pygame.Rect(x,y,width,height)
        self.red_rect = pygame.Rect(x,y,width,height)
        self.hp_total = hp_total

    def setXY(self,x,y):
        self.green_rect.x = x
        self.green_rect.y = y
        self.red_rect.x = x
        self.red_rect.y = y

    def updateHp(self, hp):
        x=0
        if self.hp_total != 0:
            x = int(self.total_width*(hp/self.hp_total))
        self.green_rect.width = x

    def draw(self):
        pygame.draw.rect(self.surface, red, self.red_rect)
        pygame.draw.rect(self.surface, green, self.green_rect)
