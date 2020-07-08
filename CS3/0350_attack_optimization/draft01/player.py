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
        self.burst_countdown = self.burst_reset #countdown to next shot
        self.burst_count = 0 #number of shots fired so far in this burst
        self.burst_limit = 3 #number of shots in a burst
        self.cooldown_reset = 120 #frames between bursts
        self.cooldown = self.cooldown_reset #countdown to next burst
        #Attack pattern variables
        self.attack_pattern = [
            300, #accelerate forward min distance condition
            600, #TODO UNUSED accelerate forward max distance condition
            2*math.pi/3, #accelerate forward angle condition
            50, #shoot min distance condition
            400, #shoot max distance condition
            math.pi/32, #shoot angle condition
            200, #avoidance min distance condition
            math.pi/2, #TODO UNUSED avoidance counter angle
            80, #TODO UNUSED avoidance distance
            math.pi/64 #turn toward buffer
        ]

    def update(self, target, bullets):
        #Cooldown
        self.cooldown-=1
        self.burst_countdown-=1

        #Get target information
        goal_angle = self.angleTo(target.x,target.y)
        turn = self.getSmallestTurnAngle(goal_angle)
        d = self.distanceTo(target)

        #Avoidance
        if d<self.attack_pattern[6]:
            #Turn away
            self.turnFrom(target.x,target.y)
            #Accelerate
            self.accelerateForward()
            #Do nothign else
            return

        #Accelerate toward
        if d>self.attack_pattern[0] and abs(turn)<self.attack_pattern[2]:
            self.accelerateForward()

        #Turn toward
        self.turnToward(target.x,target.y,close_enough=self.attack_pattern[9])

        #Shoot
        if d>self.attack_pattern[3] and d<self.attack_pattern[4] and abs(turn)<self.attack_pattern[5]:
            self.shoot(bullets)


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
