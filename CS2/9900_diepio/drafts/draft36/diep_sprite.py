from constants import *
import math, pygame, health_bar, random

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
        self.draw_shape=draw_shape

    def canLevelUp(self):
        current_level = self.getCurrentLevel()
        _,potential_level = self.getOverflowExperience()
        return potential_level > current_level

    def levelUp(self, level_index):
        current_level = self.getCurrentLevel()
        _,potential_level = self.getOverflowExperience()
        #Confirm that the sprite can level up
        if potential_level > current_level:
            self.levels[level_index] += 1
            #Make sure there is a new level that can be
            #reached, otherwise refund the level up point
            if len(level_list[level_index]) > self.levels[level_index]:
                #Adjust attributes based on new level
                self.xs[level_index] = level_list[level_index][self.levels[level_index]]
            else:
                print("You've already reached max level.")
                self.levels[level_index] -= 1

    def getCurrentLevel(self):
        #Initially the ship is at level 1 for everything
        current_level = 0
        for level in self.levels:
            current_level += level-1
        return current_level

    def getOverflowExperience(self):
        '''Returns the amount of experience overflowing to the next level
        and returns the level that this sprite could be at if it has spent
        all of its experience points.'''
        temp = self.experience
        potential_level = 0
        for c in level_cutoffs:
            if temp-c>=0:
                temp -= c
                potential_level += 1
        return temp, potential_level

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


    def draw(self, povx, povy, center_on_screen=False):
        r = self.rect.copy()
        if center_on_screen:
            r.x = screen_width_half - self.radius
            r.y = screen_height_half - self.radius
        else:
            #Get coordinate adjustments
            r.x += screen_width_half - povx
            r.y += screen_height_half - povy
            #If this sprite is not on screen, don't draw it
            if self.isOffScreen(r.x, r.y):
                return

        #Draw the main body of the sprite
        if self.draw_shape==SHAPE_CIRCLE:
            pygame.draw.ellipse(self.screen, self.color, r)
        elif self.draw_shape==SHAPE_RECT:
            pygame.draw.rect(self.screen, self.color,r)
        elif self.draw_shape==SHAPE_TRI:
            points = []
            c = 2*math.pi/3
            for i in range(3):
                y = r.y+self.radius+self.radius*math.sin(self.angle+i*c)
                x = r.x+self.radius+self.radius*math.cos(self.angle+i*c)
                points.append((x,y))
            pygame.draw.polygon(self.screen, self.color, points)
        elif self.draw_shape==SHAPE_PENTA:
            points = []
            c = 2*math.pi/5
            for i in range(5):
                y = r.y+self.radius+self.radius*math.sin(self.angle+i*c)
                x = r.x+self.radius+self.radius*math.cos(self.angle+i*c)
                points.append((x,y))
            pygame.draw.polygon(self.screen, self.color, points)
        else:
            print('ERROR in diep_sprite. Unrecognized shape: "'+str(self.draw_shape)+'"')
            pygame.quit(); exit()

        #Draw little heading circle
        if self.draw_heading:
            heading_radius = 10
            heading = pygame.Rect(r.centerx-heading_radius+math.cos(self.angle)*50,
                                  r.centery-heading_radius+math.sin(self.angle)*50,
                                  heading_radius*2,
                                  heading_radius*2)
            pygame.draw.ellipse(self.screen, self.color, heading)
        #Draw healthbar
        if self.draw_healthbar and self.hit_points!=self.xs[HP_INDEX]:
            self.healthbar.setXY(r.x,r.y+r.height)
            self.healthbar.draw()
        #Draw edges of the world
        if center_on_screen:
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

    def distanceTo(self, other):
        if other is None:
            print('ERROR in distanceTo. You cannot ask for the distance to None.')
            return 0
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)

    def angleToSprite(self,other):
        if other is None:
            print('ERROR in angleTo. You cannot ask for the angle to None.')
            return 0
        return self.angleTo(other.x, other.y)

    def angleTo(self,x,y):
        x = x - self.x
        y = y - self.y
        return math.atan2(y,x)

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