import diep_sprite, math, funcs, random, bullet
from constants import *
import pygame

pygame.init()
my_font = pygame.font.SysFont('Arial', 25)

class Ship(diep_sprite.DiepSprite):
    def __init__(self, screen, x, y, color, radius, name):
        super().__init__(screen, x, y, color, radius, 1,#base level
                        sprite_type=TYPE_CRITTER,
                        draw_healthbar=True)
        self.name=name
        #Delay between shots
        self.refire_count = 0
        #List of timeouts after which some value needs
        #to revert to default. This is used for implementing
        #many of the powerups.
        #self.expiration will be a list of lists. Inner lists
        #will be countdown,stat_index pairs.
        self.expiration = []
        #Use this to limit movement to once per turn so
        #student programmers can't spam the movement commands
        self.can_move = True
        #Text to display. Mostly for testing. Can be used
        #for taunting or boasting.
        self.message = ''
        #Whether or not this ship can shoot
        self.can_shoot = True

    def becomeRammer(self):
        #Turn this ship into a rammer
        '''Make other changes when changing to spiky such as hiding the
        heading indicator, disabling shooting, and increasing baseline
        armor, collision damage, and regen.'''
        self.setShape(SHAPE_SPIKY)
        self.draw_heading = False
        self.can_shoot = False
        #Double the damage this ship deals in collisions
        self.xs[COLLISION_DAMAGE_INDEX] = self.getDefault(COLLISION_DAMAGE_INDEX) * 2
        #Increase hp regeneration by 0.01
        self.xs[HP_REGEN_INDEX] = self.getDefault(HP_REGEN_INDEX) + 0.01
        #Don't shove out other ships
        self.xs[SHOVE_INDEX] = 0
        #Only take 90% damage
        self.xs[ARMOR_INDEX] = 0.9

        #TODO LEFT OFF HERE

    def draw(self, povx, povy, center_on_screen=False):
        super().draw(povx, povy, center_on_screen)
        if self.message != '':
            if center_on_screen:
                x = screen_width_half - self.radius
                y = screen_height_half - self.radius
            else:
                #Get coordinate adjustments
                x = self.x+screen_width_half - povx
                y = self.y+screen_height_half - povy
                #If this sprite is not on screen, don't draw it
                if self.isOffScreen(x,y):
                    return
            text = my_font.render(self.message,True,white)
            self.screen.blit(text, (x-self.radius, y-20))

    def shootAt(self, x,y):
        if self.refire_count <= 0:
            self.angle = self.angleTo(x,y)
            self.shoot()

    def shootAt(self, target):
        if target is None:
            print('ERROR in shootAt. You cannot shoot at None.')
            return
        if self.refire_count <= 0:
            self.angle = self.angleToSprite(target)
            self.shoot()

    def shoot(self):
        if not self.can_shoot:
            return
        if self.refire_count <= 0:
            self.refire_count = self.xs[REFIRE_DELAY_INDEX]
            if self.xs[BULLET_COUNT_INDEX] == 1:
                self.shootOneBullet(self.angle)
            else:
                spread = math.pi/4
                interval = spread/(self.xs[BULLET_COUNT_INDEX]-1)
                for i in range(self.xs[BULLET_COUNT_INDEX]):
                    self.shootOneBullet(self.angle-spread/2+i*interval)

    def shootOneBullet(self, angle):
        #Shoot a bullet
        spread = self.xs[BULLET_SPREAD_INDEX]
        r = (random.random()-0.5)*2*spread
        dx = math.cos(angle+r)
        r = (random.random()-0.5)*2*spread
        dy = math.sin(angle+r)
        size = self.xs[BULLET_SIZE_INDEX]
        speed = self.xs[BULLET_SPEED_INDEX]
        hp = self.xs[BULLET_HP_INDEX] #penetration
        timeout = self.xs[BULLET_LONGEVITY_INDEX]
        damage = self.xs[BULLET_DAMAGE_INDEX]
        b = bullet.Bullet(self.screen, self.x, self.y, red,
                    size, dx*speed, dy*speed, hp, damage,
                    timeout, self)
        global all_sprites
        funcs.insertInOrder(b, all_sprites)
        #Recoil
        self.dx -= dx*self.xs[RECOIL_INDEX]
        self.dy -= dy*self.xs[RECOIL_INDEX]

    def revert(self,index):
        '''Revert the index stat to default levels.'''
        self.xs[index] = self.getDefault(index)

    def update(self):
        #Cooldown guns and powerups
        self.refire_count -= 1
        #Regen health by taking negative damage
        self.takeDamage( -self.xs[HP_REGEN_INDEX] )
        #Expire temporary stats and abilities
        for i in reversed(range(len(self.expiration))):
            self.expiration[i][0] -= 1
            if self.expiration[i][0] < 0:
                self.revert(self.expiration[i][1])
                del self.expiration[i]
        self.can_move = True #Reset
        super().update()

    def getClosestSprite(self, sprites_in_range, type_list):
        '''Takes a list of sprites in range and a list of
        sprite types. Only returns sprites of the given type.'''
        #Select closest sprite as target
        closest = None
        distance = 2**28
        for s in sprites_in_range:
            #Skip self or self-shot bullets
            if s==self or (s.sprite_type==TYPE_BULLET and s.shooter==self):
                continue
            #Skip sprites other than the desired type
            if s.sprite_type not in type_list:
                continue
            #Update closest
            temp_dist = self.distanceTo(s)
            if temp_dist<distance:
                distance = temp_dist
                closest = s
        return closest

    def getClosestPlayer(self,sprites_in_range):
        return self.getClosestSprite(sprites_in_range, [TYPE_CRITTER])
    def getClosestBullet(self,sprites_in_range):
        return self.getClosestSprite(sprites_in_range, [TYPE_BULLET])
    def getClosestFood(self,sprites_in_range):
        return self.getClosestSprite(sprites_in_range, [TYPE_FOOD])
    def getClosestPowerup(self,sprites_in_range):
        return self.getClosestSprite(sprites_in_range, [TYPE_POWERUP])

    def getAllSpritesInRange(self, sprites_in_range, type_list):
        '''Gets all the sprites of a certain type in range.
        Skips self and self-shot bullets.'''
        to_return = []
        for s in sprites_in_range:
            #Skip self or self-shot bullets
            if s==self or (s.sprite_type==TYPE_BULLET and s.shooter==self):
                continue
            if s.sprite_type in type_list:
                to_return.append(s)
        return to_return

    def getPlayersInRange(self,sprites_in_range):
        return self.getAllSpritesInRange(sprites_in_range,[TYPE_CRITTER])
    def getBulletsInRange(self,sprites_in_range):
        return self.getAllSpritesInRange(sprites_in_range,[TYPE_BULLET])
    def getFoodsInRange(self,sprites_in_range):
        return self.getAllSpritesInRange(sprites_in_range,[TYPE_FOOD])
    def getPowerupsInRange(self,sprites_in_range):
        return self.getAllSpritesInRange(sprites_in_range,[TYPE_POWERUP])

    def moveToward(self, target):
        if target is None:
            print('ERROR in moveToward: target is None')
            return
        self.moveTowardLocation(target.x,target.y)

    def moveTowardLocation(self,x,y):
        if not self.can_move:
            print('WARNING in moveTowardLocation: you already moved once this turn')
            return
        self.can_move = False
        angle = self.angleTo(x,y)
        accel = self.xs[ACCEL_INDEX]
        self.dx += math.cos(angle)*accel
        self.dy += math.sin(angle)*accel

    def fleeFrom(self, target):
        if target is None:
            print('ERROR in fleeFrom: target is None')
            return
        self.fleeFromLocation(target.x,target.y)

    def fleeFromLocation(self,x,y):
        if not self.can_move:
            print('WARNING in fleeFromLocation: you already moved once this turn')
            return
        self.can_move = False
        angle = self.angleTo(x,y)
        accel = self.xs[ACCEL_INDEX]
        self.dx -= math.cos(angle)*accel
        self.dy -= math.sin(angle)*accel

    def moveTowardDirection(self,direction):
        '''direction must be in degrees between 0 and 360'''
        if not self.can_move:
            print('WARNING in moveTowardDirection: you already moved once this turn')
            return
        self.can_move = False
        #Convert direction to an angle in degrees and
        #remember that the world is upside down
        angle = (360-direction)*math.pi/180
        accel = self.xs[ACCEL_INDEX]
        self.dx += math.cos(angle)*accel
        self.dy += math.sin(angle)*accel

    def orbitClockwise(self,target,distance):
        '''Orbit clockwise around the target at the given
        distance.'''
        if target is None:
            print('ERROR in orbitClockwise: target is None')
            return
        a = target.angleToSprite(self) + math.pi/8
        x = target.x+math.cos(a)*distance
        y = target.y+math.sin(a)*distance
        self.moveTowardLocation(x,y)

    def orbitCounterclockwise(self,target,distance):
        '''Orbit counter-clockwise around the target at
        the given distance.'''
        if target is None:
            print('ERROR in orbitCounterclockwise: target is None')
            return
        a = target.angleToSprite(self) - math.pi/8
        x = target.x+math.cos(a)*distance
        y = target.y+math.sin(a)*distance
        self.moveTowardLocation(x,y)

    def hasEffect(self):
        '''Returns True if this ship is currently under some
        effect such as a powerup.'''
        return len(self.expiration)>0

    def isInvincible(self):
        '''Returns True if this ship is currently invincible.'''
        return self.xs[ARMOR_INDEX] == 0

    def faceTarget(self,target):
        #Set your angle to face the target
        self.angle = self.angleToSprite(target)

    def faceAwayFromTarget(self,target):
        #Set your angle to face away from the target.
        #Useful for using shooting to boost speed.
        self.angle = self.angleToSprite(target)+math.pi

