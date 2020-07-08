'''TODO next steps:
consider what is minimal to make a competitive game.
what if exp was gained for damaging opponents? This might make
offensive strategies more viable.

DONE 0. Add health regen as an attribute of enemy and player and have them gain
health up to max in their update functions.
DONE 1. Add bullet attribute to be leveled up.
DONE 2. Add sparkle animations
3. Diversify the powerups. Create: teleporter, spread shot,
big shot, speed boost, shove_impulse up, others?
4.
5. Level up attributes.

Next step is to display the levels on the screen.
And have arrays of levels in constants. Then experience can
be spent for the next level up. Grab numbers
from the java game.

I created arrays for the following in constants.py
Ready to level up in diep sprite:
    self.accel
    self.max_hp
    self.hp
    self.collision_damage
    self.refire_delay
    self.bullet_damage
    self.bullet_speed
    self.bullet_longevity
    self.bullet_hp
Ready to level up in enemy and player:
    self.hp_regen
6. Differentiated exp bricks.
7.
8.
9. Is there a way to implement cloaking?
Yes, for each NPC, get all objects within vision radius and only
pass those in. Cloaked ships are either not passed in or must be
closer to be seen.
Only draw the objects seen by camera/perspective ship.
Implement zoom in and zoom out.

3 lives.

Exp and upgrades.
Be able to upgrade/downgrade friction, recoil, vision radius.

I like the idea of giving students a list of all the food and a list of
all powerups and of all enemies and letting them do distance
calculations to determine what is nearest and what is a priority.

Charge up shot for extra damage and stamina bar for extra
speed both add another layer of strategy.

-diep ammo limitations and ammo pickups, stamina, burst speed, saveable powerups.
-choose ability set at start then write AI. All abilities come on cooldowns so it's less randomly dependent on landing near powerups?

Tactical item pickups that can be used later. Shove out can be used on
a rammer. Teleport can get you out of a tricky spot. Grenade can be
fired into a cluster of enemies.
Make one of the things you can level up storage for powerups.

Keep this initially separate then make a third project
integrating this with maze navigator or a sort of racing game.
'''

import pygame, diep_sprite, player, enemy, funcs, sparkle, powerup, random
from constants import *

pygame.init()

#Initialize variables:
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width,screen_height))
font = pygame.font.SysFont('Arial', 25)

critter = player.PlayerCritter(  screen,
                        500,#x
                        500,#y
                        blue,
                        50,#radius
                        player_acceleration,
                        critter_hp,#hp
                        "Neal")
funcs.insertInOrder(critter, all_sprites)
#Maintain a list of all critters exclusively.
#Initially this is mostly for the camera
all_critters = [critter]
leader_list = [critter]
camera_index = 0
critter_names = ['Bill', 'Ted', 'Socrates']

for i in range(enemy_count):
    npc_critter = enemy.EnemyCritter(screen,
                          200,#x
                          200,#y
                          yellow,
                          35,#radius
                          npc_acceleration,
                          critter_hp,#hp
                          critter_names[i])
    funcs.insertInOrder(npc_critter, all_sprites)
    all_critters.append(npc_critter)
    leader_list.append(npc_critter)

for i in range(food_count):
    f = diep_sprite.DiepSprite(screen,
                    0,0,
                    green, food_radius, 0,#acceleration
                    food_hp,#hp
                    draw_heading=False)
    f.teleport()
    funcs.insertInOrder(f, all_sprites)



#Delete dead sprites
def deleteDead():
    for i in reversed(range(len(all_sprites))):
        if all_sprites[i].hp <= 0:
            if all_sprites[i].sprite_type == TYPE_FOOD:
                #Reset the food
                all_sprites[i].reset()
            else:
                del all_sprites[i]
        elif all_sprites[i].sprite_type == TYPE_BULLET and all_sprites[i].timeout<0:
            del all_sprites[i]

def processInputs():
    global done
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            #print(event.key) #Print value of key press
            if event.key == 32:#space bar
                camera_index = (camera_index+1)%len(all_critters)
            elif event.key == pygame.K_ESCAPE:
                done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            critter.shoot()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        critter.dy -= critter.accel
    if keys[pygame.K_DOWN]:
        critter.dy += critter.accel
    if keys[pygame.K_LEFT]:
        critter.dx -= critter.accel
    if keys[pygame.K_RIGHT]:
        critter.dx += critter.accel

#Sorting pass of all_sprites
def sortSprites():
    for i in range(len(all_sprites)-1):
        if all_sprites[i].rect.left > all_sprites[i+1].rect.left:
            temp = all_sprites[i]
            all_sprites[i] = all_sprites[i+1]
            all_sprites[i+1] = temp

#Collision check between sprites
def checkCollisions():
    for i in range(len(all_sprites)-1):
        for j in range(i+1,len(all_sprites)):
            #For efficiency abort loop if nothing more is in range
            if all_sprites[i].rect.right < all_sprites[j].rect.left:
                break
            #check for collision
            if all_sprites[i].collidedWith(all_sprites[j]):
                all_sprites[i].shoveOut(all_sprites[j])
                all_sprites[j].shoveOut(all_sprites[i])
                #Prevent food on food damage
                if all_sprites[i].sprite_type != TYPE_FOOD or all_sprites[j].sprite_type != TYPE_FOOD:
                    #Check for NPC collision with powerup
                    if (all_sprites[i].sprite_type == TYPE_CRITTER and all_sprites[j].sprite_type == TYPE_POWERUP):
                        #TODO
                        all_sprites[i].invincibility_countdown = 360
                        all_sprites[j].teleport()
                        return
                    if (all_sprites[i].sprite_type == TYPE_POWERUP and all_sprites[j].sprite_type == TYPE_CRITTER):
                        #TODO
                        all_sprites[j].invincibility_countdown = 360
                        all_sprites[i].teleport()
                        return
                    #Deal damage
                    all_sprites[i].takeDamage(all_sprites[j].collision_damage)
                    all_sprites[j].takeDamage(all_sprites[i].collision_damage)
                    #If anyone died, give experience to the other.
                    if all_sprites[i].hp <= 0:
                        xp_receiver = all_sprites[j]
                        #bullet give xp to shooter
                        if xp_receiver.sprite_type == TYPE_BULLET:
                            xp_receiver = xp_receiver.shooter
                        xp_receiver.experience += all_sprites[i].getExperienceGiven()
                    if all_sprites[j].hp <= 0:
                        xp_receiver = all_sprites[i]
                        #bullet give xp to shooter
                        if xp_receiver.sprite_type == TYPE_BULLET:
                            xp_receiver = xp_receiver.shooter
                        xp_receiver.experience += all_sprites[j].getExperienceGiven()


def updateAndDraw():
    screen.fill((0,0,0)) #fill screen with black
    povx = all_critters[camera_index].x
    povy = all_critters[camera_index].y
    for a in all_sprites:
        if a.sprite_type == TYPE_CRITTER:
            visible_sprites = funcs.getSpritesInRange(all_sprites, a.vision_radius, a.x,a.y)
            a.update(visible_sprites)
            #Add sparkle on invincible critters
            if a.invincibility_countdown>0:
                randcolor = random.randint(0,255),random.randint(0,255),random.randint(0,255)
                temp = sparkle.Sparkle(screen, a.x+random.randint(-100,100),
                            a.y+random.randint(-100,100), randcolor)
                all_sprites.append(temp)
        else:
            a.update()
        a.draw(povx, povy, center_on_screen=(a==all_critters[camera_index]))

def displayLeaderboard():
    screen.blit(font.render('LEADERBOARD',True,white), (screen_width-140, 20))
    for i in range(len(leader_list)):
        screen.blit(font.render(leader_list[i].name+': '+str(int(leader_list[i].experience)),
            True,white), (screen_width-140, 45+i*25))

def sortLeaderboard():
    for i in range(len(leader_list)-1):
        if leader_list[i].experience < leader_list[i+1].experience:
            temp=leader_list[i]
            leader_list[i]=leader_list[i+1]
            leader_list[i+1]=temp


#Main program loop
done = False
testing=powerup.Powerup(screen, 500, 500, white)
all_sprites.append(testing)
while not done:
    processInputs()
    #Sorting pass of all_sprites. If we do one bubble sort per frame,
    #sprites ought to stay roughly sorted.
    sortSprites()
    #Collision check between sprites
    checkCollisions()
    #Delete dead sprites
    deleteDead()
    #Update and draw all sprites
    updateAndDraw()
    #Sort the leaderboard
    sortLeaderboard()
    #Display leaderboard
    displayLeaderboard()
    pygame.display.flip()
    #Delay to get 60 fps
    clock.tick(60)
pygame.quit()