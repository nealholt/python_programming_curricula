import pygame, game_manager
from constants import *

#Setup
pygame.init()
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
large_font = pygame.font.SysFont('Arial', 48)
small_font = pygame.font.SysFont('Arial', 24)


def userInputToPlayer(player):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.thrust()
    if keys[pygame.K_LEFT]:
        player.rotateLeft()
    if keys[pygame.K_RIGHT]:
        player.rotateRight()



#Create game manager object to manage updating and moving everything
gm = game_manager.GameManager(screen, 0) #Start on level 0


#Main loop
done = False
while not done:
    #Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            #Press enter to reset game after death
            if event.key == pygame.K_RETURN and (gm.player.lives <= 0 or gm.victory):
                gm = game_manager.GameManager(screen, 0) #Reset to level 0
    #Send user input to the player if it's alive
    if gm.player.lives > 0:
        userInputToPlayer(gm.player)
    #fill screen with black
    screen.fill(black)
    #Display level
    position = (width-150, 10)
    screen.blit(small_font.render("Level "+str(gm.level),True,white),position)
    #Check for game over
    if gm.victory:
        rating = str(gm.ground.rateTheLanding(gm.player))
        position = (width/2-100, height/2-20)
        screen.blit(large_font.render("CONGRATULATIONS",True,white),position)
        position = (width/2-75, height/2+40)
        screen.blit(small_font.render("[ENTER] to reset",True,white),position)
        position = (width/2-75, height/2+80)
        screen.blit(small_font.render("Landing Rating (low is best): "+rating,True,white),position)
    elif gm.player.lives <= 0:
        position = (width/2-100, height/2-20)
        screen.blit(large_font.render("Game Over",True,white),position)
        position = (width/2-75, height/2+40)
        screen.blit(small_font.render("[ENTER] to reset",True,white),position)
    else:
        gm.update()
    #Update the screen
    pygame.display.flip()
    pygame.display.update()
    #Delay to get 30 fps
    clock.tick(30)
pygame.quit()