import pygame, math

pygame.init()

'''TODO next steps:
1. Make an enemy DiepCritter that chases player
    def angleToTarget(self):
        x = self.target.rect.centerx - self.rect.centerx
        y = self.target.rect.centery - self.rect.centery
        return math.atan2(y,x)
2. Make the camera a follow camera
3. Make little stationary killable objects
4. Use inheritance
Keep this initially separate then make a third project integrating this with maze navigator.
'''

class DiepCritter:
    def __init__(self, surface, x, y, color, radius, speed):
        self.surface = surface
        self.color = color
        self.x = x+radius #center x
        self.y = y+radius #center y
        self.angle = 0
        self.radius = radius
        self.rect = pygame.Rect(self.x-self.radius,
                                self.y-self.radius,
                                self.radius*2,
                                self.radius*2)
        self.moving = 0
        self.turn_rate = 0
        self.speed = speed

    def move(self):
        self.x += math.cos(self.angle)*self.speed*self.moving
        self.y += math.sin(self.angle)*self.speed*self.moving
        self.rect = pygame.Rect(self.x-self.radius,
                                self.y-self.radius,
                                self.radius*2,
                                self.radius*2)

    def rotate(self):
        self.angle += self.turn_rate

    def update(self):
        self.move()
        self.rotate()

    def draw(self):
        pygame.draw.ellipse(self.surface, self.color, self.rect)
        #Draw little heading circle
        heading_radius = 10
        heading = pygame.Rect(    self.x-heading_radius+math.cos(self.angle)*100,
                                self.y-heading_radius+math.sin(self.angle)*100,
                                heading_radius*2,
                                heading_radius*2)
        pygame.draw.ellipse(self.surface, self.color, heading)


class EnemyCritter(DiepCritter):
    def __init__(self, surface, x, y, color, radius, speed):
        super().__init__(surface, x, y, color, radius, speed)


#Initialize variables:
clock = pygame.time.Clock()
screen_width = 1100
screen_height = 650
surface = pygame.display.set_mode((screen_width,screen_height))
green = 0,255,0
red = 255,0,0
blue = 0,0,255
yellow = 255,255,0
white = 255,255,255
black = 0,0,0

critter = DiepCritter(    surface,
                        100,#x
                        100,#y
                        blue,
                        50,#radius
                        20)#speed

npc_critter = DiepCritter(surface,
                          200,#x
                          200,#y
                          yellow,
                          35,#radius
                          10)#speed
#Main program loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            #print(event.key) #Print value of key press
            if event.key == pygame.K_ESCAPE:
                done = True
            elif event.key == pygame.K_RIGHT:
                critter.turn_rate = math.pi/32 #Turn clockwise
            elif event.key == pygame.K_LEFT:
                critter.turn_rate = -math.pi/32 #Turn counter-clockwise
            elif event.key == pygame.K_UP:
                critter.moving = 1 #move forward
            elif event.key == pygame.K_DOWN:
                critter.moving = -1 #move backward
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                critter.turn_rate = 0 #Stop turning
            elif event.key == pygame.K_LEFT:
                critter.turn_rate = 0 #Stop turning
            elif event.key == pygame.K_UP:
                critter.moving = 0 #Stop moving
            elif event.key == pygame.K_DOWN:
                critter.moving = 0 #Stop moving

    surface.fill((0,0,0)) #fill surface with black
    critter.update()
    critter.draw()
    pygame.display.flip()
    pygame.display.update()
    #Delay to get 30 fps
    clock.tick(30)
pygame.quit()