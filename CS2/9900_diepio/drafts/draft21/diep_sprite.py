from constants import *
import math, pygame, funcs, health_bar, random


class DiepSprite:
    def __init__(self, screen, x, y, color, radius, accel, hp,
                sprite_type=TYPE_FOOD,
                draw_heading=True,
                draw_healthbar=True):
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
        self.sprite_type = sprite_type
        self.accel = accel
        self.dx = 0
        self.dy = 0
        self.draw_heading = draw_heading
        #elasticity and bounce_friction effect how sprites bounce
        #off of each other.
        self.elasticity = 1
        self.bounce_friction = 0
        #shove_impulse affects how strongly one sprite shoves out another
        self.shove_impulse = 0.3
        #If the sprite is not circular then it is rectangular.
        #This effects bouncing and shoving.
        self.circular = True
        #Movement friction. If this is zero you have a game
        #like asteroids
        self.friction = 0.05
        #Hitpoints
        self.max_hp = hp
        self.hp = hp
        self.draw_healthbar = draw_healthbar
        self.healthbar = None
        if self.draw_healthbar:
            self.healthbar = health_bar.HealthBar(screen,0,0,self.radius*2,10,self.hp)
            self.healthbar.updateHp(self.hp)
        #Damage dealt to others upon collision
        self.collision_damage = 1
        #Delay between shots
        self.refire_delay = 20
        self.refire_count = 0

    def shoot(self):
        if self.refire_count <= 0:
            self.refire_count = self.refire_delay
            #Shoot a bullet
            dx = math.cos(self.angle)
            dy = math.sin(self.angle)
            b = Bullet(self.screen, self.x, self.y, red,
                        bullet_size, dx*bullet_speed, dy*bullet_speed, 1,#hp
                        self)
            global all_sprites
            funcs.insertInOrder(b, all_sprites)
            #Recoil
            self.dx -= dx*recoil
            self.dy -= dy*recoil

    def takeDamage(self, damage):
        self.hp -= damage
        if self.draw_healthbar:
            self.healthbar.updateHp(self.hp)

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

    def moveTo(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x-self.radius,
                                self.y-self.radius,
                                self.radius*2,
                                self.radius*2)

    def teleport(self):
        self.moveTo(random.randint(0,world_size-self.radius*2),
                    random.randint(0,world_size-self.radius*2))

    def reset(self):
        self.teleport()
        self.hp = self.max_hp
        if self.draw_healthbar:
            self.healthbar.updateHp(self.hp)

    def update(self):
        self.move()
        #apply friction
        self.dx = (1-self.friction)*self.dx
        self.dy = (1-self.friction)*self.dy
        #Keep critter in bounds
        if self.x<0:
            self.dx += border_shove_impulse
        elif self.x > world_size:
            self.dx -= border_shove_impulse
        if self.y<0:
            self.dy += border_shove_impulse
        elif self.y > world_size:
            self.dy -= border_shove_impulse
        #Cooldown guns
        self.refire_count -= 1

    def isOffScreen(self, x_adjust, y_adjust):
        return x_adjust > screen_width or \
                x_adjust+self.rect.width < 0 or \
                y_adjust > screen_height or \
                y_adjust+self.rect.height < 0


    def draw(self, povx, povy, center_on_screen=False):
        r = self.rect.copy()
        if center_on_screen:
            center_x = self.screen.get_width()/2
            center_y = self.screen.get_height()/2
            r.x = center_x - self.radius
            r.y = center_y - self.radius
        else:
            #Get coordinate adjustments
            x_adjust = self.screen.get_width()/2 - povx
            y_adjust = self.screen.get_height()/2 - povy
            r.x += x_adjust
            r.y += y_adjust
            #If this sprite is not on screen, don't draw it
            if self.isOffScreen(r.y, r.y):
                return
        #Draw the main body of the sprite
        pygame.draw.ellipse(self.screen, self.color, r)
        #Draw little heading circle
        if self.draw_heading:
            heading_radius = 10
            heading = pygame.Rect(r.centerx-heading_radius+math.cos(self.angle)*100,
                                  r.centery-heading_radius+math.sin(self.angle)*100,
                                  heading_radius*2,
                                  heading_radius*2)
            pygame.draw.ellipse(self.screen, self.color, heading)
        #Draw healthbar
        if self.draw_healthbar and self.max_hp != self.hp:
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
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)

    def angleTo(self,x,y):
        x = x - self.x
        y = y - self.y
        return math.atan2(y,x)

    def depthOfPenetration(self, other):
        #Return the depth of penetration of one sprite into the other.
        #Will return negative values if the sprites are not touching.
        return (self.radius + other.radius) - self.distanceTo(other)

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
            other.dx += temp_dx*self.shove_impulse
            other.dy += temp_dy*self.shove_impulse


class Bullet(DiepSprite):
    def __init__(self, screen, x, y, color, radius, dx, dy, hp,
                shooter):
        super().__init__(screen, x, y, color, radius, 0,#accel
                        hp,
                        sprite_type=TYPE_BULLET,
                        draw_heading=False)
        self.shooter = shooter
        self.dx = dx
        self.dy = dy
        self.friction = 0
        self.timeout = default_bullet_timeout

    #Override parent class
    def update(self):
        self.timeout -= 1
        super().update()

