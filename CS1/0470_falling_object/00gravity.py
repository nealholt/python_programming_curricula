'''
For 35 points, answer the questions about the following program.

Gravity accelerates falling objects downward. The moment an apple falls off
a tree, it isn't moving at all, but it is accelerating. A moment after
disconnecting from the branch, the apple is moving slowly downward.
Right before the apple hits the ground, it's moving much faster because
gravity has been making it move faster.

0. How many frames per second is this program running at?

1. Which basketball moves the same distance between frames?

2. How far is the basketball that moves at a constant speed moving each frame?

3. Which basketball moves slower at the start, but faster at the end?

4. For the basketball that moves faster at the end, how much faster does it
move each frame?

5. dy is short for the difference in y, in other words the vertical speed.
Modify the code so that the basketball influenced by gravity also has a
constant dx value that affects its horizontal location.

6. Further modify the code so that the basketball influenced by gravity starts
at the bottom of the screen and starts with a negative dy. Can you make the
basketball travel in a realistic arc?

'''

import pygame

def handleEvents():
    #Handle keyboard and mouse events. This is only used to quit
    #the program in this case.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit(); exit()


#Set the screen dimensions
width = 900
height = 600
#Set up pygame, the screen, and the clock
pygame.init()
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

#Load images
basketball1 = pygame.image.load('basketball.png')
basketball1 = basketball1.convert()
colorkey = basketball1.get_at((0,0))
basketball1.set_colorkey(colorkey, pygame.RLEACCEL)

basketball2 = pygame.image.load('basketball.png')
basketball2 = basketball2.convert()
colorkey = basketball2.get_at((0,0))
basketball2.set_colorkey(colorkey, pygame.RLEACCEL)

#basketball initial position
basketball_x1 = 200
basketball_y1 = 0
basketball_x2 = 500
basketball_y2 = 0

#basketball falling speed variables
dy = 0
gravity = 6
speed = 40

#Run the main loop
while True:
    handleEvents()
    #Keep moving the basketballs so long as the left one is on the screen
    if basketball_y1 < height:
        #Move basketball 1
        basketball_y1 = basketball_y1 + dy
        dy = dy + gravity

        #Move basketball 2
        basketball_y2 = basketball_y2 + speed

        #Draw images
        screen.blit(basketball1, (basketball_x1,basketball_y1))
        screen.blit(basketball2, (basketball_x2,basketball_y2))
        #Update screen.
        pygame.display.flip()

    #Delay to get 5 fps
    clock.tick(5)
