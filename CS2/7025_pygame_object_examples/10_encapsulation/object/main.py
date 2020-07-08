import sys, pygame, sprite
pygame.init()

width = 1000
height = 600
black = (0, 0, 0) #r g b

screen = pygame.display.set_mode((width, height))

ball = sprite.Sprite(0,0,"ball.gif", screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ball.move()
    screen.fill(black)
    ball.draw()
    pygame.display.flip()
