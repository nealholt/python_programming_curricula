import bullet, random, math
from constants import *

from funcs import adjustScreenCoordinates
import pygame

class BulletSeeking(bullet.Bullet):
    def __init__(self, screen, x, y, color, radius, dx, dy,
                hp, damage, timeout, shooter):
        super().__init__(screen, x, y, color, radius, dx, dy,
                hp, damage, timeout, shooter)
        #Get a location within which bullet will detect targets
        angle = math.atan2(dy,dx)
        #print('Degrees:',angle*180/math.pi) #Testing
        opp = math.sin(angle)
        adj = math.cos(angle)
        distance = 300 #pixels
        self.ahead_x = x + adj*distance
        self.ahead_y = y + opp*distance
        self.detection_radius = 250 #pixel
        #Find all potential targets
        potential_targets = []
        for sprite in all_sprites:
            if sprite.distanceToCoordinate(self.ahead_x,self.ahead_y) < self.detection_radius and sprite != shooter and sprite.sprite_type != TYPE_BULLET:
                potential_targets.append(sprite)
        #Choose specific target
        self.target = None
        if len(potential_targets) > 0:
            #Choose a random target
            self.target = random.choice(potential_targets)
        

    #Override parent class
    def update(self):
        #find and then seek out a target
        if self.target != None:
            self.moveTowardLocationAccel(self.target.x,self.target.y,seeking_bullet_acceleration)
        #Move, decrease timeout, and apply friction
        super().update()

    def draw(self, povx, povy, center_on_screen=False):
        super().draw(povx, povy)
        #TESTING
        if self.target != None:
            #Draw a line to my target
            x,y = adjustScreenCoordinates(self.x,self.y, povx, povy)
            targx,targy = adjustScreenCoordinates(self.target.x,self.target.y, povx, povy)
            pygame.draw.line(self.screen, self.color, (x,y), (targx,targy))
            #Draw where I looked for a target
            x,y = adjustScreenCoordinates(self.ahead_x,self.ahead_y, povx, povy)
            pygame.draw.circle(self.screen, self.color, [int(x),int(y)], self.detection_radius, 4)
