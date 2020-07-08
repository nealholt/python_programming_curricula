import pygame, math

'''
-block combat. big opposing blocks move together. fist, feet, block hitboxes only appear when button is pushed. duck, jump. head takes extra damage. jab, punch, low kick, roundhouse, upper cut, fireball. environmental hazards. Start this yourself in pygame pieces folder. assign stuff to Aren for next class. Students could write an AI for it?

-snes controller pygame
https://www.pygame.org/docs/ref/joystick.html
https://www.gamedev.net/forums/topic/639299-pygame-is-there-a-way-to-get-input-from-xbox-controller/
https://stackoverflow.com/questions/46557583/how-to-identify-which-button-is-being-pressed-on-ps4-controller-using-pygame
'''

pygame.init()

clock = pygame.time.Clock()
blue=(0,0,255)
red=(255,0,0)
green=(0,255,0)
surface = pygame.display.set_mode((1000,600))

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

    def crouch(self):
        pass #TODO

    def move(self):
        self.y += self.dy
        self.dy += gravity
        if self.y > floor:
            self.y = floor
            self.dy = 0

    def draw(self):
        r = pygame.Rect(self.x, self.y,self.width,self.height)
        pygame.draw.rect(self.surface,self.color,r)
        if self.punching:
            r = pygame.Rect(self.x+self.width+10,
                            self.y+self.height/2,
                            10,10)
            pygame.draw.rect(self.surface,red,r)

    def punch(self):
        r = pygame.Rect(self.x+self.width+10,
                        self.y+self.height/2,
                        10,10)

gravity = 1
floor = 200
default_height = 300

p1 = Sprite(surface, 20,20,100,default_height)

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
            #Jump
            elif event.key == 119 and p1.y == floor: #w
                p1.dy = -20
                p1.crouching = False
            #Crouch
            elif event.key == 115: #s
                p1.crouching = not p1.crouching
                p1.crouch()
        elif event.type == pygame.KEYUP:
            if event.key == 32: #space bar
                p1.punching = False

    keys = pygame.key.get_pressed()
    if keys[97]: #a
        p1.x-= 2
    if keys[100]: #d
        p1.x+= 2

    p1.move()

    surface.fill((0,0,0))
    p1.draw()
    pygame.display.flip()
    clock.tick(30)
pygame.quit()