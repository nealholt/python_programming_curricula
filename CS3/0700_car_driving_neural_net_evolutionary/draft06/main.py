import pygame, player, line_segment

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
        player.moveBackward()
    if keys[pygame.K_LEFT]:
        player.rotateLeft()
    if keys[pygame.K_RIGHT]:
        player.rotateRight()
    if keys[pygame.K_a]:
        player.speed += 0.05
    if keys[pygame.K_d]:
        player.speed -= 0.05


def handleEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return True
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(pos,',') #TODO
    return False

def drawAndDelay(player, race_track):
    #fill screen with black
    screen.fill(black)
    #Draw player
    player.draw()
    for seg in race_track:
        seg.draw()
    #Update the screen
    pygame.display.flip()
    #Delay to get 30 fps
    clock.tick(30)


#Create the player
player = player.Player(screen, 100, 200)

race_track_inner = [
(103, 283) ,
(208, 125) ,
(285, 157) ,
(227, 305) ,
(339, 372) ,
(513, 400) ,
(657, 256) ,
(746, 145) ,
(801, 292) ,
(699, 363) ,
(728, 488) ,
(563, 472) ,
(474, 433) ,
(260, 398) ,
(147, 418)]
race_track_outer = [(21, 237) ,
(202, 35) ,
(396, 85) ,
(366, 206) ,
(319, 280) ,
(404, 332) ,
(473, 344) ,
(582, 212) ,
(685, 80) ,
(748, 46) ,
(863, 143) ,
(867, 337) ,
(791, 394) ,
(848, 512) ,
(696, 577) ,
(481, 566) ,
(449, 478) ,
(330, 468) ,
(202, 545) ,
(47, 438) ,
(12, 276)]
race_track = []
white = 255,255,255
for i in range(len(race_track_inner)-1):
    seg = line_segment.LineSeg(screen, white,
                race_track_inner[i][0],
                race_track_inner[i][1],
                race_track_inner[i+1][0],
                race_track_inner[i+1][1])
    race_track.append(seg)
seg = line_segment.LineSeg(screen, white,
            race_track_inner[-1][0],
            race_track_inner[-1][1],
            race_track_inner[0][0],
            race_track_inner[0][1])
race_track.append(seg)

for i in range(len(race_track_outer)-1):
    seg = line_segment.LineSeg(screen, white,
                race_track_outer[i][0],
                race_track_outer[i][1],
                race_track_outer[i+1][0],
                race_track_outer[i+1][1])
    race_track.append(seg)
seg = line_segment.LineSeg(screen, white,
            race_track_outer[-1][0],
            race_track_outer[-1][1],
            race_track_outer[0][0],
            race_track_outer[0][1])
race_track.append(seg)

#Main loop
done = False
while not done:
    #Handle any events, possibly closing the game.
    done = handleEvents()
    #Send user input to the player
    userInputToPlayer(player)
    player.resetVision()
    player.senseTrack(race_track)
    print()
    #print(player.getSensorLengths())
    print(player.getSensorPercents())
    #Draw on the screen
    drawAndDelay(player, race_track)

pygame.quit()