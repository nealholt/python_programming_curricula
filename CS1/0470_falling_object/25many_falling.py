'''
For 35 points, answer the following questions.

The following program creates many falling basketballs and resets the balls
to the top of the screen when they fall off the bottom. Run the program and
read the code carefully before answering the following questions

1) As the program is written, what's the fastest speed a ball could fall at?

2) What is dys[i] and how does it relate to what is happening in this line
of code   y = y+dys[i]   ?

3) Why is this line of code important?
balls[i] = (x,y)

4) Why is there a zero instead of a y variable in this line of code?
balls[i] = (x,0)

5) Give a reason why the program might keep a list of ball locations instead
of a list of ball rectangles or images.

6) Modify the code so that the balls fall faster due to gravity. Don't forget
to reset their speed to zero when you put a ball back to the top of the screen.
'''
import pygame, random

def handleEvents():
    #Handle keyboard and mouse events. This is only used to quit
    #the program in this case.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit(); exit()

pygame.init()

white = 255,255,255
black = 0,0,0

#Set the screen dimensions
width = 900
height = 600
#Set up pygame, the screen, and the clock
pygame.init()
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

#Load images
basketball = pygame.image.load('basketball.png')
basketball = basketball.convert()
colorkey = basketball.get_at((0,0))
basketball.set_colorkey(colorkey, pygame.RLEACCEL)

#Make 5 different ball locations with 5 different velocities
balls = [] #ball locations
dys = [] #ball vertical velocities
for i in range(5):
    x = random.randint(0,width-50)
    y = random.randint(-50,50)
    balls.append((x,y))
    dys.append(random.randint(2,6))

#Run the main loop
while True:
    handleEvents()

    screen.fill(white) #fill screen

    #Move each ball's location based on its velocity
    for i in range(len(balls)):
        #Move the ball
        x,y = balls[i]
        y = y+dys[i]
        balls[i] = (x,y)
        #If the ball is off the bottom of the screen, reset it to a random
        #location at the top
        if y > height:
            x = random.randint(0,width-50)
            balls[i] = (x,0)

    #Draw a ball at each ball location
    for b in balls:
        screen.blit(basketball,b)
    #Update screen.
    pygame.display.flip()
    #Delay to get 30 fps
    clock.tick(30)
