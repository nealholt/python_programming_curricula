'''
1 Write a breadth first search AI just to show that you can
2
3
4
5 organized in a minimal way for students to have one file where they write
code like the maze runner is arranged.
6 Depth and breadth first search taught to CS2. Then they use it in robo rally.
Lead them to it through little investigations. Stacks and queues and
then robo rally can carry you through the end of the year.
7
8
9 Guantlet of levels with limited moves per level and a score at the end.
10 boost moves? other special moves
11 could do a no-rules game where some clever player will
figure out to relocate the flags to themself. Get it
out of their system then do a rules version.
12 add in repair station (single wrench image) that does not act as a checkpoint

Use robo rally after flappy bird for CS1 but for them it's an exercise in the
use of and and or, also possibly sub goals like getting to a particular
location. Also maybe one new map released every other day. Also writing
some functions together (including functions you have already created.
Organize which ones though.
I like the idea of little investigations being fill in the blank code for
students to write things like get flags I need and also get nearest flag
or get nearest repair station. Or even plot a course to location.
You could have students write the random choice bot and then help them make it
gradually smarter with ifs and functions.
'''
import math, random, robot, flag, robot_wait, robot_ai1, robot_ai2
from functions import *

fps = 30 #Frames per second
#Control how many times player blinks
blink_count = 6 #This must be even

level_number = 0
#If True then robots will move automatically
#as fast as the fps allows. If False, then spacebar
#can be pressed to advance the game.
play_continuous = False

#Maximum number of rounds before the game is ended
round_limit = 100
round_count = 0

flag_locations, map_choice, player_locations = createLevel(level_number)

#images is a 2d array of images
#board is a 2d array of the names of tiles
images,board = constructMap(map_choice)

board_width = len(board[0])
board_height = len(board)
map_width = int(board_width*tile_width)
map_height = int(board_height*tile_height)

surface = pygame.display.set_mode((map_width, map_height))

player1 = robot_wait.Waitbot(surface, white, 'Waiter')
player2 = robot_ai1.AI1(surface, yellow, 'SmartBoi')
player3 = robot_ai2.AI2(surface, blue, 'SimpleBoi')
player4 = robot.Robot(surface, red, 'Rando2') #Random bot
player_list = [player1, player2, player3, player4]
for i in range(4):
    player_list[i].setStart(player_locations[i][0],player_locations[i][1])

flags = []
colors = [red, yellow, blue, green]
for i in range(4):
    flags.append(flag.Flag(surface, flag_locations[i][0], flag_locations[i][1], colors[i]))

#Use this list for ordering actions
action_list = []

#List of winners
winners = []

# Draw all images on the surface
done = False
while not done and len(player_list)>0 and round_count<round_limit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            elif event.key == 32: #space bar
                step_forward = True
            elif event.key == pygame.K_RIGHT:
                player_list[0].rotateRight()
            elif event.key == pygame.K_LEFT:
                player_list[0].rotateLeft()
            elif event.key == pygame.K_UP:
                player_list[0].move(board, player_list, flags)
    if step_forward or play_continuous:
        step_forward = False
        #Reset the action list for the next round
        if len(action_list) == 0:
            round_count += 1
            #Perform board actions such as conveying before
            #next player move
            boardActions(board, player_list, flags)
            #Check for and remove winning players
            for i in reversed(range(len(player_list))):
                if len(player_list[i].flags) == 4:
                    winners.append(player_list[i].name)
                    del player_list[i]
            #All players decide what they want to do
            for p in player_list:
                p.laser_end = None #Reset laser
                action_list.append([p,p.chooseAction(board, player_list, flags)])
                #Update action text
                p.text = font.render(p.next_action,True,yellow)
            #Randomize ordering of actions
            random.shuffle(action_list)
        else:
            #Take the next action
            player, action = action_list.pop()
            #blink to indicate actor
            for i in range(blink_count):
                player.blink = not player.blink
                drawAll(surface, images, player_list, flags, clock)
            #Perform action
            player.doAction(board, player_list, flags, action)

    drawAll(surface, images, player_list, flags, clock)

#Print winners and points scored
print('Winners in order from first to last:')
print(winners)
print('Others:')
for i in range(len(player_list)):
    print(player_list[i].name+' scored '+str(len(player_list[i].flags))+' points.')
pygame.quit()