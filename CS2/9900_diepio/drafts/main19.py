'''TODO next steps:
0. DONE - Make shooting internal to the sprite class
1. DONE - Recoil
2. DONE - Make collision damage an internal attribute.
3A. DONE - Enemy shoots
3B. Vision radius
Is there a way to implement cloaking?
Yes, for each NPC, get all objects within vision radius and only pass those in.
Cloaked ships are either not passed in or must be closer to be seen.
Only draw the objects seen by camera/perspective ship.
Implement zoom in and zoom out.
3C. Enemy selects different targets. Basic AI
3D. consolidate draw code. Enable camera switching.
4. Enemy can be killed.
5. Experience
6. Differentiated exp bricks.
7. Regenerating health. (Or a shield?)
8. Level up attributes.

Cal and/or Brendan help develop parts of this?

3 lives.

Exp and upgrades.
Be able to upgrade/downgrade friction, recoil, vision radius.

I like the idea of giving students a list of all the food and a list of
all powerups and of all enemies and lettign them do distance
calculations to determine what is nearest and what is a priority.

Tactical item pickups that can be used later. Shove out can be used on
a rammer. Teleport can get you out of a tricky spot. Grenade can be
fired into a cluster of enemies.
Make one of the things you can level up storage for powerups.

Keep this initially separate then make a third project
integrating this with maze navigator or a sort of racing game.
'''

import pygame, math, random

pygame.init()

border_shove_impulse = 0.35
world_size = 2000
TYPE_CRITTER = 0
TYPE_FOOD = 1
TYPE_BULLET = 2
default_bullet_timeout = 120
food_hp = 10
critter_hp = 200
food_radius = 15
food_count = 100
player_acceleration=0.2
npc_acceleration=0.1
bullet_speed = 8
bullet_size = 6
recoil = 2


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

    def draw(self):
        pygame.draw.rect(self.surface, red, self.red_rect)
        pygame.draw.rect(self.surface, green, self.green_rect)


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
            self.healthbar = HealthBar(screen,0,0,self.radius*2,10,self.hp)
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
            b = Bullet(screen, self.x, self.y, red,
                        bullet_size, dx*bullet_speed, dy*bullet_speed, 1,#hp
                        self)
            global all_sprites
            insertInOrder(b, all_sprites)
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
        if self.draw_healthbar and self.max_hp != self.hp:
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


class PlayerCritter(DiepSprite):
    def __init__(self, screen, x, y, color, radius, accel, hp):
        super().__init__(screen, x, y, color, radius, accel, hp,
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
    def __init__(self, screen, x, y, color, radius, target, accel, hp):
        super().__init__(screen, x, y, color, radius, accel, hp,
                        sprite_type=TYPE_CRITTER,
                        draw_healthbar=True)
        self.target = target

    #Override super class's update function
    def update(self):
        #Increase velocity in direction of target.
        self.angle = self.angleTo(self.target.x, self.target.y)
        self.dx += math.cos(self.angle)*self.accel
        self.dy += math.sin(self.angle)*self.accel
        if self.distanceTo(self.target) < 350:
            self.shoot()
        super().update()


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


def insertInOrder(sprite, sprite_list):
    '''Insert the sprite into sprite_list in order by x
    coordinate. This is important for keeping the all_sprites
    list sorted. Otherwise collisions may be missed.'''
    #This could be more efficient using a binary search since
    #We can assume that sprite_list is sorted.
    if len(sprite_list)==0 or sprite.rect.left <= sprite_list[0].rect.left:
        sprite_list.insert(0, sprite)
        return
    for i in range(len(sprite_list)-1):
        if sprite.rect.left > sprite_list[i].rect.left and \
        sprite.rect.left <= sprite_list[i+1].rect.left:
            sprite_list.insert(i, sprite)
            return
    sprite_list.append(sprite)

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
                        player_acceleration,
                        critter_hp)#hp

npc_critter = EnemyCritter(screen,
                          200,#x
                          200,#y
                          yellow,
                          35,#radius
                          critter,#target of enemy
                          npc_acceleration,
                          critter_hp)#hp

all_sprites = []
insertInOrder(npc_critter, all_sprites)
insertInOrder(critter, all_sprites)

for i in range(food_count):
    f = DiepSprite(screen,
                    0,0,
                    green, food_radius, 0,#acceleration
                    food_hp,#hp
                    draw_heading=False)
    f.teleport()
    insertInOrder(f, all_sprites)

#Main program loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            #print(event.key) #Print value of key press
            if event.key == 32:#space bar
                critter.shoot()
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

    #Sorting pass of all_sprites. If we do one bubble sort per frame,
    #sprites ought to stay roughly sorted.
    for i in range(len(all_sprites)-1):
        if all_sprites[i].rect.left > all_sprites[i+1].rect.left:
            temp = all_sprites[i]
            all_sprites[i] = all_sprites[i+1]
            all_sprites[i+1] = temp

    #Collision check between sprites
    for i in range(len(all_sprites)-1):
        for j in range(i+1,len(all_sprites)):
            #For efficiency abort loop if nothing more is in range
            if all_sprites[i].rect.right < all_sprites[j].rect.left:
                break
            #check for collision
            if all_sprites[i].collidedWith(all_sprites[j]):
                all_sprites[i].shoveOut(all_sprites[j])
                all_sprites[j].shoveOut(all_sprites[i])
                #Prevent food on food damage
                if all_sprites[i].sprite_type != TYPE_FOOD or all_sprites[j].sprite_type != TYPE_FOOD:
                    all_sprites[i].takeDamage(all_sprites[j].collision_damage)
                    all_sprites[j].takeDamage(all_sprites[i].collision_damage)

    #Delete dead sprites
    for i in reversed(range(len(all_sprites))):
        if all_sprites[i].hp <= 0:
            if all_sprites[i].sprite_type == TYPE_FOOD:
                #Reset the food
                all_sprites[i].reset()
            else:
                del all_sprites[i]
        elif all_sprites[i].sprite_type == TYPE_BULLET and all_sprites[i].timeout<0:
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