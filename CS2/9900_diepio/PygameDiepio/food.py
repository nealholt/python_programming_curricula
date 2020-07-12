import diep_sprite
from constants import *

class Food(diep_sprite.DiepSprite):
    def __init__(self, screen, color, radius,
                hp, xp, hit_radius, food_shape):
        super().__init__(screen, 0,0, #x,y start as zero then it teleports
                        color, radius,
                        0, #Base level is zero
                        draw_shape=food_shape,
                        sprite_type=TYPE_FOOD,
                        draw_heading=False)
        self.experience = xp
        self.xs[HP_INDEX] = hp
        self.resetHealthbar(screen,hp)
        self.collision_radius = hit_radius
        self.teleport()
