'''
It might be more fun to adjust the controls.
DONE Ability to move left and right in the air.
DONE Don't make the left and right tilt the boat.
DONE Make depth have a sqrt effect on bouyancy.
DONE Stronger jump.
DONE Stronger gravity?

DONE splash when the boat lands.
DONE knives spawn that are to be avoided.

DONE Make a cannon that the boat can shoot.

DONE flash of fire and drifting puff of smoke when the cannon fires.

Save a draft before moving on

Go to 60 frames per second

enemy boats that shoot back

Display points and health bar. rum gains points. knives damage health

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

    gm.updateWater()
    gm.updatePickups()
    gm.updateCannonBalls()
    gm.checkCollisions(player)

    #Draw everything
    surface.fill(sky_blue)
    player.draw(surface)
    gm.draw(surface)
    pygame.display.flip()
    clock.tick(30)
pygame.quit()