import sys, pygame, sprite, random, bird, wall

pygame.init()

#Create some constant values to make the code more readable.
width = 1000
height = 600
white = (255, 255, 255) #r g b

#Create the pygame drawing surface and clock
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

#Player starts off with zero points
points = 0

#Create the game objects
bird = bird.Bird(100,0,screen)
coin = sprite.Sprite(width,0,"coin.png", screen)
walls = wall.Wall(screen)

#Run the main game loop
running = True
while running:
    #Check for events such as user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            #The up key will send the bird upward
            if event.key == pygame.K_UP:
                bird.dy = bird.dy - 4
            #The escape key will close the game
            if event.key == pygame.K_ESCAPE:
                running = False

    #Move the bird and change its velocity
    bird.update()
    #Move the walls.
    walls.moveAmount(-5,0)
    #Move the coin
    coin.moveAmount(-6,0)

    #TODO1
    '''Check to see if the x coordinate of the wall, walls.toprect.x,
    is off the left side of the screen (x coordinate zero). If it is,
    call the walls' resetLocation function.'''

    #TODO2
    '''Check to see if the x coordinate of the coin, coin.rect.x,
    is off the left side of the screen (x coordinate zero). If it is,
    call the coin's setLocation function. setLocation takes two
    arguments separated by a comma. For the first argument pass
    the variable width, for the width of the screen.
    For the second argument pass random.randint(0,height-coin.rect.height)
    to give the coin a random height that is still on the screen.'''

    #TODO3
    '''Use bird.collided(coin) to check if the bird hits the coin. If so,
    reset the coin location as you did in the previous todo, then increase
    points by 1 and print the current points.'''

    #TODO4
    '''Use walls.collided(bird) to check if the bird hits the walls. If so,
    deduct a point from the bird and reset the location of the wall by
    calling walls' resetLocation function.'''

    #Draw a white background then draw all the game objects
    screen.fill(white)
    bird.draw()
    walls.draw()
    coin.draw()
    pygame.display.flip()
    #Delay to get 60 frames per second
    clock.tick(60)
pygame.quit()