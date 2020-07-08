import pygame
#The following line of code makes it so that we don't have to say
#colors.blue to reference blue. It's as if all the code in
#colors.py was copied and pasted into our code right here.
from colors import *

#Put all the colors from colors.py in a list.
color_list = [white, blue, red, green, yellow, gray, purple, lightblue, seagreen, mauve, violet,lightgray, orange, bluegreen, purplish, gold]

#Set up the drawing surface
width = 800
height=600
surface = pygame.display.set_mode((width, height))
surface.fill(black)
clock = pygame.time.Clock()

#Loop through each color and draw the color in a rectangle
i=0
for c in color_list:
    i=i+1
    #Increase the y value each time so the rectangles don't stack
    rect1 = pygame.Rect(100, i*25, 200, 20) #x, y, width, height
    pygame.draw.rect(surface, c, rect1)
    surface.fill(c, rect1)

#Update the drawing surface once here and never again.
pygame.display.flip()

#Run a slim main loop to keep the colors on the screen.
running = True
while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    clock.tick(30)

pygame.quit()