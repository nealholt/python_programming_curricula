import math, pygame, random, cannon_ball, animation
from functions import *

pygame.init()

font = pygame.font.SysFont('Arial', 50)

class GameManager:
    def __init__(self):
        #Points gained by the player
        self.points = 0
        #Lives remaining for the player
        self.lives = 3

        #Load icon for lives
        self.compass,compass_rect = load_image('images/compass_1.png',-1)
        #Scale down the image
        dimensions = (int(compass_rect.width*compass_scaling), int(compass_rect.height*compass_scaling))
        self.compass = pygame.transform.scale(self.compass, dimensions)

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

        #Load the sword image
        self.sword,sword_rect = load_image('images/sword_1.png',-1)
        #Scale down the image
        dimensions = (int(sword_rect.width*scaling), int(sword_rect.height*scaling))
        self.sword = pygame.transform.scale(self.sword, dimensions)

        #Create a list of pickups
        self.pickups = []
        #Countdown until next rum spawn
        self.rum_spawn_countdown = 0
        #Countdown until next sword spawn
        self.sword_spawn_countdown = 0

        #List of all cannonballs
        self.cannonballs = []

        #List of animations. For now it is all explosions.
        self.animations = []

        self.explosion_frames = strip_from_sheet()

    def shoot(self, ship, direction_right):
        x,y = ship.getCenter()
        angle = -(math.pi/180)*ship.angle-cannon_ball_arc
        if not direction_right:
            angle = math.pi-angle+cannon_ball_arc
        ball = cannon_ball.CannonBall(x,y,math.cos(angle)*cannon_ball_speed,math.sin(angle)*cannon_ball_speed)
        self.cannonballs.append(ball)
        a = animation.AnimatedSprite(x,y, smoke_dx,0,self.explosion_frames, dwell_sequence)
        self.animations.append(a)

    def updateCannonBalls(self):
        for i in reversed(range(len(self.cannonballs))):
            self.cannonballs[i].update()
            x = self.cannonballs[i].x
            y = self.cannonballs[i].y
            height = getWaterHeightAt(x,self.water_heights)
            #If the ball hit the water or moved off screen, delete it
            if x<0 or x >screen_width or y>height:
                del self.cannonballs[i]

    def updatePickups(self):
        #Countdown until next rum spawn
        self.rum_spawn_countdown -= 1
        if self.rum_spawn_countdown < 0:
            x = screen_width
            y = random.randint(0,screen_height-sea_level-spawn_above_sea_level)
            speed = random.randint(rum_scroll_speed_min, rum_scroll_speed_max)
            self.pickups.append((x,y,speed,'rum'))
            self.rum_spawn_countdown = random.randint(rum_respawn_min, rum_respawn_max)
        #Countdown until next sword spawn
        self.sword_spawn_countdown -= 1
        if self.sword_spawn_countdown < 0:
            x = screen_width
            y = random.randint(0,screen_height-sea_level-spawn_above_sea_level)
            speed = random.randint(rum_scroll_speed_min, rum_scroll_speed_max)
            self.pickups.append((x,y,speed,'sword'))
            self.sword_spawn_countdown = random.randint(sword_respawn_min, sword_respawn_max)
        #Move all the pickups to the left
        for i in reversed(range(len(self.pickups))):
            x,y,speed,typ = self.pickups[i]
            x = x-speed
            if x+self.rum_rect.width < 0:
                del self.pickups[i]
            else:
                self.pickups[i] = (x,y,speed,typ)

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
                if self.pickups[i][3]=='rum':
                    self.points+=1
                else:
                    self.lives -= 1
                del self.pickups[i]

    def draw(self, surface):
        #Draw water
        pygame.draw.polygon(surface, blue, self.pointlist)
        #Draw pickups
        for x,y,_,typ in self.pickups:
            self.rum_rect.center = (x,y)
            if typ=='rum':
                surface.blit(self.rum, self.rum_rect)
            else:
                surface.blit(self.sword, self.rum_rect)
        #Draw cannonballs
        for b in self.cannonballs:
            b.draw(surface)
        #Draw animations and update and delete them
        for i in reversed(range(len(self.animations))):
            self.animations[i].update()
            self.animations[i].draw(surface)
            if self.animations[i].isDone():
                del self.animations[i]
        #Display points
        text = font.render(str(self.points),True,yellow)
        surface.blit(text, (screen_width-150,15))
        #Display lives
        for i in range(self.lives):
            surface.blit(self.compass, (screen_width-120+i*30,10))




