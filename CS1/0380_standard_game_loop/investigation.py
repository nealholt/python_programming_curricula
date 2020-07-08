'''
For 70 points, complete the following investigation and answer the
questions below.

Pygame is a wonderful resource for creating simple computer games.
The following is my version of the standard template for games.

The formatting looks roughly like this:

setup
main loop
	receive inputs
	update
	draw
	timing delay to reach the desired frame rate
'''

#Read and run the following program then answer the following questions.

import pygame
#Initialize pygame content
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
            #Up key moves the bird rectangle up
            elif event.key == pygame.K_UP:
                rectangle.y = rectangle.y - 5

#Initialize variables:
clock = pygame.time.Clock()
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode((screen_width,screen_height))
green = 0,255,0
red = 255,0,0
blue = 0,0,255
yellow = 255,255,0
white = 255,255,255
black = 0,0,0

A = 100
B = 50
C = 300
D = 400
rectangle = pygame.Rect(A,B,C,D)

#Main program loop
while True:
    handleEvents()
    screen.fill(black) #erase everything on the screen to black
    #Draw the bird rectangle on the screen
    pygame.draw.rect(screen, yellow, rectangle)
    #Update the display surface with the new things that have been drawn
    pygame.display.flip()
    #Delay to get 30 fps
    clock.tick(30)

#QUESTIONS:

#1. Change a single line of code to draw the rectangle as blue. Then 
#copy the changed line of code as your answer to this question.

#2. Write two lines of code that cause the rectangle to move down when 
#the down key is pressed. Then copy the changed line of code as your 
#answer to this question.

#3. Write four lines of code that cause the rectangle to move left and 
#right when the left and right keys are pressed. Then copy the changed 
#line of code as your answer to this question.

#4. Experiment with these values then change the names of these 
#variables to better reflect the meaning of these values. Then copy the 
#changed line of code as your answer to this question.
'''A = 100
B = 50
C = 300
D = 400
rectangle = pygame.Rect(A,B,C,D)
'''

#5. Experiment with the order of the following lines of code. There 
#will be a quiz question about which of these lines can be reordered 
#and for which lines the order does not matter.
'''
handleEvents()
screen.fill(black) #erase everything on the screen to black
pygame.draw.rect(screen, yellow, rectangle)
pygame.display.flip()
clock.tick(30)
'''
