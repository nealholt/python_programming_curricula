import pygame, math, random

pygame.init()

friction = 0.1
border_shove_impulse = 0.1
world_size = 2000

'''TODO next steps:
6.
7.
8. Implement collisions with food.
9. Implement shooting
10. Drawing can be more efficient. Only draw things that are on
the screen, for one thing.
11. Make enemy tracking like the moveToward and moveAway functions

Keep this initially separate then make a third project integrating this
with maze navigator.
'''

class DiepSprite:
    def __init__(self, screen, x, y, color, radius, accel, draw_heading=True):
        self.screen = screen
        self.color = color
        self.x = x+radius #center x
        self.y = y+radius #center y
        self.angle = 0
        self.radius = radius
        self.rect = pygame.Rect(self.x-self.radius,
                                self.y-self.radius,
                                self.radius*2,
                                self.radius*2)
        self.accel = accel
        self.dx = 0
        self.dy = 0
        self.draw_heading = draw_heading
        #elasticity and bounce_friction effect how sprites bounce
        #off of each other.
        self.elasticity = 1
        self.bounce_friction = 0
        #shove_impulse affects how strongly one sprite shoves out another
        self.shove_impulse = 0.6
        #If the sprite is not circular then it is rectangular.
        #This effects bouncing and shoving.
        self.circular = True

    def rotate(self, turn_amount):
        self.angle += turn_amount
        self.dx = math.cos(self.angle)
        self.dy = math.sin(self.angle)

    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.rect = pygame.Rect(self.x-self.radius,
                                self.y-self.radius,
                                self.radius*2,
                                self.radius*2)

    def moveAmount(self, x_amount, y_amount):
        self.x += x_amount
        self.y += y_amount
        self.rect = pygame.Rect(self.x-self.radius,
                                self.y-self.radius,
                                self.radius*2,
                                self.radius*2)

    def update(self):
        self.move()
        #apply friction
        self.dx = (1-friction)*self.dx
        self.dy = (1-friction)*self.dy
        #Keep critter in bounds
        if self.x<0:
            self.dx += border_shove_impulse
        elif self.x > world_size:
            self.dx -= border_shove_impulse
        if self.y<0:
            self.dy += border_shove_impulse
        elif self.y > world_size:
            self.dy -= border_shove_impulse

    def draw(self, povx, povy):
        #Get coordinate adjustments
        x_adjust = self.screen.get_width()/2 - povx
        y_adjust = self.screen.get_height()/2 - povy
        r = self.rect.copy()
        r.x += x_adjust
        r.y += y_adjust
        pygame.draw.ellipse(self.screen, self.color, r)
        #Draw little heading circle
        if self.draw_heading:
            heading_radius = 10
            heading = pygame.Rect(x_adjust+self.x-heading_radius+math.cos(self.angle)*100,
                                  y_adjust+self.y-heading_radius+math.sin(self.angle)*100,
                                  heading_radius*2,
                                  heading_radius*2)
            pygame.draw.ellipse(self.screen, self.color, heading)

    def distanceTo(self, other):
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)

    def angleTo(self,x,y):
        x = x - self.x
        y = y - self.y
        return math.atan2(y,x)

    def depthOfPenetration(self, other):
        #Return the depth of penetration of one sprite into the other.
        #Will return negative values if the sprites are not touching.
        return (self.radius + other.radius) - self.distanceTo(other)

    '''Bounce off the other sprite off of this using vectors
    http://stackoverflow.com/questions/573084/how-to-calculate-bounce-angle
    '''
    def bounceOff(self, other):
        #Get the dy and dx components of the line from
        #this.center to other.center
        normal_vector = [self.x - other.x,
                        self.y - other.y ]
        #Separate other's velocity into the part perpendicular
        #to other, u, and the part parallel to other, w.
        v_dot_n = self.dx*normal_vector[0] + self.dy*normal_vector[1]
        square_of_norm_length = normal_vector[0]**2 + normal_vector[1]**2
        multiplier = v_dot_n / square_of_norm_length
        u_vector = [normal_vector[0]*multiplier,
                    normal_vector[1]*multiplier ]
        w_vector = [self.dx - u_vector[0],
                    self.dy - u_vector[1] ]
        #Determine the velocity post collision while
        #factoring in the elasticity and friction of
        #the wall.
        self.dx = w_vector[0]*(1-self.bounce_friction)-u_vector[0]*self.elasticity
        self.dy = w_vector[1]*(1-self.bounce_friction)-u_vector[1]*self.elasticity

    #Moves the other sprite out of collision with this sprite
    def moveOut(self, other):
        #Get angle to other
        angle = self.angleTo(other.x, other.y)
        #get dx and dy towards other.
        temp_dx = math.cos(angle)
        temp_dy = math.sin(angle)
        #Rectangular collision is the default so only
        #use a circular collision check if the other
        #sprite is also circular, otherwise defer to the
        #other sprite.
        if other.circular:
            #Get the amount of overlap.
            overlap = self.depthOfPenetration(other)
            #Move other out by the appropriate amount
            other.moveAmount(temp_dx*overlap, temp_dy*overlap)
            #Bounce other out
            other.bounceOff(self)

    #Shoves the other sprite out of collision with this sprite
    def shoveOut(self, other):
        #Get angle to other
        angle = self.angleTo(other.x, other.y)
        #get dx and dy towards other.
        temp_dx = math.cos(angle)
        temp_dy = math.sin(angle)
        #Rectangular collision is the default so only
        #use a circular collision check if the other
        #sprite is also circular, otherwise defer to the
        #other sprite.
        if other.circular:
            #Shove other out by the appropriate amount
            other.dx += temp_dx*self.shove_impulse
            other.dy += temp_dy*self.shove_impulse


class PlayerCritter(DiepSprite):
    def __init__(self, screen, x, y, color, radius, accel):
        super().__init__(screen, x, y, color, radius, accel)

    def update(self):
        pos = pygame.mouse.get_pos()
        x = pos[0] - self.screen.get_width()/2
        y = pos[1] - self.screen.get_height()/2
        self.angle = math.atan2(y,x)
        super().update()

    #Override super class's draw function
    def draw(self, povx, povy):
        r = self.rect.copy()
        center_x = self.screen.get_width()/2
        center_y = self.screen.get_height()/2
        r.x = center_x - self.radius
        r.y = center_y - self.radius
        pygame.draw.ellipse(self.screen, self.color, r)
        #Draw little heading circle
        heading_radius = 10
        heading = pygame.Rect(center_x-heading_radius+math.cos(self.angle)*100,
                              center_y-heading_radius+math.sin(self.angle)*100,
                              heading_radius*2,
                              heading_radius*2)
        pygame.draw.ellipse(self.screen, self.color, heading)
        #Draw edges of the world
        x_diff = screen_width/2 - self.x
        if x_diff > 0:
            pygame.draw.rect(self.screen, green, [0,0,x_diff,screen_height])
        elif world_size - self.x < screen_width/2:
            x_diff = screen_width/2-(world_size-self.x)
            pygame.draw.rect(self.screen, green, [screen_width-x_diff,0,x_diff,screen_height])
        y_diff = screen_height/2 - self.y
        if y_diff > 0:
            pygame.draw.rect(self.screen, green, [0,0,screen_width,y_diff])
        elif world_size - self.y < screen_height/2:
            y_diff = screen_height/2-(world_size-self.y)
            pygame.draw.rect(self.screen, green, [0,screen_height-y_diff,screen_width,y_diff])



class EnemyCritter(DiepSprite):
    def __init__(self, screen, x, y, color, radius, target, accel):
        super().__init__(screen, x, y, color, radius, accel)
        self.target = target

    #Override super class's update function
    def update(self):
        self.angle = self.angleTo(self.target.x, self.target.y)
        '''self.dx = math.cos(self.angle)
        self.dy = math.sin(self.angle)
        self.move()'''
        #goal_dx = math.cos(self.angle)
        #goal_dy = math.sin(self.angle)
        #TODO LEFT OFF HERE
        self.dx += math.cos(self.angle)*self.accel
        self.dy += math.sin(self.angle)*self.accel
        super().update()


#Initialize variables:
clock = pygame.time.Clock()
screen_width = 1100
screen_height = 650
screen = pygame.display.set_mode((screen_width,screen_height))
green = 0,255,0
red = 255,0,0
blue = 0,0,255
green = 0,255,0
yellow = 255,255,0
white = 255,255,255
black = 0,0,0

critter = PlayerCritter(  screen,
                        100,#x
                        100,#y
                        blue,
                        50,#radius
                        0.4)#acceleration

npc_critter = EnemyCritter(screen,
                          200,#x
                          200,#y
                          yellow,
                          35,#radius
                          critter,#target of enemy
                          0.2)#acceleration

foods = []
food_radius = 15
food_count = 100
for i in range(food_count):
    f = DiepSprite(screen,
                    random.randint(0,world_size-food_radius*2),#x
                    random.randint(0,world_size-food_radius*2),#y
                    red, food_radius, 0, draw_heading=False)
    foods.append(f)

#Main program loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            #print(event.key) #Print value of key press
            if event.key == pygame.K_ESCAPE:
                done = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        critter.dy -= critter.accel
    if keys[pygame.K_DOWN]:
        critter.dy += critter.accel
    if keys[pygame.K_LEFT]:
        critter.dx -= critter.accel
    if keys[pygame.K_RIGHT]:
        critter.dx += critter.accel

    #Collision check
    if critter.depthOfPenetration(npc_critter) > 0:
        critter.shoveOut(npc_critter)
        npc_critter.shoveOut(critter)

    screen.fill((0,0,0)) #fill screen with black
    #Update and draw critters
    critter.update()
    critter.draw(critter.x, critter.y)
    npc_critter.update()
    npc_critter.draw(critter.x, critter.y)
    for f in foods:
        f.update()
        f.draw(critter.x, critter.y)
    pygame.display.flip()
    pygame.display.update()
    #Delay to get 60 fps
    clock.tick(60)
pygame.quit()