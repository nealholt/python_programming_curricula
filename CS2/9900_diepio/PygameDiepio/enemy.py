import math, pygame, ship, random
from constants import *

class EnemyCritter(ship.Ship):
    def __init__(self, screen, x, y, color, radius, name):
        super().__init__(screen, x, y, color, radius, name)
        self.resetDefaultLocation()

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
    
    def resetDefaultLocation(self):
        #Default location to seek if we don't see anything
        #to interact with
        self.goalx = random.randint(0,screen_width)
        self.goaly = random.randint(0,screen_height)

    #Override super class's update function
    def update(self, sprites_in_range):
        super().update()
        #Avoid an error
        if len(sprites_in_range)==0:
            return
        '''You can only use one of the next 7 movement
        functions per turn.

        Moves you toward the given target sprite.
        self.moveToward(target)

        Moves you toward the given x,y coordinates.
        self.moveTowardLocation(x,y)

        Moves you away from the given target sprite.
        self.fleeFrom(target)

        Moves you away from the given x,y coordinates
        self.fleeFromLocation(x,y)

        Moves you in the given direction. direction must
        be in degrees between 0 and 360.
        self.moveTowardDirection(direction)

        Orbit counterclockwise around the given target
        at the given distance.
        self.orbitCounterclockwise(target,distance)

        Orbit clockwise around the given target at the
        given distance.
        self.orbitClockwise(target,distance)

        Fires in the direction you are currently facing if
        shooting is off cooldown.
        self.shoot()

        Fires at the given x,y coordinates if shooting is
        off cooldown.
        self.shootAt(x,y)

        Fires at the given sprite if shooting is
        off cooldown.
        self.shootAt(target)

        Returns the closest sprite in range that shares
        a type with a type in type_list. If none found,
        returns None.
        self.getClosestSprite(sprites_in_range, type_list)
        For example to get the nearest food or player you
        could use
        type_list = [TYPE_CRITTER,TYPE_FOOD]
        closest = self.getClosestSprite(sprites_in_range, type_list)

        #Returns the closest player or None
        p = self.getClosestPlayer(sprites_in_range)
        #Returns the closest bullet that is not your own or None
        b = self.getClosestBullet(sprites_in_range)
        #Returns the closest food or None
        f = self.getClosestFood(sprites_in_range)
        #Returns the closest powerup or None
        p = self.getClosestPowerup(sprites_in_range)

        Returns a list of all the sprites in range that share
        a type with a type in type_list. If none found,
        returns an empty list.
        self.getAllSpritesInRange(sprites_in_range, type_list)
        For example to get all the nearest food and powerups
        you could use
        type_list = [TYPE_POWERUP,TYPE_FOOD]
        food_and_ups = self.getAllSpritesInRange(sprites_in_range, type_list)

        Returns a list of all the players in range, not
        including yourself.
        players = self.getPlayersInRange(sprites_in_range)
        Returns a list of all the bullets in range, not
        including your own.
        bullets = self.getBulletsInRange(sprites_in_range)
        Returns a list of all the food in range.
        foods = self.getFoodsInRange(sprites_in_range)
        Returns a list of all the powerups in range.
        ups = self.getPowerupsInRange(sprites_in_range)

        Get the distance in pixels to the given sprite named
        closest.
        distance = self.distanceTo(closest)

        Returns True if this ship is currently under some
        effect such as a powerup.
        self.hasEffect()

        Returns True if this ship is currently invincible.
        self.isInvincible()

        Sets your angle to face the given sprite. This will
        happen automatically if you shoot at the sprite.
        self.faceTarget(target)

        Sets your angle to face away from the given sprite.
        This can be useful in order to move toward the
        target faster by using recoil from shooting.
        self.faceAwayFromTarget(target)
        '''
        #Level up
        if self.canLevelUp():
            #Get the next upgrade in the level_choices list
            current_level = self.getCurrentLevel()%len(self.level_choices)
            to_upgrade = self.level_choices[current_level]
            self.levelUp(to_upgrade)

        #Dodge bullets
        b = self.getClosestBullet(sprites_in_range)
        if b!=None:
            #Either orbit around a bullet or flee directly
            #away from it depending on if the bullet is headed 
            #directly for us or not
            threshold = 30*math.pi/180 #30 degrees
            a1 = self.angleToSprite(b)
            a2 = self.angleToSprite(b.shooter)
            if abs(a1-a2) < threshold:
                distance = self.distanceTo(b)
                self.orbitClockwise(b,distance)
            else:
                self.fleeFrom(b)
        
        #Powerups
        p = self.getClosestPowerup(sprites_in_range)
        if p!=None:
            self.moveToward(p)
            self.faceAwayFromTarget(p)
            self.shoot()
            return

        #Attack other players
        #Two behaviors: Run away and shoot at versus approach and shoot at depending on relative health and experience.
        p = self.getClosestPlayer(sprites_in_range)
        if p!=None:
            if p.experience < self.experience or p.xs[HP_INDEX] < self.xs[HP_INDEX]:
                self.orbitClockwise(p,150)
            else:
                self.orbitClockwise(p,800)
            self.shootAt(p)
            return

        #Gain experience
        #Get all the food/experience that we can see
        foods = self.getFoodsInRange(sprites_in_range)
        #if there is any food at all, find the and shoot the best food
        if len(foods) > 0:
            #Assume the first food is the best for starters
            best_food = foods[0]
            shots_to_kill = best_food.xs[HP_INDEX] / self.xs[BULLET_DAMAGE_INDEX]
            best_xp_ratio = best_food.getExperienceGiven() / shots_to_kill
            #Loop through all the food
            for food in foods:
                #Figure out the experience per shot gained by attacking
                #this food
                shots_to_kill = food.xs[HP_INDEX] / self.xs[BULLET_DAMAGE_INDEX]
                xp_ratio = food.getExperienceGiven() / shots_to_kill
                #If this food gives a better experience ratio then it's the best
                if best_xp_ratio < xp_ratio:
                    best_food = food
                    best_xp_ratio = xp_ratio
            #Attack food
            self.orbitClockwise(best_food,100)
            self.shootAt(best_food)
            return
        
        #Random movement
        if self.can_move:
            self.moveTowardLocation(self.goalx,self.goaly)
            if self.distanceToCoordinate(self.goalx,self.goaly) < self.radius:
                self.resetDefaultLocation()
