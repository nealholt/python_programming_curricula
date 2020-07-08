import pygame

class Sprite:
    def __init__(self, screen, x, y, size, dx, dy, shape, color, hp, my_type):
        self.screen = screen
        self.x = x
        self.y = y
        self.size = size
        self.dx = dx
        self.dy = dy
        self.shape = shape
        self.color = color
        self.hp = hp
        self.my_type = my_type

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def getRect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

    def collided(self, other):
        r = other.getRect()
        return r.colliderect(self.getRect())

    def isOffScreen(self):
        return self.x<0 or self.x+self.size>self.screen.get_width() or self.y<0 or self.y+self.size>self.screen.get_height()

    def draw(self):
        r = self.getRect()
        if self.shape=='rect':
            pygame.draw.rect(self.screen, self.color, r)
        elif self.shape=='ellipse':
            pygame.draw.ellipse(self.screen, self.color, r)
        else:
            print('ERROR: unrecognized shape "'+shape+'" in Sprite.draw')
            sys.exit()
