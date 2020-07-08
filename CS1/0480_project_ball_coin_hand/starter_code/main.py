import sys, pygame, sprite, random
pygame.init()

width = 1000
height = 600
black = (0, 0, 0) #r g b

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

#Create a sprite named ball using ball.png
ball = sprite.Sprite(0,0,"ball.png", screen)
#Create a sprite named hand using hand.png
#______________
#Create a sprite named coin using coin.png
#______________

#Create a variable to store the player's points
#______________

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        '''
        #Uncomment the following to move the hand.
        #This will only work after the hand has
        #been created.
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                hand.moveAmount(-70,0)
            if event.key == pygame.K_RIGHT:
                hand.moveAmount(70,0)
            if event.key == pygame.K_UP:
                hand.moveAmount(0,-70)
            if event.key == pygame.K_DOWN:
                hand.moveAmount(0,70)
        '''

    ball.move()

    #Check to see if the hand collided with the coin.
    #Use hand.collided(coin) which returns True if
    #they did collide and false otherwise.
    #If they did collide, use setLocation and random.randint
    #to set the coin to a a new random loction.
    #Then increase the player's points by one.
    #Then print the player's score.
    #______________
    #______________
    #______________
    #______________
    #______________

    #Check to see if the hand collided with the ball.
    #Use hand.collided(ball) which returns True if
    #they did collide and false otherwise.
    #If they did collide, print GAME OVER,
    #then end the game.
    #______________
    #______________
    #______________

    screen.fill(black)
    ball.draw() #draw the ball
    #______________ #draw the hand
    #______________ #draw the coin
    pygame.display.flip()
    #Delay to get 60 fps
    clock.tick(60)
pygame.quit()