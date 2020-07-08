import pygame, physics_object, math, bullet

speed = 10
white = 255,255,255

class Player(physics_object.PhysicsObject):
    #Create a player
    def __init__(self, screen, x, y):
        #              x,y,radius, angle, rotation rate
        super().__init__(x, y, 11, 0, math.pi/32)
        self.screen = screen
        #Firing controls
        self.burst_reset = 5 #frames between shots in a burst
        self.burst_countdown = 0 #countdown to next shot
        self.burst_count = 0 #number of shots fired so far in this burst
        self.burst_limit = 3 #number of shots in a burst
        self.cooldown_reset = 120 #frames between bursts
        self.cooldown = 0 #countdown to next burst
        #Attack pattern variables
        self.attack_pattern = [
            #Distance first 100 pixels
            0, #shoot
            -1, #forward or backward
            -1, #yaw closer 1 or further -1
            -1, #turn toward, away, or neither
            #Distance second 100 pixels
            0, #shoot
            0, #forward or backward
            -1, #yaw closer 1 or further -1
            -1, #turn toward, away, or neither
            #2
            1, #shoot
            0, #forward or backward
            -1, #yaw closer or further
            1, #turn toward, away, or neither
            #3
            0, #shoot
            0, #forward or backward
            0, #yaw closer or further
            1, #turn toward, away, or neither
            #4
            0, #shoot
            1, #forward or backward
            1, #yaw closer or further
            1, #turn toward, away, or neither
            #5
            0, #shoot
            1, #forward or backward
            1, #yaw closer or further
            1, #turn toward, away, or neither
            #6
            0, #shoot
            1, #forward or backward
            1, #yaw closer or further
            1, #turn toward, away, or neither
            #7
            0, #shoot
            1, #forward or backward
            1, #yaw closer or further
            1, #turn toward, away, or neither
            #8
            0, #shoot
            1, #forward or backward
            1, #yaw closer or further
            1, #turn toward, away, or neither
            #9
            0, #shoot
            1, #forward or backward
            1, #yaw closer or further
            1 #turn toward, away, or neither
        ]
        #Optimized pattern:
        #self.attack_pattern = [0, -1, -1, -1, 0, 0, 0, 1, 1, 0, -1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1]

    def update(self, target, bullets):
        #Cooldown
        self.cooldown-=1
        self.burst_countdown-=1

        #Get target information
        goal_angle = self.angleTo(target.x,target.y)
        turn = self.getSmallestTurnAngle(goal_angle)
        d = self.distanceTo(target)

        #Get action profile index based on distance
        #The 4's are for the 4 actions in each set: shoot, forward/back, yaw, turn toward/away
        #100 defines the distance between nested rings for different actions
        index = 4*min(int(d/100), (len(self.attack_pattern)/4)-1)

        #Testing:
        #print(d)
        #print(index)
        #print(self.attack_pattern[index:index+4])

        if self.attack_pattern[index]==1: #shoot
            self.shoot(bullets)

        if self.attack_pattern[index+1]==1: #forward or backward
            self.accelerateForward()
        elif self.attack_pattern[index+1]==-1: #forward or backward
            self.accelerateBackward()

        if self.attack_pattern[index+2]==1: #yaw closer or further
            if turn>0:
                self.accelerateRight()
            else:
                self.accelerateLeft()
        if self.attack_pattern[index+2]==-1: #yaw closer or further
            if turn>0:
                self.accelerateLeft()
            else:
                self.accelerateRight()

        if self.attack_pattern[index+3]==1: #turn toward, away, or neither
            self.turnToward(target.x,target.y,close_enough=math.pi/64)
        elif self.attack_pattern[index+3]==-1: #turn toward, away, or neither
            self.turnFrom(target.x,target.y)



    def shoot(self, bullets):
        if self.cooldown<=0 and self.burst_countdown<=0:
            #Count another shot fired in this burst
            self.burst_count += 1
            #Reset burst countdown
            self.burst_countdown = self.burst_reset
            #If we have fired the limit for this burst, reset the cooldown
            if self.burst_count >= self.burst_limit:
                self.cooldown = self.cooldown_reset
                self.burst_count = 0
            #Create new bullet
            b = bullet.Bullet(self.screen, self.x,self.y,self.angle)
            #Add new bullet to list
            bullets.append(b)


    def draw(self):
        #Angles and radii to determine shape of the player
        angles = [0,135,-135] #in degrees
        radii = [18,10,10] #in pixels
        #Draw outline of player.
        points = self.getCorners(radii, angles)
        #5 is line thickness.
        pygame.draw.polygon(self.screen, white, points,1)
        #Draw a "vision" arc
        dist = 40
        green = 0,255,0
        for i in range(-5,6,1):
            x = self.x+math.cos(self.angle+i*math.pi/60)*dist
            y = self.y+math.sin(self.angle+i*math.pi/60)*dist
            pygame.draw.line(self.screen, green, (self.x,self.y),(x,y))

    def getCorners(self, radii, angles):
        #Returns list of points to draw the Player
        points = []
        for i in range(len(angles)):
            a = angles[i]*math.pi/180+self.angle
            x = self.x+radii[i]*math.cos(a)
            y = self.y+radii[i]*math.sin(a)
            points.append((x,y))
        return points
