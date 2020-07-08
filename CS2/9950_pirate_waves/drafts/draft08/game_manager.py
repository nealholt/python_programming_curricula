import math, pygame
from constants import *

class GameManager:
    def __init__(self):
        #height of the water at various positions
        self.water_heights = []
        #vertical acceleration of the water
        self.water_dys = []
        for i in range(0,screen_width+spacing,spacing):
            self.water_heights.append(screen_height-sea_level)
            self.water_dys.append(0)

        #Create pointlist for drawing water
        self.pointlist = []
        for i in range(len(self.water_heights)):
            self.pointlist.append((spacing*i,self.water_heights[i]))
        #Add in the bottom corners of the screen to complete the polygon.
        self.pointlist.append((screen_width,screen_height))
        self.pointlist.append((0,screen_height))

        #Use to oscillate the right-most water_heights value
        self.oscillator = 0

    def updateWater(self):
        '''Update the heights and velocities of all the water'''
        #Update all dy values based on height, neighboring dy values, and friction.
        for i in range(len(self.water_dys)):
            #Neighboring heights pull on the dy values
            neighbor_heights = 0
            neighbor_count = 0
            if i>0:
                neighbor_heights += self.water_heights[i-1]
                neighbor_count += 1
            if i<len(self.water_dys)-1:
                neighbor_heights += self.water_heights[i+1]
                neighbor_count += 1
            self.water_dys[i] += surface_tension*(neighbor_heights - neighbor_count*self.water_heights[i])
            #friction
            self.water_dys[i] = (1-friction)*self.water_dys[i]

        #Update all y values based on dy.
        for i in range(len(self.water_heights)):
            self.water_heights[i] += self.water_dys[i]

        #Update pointlist
        for i in range(len(self.water_heights)):
            self.pointlist[i] = (spacing*i,self.water_heights[i])

        #Oscillate the right-most water height value
        self.water_heights[-1] = screen_height-sea_level-amplitude*math.sin(self.oscillator/period)
        self.oscillator += 1

    def draw(self, surface):
        pygame.draw.polygon(surface, blue, self.pointlist)
