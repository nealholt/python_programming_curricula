'''
For 15 points, modify the code below to cut out one of the
running man images from walksequence_spritesheet.png.
The cut out must be centered on the man, without overlapping any
of the other running man image segments.

The Pygame subsurface function can be used to make a new image
from a part of another image as in:
    sub_image = sheet.subsurface(rect)
where sheet is the original image and rect is a rectangle
specifying the x, y, width, and height we want to use for the
cut out.

For instance:

#Get the original image:
sheet = pygame.image.load('walksequence_spritesheet.png')

#Use these variables to cut out a sub image
x = 250
y = 480
width = 200
height = 150
rect = pygame.Rect(x,y,width,height)

sub_image = sheet.subsurface(rect)
#Now sub_image is a new image that can be blitted on the screen.
'''
import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((500,600))

#Load the image
#Image source: dgkidderminster.blogspot.com/p/sprites.html
sheet = pygame.image.load('walksequence_spritesheet.png')

#Use these variables to cut out a sub image
x = 250
y = 480
width = 200
height = 150

#Get the rectangle of the subimage
rect = pygame.Rect(x,y,width,height)

#Cut out the sub_image using the subsurface function
sub_image = sheet.subsurface(rect)


#Draw all images on the screen
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #Draw the image at the location x=20, y=20
    screen.blit(sub_image, (20,20))

    #Update the screen
    pygame.display.flip()
    #Delay to get 10 fps
    clock.tick(10)

pygame.quit()