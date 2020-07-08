import pygame, math, line_segment

display_sensors = False
crash_limit = 7 #Getting this close to a wall signifies a crash
speed_max = 5
acceleration = 0.004 #percentage of max speed per frame
white = 255,255,255
default_vision_length = 400

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
        self.rotation_rate = math.pi/128
        self.speed_percent = 0
        self.crashed = False
        self.line_thickness = 1
        #vision sensors
        self.resetVision()

    def resetVision(self):
        self.vision = []
        color = (255,255,0)
        for i in range(-2,3):
            a = self.angle+i*math.pi/4
            x2 = self.x+math.cos(a)*default_vision_length
            y2 = self.y+math.sin(a)*default_vision_length
            sensor = line_segment.LineSeg(self.screen, color, self.x, self.y, x2, y2)
            self.vision.append(sensor)

    def getSensorLengths(self):
        lengths = []
        for v in self.vision:
            length = v.getLength()
            lengths.append(length)
            if length < crash_limit:
                self.crashed = True
        return lengths

    def getSensorPercents(self):
        percents=self.getSensorLengths()
        for i in range(len(percents)):
            percents[i] = percents[i]/default_vision_length
        return percents

    def accelerate(self):
        self.speed_percent = min(self.speed_percent+acceleration,1)

    def brake(self):
        self.speed_percent = max(self.speed_percent-acceleration,0)

    def getSensorData(self):
        '''This is the data that will be fed directly to
        the neural net.'''
        data = self.getSensorPercents()
        data.append(self.speed_percent)
        #Angle in the range 0 to 1
        #print()
        #print(self.angle)
        while self.angle < 0:
            self.angle += 2*math.pi
        self.angle = self.angle % (2*math.pi)
        #print(self.angle)
        data.append(self.angle / (2*math.pi))
        return data

    def respondToInput(self, inputs):
        '''This function makes the car respond to neural
        net input.

        inputs should be a length 2 list

        All the inputs should be between 0 and 1.'''
        if inputs[0] < 0.3333:
            self.rotateLeft()
        elif inputs[0] > 0.6666:
            self.rotateRight()

        if inputs[1] < 0.3333:
            self.accelerate()
        elif inputs[1] > 0.6666:
            self.brake()

    def senseTrack(self, track):
        '''Pre: track is a list of line segments.'''
        for seg in track:
            for i in range(len(self.vision)):
                intersection = self.vision[i].getIntersection(seg)
                if intersection != None:
                    self.vision[i].x2 = intersection[0]
                    self.vision[i].y2 = intersection[1]

    def moveForward(self):
        if not self.crashed:
            self.x = self.x+math.cos(self.angle)*self.speed_percent*speed_max
            self.y = self.y+math.sin(self.angle)*self.speed_percent*speed_max

    def moveBackward(self):
        self.x = self.x-math.cos(self.angle)*self.speed_percent*speed_max
        self.y = self.y-math.sin(self.angle)*self.speed_percent*speed_max
        self.crashed = False

    def rotateLeft(self):
        self.angle -= self.rotation_rate

    def rotateRight(self):
        self.angle += self.rotation_rate

    def contains(self, point):
        return self.distanceTo(point) < crash_limit

    def distanceTo(self, point):
        return math.sqrt((point[0]-self.x)**2 + (point[1]-self.y)**2)

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
        pygame.draw.polygon(self.screen, white, points,self.line_thickness)
        if display_sensors:
            for v in self.vision:
                v.draw()
