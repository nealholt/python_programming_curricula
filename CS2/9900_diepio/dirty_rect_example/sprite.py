import pygame

class Sprite:
    def __init__(self, screen, x, y, size, dx, dy,
                shape, color, hp, my_type):
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
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.rect.x = self.x
        self.rect.y = self.y

    def collided(self, other):
        return other.rect.colliderect(self.rect)

    def isOffScreen(self):
        return self.x<0 or self.x+self.size>self.screen.get_width() or self.y<0 or self.y+self.size>self.screen.get_height()

    def draw(self):
        if self.shape=='rect':
            pygame.draw.rect(self.screen, self.color, self.rect)
        elif self.shape=='ellipse':
            pygame.draw.ellipse(self.screen, self.color, self.rect)
        else:
            print('ERROR: unrecognized shape "'+shape+'" in Sprite.draw')
            sys.exit()
