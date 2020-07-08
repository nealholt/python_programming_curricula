import pygame
from constants import gravity, black

class CannonBall:
    def __init__(self,x,y,dx,dy):
        self.x=x
        self.y=y
        self.dx=dx
        self.dy=dy
        #Delay (in frames) before this cannon ball can damage anyone
        self.damage_delay = 15

    def update(self):
        self.x+=self.dx
        self.y+=self.dy
        self.dy+=gravity
        self.damage_delay -= 1

    def draw(self, surface):
        radius = 5
        pygame.draw.circle(surface,black,(int(self.x),int(self.y)),radius)





