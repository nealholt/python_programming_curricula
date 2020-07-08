import diep_sprite
from constants import *

class Bullet(diep_sprite.DiepSprite):
    def __init__(self, screen, x, y, color, radius, dx, dy,
                hp, damage, timeout, shooter):
        super().__init__(screen, x, y, color, radius, 0,
                        sprite_type=TYPE_BULLET,
                        draw_heading=False)
        self.shooter = shooter
        self.dx = dx
        self.dy = dy
        self.friction = 0
        self.timeout = timeout
        self.draw_healthbar = False
        self.xs[HP_INDEX] = hp
        self.hit_points = hp
        self.xs[COLLISION_DAMAGE_INDEX] = damage
        self.xs[FRICTION_INDEX] = bullet_friction

    #Override parent class
    def update(self):
        self.timeout -= 1
        super().update()

