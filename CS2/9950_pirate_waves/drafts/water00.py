'''
Display blue on the bottom
Get a list of heights of y values along the bottom.
Click to raise a single y value to height of mouse click.
Make a new array of dy values for each y value.
Update all y values based on dy.
Update all dy values based on neighboring dy values and friction.

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

spacing = 30 #pixels
sea_level = 200
water_heights = []
for i in range(0,screen_width+spacing,spacing):
    water_heights.append(screen_height-sea_level)


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

    #Update pointlist
    for i in range(len(water_heights)):
        pointlist[i] = (spacing*i,water_heights[i])


    surface.fill(black)
    pygame.draw.polygon(surface, blue, pointlist)
    pygame.display.flip()
    clock.tick(30)
pygame.quit()