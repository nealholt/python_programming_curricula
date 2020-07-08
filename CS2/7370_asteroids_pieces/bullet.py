import pygame, math

white = 255,255,255

class Bullet:
    #Create a bullet
    def __init__(self, screen, x, y, angle):
        self.screen = screen
        #Coordinates of the center of the bullet
        self.x = x
        self.y = y
        #Current direction bullet is facing
        self.angle = angle
        #Bullet speed
        self.speed = 20
        #how many frames until bullet evaporates
        self.timeout = 60

    def moveForward(self):
        self.x = self.x+math.cos(self.angle)*self.speed
        self.y = self.y+math.sin(self.angle)*self.speed

    def draw(self):
        radius = 8
        x = int(self.x)
        y = int(self.y)
        pygame.draw.circle(self.screen, white, (x,y), radius)
