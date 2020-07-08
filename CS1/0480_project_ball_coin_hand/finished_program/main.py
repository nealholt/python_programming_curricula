import pygame, sprite, random
pygame.init()

width = 1000
height = 600
black = (0, 0, 0) #r g b

screen = pygame.display.set_mode((width, height))

points = 0

ball = sprite.Sprite(0,0,"ball.png", screen)
hand = sprite.Sprite(220,0,"hand.png", screen)
coin = sprite.Sprite(0,330,"coin.png", screen)

points = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            #print(event.key)
            if event.key == pygame.K_LEFT:
                hand.moveAmount(-70,0)
            if event.key == pygame.K_RIGHT:
                hand.moveAmount(70,0)
            if event.key == pygame.K_UP:
                hand.moveAmount(0,-70)
            if event.key == pygame.K_DOWN:
                hand.moveAmount(0,70)

    ball.move()

    if hand.collided(coin):
        x = random.randint(0, width-100)
        y = random.randint(0, height-100)
        coin.setLocation(x, y)
        points = points + 1
        print("Points: "+str(points))

    if hand.collided(ball):
        print("GAME OVER")
        pygame.quit()
        exit(0)

    #Do all the drawing on the screen
    screen.fill(black) #erase
    ball.draw()
    hand.draw()
    coin.draw()
    pygame.display.flip() #update the screen
pygame.quit()