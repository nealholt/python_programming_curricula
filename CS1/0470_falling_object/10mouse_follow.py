'''
For 18 points, answer the following questions.

pos = pygame.mouse.get_pos()
The line of code above creates a list with two values in it where the first
value is the x coordinate of the mouse and the second value is the y
coordinate of the mouse.

1) How does the hoop image relate to the mouse in this program?

2) How does the program change if you replace this line of code
hoop_rect.y = pos[1]
with this instead
hoop_rect.y = height - hoop_rect.height

3) The height variable represents the height of what?

4) What happens if you use hoop_rect.height/2 instead of hoop_rect.height
in this line of code?
hoop_rect.y = height - hoop_rect.height

5) Based on the previous question, what can you conclude is the purpose of
hoop_rect.height ?

6) It would be better if the hoop stayed centered on the mouse.
Use   hoop_rect.width/2   to modify the position of the hoop so it centers
on the mouse. Note that   hoop_rect.width/2   is half the width of the hoop
image.

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

#Run the main loop
while True:
    handleEvents()

    screen.fill(white) #fill screen

    #Get mouse coordinates
    pos = pygame.mouse.get_pos()
    hoop_rect.x = pos[0]
    hoop_rect.y = pos[1]

    #Draw image
    screen.blit(hoop, hoop_rect)

    #Update screen.
    pygame.display.flip()
    #Delay to get 30 fps
    clock.tick(30)
