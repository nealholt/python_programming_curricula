'''

How to simulate big waves?

What if you smooth things out by either skipping various peaks or drawing
ovals at the heights of various peaks?

https://opengameart.org/content/free-pirates-game-assets-by-unlucky-studio
mixed with this on the water
https://www.youtube.com/watch?v=SO7FFteErWs
Do you just need slope of secant line to figure the angle?
'''
import pygame, math, random

pygame.init()

clock = pygame.time.Clock()
black=0,0,0
blue=(0,0,255)
red=(255,0,0)
green=(0,255,0)
screen_width = 1000
screen_height = 600
surface = pygame.display.set_mode((screen_width,screen_height))

#Spacing between water height locations
spacing = 10 #pixels
#Height at which gravity is neutral
sea_level = 200
gravity = 0.5
friction = 0.1
surface_tension = 0.3
#height of the water at various positions
water_heights = []
#vertical acceleration of the water
dy = []
for i in range(0,screen_width+spacing,spacing):
    water_heights.append(screen_height-sea_level)
    dy.append(0)


#Create pointlist for drawing water
pointlist = []
for i in range(len(water_heights)):
    pointlist.append((spacing*i,water_heights[i]))
pointlist.append((screen_width,screen_height))
pointlist.append((0,screen_height))



def shiftWaterHeight(mouse_pos, water_heights):
    '''Shift the height of the water at a point to the height
    of the mouse click.'''
    x,y = mouse_pos
    index = 0
    for i in range(len(water_heights)):
        if spacing*i <= x and x <= spacing*(i+1):
            index = i
            break
    water_heights[index] = y



done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            print(event.key)
            if event.key == pygame.K_ESCAPE:
                done = True
            if event.key == 32: #space bar
                pass
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            shiftWaterHeight(pos, water_heights)

    #Update all dy values based on height, neighboring dy values, and friction.
    for i in range(len(dy)):
        #Neighboring heights pull on the dy values
        neighbor_heights = 0
        neighbor_count = 0
        if i>0:
            neighbor_heights += water_heights[i-1]
            neighbor_count += 1
        if i<len(dy)-1:
            neighbor_heights += water_heights[i+1]
            neighbor_count += 1
        dy[i] += surface_tension*(neighbor_heights - neighbor_count*water_heights[i])
        #High water falls and low water rises
        if water_heights[i] < screen_height-sea_level:
            dy[i] += gravity
        elif water_heights[i] > screen_height-sea_level:
            dy[i] -= gravity
        #friction
        dy[i] = (1-friction)*dy[i]

    #Update all y values based on dy.
    for i in range(len(water_heights)):
        water_heights[i] += dy[i]

    #Update pointlist
    for i in range(len(water_heights)):
        pointlist[i] = (spacing*i,water_heights[i])


    surface.fill(black)
    pygame.draw.polygon(surface, blue, pointlist)
    pygame.display.flip()
    clock.tick(30)
pygame.quit()