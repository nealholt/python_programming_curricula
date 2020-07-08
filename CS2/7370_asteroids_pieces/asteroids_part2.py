'''
ASTEROIDS: Rotating Polygons

A great way to create polygon shapes is to use a list of angles
and a corresponding list of radii (plural of radius).
Below, a polygon object specifies the center of the polygon
at x,y and uses a list of angles and radii extending from
the central point to draw a triangle.

This is a useful implementation because it makes rotation
very easy.

For 35 points, modify the following code as described below.

Insert code to rotate the polygon counterclockwise when the a
key is pressed and clockwise when the d key is pressed.

Then add to the radii and angles lists to change the triangle's
shape to look more like the classic Asteroids ship shown here:
asteroids_image.jpg
https://drive.google.com/open?id=1EUNGtEy6KkqeN5mEMpLMyTCr8g3u2jTT
'''
import pygame, math

pygame.init()
clock = pygame.time.Clock()
blue=(0,0,255)
surface = pygame.display.set_mode((1000,500))

class Polygon:
    def __init__(self, surface, x, y):
        self.surface = surface
        self.x = x
        self.y = y
        #For your convenience, all angles are in degrees
        self.angle = 0
        self.angles = [0, 135, -135]
        self.radii = [100,50,50]

    def draw(self):
        pointlist=[]
        for i in range(len(self.angles)):
            angle = self.angle+self.angles[i]
            angle = angle*math.pi/180 #convert to radians
            x = self.x + math.cos(angle)*self.radii[i]
            y = self.y + math.sin(angle)*self.radii[i]
            pointlist.append((x,y))
        pygame.draw.polygon(self.surface,blue,pointlist)

x=50
y=50
player=Polygon(surface,x,y)

done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_a]:
        pass
    if pressed[pygame.K_d]:
        pass
    if pressed[pygame.K_RIGHT]:
        player.x+=10
    if pressed[pygame.K_LEFT]:
        player.x-=10
    if pressed[pygame.K_UP]:
        player.y-=10
    if pressed[pygame.K_DOWN]:
        player.y+=10

    surface.fill((0,0,0))
    player.draw()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
