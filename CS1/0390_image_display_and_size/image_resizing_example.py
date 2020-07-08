'''
There is no assignment here. This is just an example of how to
re-size then display an image on the screen using Pygame.
'''

import pygame
pygame.init()

#All keyboard and mouse input will be handled by the following function
def handleEvents():
    #Check for new events
    for event in pygame.event.get():
        #This if makes it so that clicking the X actually closes the game
        #weird that that wouldn't be default.
        if event.type == pygame.QUIT:
            pygame.quit(); exit()
        #Has any key been pressed?
        elif event.type == pygame.KEYDOWN:
            #Escape key also closes the game.
            if event.key == pygame.K_ESCAPE:
                pygame.quit(); exit()


black = 0,0,0
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

#Load the image to display
image = pygame.image.load('donut.png')


#Resize the image
rectangle = image.get_rect()
scaling = 2 #How much larger or smaller to make the image. 1 is no change. Half size would be 0.5
#Get the new image dimensions
dimensions = (rectangle.width*scaling,rectangle.height*scaling)
#Get the new re-sized image
image = pygame.transform.scale(image, dimensions)


done = False
while not done:
	handleEvents()
    #Draw everything
	screen.fill(black) #fill screen
	screen.blit(image, (0,0))
	pygame.display.flip()
	#Delay to get 30 fps
	clock.tick(30)

pygame.quit()