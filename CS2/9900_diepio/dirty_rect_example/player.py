import sprite,pygame
from colors import *

class Player(sprite.Sprite):
    def __init__(self, screen, x, y):
        super().__init__(screen, x, y, 30, 0, 0, '', purple, 10, 'player')

    def collided(self, other):
        #Override parent method.
        #Avoid friendly fire
        if other.my_type == 'bullet':
            return False
        else:
            #Call parent method
            return super().collided(other)

    def move(self):
        #Call parent method:
        super().move()
        #Stay on screen
        if self.isOffScreen():
            #Undo movement if it moved us off screen
            self.x -= self.dx
            self.y -= self.dy
            self.rect.x = self.x
            self.rect.y = self.y

    def draw(self):
        #Override parent method
        r = pygame.Rect(self.x, self.y+20, self.size, 10)
        pygame.draw.rect(self.screen, self.color, r)
        r = pygame.Rect(self.x+10, self.y, 10, self.size)
        pygame.draw.rect(self.screen, self.color, r)
