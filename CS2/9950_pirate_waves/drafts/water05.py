'''
This is awesome. Next you could give the boat a little more dy so it bounces up
off the waves then sinks a little in the water.

When the back is above water, gravity pulls it down.
When it is below water bouyancy shoves it up.
There is also some friction.



Implement a "jump" ability for the ship and collectibles that scroll past.

Add in little islands with cannons to defeat.

Implement splash in the water.

https://www.youtube.com/watch?v=SO7FFteErWs

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


def load_image(name, colorkey=None):
    #Load the image from file
    try:
        image = pygame.image.load(name)
    except pygame.error:
        print('ERROR: Failed to load image named "'+name+'". Probably a typo.')
        pygame.quit()
        exit()
    #This next line creates a copy that will draw more quickly on the screen.
    image = image.convert()
    #If colorkey is None, then don't worry about transparency
    if colorkey is not None:
        #colorkey of -1 means that the color of upper left most pixel should
        #be used as transparency color.
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        '''The optional flags argument can be set to pygame.RLEACCEL to provide better performance on non accelerated displays. An RLEACCEL Surface will be slower to modify, but quicker to blit as a source.'''
        image.set_colorkey(colorkey, pygame.RLEACCEL)
    #Return the image and its rectangle
    return image, image.get_rect()

def rotateImage(image, original_rect, angle):
    '''Rotate an image while keeping its center the same.
    The size of the image's rectangle will change.
    Angle is in degrees.'''
    #Get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)
    #Get the rectangle of the new image
    rotated_rect = rotated_image.get_rect()
    #Set the center of the new rectangle to match the center of the old rectangle
    rotated_rect.center = original_rect.center
    #Return new image and rectangle
    return rotated_image, rotated_rect

#Spacing between water height locations
spacing = 10 #pixels
sea_level = 200
friction = 0.01
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

def getWaterHeightAt(x,water_heights):
    index = 0
    for i in range(len(water_heights)):
        if spacing*i <= x and x <= spacing*(i+1):
            index = i
            break
    adjusted_x = x-spacing*index
    rise = water_heights[index+1]-water_heights[index]
    run = spacing*(i+1)-spacing*i
    slope = rise/run
    return adjusted_x*slope+water_heights[index]


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



boat_img,boat_rect = load_image('images/1stship_3.png',-1)
#Scale down the image
scaling = 0.2
dimensions = (int(boat_rect.width*scaling), int(boat_rect.height*scaling))
boat_img = pygame.transform.scale(boat_img, dimensions)
boat_rect.width = dimensions[0]
boat_rect.height = dimensions[1]
#Horizontal flip
boat_img = pygame.transform.flip(boat_img, True, False)
boat_rect.x = int(screen_width/3)

#Buffer of empty pixels around boat image to make the boat
#sink down in the water more.
buffer = 15

#Upward pressure from being under water. Is a function of depth
bouyancy = 0.09
#Constant downward acceleration
gravity = 0.5
air_friction = 0.01
water_friction = 0.1
#Vertical velocity for front and back of the ship
rear_dy = 0
rear_y = screen_height-sea_level
front_dy = 0
front_y = screen_height-sea_level

#Use to oscillate the right-most water_heights value
oscillator = 0
amplitude = 100
period = 30

done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            print(event.key)
            if event.key == pygame.K_ESCAPE:
                done = True
            if front_under_water and rear_under_water and event.key == 32: #space bar
                #Jump with spacebar if the boat is solidly in the water!
                rear_dy-=20
                front_dy-=20
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
        #friction
        dy[i] = (1-friction)*dy[i]

    #Update all y values based on dy.
    for i in range(len(water_heights)):
        water_heights[i] += dy[i]

    #Update pointlist
    for i in range(len(water_heights)):
        pointlist[i] = (spacing*i,water_heights[i])

    #Oscillate the right-most water height value
    water_heights[-1] = screen_height-sea_level-amplitude*math.sin(oscillator/period)
    oscillator += 1

    #Update vertical velocity of left and right sides of the boat
    lefty = getWaterHeightAt(boat_rect.left,water_heights)+buffer
    rear_under_water = False
    if rear_y>lefty: #under water
        rear_under_water = True
        depth = rear_y-lefty
        rear_dy = (1-water_friction)*rear_dy-bouyancy*depth
    rear_dy = (1-air_friction)*rear_dy+gravity
    righty = getWaterHeightAt(boat_rect.right,water_heights)+buffer
    front_under_water = False
    if front_y>righty: #under water
        front_under_water = True
        depth = front_y-righty
        front_dy = (1-water_friction)*front_dy-bouyancy*depth
    front_dy = (1-air_friction)*front_dy+gravity
    #Update height of left and right sides of the boat.
    rear_y += rear_dy
    front_y += front_dy
    #Position boat
    angle = (180/math.pi)*math.atan2(rear_y-front_y, boat_rect.width)
    rota_img,rota_rect = rotateImage(boat_img, boat_rect, angle)
    #I assume that the bottom of the rectangle needs to be the lower of
    #the two y values
    rota_rect.bottom = max(rear_y,front_y)

    #Draw everything
    surface.fill(black)
    surface.blit(rota_img, rota_rect)
    pygame.draw.polygon(surface, blue, pointlist)
    pygame.display.flip()
    clock.tick(30)
pygame.quit()