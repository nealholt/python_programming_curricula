import pygame
from constants import gravity, black

class CannonBall:
    def __init__(self,x,y,dx,dy):
        self.x=x
        self.y=y
        self.dx=dx
        self.dy=dy

    def update(self):
        self.x+=self.dx
        self.y+=self.dy
        self.dy+=gravity

    def draw(self, surface):
        radius = 5
        pygame.draw.circle(surface,black,(int(self.x),int(self.y)),radius)





