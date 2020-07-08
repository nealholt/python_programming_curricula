import pygame, player, bullet, math

#Setup
pygame.init()
screen_width = 1100
screen_height = 650
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
black = 0,0,0


def userInputToPlayer(p):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        p.accelerateForward()
    if keys[pygame.K_DOWN]:
        p.accelerateBackward()
    if keys[pygame.K_LEFT]:
        p.accelerateLeft()
    if keys[pygame.K_RIGHT]:
        p.accelerateRight()
    if keys[pygame.K_a]:
        p.rotateCounterClockwise()
    if keys[pygame.K_d]:
        p.rotateClockwise()


def handleEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return True
            elif event.key == pygame.K_SPACE:
                #Create new bullet
                b = bullet.Bullet(screen, p.x,p.y,p.angle)
                #Add new bullet to list
                bullets.append(b)
    return False

def drawAndDelay(p, bullets, target):
    #fill screen with black
    screen.fill(black)
    #Draw ps and bullets
    p.draw()
    for b in bullets:
        b.draw()
    target.draw()
    #Update the screen
    pygame.display.flip()
    #Delay to get 30 fps
    clock.tick(30)

def updateBullets(bullets):
    for i in reversed(range(len(bullets))):
        #Move bullets[i]
        bullets[i].moveForward()
        #Reduce the timer on bullets[i]
        bullets[i].timeout = bullets[i].timeout - 1
        #Delete bullets[i] if its timer is less than zero
        if bullets[i].timeout < 0:
            del bullets[i]



#Create the player
p = player.Player(screen, 100, 200)
#Create bullet list
bullets = []
#create the target
target = bullet.Bullet(screen, screen_width/2, screen_height/2, 0)

#Main loop
done = False
while not done:
    #Handle any events, possibly closing the game.
    done = handleEvents()

    #Send user input to the player
    #userInputToPlayer(p)
    p.update(target,bullets)

    p.moveBallistic()
    updateBullets(bullets)
    #Draw on the screen
    drawAndDelay(p, bullets, target)

pygame.quit()