import pygame

class Sprite:
    def __init__(self, x, y, image_file):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.image = pygame.image.load(image_file)

    def move(self):
        self.x = self.x + self.dx
        self.y = self.y + self.dy

    def getRect(self):
        rect = self.image.get_rect()
        rect.x = int(self.x)
        rect.y = int(self.y)
        return rect

    def collided(self, other_sprite):
        r = self.getRect()
        other_rect = other_sprite.getRect()
        return r.colliderect(other_rect)

    def draw(self, screen):
        x = int(self.x)
        y = int(self.y)
        screen.blit(self.image,(x,y))
