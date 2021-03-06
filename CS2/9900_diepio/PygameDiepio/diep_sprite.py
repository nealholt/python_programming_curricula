from constants import *
import math, pygame, health_bar, random
from funcs import adjustScreenCoordinates

class DiepSprite:
    def __init__(self, screen, x, y, color, radius, base_level,
                draw_shape=SHAPE_CIRCLE,
                sprite_type=TYPE_FOOD,
                draw_heading=True,
                draw_healthbar=True):
        self.screen = screen
        self.color = color
        self.x = x+radius #center x
        self.y = y+radius #center y
        self.angle = random.random()*math.pi*2
        self.radius = radius
        self.collision_radius = radius
        self.rect = pygame.Rect(self.x-self.radius,
                                self.y-self.radius,
                                self.radius*2,
                                self.radius*2)
        self.sprite_type = sprite_type

        #Levels of this sprite.
        self.levels = [base_level for _ in range(len(level_list))]
        #Current attributes based on level
        self.xs = [level_list[i][self.levels[i]] for i in range(len(self.levels))]

        #self.xs only stores the max hitpoints. Current hit
        #points are stored in this variable.
        self.hit_points = self.xs[HP_INDEX]

        self.dx = 0
        self.dy = 0
        self.draw_heading = draw_heading
        #elasticity and bounce_friction effect how sprites bounce
        #off of each other.
        self.elasticity = 1
        self.bounce_friction = 0
        #If the sprite is not circular then it is rectangular.
        #This effects bouncing and shoving.
        self.circular = True
        self.draw_healthbar = draw_healthbar
        self.healthbar = None
        self.resetHealthbar(screen, self.hit_points)
        self.experience = 0 #This is always the total experience
        #Set the draw function for this sprite
        self.setShape(draw_shape)

        self.drawHeadingIndicator = self.drawDefaultHeadingIndicator

    def setShape(self, draw_shape):
        if draw_shape==SHAPE_CIRCLE:
            self.drawSpriteBody = self.drawSpriteBodyCircle
        elif draw_shape==SHAPE_RECT:
            self.drawSpriteBody = self.drawSpriteBodyRect
        elif draw_shape==SHAPE_TRI:
            self.drawSpriteBody = self.drawSpriteBodyTri
        elif draw_shape==SHAPE_PENTA:
            self.drawSpriteBody = self.drawSpriteBodyPenta
        elif draw_shape==SHAPE_SPIKY:
            self.drawSpriteBody = self.drawSpriteBodySpiky
        else:
            print('ERROR in diep_sprite. Unrecognized shape: "'+str(draw_shape)+'"')
            pygame.quit(); exit()

    def resetHealthbar(self,screen,hp):
        if self.draw_healthbar:
            self.hit_points = hp
            self.healthbar = health_bar.HealthBar(screen,0,0,self.radius*2,10,self.xs[HP_INDEX])
            self.healthbar.updateHp(hp)

    def getExperienceGiven(self):
        #Returns how much experience this sprite gives when
        #someone else kills it.
        return self.experience

    def takeDamage(self, damage):
        '''This can also be used to gain health by passing
        in negative damage.'''
        #Reduce positive damage by the armor multiplier
        if damage > 0:
            damage = self.xs[ARMOR_INDEX] * damage
        #Get the new hit point value. Keep it under maximum.
        self.hit_points = min(self.xs[HP_INDEX], self.hit_points-damage)
        #Update the health bar.
        if self.draw_healthbar:
            self.healthbar.updateHp(self.hit_points)

    def rotate(self, turn_amount):
        self.angle += turn_amount
        self.dx = math.cos(self.angle)
        self.dy = math.sin(self.angle)

    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.rect.x = self.x-self.radius
        self.rect.y = self.y-self.radius

    def moveAmount(self, x_amount, y_amount):
        self.x += x_amount
        self.y += y_amount
        self.rect.x = self.x-self.radius
        self.rect.y = self.y-self.radius

    def moveTo(self, x, y):
        self.x = x
        self.y = y
        self.rect.x = self.x-self.radius
        self.rect.y = self.y-self.radius

    def teleport(self):
        self.moveTo(random.randint(0,world_size-self.radius*2),
                    random.randint(0,world_size-self.radius*2))

    def reset(self):
        self.teleport()
        if self.draw_healthbar:
            self.hit_points = self.xs[HP_INDEX]
            self.healthbar.updateHp(self.hit_points)

    def update(self):
        self.move()
        #apply friction
        self.dx = (1-self.xs[FRICTION_INDEX])*self.dx
        self.dy = (1-self.xs[FRICTION_INDEX])*self.dy
        #Keep critter in bounds
        if self.x<0:
            self.dx += border_shove_impulse
        elif self.x > world_size:
            self.dx -= border_shove_impulse
        if self.y<0:
            self.dy += border_shove_impulse
        elif self.y > world_size:
            self.dy -= border_shove_impulse

    def isOffScreen(self, x_adjust, y_adjust):
        return x_adjust > screen_width or \
                x_adjust+self.rect.width < 0 or \
                y_adjust > screen_height or \
                y_adjust+self.rect.height < 0

    def getScreenRect(self,povx, povy, center_on_screen):
        '''Returns a rectangle to be used for displaying this
        sprite on the screen.'''
        r = self.rect.copy()
        if center_on_screen:
            r.x = screen_width_half - self.radius
            r.y = screen_height_half - self.radius
        else:
            #Get coordinate adjustments
            r.x,r.y = adjustScreenCoordinates(r.x,r.y, povx, povy)
        return r

    def drawSpriteBodyCircle(self, r):
        pygame.draw.ellipse(self.screen, self.color, r)
    def drawSpriteBodyRect(self, r):
        pygame.draw.rect(self.screen, self.color,r)
    def drawSpriteBodyTri(self, r):
        points = []
        c = 2*math.pi/3
        for i in range(3):
            y = r.y+self.radius+self.radius*math.sin(self.angle+i*c)
            x = r.x+self.radius+self.radius*math.cos(self.angle+i*c)
            points.append((x,y))
        pygame.draw.polygon(self.screen, self.color, points)
    def drawSpriteBodyPenta(self, r):
        points = []
        c = 2*math.pi/5
        for i in range(5):
            y = r.y+self.radius+self.radius*math.sin(self.angle+i*c)
            x = r.x+self.radius+self.radius*math.cos(self.angle+i*c)
            points.append((x,y))
        pygame.draw.polygon(self.screen, self.color, points)
    def drawSpriteBodySpiky(self, r):
        #Draw the body of the sprite
        points = []
        spike_count = 20
        increment = 2*math.pi/spike_count
        for i in range(20):
            adjust = self.radius*1.2
            if i%2:
                adjust = self.radius*0.8
            x = math.cos(increment*i)*adjust+r.x+self.radius
            y = math.sin(increment*i)*adjust+r.y+self.radius
            points.append((x,y))
        pygame.draw.polygon(self.screen, self.color, points)


    def drawDefaultHeadingIndicator(self,r):
        heading_radius = 10
        heading = pygame.Rect(r.centerx-heading_radius+math.cos(self.angle)*50,
                              r.centery-heading_radius+math.sin(self.angle)*50,
                              heading_radius*2,
                              heading_radius*2)
        pygame.draw.ellipse(self.screen, self.color, heading)


    def drawHeadingMachineGun(self,r):
        points = []
        adjust = math.pi/16
        distance = 35
        x = r.centerx+math.cos(self.angle+adjust)*distance
        y = r.centery+math.sin(self.angle+adjust)*distance
        points.append((int(x),int(y)))
        
        x = r.centerx+math.cos(self.angle-adjust)*distance
        y = r.centery+math.sin(self.angle-adjust)*distance
        points.append((int(x),int(y)))

        adjust = math.pi/8
        distance = 70
        x = r.centerx+math.cos(self.angle-adjust)*distance
        y = r.centery+math.sin(self.angle-adjust)*distance
        points.append((int(x),int(y)))
        
        x = r.centerx+math.cos(self.angle+adjust)*distance
        y = r.centery+math.sin(self.angle+adjust)*distance
        points.append((int(x),int(y)))

        pygame.draw.polygon(self.screen, self.color, points)
    

    def drawHeadingSniper(self,r):
        points = []
        width = 15
        distance = 35

        adjust = math.pi/2
        cos90 = math.cos(self.angle+adjust)
        sin90 = math.sin(self.angle+adjust)
        cos_angle = math.cos(self.angle)
        sin_angle = math.sin(self.angle)

        x = r.centerx + cos90*width + cos_angle*distance
        y = r.centery + sin90*width + sin_angle*distance
        points.append((int(x),int(y)))
        
        x = r.centerx - cos90*width + cos_angle*distance
        y = r.centery - sin90*width + sin_angle*distance
        points.append((int(x),int(y)))

        distance = 80
        x = r.centerx - cos90*width + cos_angle*distance
        y = r.centery - sin90*width + sin_angle*distance
        points.append((int(x),int(y)))

        x = r.centerx + cos90*width + cos_angle*distance
        y = r.centery + sin90*width + sin_angle*distance
        points.append((int(x),int(y)))

        pygame.draw.polygon(self.screen, self.color, points)


    def drawWorldEdge(self):
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

    def drawVisionRadius(self):
        #Draw vision radius
        x = screen_width_half - self.xs[VISION_RADIUS_INDEX]
        y = screen_height_half - self.xs[VISION_RADIUS_INDEX]
        size = 2*self.xs[VISION_RADIUS_INDEX]
        pygame.draw.ellipse(self.screen, white, (x,y,size,size), 1)

    def draw(self, povx, povy, center_on_screen=False):
        r = self.getScreenRect(povx, povy, center_on_screen)
        #If this sprite is not on screen, don't draw it
        if self.isOffScreen(r.x, r.y):
            return
        #Draw the body of the sprite
        self.drawSpriteBody(r)
        #Draw little heading circle
        if self.draw_heading:
            self.drawHeadingIndicator(r)
        #Draw healthbar
        if self.draw_healthbar and self.hit_points!=self.xs[HP_INDEX]:
            self.healthbar.setXY(r.x,r.y+r.height)
            self.healthbar.draw()
        #This sprite is currently centered on the screen
        if center_on_screen:
            self.drawWorldEdge()
            self.drawVisionRadius()

    def distanceTo(self, other):
        if other is None:
            print('ERROR in distanceTo. You cannot ask for the distance to None.')
            return 0
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)

    def distanceToCoordinate(self, x,y):
        return math.sqrt((self.x-x)**2 + (self.y-y)**2)

    def angleToSprite(self,other):
        if other is None:
            print('ERROR in angleTo. You cannot ask for the angle to None.')
            return 0
        return self.angleTo(other.x, other.y)

    def angleTo(self,x,y):
        x = x - self.x
        y = y - self.y
        return math.atan2(y,x)

    def moveTowardLocationAccel(self,x,y,accel):
        angle = self.angleTo(x,y)
        self.dx += math.cos(angle)*accel
        self.dy += math.sin(angle)*accel

    def depthOfPenetration(self, other):
        #Return the depth of penetration of one sprite into the other.
        #Will return negative values if the sprites are not touching.
        return (self.collision_radius + other.collision_radius) - self.distanceTo(other)

    def collidedWith(self, other):
        if self.depthOfPenetration(other) > 0:
            if self.sprite_type == TYPE_BULLET and self.shooter == other:
                return False
            elif other.sprite_type == TYPE_BULLET and self == other.shooter:
                return False
            else:
                return True
        else:
            return False

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
            other.dx += temp_dx*self.xs[SHOVE_INDEX]
            other.dy += temp_dy*self.xs[SHOVE_INDEX]

    def getDefault(self,index):
        '''Get default value at given level for the
        given attribute index.'''
        return getDefault(self.levels[index],index)

    def revertAll(self):
        '''Revert stats to default values.
        This called from ship.py'''
        for i in range(len(self.xs)):
            self.xs[i] = self.getDefault(i)
        self.use_seeking = False
        self.setShape(SHAPE_CIRCLE)
        self.draw_heading = True
        self.can_shoot = True
        self.drawHeadingIndicator = self.drawDefaultHeadingIndicator
