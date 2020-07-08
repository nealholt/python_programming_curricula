import pygame, math, line_segment

speed = 10
white = 255,255,255

class Player:
    #Create a player
    def __init__(self, screen, x, y):
        self.screen = screen
        #Coordinates of the center of the player
        self.x = x
        self.y = y
        #Current direction player is facing
        self.angle = 0
        #How fast this player turns
        self.rotation_rate = math.pi/32
        #vision sensors
        self.resetVision()

    def resetVision(self):
        self.vision = []
        color = (255,255,0)
        dist = 500
        for i in range(-2,3):
            a = self.angle+i*math.pi/4
            x2 = self.x+math.cos(a)*dist
            y2 = self.y+math.sin(a)*dist
            sensor = line_segment.LineSeg(self.screen, color, self.x, self.y, x2, y2)
            self.vision.append(sensor)

    def moveForward(self):
        self.x = self.x+math.cos(self.angle)*speed
        self.y = self.y+math.sin(self.angle)*speed
        self.resetVision()

    def rotateLeft(self):
        self.angle -= self.rotation_rate
        self.resetVision()

    def rotateRight(self):
        self.angle += self.rotation_rate
        self.resetVision()

    def getCorners(self, radii, angles):
        #Returns list of points to draw the Player
        points = []
        for i in range(len(angles)):
            a = angles[i]*math.pi/180+self.angle
            x = self.x+radii[i]*math.cos(a)
            y = self.y+radii[i]*math.sin(a)
            points.append((x,y))
        return points

    def draw(self):
        #Angles and radii to determine shape of the player
        angles = [0,135,-135] #in degrees
        radii = [12,10,10] #in pixels
        #Draw outline of player.
        points = self.getCorners(radii, angles)
        #1 is line thickness.
        pygame.draw.polygon(self.screen, white, points,1)
        for v in self.vision:
            v.draw()
