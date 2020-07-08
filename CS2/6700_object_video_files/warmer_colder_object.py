import random, math

#Encapsulation
class Coordinate:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def distanceTo(self,other):
        #other should be a Coordinate object
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)
    def move(self,angle,distance):
        self.x = self.x + math.cos(angle)*distance
        self.y = self.y + math.sin(angle)*distance
    def print(self):
        print(self.x,',',self.y)

temp_x = random.randint(0,10)
temp_y = random.randint(0,10)
goal = Coordinate(temp_x,temp_y)

start = Coordinate(0,0)

recent_distance = start.distanceTo(goal)

close_enough = 1.0

#While I haven't reached the goal
while recent_distance > close_enough:
    angle = float(input('Give angle in degrees?'))
    distance = float(input('Give distance?'))
    radians = angle * (math.pi/180)
    start.move(radians,distance)
    start.print()
    #Recalculate distance
    new_distance = start.distanceTo(goal)
    #Compare distances and update user regarding
    #progress.
    if new_distance < recent_distance:
        print('WARMER')
    else:
        print('COLDER')
    recent_distance = new_distance

print('Success!')