'''
For 70 points, use this program to answer the following questions about
moving an image on the screen.

1. Run this program and describe what happens


Uncomment the code right after   #PART A.
2. How is the program different when you run it now?


3. Write a comment in the code (and copy what you write here) that describes
why the code after   #PART A   is useful.


Experiment with the values of   dx = 3   and   dy = 3
3. In your own words, what does dx affect?
4. In your own words, what does dy affect?


Uncomment the code right after #PART B.
5. How is the program different when you run it now?


6. Write a comment in the code (and copy what you write here) that describes
why the code after   #PART B   might be useful.


Uncomment the code right after   #PART C.
7. How is the program different when you run it now?


8. What would you say the code after   #PART C   simulates?


9. Write a comment for the code after   #PART C.


For 70 MORE points, modify this program so that the ball does not "jitter"
and then slowly sink into the floor. Start by considering what might be
causing this.


For 35 MORE points, modify this program to use the arrow keys to change dx
and dy. See what interesting control schemes you can create for the ball.
Code to get you started on this already exists in the handleEvents function.
'''
import pygame
pygame.init()

#All keyboard and mouse input will be handled by the following function
def handleEvents():
    #This next line of code lets this function access the dx and dy
    #variables without passing them to the function or returning them.
    global dx,dy
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
            elif event.key == pygame.K_RIGHT:
                pass
            elif event.key == pygame.K_LEFT:
                pass
            elif event.key == pygame.K_UP:
                pass
            elif event.key == pygame.K_DOWN:
                pass

width = 1000
height = 600
size = (width, height)
black = (0, 0, 0) #r g b

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

ball = pygame.image.load("ball.gif")
ballrect = ball.get_rect()

x = 0
y = 0
dx = 3
dy = 3

done = False
while not done:
    handleEvents()

    #Move the ball
    x = x + dx
    y = y + dy
    ballrect.topleft = (x,y)

    #PART A
    '''
    if ballrect.left < 0 or ballrect.right > width:
        dx = -dx
    if ballrect.top < 0 or ballrect.bottom > height:
        dy = -dy
    '''

    #PART B
    '''
    dy = dy * 0.99
    dx = dx * 0.99
    '''

    #PART C
    '''
    dy = dy + 0.3
    '''

    #Draw everything
    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()

    #Delay to get 30 fps
    clock.tick(30)

pygame.quit()