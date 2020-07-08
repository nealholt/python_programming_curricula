import pygame

pygame.init()

#Variables
black = 0,0,0
white = 255,255,255

#Load image
cutout_image = pygame.image.load('images/cat.png')

#Scale the image
rectangle = cutout_image.get_rect()
scaling = 1
dimensions = (int(rectangle.width*scaling),
              int(rectangle.height*scaling))
cutout_image = pygame.transform.scale(cutout_image, dimensions)

#Set the screen dimensions to fit the image perfectly.
width = dimensions[0]
height = dimensions[1]
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

#Run the main loop
done = False
while not done:
    #Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
    screen.fill(white) #fill screen
    #Get mouse coordinates
    pos = pygame.mouse.get_pos()
    mouse_x = pos[0]
    mouse_y = pos[1]
    #Draw eyes cutout image
    screen.blit(cutout_image, (0,0))
    #Draw pupils
    pygame.draw.ellipse(screen, black,
                    [100, #x
                    100, #y
                    30, #width
                    30] #height
                    )
    #Draw image that follows the cursor

    #Update screen.
    pygame.display.flip()
    #Delay to get 30 fps
    clock.tick(30)

pygame.quit()