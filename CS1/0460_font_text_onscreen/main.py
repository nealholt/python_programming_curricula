'''
This is not a project, just an example of how to write text on the 
screen.
'''
import pygame

pygame.init()

black = 0,0,0
white = 255,255,255
red = 255,0,0

width = 800
height = 600
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

#Create a font object for drawing text. Choose the font and font size
font = pygame.font.SysFont('Arial', 25)
#Create a text object that can be drawn on the screen. This text
#object says cookies
text = font.render('Cookies',True,white)
#This text object has a number
x = 1
numeric_text = font.render(str(x),True,red)

done = False
while not done:
     #Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True

    screen.fill(black) #fill screen

    #Draw the text on the screen
    screen.blit(text, (100, 200))
    screen.blit(numeric_text, (300, 100))

    #Increase the number
    x = x+1
    numeric_text = font.render(str(x),True,red)

    pygame.display.flip()
    #Delay to get 30 fps
    clock.tick(30)

pygame.quit()