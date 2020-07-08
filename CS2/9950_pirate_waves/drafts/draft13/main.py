'''
enemy boats that shoot back
    DONE create a new enemy_boat object that extends boat, has health, volley count,
        refire counter between volleys
    DONE verify that self damage is possible
    DONE make the enemy boat shoot the player
    DONE make enemy shoot in right direction
    DONE add some random spread to the enemy's volley's angle
    DONE when the enemy boat dies have it pop up in the air and then sink under the
        waves with a splash and explosions. Modify the enemy boat's draw and
        update functions to implement this death of the boat.
    DONE Consolidate duplicate code in boat and enemy_boat update functions into other functions
    DONE then see if you can delete math and functinos imports out of enemy_boat.py
    DONE have new enemy boats occassionally spawn and scroll onto the screen
    DONE Have enemies spawn at water height
    DONE Make it so player can't move off screen
    save a draft

Move player into the game manager

Consider making the rum replenish life.

Add in little islands with cannons to defeat. You might use a colored rect
beneath the tiles for when the waves are low.
Plant flag on the island when it is defeated.

Game over screen.

Implement splash in the water. Little white circles that pop up and drift along the top of waves before disappearing.

cannon balls splash in water

https://www.youtube.com/watch?v=SO7FFteErWs

'''
import boat, game_manager
from functions import *

pygame.init()

clock = pygame.time.Clock()
surface = pygame.display.set_mode((screen_width,screen_height))

gm = game_manager.GameManager()

player = boat.Boat('images/1stship_3.png',True,int(screen_width/3))

done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            print(event.key)
            if event.key == pygame.K_ESCAPE:
                done = True
            elif event.key == pygame.K_UP:
                player.jump()
            elif event.key == 32: #space bar
                #Shoot a cannonball
                gm.shoot(player, True)
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            shiftWaterHeight(pos, gm.water_heights)

    #Detect held down keys:
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        player.moveLeft()
    if pressed[pygame.K_RIGHT]:
        player.moveRight()

    player.update(gm.water_heights)

    gm.update(player)

    #Draw everything
    surface.fill(sky_blue)
    player.draw(surface)
    gm.draw(surface)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()