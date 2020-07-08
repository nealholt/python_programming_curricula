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
            closest = self.getClosestSprite(sprites_in_range,[TYPE_FOOD])
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
