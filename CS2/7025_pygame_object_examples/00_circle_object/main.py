import pygame, circle

screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

black = 0,0,0
white = 255,255,255
green = 0,255,0
red = 255,0,0
blue = 0,0,255

x = 100
y = 100
radius = 150

c = circle.Circle(screen, green, x, y, radius)

running = True
while running:
    #Respond to events such as closing game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    c.move(1,0)
    screen.fill(black)
    c.draw()
    pygame.display.flip()
    #Delay the program to run 60 loops per second
    clock.tick(60)

pygame.quit()