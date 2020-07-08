import pygame
#Initialize pygame content
pygame.init()

#All keyboard and mouse input will be handled by the following function
def handleEvents():
    #Check for new events
    for event in pygame.event.get():
        #This if makes it so that clicking the X actually closes the game
        #weird that that wouldn't be default.
        if event.type == pygame.QUIT:
            pygame.quit(); exit()
        #Has any key been pressed?
        elif event.type == pygame.KEYDOWN:
            #Escape key also closes the game.
            if event.key == pygame.K_ESCAPE:
                pygame.quit(); exit()
            #Up key moves the bird rectangle up
            elif event.key == pygame.K_UP:
                bird_rect.y = bird_rect.y - 5

#Initialize variables:
clock = pygame.time.Clock()
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode((screen_width,screen_height))
green = 0,255,0
red = 255,0,0
blue = 0,0,255
yellow = 255,255,0
white = 255,255,255
black = 0,0,0

#Create a rectangle object named bird_rect
bird_rect = pygame.Rect(100,100,50,50)

#Main program loop
while True:
    handleEvents()
    screen.fill(black) #erase everything on the screen to black
    #Draw the bird rectangle on the screen
    pygame.draw.rect(screen, yellow, bird_rect)
    #Update the display screen with the new things that have been drawn
    pygame.display.flip()
    #Delay to get 30 fps
    clock.tick(30)
