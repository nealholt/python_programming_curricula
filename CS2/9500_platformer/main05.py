import pygame, random, math

'''Press the space bar to rewind!'''

gravity = 0.8

class Platform:
    def __init__(self, surface, color, rect):
        self.surface = surface
        self.rect = rect
        self.color = color

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rect)

    def putAbove(self, other):
        r = other.getRect()
        other.y = self.rect.y-r.height

    def putBelow(self, other):
        r = other.getRect()
        #Plus 1 so no more collisions occur
        other.y = self.rect.y+self.rect.height+1



class Blob:
    def __init__(self, surface, color, x, y, radius):
        self.surface = surface
        self.x = x
        self.y = y
        self.dy = 0
        self.color = color
        self.radius = radius
        self.can_jump = False

    def getRect(self):
        return pygame.Rect(self.x,
                            self.y,
                            self.radius*2, #width
                            self.radius*2) #height

    def draw(self):
        pygame.draw.ellipse(self.surface, self.color, self.getRect())


def draw():
    #Fill the screen with black
    screen.fill(BLACK)
    #Draw the "hippo"
    hippo.draw()
    for p in platform_list:
        p.draw()
    #Update screen display
    pygame.display.flip()
    #Delay to get 60 fps
    clock.tick(60)


def rewind():
    global memory_index
    start = (memory_index+1)%len(memory)
    while memory_index != start:
        memory_index -= 1
        if memory_index < 0:
            memory_index = len(memory)-1
        x,y = memory[memory_index]
        hippo.x = x
        hippo.y = y
        draw()

BLACK = (0,0,0)
WHITE = (255,255,255)
ORANGE = (255,100,0)

#Width and height of the screen are both 500
width = 500
height = 500
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

#Put blob in center of the screen
hippo = Blob(screen,
            WHITE,
            250, #x
            250, #y
            15) #radius

#Create platorms
platform_list = []
r = pygame.Rect(350,250,100, 10)
platform_list.append(Platform(screen, ORANGE, r))
r = pygame.Rect(150,350,100, 10)
platform_list.append(Platform(screen, ORANGE, r))
r = pygame.Rect(150,150,100, 10)
platform_list.append(Platform(screen, ORANGE, r))

#Use this to rewind the game
memory = []
for i in range(100):
    memory.append((hippo.x, hippo.y))
memory_index = 0

running = True
while running:
    #Make hippo fall
    hippo.dy = hippo.dy + gravity
    hippo.y = hippo.y + hippo.dy
    #record the most recent location
    memory_index = (memory_index+1)%len(memory)
    memory[memory_index] = (hippo.x, hippo.y)
    #Keep hippo on screen
    if hippo.y+hippo.radius*2 > height:
        hippo.y = height-hippo.radius*2
        hippo.dy = 0
        #Hippo is on ground. It can jump
        hippo.can_jump = True
    #Check for collision with platform
    for p in platform_list:
        if p.rect.colliderect(hippo.getRect()):
            #Push hippo up or down
            if hippo.dy > 0: #hippo was headed down
                p.putAbove(hippo)
                hippo.can_jump = True
            else: #hippo was headed up
                p.putBelow(hippo)
                #Hippo hit underside of platform, can't jump
                hippo.can_jump = False
            #Reset dy to zero
            hippo.dy = 0
    #Respond to events such as closing the game or moving the hippo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == 32: #space bar
                rewind()
    keys = pygame.key.get_pressed()
    #The second condition checks to see if the hippo is stationary
    if keys[pygame.K_UP] and hippo.dy == 0 and hippo.can_jump:
        #Jump
        hippo.dy = hippo.dy-20
        hippo.can_jump = False
    if keys[pygame.K_LEFT]:
        hippo.x = hippo.x-4
    if keys[pygame.K_RIGHT]:
        hippo.x = hippo.x+4
    draw()
pygame.quit()