from enemy import *

class AI(EnemyCritter):
    def __init__(self, screen, x, y, color, radius, name):
        super().__init__(screen, x, y, color, radius, name)
        self.ai_type = 0
        self.level_choices = [
BULLET_DAMAGE_INDEX,
BULLET_DAMAGE_INDEX,
HP_REGEN_INDEX,
HP_REGEN_INDEX,
ACCEL_INDEX,
HP_INDEX,
REFIRE_DELAY_INDEX,
REFIRE_DELAY_INDEX,
BULLET_SPEED_INDEX,
BULLET_LONGEVITY_INDEX,
BULLET_HP_INDEX,
COLLISION_DAMAGE_INDEX,
BULLET_DAMAGE_INDEX
]
    #Override super class's update function
    def update(self, sprites_in_range):
        super().update(sprites_in_range)
        #Avoid an error
        if len(sprites_in_range)==0:
            return


        if self.canLevelUp():
            current_level = self.getCurrentLevel()
            print('Current level:',current_level)
            to_upgrade = self.level_choices[current_level]
            self.levelUp(to_upgrade)


        if self.ai_type==0: #aggressive
            closest=self.getClosestSprite(sprites_in_range,[TYPE_FOOD])
            p = self.getClosestPlayer(sprites_in_range)
            if not(p is None):
                self.orbitClockwise(p,150)
                #Shoot at target
                self.shootAt(p)
            elif closest is None:
                #When in doubt, move toward the middle
                self.moveTowardLocation(world_size/2,world_size/2)
            else:
                self.orbitClockwise(closest,100)
                #Shoot at target
                self.shootAt(closest)


        elif self.ai_type==1: #turtle
            closest=self.getClosestSprite(sprites_in_range,[TYPE_FOOD])
            p = self.getClosestPlayer(sprites_in_range)
            if not(p is None):
                self.fleeFrom(p)
                self.shootAt(p)
            elif closest is None:
                #When in doubt, move toward the middle
                self.moveTowardLocation(world_size/2,world_size/2)
            else:
                self.orbitClockwise(closest,100)
                #Shoot at target
                self.shootAt(closest)


        elif self.ai_type==2: #power ups
            self.message = ''
            p = self.getClosestPowerup(sprites_in_range)
            closest=self.getClosestSprite(sprites_in_range,[TYPE_FOOD,TYPE_CRITTER])

            if self.isInvincible():
                f = self.getClosestFood(sprites_in_range)
                self.moveToward(f)
                #Use recoil shooting to boost speed
                self.faceAwayFromTarget(f)
                self.shoot()
                self.message = 'Go ham!'
            elif not(p is None):
                self.moveToward(p)
                #Use recoil shooting to boost speed
                self.faceAwayFromTarget(p)
                self.shoot()
                self.message = 'hungry for power!'
            elif closest is None:
                #When in doubt, move toward the middle
                self.moveTowardLocation(world_size/2,world_size/2)
                self.message = 'bored'
            else:
                self.orbitClockwise(closest,100)
                #Shoot at target
                self.shootAt(closest)
                self.message = 'targeting'


        elif self.ai_type==3: #big block turtle
            foods = self.getFoodsInRange(sprites_in_range)
            p = self.getClosestPlayer(sprites_in_range)
            if not(p is None):
                self.fleeFrom(p)
                self.shootAt(p)
            elif len(foods) == 0:
                #When in doubt, move toward the middle
                self.moveTowardLocation(world_size/2,world_size/2)
            else:
                #Find the biggest food and attack it
                biggest = foods[0]
                for f in foods:
                    if f.experience > biggest.experience:
                        biggest = f
                self.orbitClockwise(biggest,100)
                #Shoot at target
                self.shootAt(biggest)

