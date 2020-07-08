import pygame
from constants import default_speed, num_goal
from math import sqrt

#All keyboard and mouse input will be handled by the following function
def handleEvents(player):
    #Check for new events
    for event in pygame.event.get():
        #This if makes it so that clicking the X actually closes the game
        if event.type == pygame.QUIT:
            pygame.quit(); exit()
        #Has any key been pressed?
        elif event.type == pygame.KEYDOWN:
            #Escape key also closes the game.
            if event.key == pygame.K_ESCAPE:
                pygame.quit(); exit()
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        player.moveLeft(default_speed)
    if pressed[pygame.K_UP]:
        player.moveUp(default_speed)
    if pressed[pygame.K_RIGHT]:
        player.moveRight(default_speed)
    if pressed[pygame.K_DOWN]:
        player.moveDown(default_speed)

def checkCollisions(player, deadly_rects, goal_rects):
    for d in deadly_rects:
        if player.collides(d):
            print('GAME OVER')
            pygame.quit(); exit()
    for i in reversed(range(len(goal_rects))):
        if player.collides(goal_rects[i]):
            del goal_rects[i]
            player.points = player.points + 1
            if player.points >= num_goal:
                print('VICTORY')

def distance(x1,y1,x2,y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)


