'''
Implement collectibles that scroll past that you have to jump to get.
    load the collectible image in game_manager
    create a list of pickups in game manager.
        This will be a list of positions used for both drawing and collision
        with the ship
    spawn them, draw them and have them scroll past
    make them collide with the ship

It might be more fun to adjust the controls. Move left and right in the air.
Don't make the left and right tilt the boat.
Make depth have a sqrt effect on bouyancy.
Stronger jump.
Stronger gravity?

Display points

Make a cannon that the boat can shoot.

Add in little islands with cannons to defeat. You might use a colored rect
beneath the tiles for when the waves are low.

Implement splash in the water. Little white circles that pop up and drift along the top of waves before disappearing.

https://www.youtube.com/watch?v=SO7FFteErWs

'''
import boat, game_manager
from functions import *

pygame.init()

clock = pygame.time.Clock()
surface = pygame.display.set_mode((screen_width,screen_height))

gm = game_manager.GameManager()

player = boat.Boat()

done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            print(event.key)
            if event.key == pygame.K_ESCAPE:
                done = True
            if event.key == 32: #space bar
                player.jump()
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            shiftWaterHeight(pos, gm.water_heights)

    #Can only move left or right when part of the boat is in the water
    if player.front_under_water or player.rear_under_water:
        #Detect held down keys:
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            player.moveLeft()
        if pressed[pygame.K_RIGHT]:
            player.moveRight()

    player.update(gm.water_heights)

    gm.updateWater()
    gm.updatePickups()
    gm.checkCollisions(player)

    #Draw everything
    surface.fill(black)
    player.draw(surface)
    gm.draw(surface)
    pygame.display.flip()
    clock.tick(30)
pygame.quit()