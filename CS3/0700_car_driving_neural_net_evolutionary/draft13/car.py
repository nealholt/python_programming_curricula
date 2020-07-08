import pygame, math, line_segment

#Whether or not to draw sensor lines
display_sensors = False
#Getting this close to a wall signifies a crash
crash_limit = 7
#Max speed of all cars in pixels per frame
speed_max = 5
#Acceleration as a percentage of max speed per frame
acceleration = 0.004
#How far vision senses extend
default_vision_length = 400
#car color
white = 255,255,255

class Car:
    #Create a player
    def __init__(self, screen, x, y):
        self.screen = screen
        #Coordinates of the center of the player
        self.x = x
        self.y = y
        #Current direction player is facing
        self.angle = -4*math.pi/3
        #How fast this player turns
        self.rotation_rate = math.pi/128
        #Current speed as a percent of max speed
        self.speed_percent = 0
        #Whether or not the car crashed
        self.crashed = False
        #Line thickness at which to draw this car
        self.line_thickness = 1
        #vision sensors
        self.resetVision()

    def resetVision(self):
        '''Create 5 line segments extending outward from this
        object in a 180 degree arc. Collisions between these
        lines and the race track are used to sense how close
        to the wall a car is.'''
        self.vision = []
        color = (255,255,0)
        for i in range(-2,3):
            a = self.angle+i*math.pi/4
            x2 = self.x+math.cos(a)*default_vision_length
            y2 = self.y+math.sin(a)*default_vision_length
            sensor = line_segment.LineSeg(self.screen, color, self.x, self.y, x2, y2)
            self.vision.append(sensor)

    def getSensorLengths(self):
        '''Get a list of lengths of the sensors. This is a measure
        of how far away the walls of the race course are.
        Also check to see if this car crashed.'''
        lengths = []
        for v in self.vision:
            length = v.getLength()
            lengths.append(length)
            #Check if this car crashed
            if length < crash_limit:
                self.crashed = True
        return lengths

    def getSensorPercents(self):
        '''Get a list of the percentage lengths of all
        the sensors. This is handy for feeding data to the
        neural network in the range 0 to 1.'''
        percents=self.getSensorLengths()
        for i in range(len(percents)):
            percents[i] = percents[i]/default_vision_length
        return percents

    def accelerate(self):
        self.speed_percent = min(self.speed_percent+acceleration,1)

    def brake(self):
        self.speed_percent = max(self.speed_percent-acceleration,0)

    def getSensorData(self):
        '''Get and return the data that will be fed directly to
        the neural net.'''
        data = self.getSensorPercents()
        data.append(self.speed_percent)
        #Normalize the angle
        while self.angle < 0:
            self.angle += 2*math.pi
        self.angle = self.angle % (2*math.pi)
        #Append an angle value in the range 0 to 1
        data.append(self.angle / (2*math.pi))
        return data

    def respondToInput(self, inputs):
        '''This function makes the car respond to neural
        net input.

        inputs should be a length 2 list of values
        between 0 and 1.'''
        if inputs[0] < 0.3333:
            self.rotateLeft()
        elif 0.6666 < inputs[0]:
            self.rotateRight()

        if inputs[1] < 0.3333:
            self.accelerate()
        elif 0.6666 < inputs[1]:
            self.brake()

    def senseTrack(self, track):
        '''track is a list of line segments.
        This function checks collisions between this car's
        sensors and the track and shortens the sensors
        so that they end at the point of collision.'''
        for seg in track:
            for i in range(len(self.vision)):
                intersection = self.vision[i].getIntersection(seg)
                if intersection != None:
                    self.vision[i].x2 = intersection[0]
                    self.vision[i].y2 = intersection[1]

    def moveForward(self):
        self.x = self.x+math.cos(self.angle)*self.speed_percent*speed_max
        self.y = self.y+math.sin(self.angle)*self.speed_percent*speed_max

    def moveBackward(self):
        self.x = self.x-math.cos(self.angle)*self.speed_percent*speed_max
        self.y = self.y-math.sin(self.angle)*self.speed_percent*speed_max

    def rotateLeft(self):
        self.angle -= self.rotation_rate

    def rotateRight(self):
        self.angle += self.rotation_rate

    def contains(self, point):
        '''Check to see if this object contains the point.
        This is used for letting the user click on cars.'''
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
        #Draw the sensors
        if display_sensors:
            for v in self.vision:
                v.draw()
