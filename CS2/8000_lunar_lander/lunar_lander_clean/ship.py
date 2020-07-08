import math, pygame
from constants import *

class Ship:
    def __init__(self, surface, x, y):
        self.surface = surface
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.speed = 0.2
        self.sides = 3
        self.radius = 20
        self.angle = 0
        self.rotation_rate = math.pi/64
        self.thrust_on = False
        self.lives = 1
        self.remove = False

    def rotateLeft(self):
        self.angle -= self.rotation_rate

    def rotateRight(self):
        self.angle += self.rotation_rate

    def thrust(self):
        self.dx += math.cos(self.angle)*self.speed
        self.dy += math.sin(self.angle)*self.speed
        self.thrust_on = True

    def move(self):
        #Move dx and dy
        self.x += self.dx
        self.y += self.dy
        #Apply gravity
        self.dy += gravity

    def getCorners(self, x_to_use, y_to_use):
        '''x_to_use, y_to_use are arguments that are either
        the center of the screen (for drawing the ship)
        or the "actual" x and y coordinates of the ship
        (for checking collisions with the ground).'''
        #Returns list of points to draw the ship
        points = []
        #Nose
        angle = self.angle+math.pi*2
        x = x_to_use + math.cos(angle)*self.radius*1.5
        y = y_to_use + math.sin(angle)*self.radius*1.5
        points.append([x, y])
        #wing 1
        angle = self.angle+math.pi*2*(1.2/self.sides)
        x = x_to_use + math.cos(angle)*self.radius
        y = y_to_use + math.sin(angle)*self.radius
        points.append([x, y])
        #rear
        angle = self.angle+math.pi
        x = x_to_use + math.cos(angle)*self.radius*0.5
        y = y_to_use + math.sin(angle)*self.radius*0.5
        points.append([x, y])
        #wing 2
        angle = self.angle+math.pi*2*(1.8/self.sides)
        x = x_to_use + math.cos(angle)*self.radius
        y = y_to_use + math.sin(angle)*self.radius
        points.append([x, y])
        return points

    def draw(self):
        #Draw thrust
        if self.thrust_on:
            angle = self.angle+math.pi
            x = self.surface.get_width()/2 + math.cos(angle)*self.radius*0.7
            y = self.surface.get_height()/2 + math.sin(angle)*self.radius*0.7
            radius = 10
            r = pygame.Rect(x-radius/2,y-radius/2,radius,radius)
            pygame.draw.ellipse(self.surface, red, r)
        #Reset thrust
        self.thrust_on = False
        #Draw outline of ship. Note: 3 is line thickness.
        points = self.getCorners(self.surface.get_width()/2, self.surface.get_height()/2)
        pygame.draw.polygon(self.surface, white, points,3)

