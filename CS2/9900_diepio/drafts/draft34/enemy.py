import math, pygame, ship
from constants import *

class EnemyCritter(ship.Ship):
    def __init__(self, screen, x, y, color, radius, name):
        super().__init__(screen, x, y, color, radius, name)

    #Override super class's update function
    def update(self, sprites_in_range):
        #Avoid an error
        if len(sprites_in_range)==0:
            super().update()
            return
        #Select closest sprite as target
        closest = sprites_in_range[0]
        distance = 999999
        for s in sprites_in_range:
            #Skip self or self-shot bullets
            if s==self or (s.sprite_type == TYPE_BULLET and s.shooter == self):
                continue
            #Update closest
            temp_dist = self.distanceTo(s)
            if temp_dist<distance:
                distance = temp_dist
                closest = s
        #Maintain optimal distance from target
        self.angle = self.angleTo(closest.x, closest.y)
        a = self.xs[ACCEL_INDEX]
        if distance > 300:
            self.dx += math.cos(self.angle)*a
            self.dy += math.sin(self.angle)*a
        elif distance < 100:
            self.dx -= math.cos(self.angle)*a
            self.dy -= math.sin(self.angle)*a
        #Shoot at target
        if distance <= 350:
            self.shoot()
        super().update()
