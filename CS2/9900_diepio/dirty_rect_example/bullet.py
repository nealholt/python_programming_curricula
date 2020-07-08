import sprite
from colors import *

class Bullet(sprite.Sprite):
    def __init__(self, screen, x, y):
        super().__init__(screen, x, y, 10, 0, -5, 'rect', red, 1, 'bullet')

    def collided(self, other):
        #Override parent method.
        #Avoid friendly fire and bullet-on-bullet collisions
        if other.my_type == 'bullet' or other.my_type == 'player':
            return False
        else:
            #Call parent method
            return super().collided(other)
