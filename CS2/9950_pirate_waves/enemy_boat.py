import boat
from constants import *

class EnemyBoat(boat.Boat):
    def __init__(self, image_name, face_right, x):
        super().__init__(image_name, face_right, x)
        self.health = enemy_health
        self.volley_count = enemy_volley_count
        self.refire_countdown = enemy_volley_delay
        #Remember which shot of the volley we are on
        self.volley_tracker = 0

    def update(self, water_heights):
        if self.isDead(): #Begin the death animation:
            self.updateDy()
            self.updateHeightAndRotation()
            self.splash(water_heights, 2**31) #Huge delay to only splash once and never again
        else:
            super().update(water_heights)
            self.refire_countdown -= 1
            #Move the boat slightly to the left
            if self.rect.x > enemy_stop_point:
                self.rect.x-=1

    def deleteMe(self):
        _,y = self.getCenter()
        return y>screen_height

    def isDead(self):
        return self.health <= 0

    def readyToShoot(self):
        return self.refire_countdown < 0

    def shoot(self):
        self.volley_tracker += 1
        if self.volley_tracker >= self.volley_count:
            self.volley_tracker = 0
            self.refire_countdown = enemy_volley_delay

