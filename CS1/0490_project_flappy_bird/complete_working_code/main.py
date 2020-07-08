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
while True:
    #Check for events such as user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        elif event.type == pygame.KEYDOWN:
            #The up key will send the bird upward
            if event.key == pygame.K_UP:
                bird.dy = bird.dy - 4
            #The escape key will close the game
            if event.key == pygame.K_ESCAPE:
                pygame.quit(); sys.exit()

    #Move the bird and change its velocity
    bird.update()

    #Move the walls.
    walls.moveAmount(-5,0)
    #If the walls move off the left side of the screen, set their
    #location to be to the right of the screen.
    if walls.toprect.x < -walls.width:
        walls.resetLocation()

    #Move the coin
    coin.moveAmount(-6,0)
    #If the coin moves off the left side of the screen, set its
    #location to be to the right of the screen.
    if coin.rect.x < -coin.rect.width or walls.collided(coin):
        coin.setLocation(width,random.randint(0,height-coin.rect.height))

    #If the bird hits the coin, reset the coin location and
    #give the bird a point.
    if bird.collided(coin):
        coin.setLocation(width,random.randint(0,height-50))
        points = points + 1
        print("Points: "+str(points))

    #If the bird hits a wall, deduct a point from the bird and
    #reset the location of the wall.
    if walls.collided(bird):
        points = points - 1
        print("Points: "+str(points))
        walls.resetLocation()

    #Draw a white background then draw all the game objects
    screen.fill(white)
    bird.draw()
    walls.draw()
    coin.draw()
    pygame.display.flip()
    #Delay to get 60 frames per second
    clock.tick(60)
