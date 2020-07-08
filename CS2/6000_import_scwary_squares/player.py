import pygame

class Player:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.points = 0

    def moveLeft(self, speed):
        self.x = self.x-speed

    def moveRight(self, speed):
        self.x = self.x+speed

    def moveUp(self, speed):
        self.y = self.y-speed

    def moveDown(self, speed):
        self.y = self.y+speed

    def collides(self, other):
        #Other is a rectangle.
        #Returns true if player collides with other.
        rect = pygame.Rect(self.x,self.y,self.size,self.size)
        return rect.colliderect(other)

    def draw(self, screen):
        rect = pygame.Rect(self.x,self.y,self.size,self.size)
        pygame.draw.rect(screen, self.color, rect)
