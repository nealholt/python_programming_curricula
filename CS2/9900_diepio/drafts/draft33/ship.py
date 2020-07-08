import diep_sprite, math, funcs, random
from constants import *

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
        #self.expiration will be a list of lists. Inner lists will
        #be countdown,stat_index pairs.
        self.expiration = []

    def shoot(self):
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
        b = Bullet(self.screen, self.x, self.y, red, size,
                    dx*speed, dy*speed, hp, damage,
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
        super().update()



class Bullet(diep_sprite.DiepSprite):
    def __init__(self, screen, x, y, color, radius, dx, dy,
                hp, damage, timeout, shooter):
        super().__init__(screen, x, y, color, radius, 0,
                        sprite_type=TYPE_BULLET,
                        draw_heading=False)
        self.shooter = shooter
        self.dx = dx
        self.dy = dy
        self.friction = 0
        self.timeout = timeout
        self.draw_healthbar = False
        self.xs[HP_INDEX] = hp
        self.hit_points = hp
        self.xs[COLLISION_DAMAGE_INDEX] = damage
        self.xs[FRICTION_INDEX] = bullet_friction

    #Override parent class
    def update(self):
        self.timeout -= 1
        super().update()

