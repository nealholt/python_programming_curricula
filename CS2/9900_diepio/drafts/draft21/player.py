import math, pygame, diep_sprite
from constants import *

class PlayerCritter(diep_sprite.DiepSprite):
    def __init__(self, screen, x, y, color, radius, accel, hp):
        super().__init__(screen, x, y, color, radius, accel, hp,
                        sprite_type=TYPE_CRITTER,
                        draw_healthbar=True)
        self.vision_radius = 500

    def update(self, sprites_in_range):
        pos = pygame.mouse.get_pos()
        x = pos[0] - self.screen.get_width()/2
        y = pos[1] - self.screen.get_height()/2
        self.angle = math.atan2(y,x)
        super().update()

    '''#Override super class's draw function
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
            self.healthbar.draw() '''
