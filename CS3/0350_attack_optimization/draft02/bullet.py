import pygame, physics_object

white = 255,255,255

class Bullet(physics_object.PhysicsObject):
    #Create a bullet
    def __init__(self, screen, x, y, angle):
        #8 is the radius, 0 is the rotation rate
        super().__init__(x, y, 8, angle, 0)
        self.screen = screen
        #Bullet speed
        self.speed = 20
        #how many frames until bullet evaporates
        self.timeout = 60

    def moveForward(self):
        super().moveForward(self.speed)

    def draw(self):
        pygame.draw.circle(self.screen, white, (int(self.x),int(self.y)), self.radius)
