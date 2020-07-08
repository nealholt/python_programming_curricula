import pygame, diep_sprite, random
from constants import *

pygame.init()
powerup_font = pygame.font.SysFont("colonna", 32)

class Powerup(diep_sprite.DiepSprite):
    def __init__(self, screen, x, y, color):
        super().__init__(screen, x,y,color,0,0,
                        sprite_type=TYPE_POWERUP,
                        draw_healthbar=False)
        self.randomizePower()
        self.xs[COLLISION_DAMAGE_INDEX] = 0

    def draw(self, povx, povy, center_on_screen=False):
        #Get coordinate adjustments
        x_adjust = screen_width_half - povx
        y_adjust = screen_height_half - povy
        x = self.x + x_adjust + powerup_x_shift
        y = self.y + y_adjust
        #If this sprite is not on screen, don't draw it
        if self.isOffScreen(x, y):
            return
        self.screen.blit(self.text,(x,y))

    def applyPower(self, other):
        '''Apply the powerup to other.'''
        if self.power == "invincibility":
            other.xs[ARMOR_INDEX] = 0
            other.expiration.append([powerup_time, ARMOR_INDEX])
        elif self.power == "teleporter":
            other.teleport()
        elif self.power == "spread shot":
            other.xs[BULLET_COUNT_INDEX] *= 3
            other.expiration.append([powerup_time, BULLET_COUNT_INDEX])
        elif self.power == "big shot":
            other.xs[BULLET_SIZE_INDEX] = other.xs[BULLET_SIZE_INDEX]*5
            other.expiration.append([powerup_time, BULLET_SIZE_INDEX])
        elif self.power == "speed boost":
            other.xs[ACCEL_INDEX] = other.xs[ACCEL_INDEX]*3
            other.expiration.append([powerup_time, ACCEL_INDEX])
        elif self.power == "shove":
            other.xs[SHOVE_INDEX] = other.xs[SHOVE_INDEX]*10
            other.expiration.append([powerup_time, SHOVE_INDEX])
        elif self.power == "rapid fire":
            other.xs[REFIRE_DELAY_INDEX] = other.xs[REFIRE_DELAY_INDEX]/10
            other.expiration.append([powerup_time, REFIRE_DELAY_INDEX])
        elif self.power == "seeking shots":
            other.use_seeking = True
            other.expiration.append([powerup_time, 0])
        else:
            print('Error in powerup.applyPower.')
            pygame.quit(); exit()
        #Relocate the powerup
        self.teleport()
        #Rerandomize the powerup type
        self.randomizePower()

    def randomizePower(self):
        self.power = random.choice(powerup_options)
        self.text = powerup_font.render(self.power, True, white)

    def takeDamage(self, damage):
        '''Override parent function so powerups never take damage.'''
        pass
