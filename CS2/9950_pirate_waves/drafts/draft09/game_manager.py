import math, pygame, random
from functions import *

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

        #Load the rum image
        self.rum,self.rum_rect = load_image('images/wine_2.png',-1)
        #Scale down the image
        dimensions = (int(self.rum_rect.width*scaling), int(self.rum_rect.height*scaling))
        self.rum = pygame.transform.scale(self.rum, dimensions)
        self.rum_rect.width = dimensions[0]
        self.rum_rect.height = dimensions[1]
        #Create a list of pickups
        self.pickups = []
        #Countdown until next rum spawn
        self.rum_spawn_countdown = 0

    def updatePickups(self):
        #Countdown until next rum spawn
        self.rum_spawn_countdown -= 1
        if self.rum_spawn_countdown < 0:
            x = screen_width
            y = random.randint(0,screen_height-sea_level-100)
            speed = random.randint(rum_scroll_speed_min, rum_scroll_speed_max)
            self.pickups.append((x,y,speed))
            self.rum_spawn_countdown = random.randint(rum_respawn_min, rum_respawn_max)
        #Move all the pickups to the left
        for i in reversed(range(len(self.pickups))):
            x,y,speed = self.pickups[i]
            x = x-speed
            if x+self.rum_rect.width < 0:
                del self.pickups[i]
            else:
                self.pickups[i] = (x,y,speed)

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

    def checkCollisions(self, player):
        '''Check to see if the player collides with any of the rum.'''
        for i in reversed(range(len(self.pickups))):
            x,y = player.getCenter()
            if distance(x, y, self.pickups[i][0], self.pickups[i][1]) < rum_collision_distance:
                del self.pickups[i]

    def draw(self, surface):
        pygame.draw.polygon(surface, blue, self.pointlist)
        for x,y,_ in self.pickups:
            self.rum_rect.center = (x,y)
            surface.blit(self.rum, self.rum_rect)
