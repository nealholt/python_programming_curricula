import math
from functions import *

class Boat:
    def __init__(self):
        #Load the image and format it
        self.img,self.rect = load_image('images/1stship_3.png',-1)
        #Scale down the image
        dimensions = (int(self.rect.width*scaling), int(self.rect.height*scaling))
        self.img = pygame.transform.scale(self.img, dimensions)
        self.rect.width = dimensions[0]
        self.rect.height = dimensions[1]
        #Horizontal flip
        self.img = pygame.transform.flip(self.img, True, False)
        self.rect.x = int(screen_width/3)

        #Rotated version of the image and rectangle for drawing the boat
        #at an angle
        self.rota_img = None
        self.rota_rect = None

        #If the front or back of the boat is actually in the water
        self.rear_under_water = False
        self.front_under_water = False

        #Vertical position and velocity for front and back of the ship
        self.rear_dy = 0
        self.rear_y = screen_height-sea_level
        self.front_dy = 0
        self.front_y = screen_height-sea_level

    def getCenter(self):
        return self.rota_rect.center

    def update(self, water_heights):
        '''Update the position and angle of the boat in the water.'''
        #Update vertical velocity of left (rear) of the boat
        lefty = getWaterHeightAt(self.rect.left,water_heights)+buffer
        self.rear_under_water = False
        if self.rear_y>lefty: #under water
            self.rear_under_water = True
            depth = self.rear_y-lefty
            self.rear_dy = (1-water_friction)*self.rear_dy-bouyancy*depth
        self.rear_dy = (1-air_friction)*self.rear_dy+gravity
        #Update vertical velocity of left (rear) of the boat
        righty = getWaterHeightAt(self.rect.right,water_heights)+buffer
        self.front_under_water = False
        if self.front_y>righty: #under water
            self.front_under_water = True
            depth = self.front_y-righty
            self.front_dy = (1-water_friction)*self.front_dy-bouyancy*depth
        self.front_dy = (1-air_friction)*self.front_dy+gravity
        #Update height of left and right sides of the boat.
        self.rear_y += self.rear_dy
        self.front_y += self.front_dy
        #Rotate the boat
        angle = (180/math.pi)*math.atan2(self.rear_y-self.front_y, self.rect.width)
        self.rota_img,self.rota_rect = rotateImage(self.img, self.rect, angle)
        #I assume that the bottom of the rectangle needs to be the lower of
        #the two y values
        self.rota_rect.bottom = max(self.rear_y,self.front_y)

    def jump(self):
        #Jump only if some of the boat is in the water!
        if self.front_under_water or self.rear_under_water:
            self.rear_dy-=jump_power
            self.front_dy-=jump_power

    def moveLeft(self):
        self.rect.x-=speed
        self.rear_dy+=tilt

    def moveRight(self):
        self.rect.x+=speed
        self.front_dy+=tilt

    def draw(self, surface):
        surface.blit(self.rota_img, self.rota_rect)
