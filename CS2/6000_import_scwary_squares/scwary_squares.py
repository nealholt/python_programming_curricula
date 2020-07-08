import pygame, random, functions, player
from constants import * #import everything as if the code was copied
#Initialize pygame content
pygame.init()

#Initialize variables:
clock = pygame.time.Clock()
surface = pygame.display.set_mode((screen_width,screen_height))

#Create a rectangle object for the player
p = player.Player(100,100,rect_size, yellow)

#Create deadly-to-touch rectangles
deadly_rects = []
for i in range(num_deadly):
    x = random.randint(0,screen_width-rect_size)
    y = random.randint(0,screen_height-rect_size)
    temp = pygame.Rect(x,y,rect_size,rect_size)
    deadly_rects.append(temp)

#Create our goal rectangles
goal_rects = []
for i in range(num_goal):
    x = random.randint(0,screen_width-rect_size)
    y = random.randint(0,screen_height-rect_size)
    temp = pygame.Rect(x,y,rect_size,rect_size)
    goal_rects.append(temp)

#Main program loop
while True:
    functions.handleEvents(p)
    functions.checkCollisions(p, deadly_rects, goal_rects)
    surface.fill(black) #erase everything on the screen to black
    #Draw the player rectangle on the surface (which is our screen)
    p.draw(surface)
    for d in deadly_rects:
        if functions.distance(p.x,p.y,d.x,d.y) < vision_radius:
            pygame.draw.rect(surface, red, d)
    for g in goal_rects:
        if functions.distance(p.x,p.y,g.x,g.y) < vision_radius:
            pygame.draw.rect(surface, green, g)
    #Update the display surface with the new things that have been drawn
    pygame.display.flip()
    #Delay to get 30 fps
    clock.tick(30)
