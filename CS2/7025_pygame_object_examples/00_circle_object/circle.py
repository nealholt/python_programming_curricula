import pygame

class Circle:
    def __init__(self, surface, color, x, y, radius):
        self.surface = surface
        #x and y will be the center of the circle.
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius

    def draw(self):
        center_x = self.x-self.radius
        center_y = self.y-self.radius
        width = self.radius*2
        height = width
        pygame.draw.ellipse(self.surface, self.color, [center_x, center_y, width, height])

    def move(self, changex, changey):
       self.x = self.x + changex
       self.y = self.y + changey
