import pygame, math, random

pygame.init()

border_shove_impulse = 0.35
world_size = 2000
TYPE_CRITTER = 0
TYPE_FOOD = 1
TYPE_BULLET = 2

'''TODO next steps:
0. Implement taking damage
    write a take damage function
1. Make hp a parameter of the sprite constructor
2.
3. Reset dead food (reset and relocate as if it was destroyed and regenerated)
4. increase collision detection efficiency by sorting collision lists.

Keep this initially separate then make a third project
integrating this with maze navigator.
'''

class HealthBar:
    def __init__(self, surface, x,y,width,height,hp_total):
        self.surface = surface
        self.total_width = width
        self.green_rect = pygame.Rect(x,y,width,height)
        self.red_rect = pygame.Rect(x,y,width,height)
        self.hp_total = hp_total

    def setXY(self,x,y):
        self.green_rect.x = x
        self.green_rect.y = y
        self.red_rect.x = x
        self.red_rect.y = y

    def updateHp(self, hp):
        x=0
        if self.hp_total != 0:
            x = int(self.total_width*(hp/self.hp_total))
        self.green_rect.width = x
        self.red_rect.x = self.green_rect.x+x
        self.red_rect.width = self.total_width - self.green_rect.width

    def draw(self):
        pygame.draw.rect(self.surface, green, self.green_rect)
        if self.red_rect.width!=0:
            pygame.draw.rect(self.surface, red, self.red_rect)


class DiepSprite:
    def __init__(self, screen, x, y, color, radius, accel,
                sprite_type=TYPE_FOOD,
                draw_heading=True,
                draw_healthbar=False):
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
        self.friction = 0.1
        #Hitpoints
        self.hp = 10
        self.draw_healthbar = draw_healthbar
        self.healthbar = None
        if self.draw_healthbar:
            self.healthbar = HealthBar(screen,0,0,self.radius*2,10,self.hp)
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

    def isOffScreen(self, x_adjust, y_adjust):
        return x_adjust > screen_width or \
                x_adjust+self.rect.width < 0 or \
                y_adjust > screen_height or \
                y_adjust+self.rect.height < 0


    def draw(self, povx, povy):
        #Get coordinate adjustments
        x_adjust = self.screen.get_width()/2 - povx
        y_adjust = self.screen.get_height()/2 - povy
        r = self.rect.copy()
        r.x += x_adjust
        r.y += y_adjust
        #If this sprite is not on screen, don't draw it
        if self.isOffScreen(r.y, r.y):
            return
        pygame.draw.ellipse(self.screen, self.color, r)
        #Draw little heading circle
        if self.draw_heading:
            heading_radius = 10
            heading = pygame.Rect(x_adjust+self.x-heading_radius+math.cos(self.angle)*100,
                                  y_adjust+self.y-heading_radius+math.sin(self.angle)*100,
                                  heading_radius*2,
                                  heading_radius*2)
            pygame.draw.ellipse(self.screen, self.color, heading)
        #Draw healthbar
        if self.draw_healthbar:
            self.healthbar.setXY(r.x,r.y+r.height)
            self.healthbar.draw()

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
        return self.depthOfPenetration(other) > 0

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
        super().__init__(screen, x, y, color, radius, accel,
                        sprite_type=TYPE_CRITTER,
                        draw_healthbar=True)

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
        #Draw healthbar
        if self.draw_healthbar:
            self.healthbar.setXY(r.x,r.y+r.height)
            self.healthbar.draw()


class EnemyCritter(DiepSprite):
    def __init__(self, screen, x, y, color, radius, target, accel):
        super().__init__(screen, x, y, color, radius, accel,
                        sprite_type=TYPE_CRITTER,
                        draw_healthbar=True)
        self.target = target

    #Override super class's update function
    def update(self):
        #Increase velocity in direction of target.
        self.angle = self.angleTo(self.target.x, self.target.y)
        self.dx += math.cos(self.angle)*self.accel
        self.dy += math.sin(self.angle)*self.accel
        super().update()


class Bullet(DiepSprite):
    def __init__(self, screen, x, y, color, radius, dx, dy, shooter):
        super().__init__(screen, x, y, color, radius, 0,
                        sprite_type=TYPE_BULLET,
                        draw_heading=False)
        self.shooter = shooter
        self.dx = dx
        self.dy = dy
        self.friction = 0
        self.timeout = 120

    #Override parent class
    def collidedWith(self, other):
        return super().collidedWith(other) and other!=self.shooter

    #Override parent class
    def update(self):
        self.timeout -= 1
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

all_sprites = [critter, npc_critter]

food_radius = 15
food_count = 100
for i in range(food_count):
    f = DiepSprite(screen,
                    random.randint(0,world_size-food_radius*2),#x
                    random.randint(0,world_size-food_radius*2),#y
                    green, food_radius, 0, draw_heading=False)
    all_sprites.append(f)

#Main program loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            #print(event.key) #Print value of key press
            if event.key == 32:#space bar
                #Shoot a bullet
                bullet_speed = 10
                bullet_size = 4
                dx = math.cos(critter.angle)*bullet_speed
                dy = math.sin(critter.angle)*bullet_speed
                b = Bullet(screen, critter.x, critter.y, red,
                            bullet_size, dx, dy, critter)
                b.hp = 1
                all_sprites.append(b)
            elif event.key == pygame.K_ESCAPE:
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

    #Collision check between sprites
    for i in range(len(all_sprites)-1):
        for j in range(i+1,len(all_sprites)):
            if all_sprites[i].collidedWith(all_sprites[j]):
                all_sprites[i].shoveOut(all_sprites[j])
                all_sprites[j].shoveOut(all_sprites[i])
                all_sprites[i].hp - 1
                all_sprites[j].hp - 1

    #Delete dead sprites
    for i in reversed(range(len(all_sprites))):
        if all_sprites[i].sprite_type == TYPE_BULLET:
            if all_sprites[i].timeout<0 or all_sprites[i].hp <= 0:
                del all_sprites[i]

    screen.fill((0,0,0)) #fill screen with black
    #Update and draw critters
    for a in all_sprites:
        a.update()
        a.draw(critter.x, critter.y)
    pygame.display.flip()
    #Delay to get 60 fps
    clock.tick(60)
pygame.quit()