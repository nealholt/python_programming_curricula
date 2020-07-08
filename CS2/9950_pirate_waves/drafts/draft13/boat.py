import math
from functions import *

class Boat:
    def __init__(self, image_name, face_right, x):
        #Load the image and format it
        self.img,self.rect = load_image(image_name,-1)
        #Scale down the image
        dimensions = (int(self.rect.width*scaling), int(self.rect.height*scaling))
        self.img = pygame.transform.scale(self.img, dimensions)
        self.rect.width = dimensions[0]
        self.rect.height = dimensions[1]
        if face_right:
            #Horizontal flip
            self.img = pygame.transform.flip(self.img, True, False)
        #Starting position
        self.rect.x = x
        self.angle = 0

        #Rotated version of the image and rectangle for drawing the boat
        #at an angle
        self.rota_img = self.img.copy()
        self.rota_rect = self.rect.copy()

        #If the front or back of the boat is actually in the water
        self.rear_under_water = False
        self.front_under_water = False

        #Vertical position and velocity for front and back of the ship
        self.rear_dy = 0
        self.rear_y = screen_height-sea_level
        self.front_dy = 0
        self.front_y = screen_height-sea_level

        #Delay before the boat can cause another splash
        self.splash_countdown = 0

    def getCenter(self):
        return self.rota_rect.center

    def update(self, water_heights):
        '''Update the position and angle of the boat in the water.'''
        #Update vertical velocity of left (rear) of the boat
        lefty = getWaterHeightAt(self.rect.left,water_heights)+buffer
        if self.rear_y>lefty: #under water
            self.rear_under_water = True
            #sqrt reduces the affect of bouyancy when shallow
            depth = math.sqrt(self.rear_y-lefty)
            self.rear_dy = (1-water_friction)*self.rear_dy-bouyancy*depth
        else:
            self.rear_under_water = False
        #Update vertical velocity of left (rear) of the boat
        righty = getWaterHeightAt(self.rect.right,water_heights)+buffer
        if self.front_y>righty: #under water
            self.front_under_water = True
            #sqrt reduces the affect of bouyancy when shallow
            depth = math.sqrt(self.front_y-righty)
            self.front_dy = (1-water_friction)*self.front_dy-bouyancy*depth
        else:
            self.front_under_water = False
        self.updateDy()
        self.updateHeightAndRotation()
        self.splash(water_heights, splash_delay)

    def updateDy(self):
        self.rear_dy = (1-air_friction)*self.rear_dy+gravity
        self.front_dy = (1-air_friction)*self.front_dy+gravity

    def updateHeightAndRotation(self):
        #Update height of left and right sides of the boat.
        self.rear_y += self.rear_dy
        self.front_y += self.front_dy
        #Rotate the boat
        self.angle = (180/math.pi)*math.atan2(self.rear_y-self.front_y, self.rect.width)
        self.rota_img,self.rota_rect = rotateImage(self.img, self.rect, self.angle)
        #I assume that the bottom of the rectangle needs to be the lower of
        #the two y values
        self.rota_rect.bottom = max(self.rear_y,self.front_y)

    def splash(self, water_heights, delay):
        #If the center of the boat is ever significantly underwater,
        #push the water down to make a wave. This should happen when
        #the boat lands from having leaped out of the water.
        self.splash_countdown -= 1
        if self.splash_countdown < 0:
            height = getWaterHeightAt(self.rota_rect.centerx,water_heights)
            center_depth = (self.rear_y+self.front_y)/2
            if center_depth-height > splash_depth:
                shiftWaterHeight((self.rota_rect.centerx,center_depth-splash_adjust), water_heights)
                self.splash_countdown = splash_delay

    def jump(self):
        #Jump only if some of the boat is in the water!
        if self.front_under_water or self.rear_under_water:
            self.rear_dy-=jump_power
            self.front_dy-=jump_power

    def moveLeft(self):
        self.rect.x-=speed
        if self.rect.x < 0:
            self.rect.x = 0

    def moveRight(self):
        self.rect.x+=speed
        if self.rect.x+self.rect.width > screen_width:
            self.rect.x = screen_width-self.rect.width

    def draw(self, surface):
        surface.blit(self.rota_img, self.rota_rect)
