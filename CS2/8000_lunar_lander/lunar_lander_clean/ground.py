import pygame, math
from constants import *

class Ground:
    def __init__(self, surface):
        self.surface = surface
        self.ground_heights = [[0,0],[200,700],[400,200],[600,550],
                              [800,0],[1000,300],[1200,800],[1400,400],
                              [1600,600],[1650,600],#Landing pad start and end
                              [1800,500],[2000,500],[2200,100]]

    def getVectorToPad(self, x, y):
        '''Use this to figure out trajectory to the pad.'''
        midpoint = self.ground_heights[landing_pad_index+1][0] - self.ground_heights[landing_pad_index][0]
        return (x - midpoint, y - self.ground_heights[landing_pad_index][1])

    def overLandingPad(self,x):
        return x>self.ground_heights[landing_pad_index][0] and x<self.ground_heights[landing_pad_index+1][0]

    def shipHitGround(self, ship):
        points = ship.getCorners(ship.x, ship.y)
        for p in points:
            if p[1] >= self.getHeightAt(p[0]):
                return True
        return False

    def safeLanding(self, player_ship):
        print('Over pad: '+str(self.overLandingPad(player_ship.x)))
        print('Collided: '+str(self.shipHitGround(player_ship)))
        print('Good dx: '+str(abs(player_ship.dx)<1))
        print('Good dy: '+str(player_ship.dy>0 and player_ship.dy<1.5))
        print('Good angle: '+str(abs((player_ship.angle%math.pi)-math.pi/2)<math.pi/32))
        print('angle: '+str(player_ship.angle))
        print('angle difference to pi/2: '+str(abs((player_ship.angle%math.pi)-math.pi/2)))
        print('dx: '+str(player_ship.dx))
        print('dy: '+str(player_ship.dy))
        if self.overLandingPad(player_ship.x) and self.shipHitGround(player_ship):
            #Check that the player is facing upright, and
            #has minimal dx and sufficiently small dy for a safe landing.
            if abs(player_ship.dx)<1 and player_ship.dy>0 and player_ship.dy<1.5:
                return abs((player_ship.angle%math.pi)-math.pi/2)<math.pi/32
        else:
            return False

    def rateTheLanding(self, player_ship):
        return int(100*(abs(player_ship.dx) + abs(player_ship.dy) + abs((player_ship.angle%math.pi)-math.pi/2)))

    def getHeightAt(self, x):
        #Get coordinates that x is between and use those coordinates
        #as a line to calculate the height of the ground at that x value.
        if x<=self.ground_heights[0][0] or x>=self.ground_heights[-1][0]:
            return 0
        for i in range(len(self.ground_heights)-1):
            if x>=self.ground_heights[i][0] and x<self.ground_heights[i+1][0]:
                start = self.ground_heights[i]
                end = self.ground_heights[i+1]
                slope = (end[1]-start[1]) / (end[0]-start[0])
                #Point slope form:
                return slope*(x-end[0])+end[1]

    def draw(self, povx, povy):
        x_adjust = self.surface.get_width()/2 - povx
        y_adjust = self.surface.get_height()/2 - povy
        #Draw the line segments
        for i in range(len(self.ground_heights)-1):
            coord1 = [self.ground_heights[i][0]+x_adjust, self.ground_heights[i][1]+y_adjust]
            coord2 = [self.ground_heights[i+1][0]+x_adjust, self.ground_heights[i+1][1]+y_adjust]
            color = white
            thickness = 3
            if i == landing_pad_index:
                color = green
                thickness = 5
            pygame.draw.line(self.surface, color, coord1, coord2, thickness)
