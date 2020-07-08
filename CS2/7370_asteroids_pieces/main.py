import pygame, player, bullet

'''
Assignment:
    1. What happens in player.py if you add math.pi/2 inside
    the parentheses of math.cos() and math.sin() ?
    Use this information to write strafeLeft() and strafeRight()
    functions.
    2. Next, bind these new functions to the "a" and "d" keys
    on the keyboard. These keys have a numeric value. Print
    out event.key in the handleEvents() function then run the
    game and press these keys to see what value the keys have.
    3. In the updateBullets function, fill in the code to make
    the bullets fly around the screen.
'''

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
            elif event.key == pygame.K_SPACE:
                #Create new bullet
                b = bullet.Bullet(screen, player.x,player.y,player.angle)
                #Add new bullet to list
                bullets.append(b)
    return False

def drawAndDelay(player, bullets):
    #fill screen with black
    screen.fill(black)
    #Draw players and bullets
    player.draw()
    for b in bullets:
        b.draw()
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
player = player.Player(screen, 100, 200)
#Create bullet list
bullets = []

#Main loop
done = False
while not done:
    #Handle any events, possibly closing the game.
    done = handleEvents()
    #Send user input to the player
    userInputToPlayer(player)
    updateBullets(bullets)
    #Draw on the screen
    drawAndDelay(player, bullets)

pygame.quit()