'''
0
1 organize in a minimal way for students to have one file where they write
code like the maze runner is arranged. Plan first couple investigations.
2
3
4
5 Depth and breadth first search taught to CS2. Then they use it in robo rally.
Lead them to it through little investigations. Stacks and queues and
then robo rally can carry you through the end of the year.
6
7 boost moves? other special moves
8 could do a no-rules game where some clever player will
figure out to relocate the flags to themself. Get it
out of their system then do a rules version.
9 add in repair station (single wrench image) that does not act as a checkpoint
'''
import math, random, robot, flag, robot_wait, robot_random, robot_ai1, robot_ai2, robot_ai3, robot_greedy, robot_BFS, robot_smart_random, robot_easier, robot_student
from functions import *

fps = 5 #Frames per second
#Control how many times player blinks
blink_count = 2 #This must be even

level_number = 2
#If True then robots will move automatically
#as fast as the fps allows. If False, then spacebar
#can be pressed to advance the game.
play_continuous = True

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

#player1 = robot_wait.Waitbot(surface, white, 'Waiter')
#player1 = robot_BFS.BFSbot(surface, white, 'BFS')
#player1 = robot_greedy.Greedybot(surface, black, 'Greedy')
#player1 = robot_ai3.AI3(surface, blue, 'SimpleBoi')
#player1 = robot_easier.EasierTestBot(surface, blue, 'Easy')
player1 = robot_easier.robot_student.StudentBot(surface, blue, 'Student')
player_list = [player1]

'''#player1 = robot_wait.Waitbot(surface, white, 'Waiter')
player2 = robot_ai1.AI1(surface, yellow, 'SmartBoi')
#player3 = robot_ai2.AI2(surface, blue, 'SimpleBoi')
player3 = robot_ai3.AI3(surface, blue, 'SimpleBoi')
#player4 = robot_random.RandomBot(surface, red, 'Rando') #Random bot
player4 = robot_smart_random.SmartRandomBot(surface, red, 'Rando') #Random bot
player5 = robot_greedy.Greedybot(surface, black, 'Greedy')
player_list = [player1, player2, player3, player4, player5]
'''
for i in range(len(player_list)):
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
            #Check for and remove dead robots
            for i in reversed(range(len(player_list))):
                if player_list[i].hp <= 0:
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
                drawAll(surface, images, player_list, flags, clock, fps)
            #Perform action
            #print('player '+player.name+' performing action '+action)
            #print('at '+str(player.row)+','+str(player.col))
            player.doAction(board, player_list, flags, action)
            #print('action done')

    drawAll(surface, images, player_list, flags, clock, fps)

#Print winners and points scored
print('Winners in order from first to last:')
print(winners)
print('Others:')
for i in range(len(player_list)):
    print(player_list[i].name+' scored '+str(len(player_list[i].flags))+' points.')
pygame.quit()