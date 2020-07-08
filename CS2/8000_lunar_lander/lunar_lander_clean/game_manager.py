import ground, ship
from constants import *


class GameManager:
    def __init__(self, screen, level):
        self.screen = screen
        self.level = level
        #Create player
        self.player = ship.Ship(screen, 400, 0)
        #Create the ground
        self.ground = ground.Ground(screen)
        #List of intangible animation objects
        self.animation_list = []
        self.victory = False

    def update(self):
        #Move and draw
        self.ground.draw(self.player.x, self.player.y)
        for item in self.animation_list:
            item.move()
            item.draw(self.player.x, self.player.y)
        #Draw the player if the player is still alive
        if self.player.lives > 0:
            self.player.move()
            self.player.draw()
            #Check for a collision with the ground or a landing
            if self.ground.safeLanding(self.player):
                self.victory = True
            elif self.ground.shipHitGround(self.player):
                self.player.lives = 0

    def getData(self):
        '''Returns a list of data relevant to an algorithm trying to
        optimize the landing including:
        ship angle, dx, dy, horizontal distance to center of pad,
        altitude'''
        a = self.player.angle #in radians
        dx = self.player.dx #in pixels per frame
        dy = self.player.dy #in pixels per frame
        #Distance to center of pad in pixels:
        xv, _ = self.ground.getVectorToPad(self.player.x, self.player.y)
        altitude = self.ground.getHeightAt(self.player.x)
        return [a, dx, dy, xv, altitude]

