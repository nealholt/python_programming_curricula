import pygame, ship
from constants import *

class EnemyCritter(ship.Ship):
    def __init__(self, screen, x, y, color, radius, name):
        super().__init__(screen, x, y, color, radius, name)

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
        pass #Your code goes here