import pygame, math, random, sys, sprite, bullet, time
import player as player_character
from colors import *

#Setup
pygame.init()
width = 900
height = 600
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

def userInputToPlayer(player):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.dy -= 1
    if keys[pygame.K_DOWN]:
        player.dy += 1
    if keys[pygame.K_LEFT]:
        player.dx -= 1
    if keys[pygame.K_RIGHT]:
        player.dx += 1

def getNewEnemy():
    return sprite.Sprite(screen, random.randint(0, screen.get_width()-20), 0,
                  30, random.randint(-5,5), 3, 'ellipse', green, 4, 'enemy')


def shootBullet(player):
    return bullet.Bullet(screen, player.x, player.y)


player = player_character.Player(screen, screen.get_width()/2, screen.get_height()-50)
all_sprites = []
all_sprites.append(player)
enemy_respawn_countdown = 0

#Measure the effects of dirty rects
sleep_time = 0
work_time = 0

#Main loop
done = False
while not done:
    start = time.time()
    #Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            elif event.key == pygame.K_SPACE:
                all_sprites.append(shootBullet(player))
            userInputToPlayer(player)
    #Spawn new enemies
    enemy_respawn_countdown -= 1
    if enemy_respawn_countdown < 0:
        all_sprites.append(getNewEnemy())
        enemy_respawn_countdown = 5
    #Move everything
    for s in all_sprites:
        s.move()
    #Check for collisions
    for i in range(len(all_sprites)-1):
        for j in range(i+1, len(all_sprites)):
            if all_sprites[i].collided(all_sprites[j]):
                #Damage them both
                all_sprites[i].hp -= 1
                all_sprites[j].hp -= 1
    #Remove dead or offscreen sprites
    for i in reversed(range(len(all_sprites)-1)):
        if all_sprites[i].isOffScreen() or all_sprites[i].hp <= 0:
            del all_sprites[i]
    #fill screen with black
    screen.fill(black)
    #Draw all sprites
    for s in all_sprites:
        s.draw()
    #Update the screen
    pygame.display.flip()
    #Measure work time
    work_time += time.time()-start
    #Delay to get 30 fps
    start = time.time()
    clock.tick(30)
    sleep_time += time.time()-start
pygame.quit()

total = work_time+sleep_time
print('Sleep time percent: '+str(int(100*sleep_time/total)))
print('Work time percent: '+str(int(100*work_time/total)))
