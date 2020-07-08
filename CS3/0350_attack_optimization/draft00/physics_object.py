import math

CIRCLE_RADIANS = 2*math.pi

def normalizeAngle(angle):
    '''Given an angle, returns an identical angle in the range -pi/2 to pi/2 '''
    angle = angle % CIRCLE_RADIANS
    if angle > math.pi:
        angle -= CIRCLE_RADIANS
    if angle < -math.pi:
        angle += CIRCLE_RADIANS
    return angle

class PhysicsObject:
    def __init__(self, x, y, radius, angle, rotation_rate):
        self.x = x
        self.y = y
        self.radius = radius
        #Initial velocity
        self.dx = 0
        self.dy = 0
        #Current direction
        self.angle = angle
        #How fast this object turns
        self.rotation_rate = rotation_rate
        self.accel = 0.1
        self.friction = 0.15

    def distanceTo(self, other):
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)

    def distanceToCoords(self, x,y):
        return math.sqrt((self.x-x)**2 + (self.y-y)**2)

    def angleTo(self,x,y):
        x = x - self.x
        y = y - self.y
        return math.atan2(y,x)

    def getSmallestTurnAngle(self, goal_angle):
        '''Returns smallest angle to turn toward the goal.'''
        self.angle = normalizeAngle(self.angle)
        goal_angle = normalizeAngle(goal_angle)
        return normalizeAngle(goal_angle - self.angle)

    def getSmallestTurnLoc(self, x,y):
        '''Returns smallest angle to turn toward the given x,y.'''
        a = self.angleTo(x,y)
        return self.getSmallestTurnAngle(a)

    def rotateCounterClockwise(self):
        self.angle -= self.rotation_rate

    def rotateClockwise(self):
        self.angle += self.rotation_rate

    def accelerate(self, angle, accel):
        self.dx = self.dx + math.cos(angle)*accel
        self.dy = self.dy + math.sin(angle)*accel

    def accelerateForward(self):
        self.accelerate(self.angle,self.accel)

    def accelerateBackward(self):
        self.accelerate(self.angle+math.pi,self.accel/2)

    def accelerateLeft(self):
        self.accelerate(self.angle-math.pi/2,self.accel/2)

    def accelerateRight(self):
        self.accelerate(self.angle+math.pi/2,self.accel/2)

    def moveForward(self, speed):
        self.x = self.x+math.cos(self.angle)*speed
        self.y = self.y+math.sin(self.angle)*speed

    def moveBallistic(self):
        self.x += self.dx
        self.y += self.dy

