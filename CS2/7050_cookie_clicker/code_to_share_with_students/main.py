import pygame

pygame.init()

black = 0,0,0
white = 255,255,255

width = 800
height = 600
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

#Create a font object that is needed for drawing text on the screen.
font = pygame.font.SysFont('Arial', 25)
text_position = (100, 100)
#Get a new text object of the word cookies
text_image = font.render('Cookies',True,white)
#Whether or not to display the text
text_on = True

#Draw all images on the screen
done = False
while not done:
    #Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #Detect mouse clicks
        elif event.type == pygame.MOUSEBUTTONUP:
            #Get the x,y coordinates of the mouse as a pair in the variable pos
            pos = pygame.mouse.get_pos()
            print(pos)
            #If the text was on, turn it off, and vice versa.
            text_on = not text_on
            #How to see if a rectangle contains a point:
            #rect.collidepoint(pos) - returns true or false
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True

    screen.fill(black) #fill screen

    if text_on:
        #Draw text on the screen
        screen.blit(text_image, text_position)

    pygame.display.flip()
    #Delay to get 60 fps
    clock.tick(60)
pygame.quit()