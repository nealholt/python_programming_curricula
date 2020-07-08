'''You can create an animation by loading and displaying a sequence 
of images.
For 35 points, read and run the following program then answer the 
following questions.'''

import pygame, time

pygame.init()
screen_width = 100
screen_height = 150
dimensions = (screen_width,screen_height)
screen = pygame.display.set_mode(dimensions)

#Load the images from file
image1 = pygame.image.load('images/right001.png')
image2 = pygame.image.load('images/right000.png')

for i in range(0,60,4):
    screen.fill((0,0,0)) #fill the screen with black. In other words, erase previous images
    screen.blit(image1, (i,0))
    pygame.display.flip()
    time.sleep(0.2)

    screen.fill((0,0,0)) #fill the screen with black. In other words, erase previous images
    screen.blit(image2, (i,0))
    pygame.display.flip()
    time.sleep(0.2)

pygame.quit()

#1. How many times does the for loop repeat?
#2. How is the loop control variable i being used?
'''3. Create and turn in your own animation. For full credit you must
load at least three different images and use at least two different
for loops. Your animation can be as simple as making the slime
monster walk right and then walk left.
Feel free to make your program more complicated than that if you wish.'''
