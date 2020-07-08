import pygame, math

'''
-block combat. big opposing blocks move together.
fist, feet, block hitboxes only appear when button
is pushed. duck, jump. head takes extra damage.
jab, punch, low kick, roundhouse, upper cut, fireball.
environmental hazards. Start this yourself in pygame
pieces folder. assign stuff to Aren for next class.
'''

pygame.init()

clock = pygame.time.Clock()
blue=(0,0,255)
red=(255,0,0)
green=(0,255,0)
surface = pygame.display.set_mode((1000,600))

gravity = 1
floor = 500
default_height = 300
player_width = 100
jump_power = 20
punch_size = 10
default_move_speed = 5
crouch_move_speed = 2


class Sprite:
    def __init__(self, surface, x, y, width, height):
        self.surface = surface
        self.x = x
        self.y = y
        self.dy = 0
        self.color = blue
        self.width = width
        self.height = height
        self.punching = False
        self.crouching = False
        self.facing_right = True

    def crouch(self):
        if self.crouching: #then un-crouch, stand back up
            self.y -= default_height/2
            self.height = default_height
        else: #then crouch
            self.y += default_height/2
            self.height = default_height/2
        self.crouching = not(self.crouching)

    def move(self):
        self.y += self.dy
        self.dy += gravity
        if self.y+self.height > floor:
            self.y = floor-self.height
            self.dy = 0

    def left(self):
        self.facing_right = False
        if self.crouching:
            self.x -= crouch_move_speed
        else:
            self.x -= default_move_speed

    def right(self):
        self.facing_right = True
        if self.crouching:
            self.x += crouch_move_speed
        else:
            self.x += default_move_speed

    def jump(self):
        if self.y+self.height == floor:
            self.dy = -jump_power
            if self.crouching: #uncrouch
                self.crouch()

    def draw(self):
        r = pygame.Rect(self.x, self.y,self.width,self.height)
        pygame.draw.rect(self.surface,self.color,r)
        if self.punching:
            if self.facing_right:
                r = pygame.Rect(self.x+self.width+10,
                                self.y+self.height/2,
                                punch_size,punch_size)
            else:
                r = pygame.Rect(self.x-10-punch_size,
                                self.y+self.height/2,
                                punch_size,punch_size)
            pygame.draw.rect(self.surface,red,r)


p1 = Sprite(surface, 20,20,player_width,default_height)

done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            print(event.key)
            if event.key == pygame.K_ESCAPE:
                done = True
            elif event.key == 32: #space bar
                p1.punching = True
            elif event.key == 119: #w
                p1.jump()
            #Crouch
            elif event.key == 115: #s
                p1.crouch()
        elif event.type == pygame.KEYUP:
            if event.key == 32: #space bar
                p1.punching = False

    keys = pygame.key.get_pressed()
    if keys[97]: #a
        p1.left()
    if keys[100]: #d
        p1.right()

    p1.move()

    surface.fill((0,0,0))
    p1.draw()
    pygame.display.flip()
    clock.tick(30)
pygame.quit()