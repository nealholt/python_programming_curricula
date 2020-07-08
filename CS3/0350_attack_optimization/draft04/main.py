import pygame, player, bullet, math, random

#Setup
pygame.init()
screen_width = 1100
screen_height = 650
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
black = 0,0,0
fps = 30

iterations = 50

visual = True
player_controlled = True

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
            pygame.quit(); exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit(); exit()

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
    #Delay to get desired fps
    global fps
    clock.tick(fps)

def updateBullets(bullets, target):
    points = 0
    for i in reversed(range(len(bullets))):
        #Move bullets[i]
        bullets[i].moveForward()
        #Reduce the timer on bullets[i]
        bullets[i].timeout = bullets[i].timeout - 1
        #Delete bullets[i] if its timer is less than zero
        if bullets[i].timeout < 0:
            del bullets[i]
        #Check collisions
        elif bullets[i].collidedCircular(target):
            points += 1
            del bullets[i]
    return points

def mutateAttackPattern(input_pattern):
    #Copy the pattern
    pattern = []
    for p in input_pattern:
        pattern.append(p)
    #mutate the pattern
    i = random.randint(0,len(pattern)-1)
    new_value = random.randint(-1,1)
    #Make sure this actually changes the pattern
    while pattern[i] == new_value:
        i = random.randint(0,len(pattern)-1)
        new_value = random.randint(-1,1)
    pattern[i] = new_value
    #Return new pattern
    return pattern


def experiment(pattern, visual=False, player_controlled=False):
    #Create the player
    p = player.Player(screen, 100, 200)
    p.attack_pattern = pattern
    #Create bullet list
    bullets = []
    #create the target
    target = bullet.Bullet(screen, screen_width/2, screen_height/2, 0)

    points = 0

    #Main loop
    timelimit = 20*fps
    for _ in range(timelimit):
        #Handle any events, possibly closing the game.
        handleEvents()

        #Send user input to the player
        if player_controlled:
            userInputToPlayer(p)
        else:
            p.update(target,bullets)

        #Lose points for colliding with target
        if p.collidedCircular(target):
            points -= 5

        p.moveBallistic()
        points += updateBullets(bullets, target)
        if visual:
            #Draw on the screen
            drawAndDelay(p, bullets, target)
    return points


#Perform experiments

#Get starting pattern
temp = player.Player(screen, 100, 200)
pattern1 = temp.attack_pattern

#Start with triple mutation
for _ in range(iterations):
    pattern2 = mutateAttackPattern(pattern1)
    pattern2 = mutateAttackPattern(pattern1)
    pattern2 = mutateAttackPattern(pattern1)
    points1 = experiment(pattern1, visual, player_controlled)
    points2 = experiment(pattern2, visual, player_controlled)
    print(points1,points2)
    if points2 > points1:
        pattern1 = pattern2
        print('better pattern found')
#Dial down to double mutation
for _ in range(iterations):
    pattern2 = mutateAttackPattern(pattern1)
    pattern2 = mutateAttackPattern(pattern1)
    points1 = experiment(pattern1, visual, player_controlled)
    points2 = experiment(pattern2, visual, player_controlled)
    print(points1,points2)
    if points2 > points1:
        pattern1 = pattern2
        print('better pattern found')
#Ease in with single mutation
for _ in range(iterations):
    pattern2 = mutateAttackPattern(pattern1)
    points1 = experiment(pattern1, visual, player_controlled)
    points2 = experiment(pattern2, visual, player_controlled)
    print(points1,points2)
    if points2 > points1:
        pattern1 = pattern2
        print('better pattern found')

print('Best attack pattern:')
print(pattern1)
pygame.quit()