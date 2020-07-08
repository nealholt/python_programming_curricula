'''
For 18 points, answer the following questions.

colliderect is a function for checking to see if two Pygame Rect objects
are colliding. If A and B are Rects then we can run some code if they are
currently colliding using
if A.colliderect(B):
    #do some code cuz they be collid'n!
This can be very handy for implementing hitboxes and hurtboxes in games
and generally creating interesting interaction.

1) How does the program's behavior change if this code is deleted or
commented out?
    else:
        test_color = blue

2) How does the program's behavior change if you reverse the order of theses
lines of code?
    pygame.draw.rect(screen, test_color, test_rectangle)
    screen.blit(hoop, hoop_rect)

3) Modify the program so that instead of changing the color of the test
rectangle every time it collides with the hoop, the test_rectangle moves to
a random new location on the screen.
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
red = 255,0,0
blue = 0,0,255

#Set the screen dimensions
width = 900
height = 600
#Set up pygame, the screen, and the clock
pygame.init()
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

#Load image
hoop = pygame.image.load('hoop.png')
hoop = hoop.convert()
hoop_rect = hoop.get_rect()
colorkey = hoop.get_at((0,hoop_rect.height-1))
hoop.set_colorkey(colorkey, pygame.RLEACCEL)

#Create a rectangle
test_rectangle = pygame.Rect(300,300,100,100)
test_color = blue

#Run the main loop
while True:
    handleEvents()

    screen.fill(white) #fill screen

    #Get mouse coordinates
    pos = pygame.mouse.get_pos()
    hoop_rect.x = pos[0]
    hoop_rect.y = pos[1]

    #Test for collision
    if hoop_rect.colliderect(test_rectangle):
        test_color = red
    else:
        test_color = blue

    #Draw image
    pygame.draw.rect(screen, test_color, test_rectangle)
    screen.blit(hoop, hoop_rect)

    #Update screen.
    pygame.display.flip()
    #Delay to get 30 fps
    clock.tick(30)
