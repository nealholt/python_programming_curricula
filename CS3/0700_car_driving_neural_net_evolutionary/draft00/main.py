import pygame, player

#Setup
pygame.init()
width = 900
height = 600
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
black = 0,0,0

def userInputToPlayer(player):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.moveForward()
    if keys[pygame.K_DOWN]:
        pass #Do nothing
    if keys[pygame.K_LEFT]:
        player.rotateLeft()
    if keys[pygame.K_RIGHT]:
        player.rotateRight()
    if keys[pygame.K_a]:
        pass
    if keys[pygame.K_d]:
        pass


def handleEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return True
    return False

def drawAndDelay(player):
    #fill screen with black
    screen.fill(black)
    #Draw player
    player.draw()
    #Update the screen
    pygame.display.flip()
    #Delay to get 30 fps
    clock.tick(30)


#Create the player
player = player.Player(screen, 100, 200)

#Main loop
done = False
while not done:
    #Handle any events, possibly closing the game.
    done = handleEvents()
    #Send user input to the player
    userInputToPlayer(player)
    #Draw on the screen
    drawAndDelay(player)

pygame.quit()