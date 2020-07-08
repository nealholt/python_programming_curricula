import pygame, diep_sprite, random
from constants import *

pygame.init()

#Center the powerup hitbox better in the center of the word
powerup_x_shift = -40

powerup_options = ["invincibility", "teleporter",
        "spread shot","big shot", "speed boost", "shove"]
powerup_font = pygame.font.SysFont("colonna", 32)

class Powerup(diep_sprite.DiepSprite):

    def __init__(self, screen, x, y, color):
        super().__init__(screen, x, y, color, 0, 0,
                        1, #hp
                        sprite_type=TYPE_POWERUP,
                        draw_healthbar=False)
        self.collision_damage=0
        self.randomizePower()
        #self.power = random.choice(powerup_options)
        #self.text = powerup_font.render(self.power, True, white)

    def draw(self, povx, povy, center_on_screen=False):
        #Get coordinate adjustments
        x_adjust = self.screen.get_width()/2 - povx
        y_adjust = self.screen.get_height()/2 - povy
        x = self.x + x_adjust + powerup_x_shift
        y = self.y + y_adjust
        #If this sprite is not on screen, don't draw it
        if self.isOffScreen(x, y):
            return
        self.screen.blit(self.text,(x,y))

    def applyPower(self, other):
        '''Apply the powerup to other.'''
        if self.power == "invincibility":
            other.invincibility_countdown = 360
        elif self.power == "teleporter":
            other.teleport()
        elif self.power == "spread shot":
            self.spread_shot_countdown = 360
        elif self.power == "big shot":
            self.big_shot_countdown = 360
        elif self.power == "speed boost":
            self.speed_boost_countdown = 360
        elif self.power == "shove":
            self.shove_countdown = 360
        else:
            print('Error in powerup.applyPower.')
            exit()
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
