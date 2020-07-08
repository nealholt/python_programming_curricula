'''
Save a draft before doing the string thing.

-2 Use only string directions like north and south, not numbers for readability

-1 see TODO An AI that CS1 could write. Something a little simpler
though I like the idea of little investigations being fill in the blank code for
students to write things like get flags I need and also get nearest flag
or get nearest repair station. Or even plot a course to location.

0 Write a depth first and breadth first search AI just to show that you can

1 split this up into many different files for organization

2 lazers? repairs? health bars? I love this idea.
Falling in a hole cuts your health in half and sends
you back to check point. Laser blast reduces your health
a little. Finishing a turn at a checkpoint or repair
station increases your health by twice as much as a
laser blast hurts it.

3 repair station that does not act as a checkpoint

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

Use robo rally after flappy bird for CS1 but for them it's an exercise in the
use of and and or, also possibly sub goals like getting to a particular
location. Also maybe one new map released every other day. Also writing
some functions together (including functions you have already created.
Organize which ones though.
'''
import pygame, math, random

fps = 30 #Frames per second
#Control how many times player blinks
blink_count = 6 #This must be even

level_number = 2
#If True then robots will move automatically
#as fast as the fps allows. If False, then spacebar
#can be pressed to advance the game.
play_continuous = True

#Maximum number of rounds before the game is ended
round_limit = 100
round_count = 0

def createLevel(level_num):
    if level_num == -1:
        flags = [(2, 3),(5, 5),(6, 1),(6, 3)]
        player_starts = [(0,0),(1,0),(2,0),(3,0)]
        return flags, 'maps/map00.txt', player_starts
    elif level_num == 0:
        flags = [(2, 3),(5, 5),(6, 1),(6, 3)]
        player_starts = [(0,0),(5,5),(5,6),(5,7)]
        return flags, 'maps/map01.txt', player_starts
    elif level_num == 1:
        flags = [(1, 1),(1, 6),(6, 1),(6, 6)]
        player_starts = [(1,0),(2,0),(3,0),(4,0)]
        return flags, 'maps/level050.txt', player_starts
    elif level_num == 2:
        flags = [(1, 3),(8, 3),(1, 13),(8, 13)]
        player_starts = [(1,0),(2,0),(3,0),(4,0)]
        return flags, 'maps/level300.txt', player_starts

pygame.init()
initial_width = 144
initial_height = 144

scaling = 0.5

font = pygame.font.SysFont('Arial', int(48*scaling))

tile_width = int(initial_width*scaling)
tile_height = int(initial_height*scaling)

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
yellow = (255,255,0)
green = (0,255,0)
blue = (0,0,255)

direction_list = ['north', 'east', 'south', 'west']

#If the index of the conveyor in this list matches up
#to the index of the direction in direction_list
#then we can use index to force move players on conveyors
conveyors = ['cv1u', 'cv1r', 'cv1d', 'cv1l']
left_turn_conveyors = ['cvlu', 'cvlr', 'cvld', 'cvll', ]
right_turn_conveyors = ['cvru', 'cvrr', 'cvrd', 'cvrl', ]

step_forward = False

def getRowColChange(direction):
    temp_row = 0
    temp_col = 0
    if direction == 0: #north
        temp_row -= 1
    elif direction == 1: #east
        temp_col += 1
    elif direction == 2: #south
        temp_row += 1
    elif direction == 3: #west
        temp_col -= 1
    return temp_row,temp_col

def isConveyor(board, row, col):
    #Returns True if requested tile is a conveyor
    tile = board[row][col]
    return tile in conveyors or tile in left_turn_conveyors or tile in right_turn_conveyors

def conveysTo(board, row, col):
    '''Returns a triple of row change, col change, and
    rotation, indicating how the requested tile would
    move a robot. All non-conveyor tiles return 0,0,0.'''
    if not isConveyor(board,row,col):
        return 0,0,0
    elif board[row][col] in conveyors:
        direction = conveyors.index(board[p.row][p.col])
        row_change,col_change = getRowColChange(self.direction)
        return row_change,col_change,0
    elif board[row][col] in left_turn_conveyors:
        direction = left_turn_conveyors.index(board[p.row][p.col])
        row_change,col_change = getRowColChange(self.direction)
        return row_change,col_change,-1 #left rotation
    elif board[row][col] in right_turn_conveyors:
        direction = right_turn_conveyors.index(board[p.row][p.col])
        row_change,col_change = getRowColChange(self.direction)
        return row_change,col_change,1 #right rotation

def getPlayerAt(players, row, col):
    '''Returns player at given location or returns None.'''
    for p in players:
        if p.row == row and p.col == col:
            return p
    return None

def outOfBounds(board,row,col):
    return row<0 or col<0 or row>=len(board) or col>=len(board[0])

def canMove(board, players, row, col, direction):
    #Robots can always move out of bounds
    if outOfBounds(board, row, col):
        return True
    #Check indicated direction
    if direction == 0: #north
        #Make sure there is no wall to the north
        if board[row][col] != '1wu ' and board[row][col] != '2wur' and board[row][col] != '2wlu':
            #If there is a player to the north...
            if getPlayerAt(players, row-1, col) != None:
                #...then recursively check that it can be moved north
                return canMove(board, players, row-1, col, direction)
            else:
                return True
    elif direction == 1: #east
        #Make sure there is no wall to the east
        if board[row][col] != '1wr ' and board[row][col] != '2wur' and board[row][col] != '2wrd':
            #If there is a player to the east...
            if getPlayerAt(players, row, col+1) != None:
                #...then recursively check that it can be moved east
                return canMove(board, players, row, col+1, direction)
            else:
                return True
    elif direction == 2: #south
        #Make sure there is no wall to the south
        if board[row][col] != '1wd ' and board[row][col] != '2wrd' and board[row][col] != '2wdl':
            #If there is a player to the south...
            if getPlayerAt(players, row+1, col) != None:
                #...then recursively check that it can be moved south
                return canMove(board, players, row+1, col, direction)
            else:
                return True
    elif direction == 3: #west
        #Make sure there is no wall to the west
        if board[row][col] != '1wl ' and board[row][col] != '2wdl' and board[row][col] != '2wlu':
            #If there is a player to the west...
            if getPlayerAt(players, row, col-1) != None:
                #...then recursively check that it can be moved west
                return canMove(board, players, row, col-1, direction)
            else:
                return True
    else:
        print('ERROR This should be impossible.')
        exit()
    return False

class Robot:
    def __init__(self, screen, color, name):
        self.screen = screen
        self.name = name
        self.row = 0
        self.col = 0
        self.color = color
        self.sides = 3
        self.radius = 40*scaling
        self.direction = 1
        self.checkpoint = (0,0)
        self.next_action = ''
        self.text = font.render('', True,yellow)
        self.blink = False
        self.flags = []
    def setStart(self, row, col):
        self.row = row
        self.col = col
        self.checkpoint = (row,col)
    def flagsINeed(self, flags):
        #Returns a list of flags that this robot still needs
        to_return = []
        for f in flags:
            if not(f.color in self.flags):
                to_return.append(f)
        return to_return
    def turnTowardDirection(self, direction):
        '''Pre: direction is a string, not an int.
        This function has a bias toward turning left.
        This function will request a turn even if the
        bot is currently facing the desired direction.
        Post: returns a string, left or right,
        representing quickest rotation to turn to face
        direction.'''
        current_direction = self.getHeading()
        if direction == 'north':
            if current_direction == 'west':
                return 'right'
            else:
                return 'left'
        elif direction == 'south':
            if current_direction == 'east':
                return 'right'
            else:
                return 'left'
        elif direction == 'east':
            if current_direction == 'north':
                return 'right'
            else:
                return 'left'
        else: #elif direction == 'west':
            if current_direction == 'south':
                return 'right'
            else:
                return 'left'
    def doAction(self, board, players, flags, action):
        if action == 'left':
            self.rotateLeft()
        elif action == 'right':
            self.rotateRight()
        elif action == 'move':
            self.move(board, players, flags)
        self.next_action = ''
        self.text = font.render('', True,yellow)
    def getHeading(self):
        return direction_list[self.direction]
    def isNorth(self, row):
        return row<self.row
    def isSouth(self, row):
        return row>self.row
    def isEast(self, col):
        return col>self.col
    def isWest(self, col):
        return col<self.col
    def chooseAction(self, board, players, flags):
        #Choose an action randomly
        r = random.randint(0,3)
        if r == 0:
            self.next_action = 'left'
        elif r == 1:
            self.next_action = 'right'
        elif r == 2:
            self.next_action = 'move'
        else:
            self.next_action = 'wait'
        self.text = font.render(self.next_action, True,yellow)
        return self.next_action
    def rotateLeft(self):
        self.direction -= 1
        if self.direction < 0:
            self.direction = len(direction_list)-1
    def rotateRight(self):
        self.direction = (self.direction+1)%len(direction_list)
    def forceMove(self, players, direction, flags):
        row_change,col_change = getRowColChange(direction)
        temp_row = self.row + row_change
        temp_col = self.col + col_change
        #Check for another player that got shoved and
        #pass the shove down the line.
        p = getPlayerAt(players, temp_row, temp_col)
        if p != None:
            p.forceMove(players, direction, flags)
        #Complete the move
        self.row = temp_row
        self.col = temp_col
        self.eventAtLocation(board, flags)
    def move(self, board, players, flags):
        if canMove(board, players, self.row, self.col, self.direction):
            row_change,col_change = getRowColChange(self.direction)
            temp_row = self.row + row_change
            temp_col = self.col + col_change
            #If someone else is in this space, shove them.
            p = getPlayerAt(players, temp_row, temp_col)
            if p != None:
                p.forceMove(players, self.direction, flags)
            #Complete the move
            self.row = temp_row
            self.col = temp_col
            self.eventAtLocation(board, flags)
    def eventAtLocation(self, board, flags):
        '''Check for and activate any event at current location'''
        #Check for off the board and reset to a checkpoint
        if outOfBounds(board,self.row,self.col):
            self.row, self.col = self.checkpoint
        #Check for falling in a hole
        elif board[self.row][self.col] == 'hole':
            #print('Fell in a hole. Reset to last checkpoint')
            self.row, self.col = self.checkpoint
        #Update our checkpoint if we landed on a checkpoint
        elif board[self.row][self.col] == 'chek':
            self.checkpoint = (self.row, self.col)
        #Check for getting a flag
        for f in flags:
            if f.row==self.row and f.col==self.col and not(f.color in self.flags):
                self.flags.append(f.color)
    def getCenter(self):
        offset_x = self.col*tile_width + tile_width/2
        offset_y = self.row*tile_height + tile_height/2
        return offset_x, offset_y
    def getCorners(self):
        #Returns list of points to draw the robot
        points = []
        offset_x, offset_y = self.getCenter()
        heading = 0
        if self.direction == 0:
            heading = -math.pi/2
        elif self.direction == 2:
            heading = math.pi/2
        elif self.direction == 3:
            heading = math.pi
        #Nose
        angle = heading+math.pi*2
        x = offset_x + math.cos(angle)*self.radius*1.5
        y = offset_y + math.sin(angle)*self.radius*1.5
        points.append([x, y])
        #wing 1
        angle = heading+math.pi*2*(1.2/self.sides)
        x = offset_x + math.cos(angle)*self.radius
        y = offset_y + math.sin(angle)*self.radius
        points.append([x, y])
        #rear
        angle = heading+math.pi
        x = offset_x + math.cos(angle)*self.radius*0.5
        y = offset_y + math.sin(angle)*self.radius*0.5
        points.append([x, y])
        #wing 2
        angle = heading+math.pi*2*(1.8/self.sides)
        x = offset_x + math.cos(angle)*self.radius
        y = offset_y + math.sin(angle)*self.radius
        points.append([x, y])
        return points
    def draw(self):
        #Draw all flags you are carrying
        i = -1.5
        for f in self.flags:
            temp = Flag(self.screen, self.row, self.col, f)
            temp.drawSmall(int(0.25*i*tile_width), 0.5)
            i = i+1
        #Blink
        c = self.color
        if self.blink:
            c = black
        #Draw outline of ship.
        points = self.getCorners()
        pygame.draw.polygon(self.screen, c,
                            points,int(scaling*8))
        #Draw current action
        offset_x, offset_y = self.getCenter()
        self.screen.blit(self.text, (offset_x, offset_y))


class Flag:
    def __init__(self, screen, row, col, color):
        self.screen = screen
        self.row = row
        self.col = col
        self.color = color
        self.radius = 40*scaling
    def getCenter(self):
        offset_x = self.col*tile_width + tile_width/2
        offset_y = self.row*tile_height + tile_height/2
        return offset_x, offset_y
    def getCorners(self, x_adjust=0, shrink=1):
        #Returns list of points to draw the flag
        points = []
        offset_x, offset_y = self.getCenter()
        #top
        x = offset_x + x_adjust
        y = offset_y - self.radius*1.3*shrink
        points.append([int(x), int(y)])
        #tri corner flag
        x = offset_x -0.8*self.radius*shrink + x_adjust
        y = offset_y - self.radius*shrink
        points.append([int(x), int(y)])
        x = offset_x + x_adjust
        y = offset_y - 0.7*self.radius*shrink
        points.append([int(x), int(y)])
        x = offset_x + x_adjust
        y = offset_y - self.radius*1.3*shrink
        points.append([int(x), int(y)])
        #base
        x = offset_x + x_adjust
        y = offset_y + self.radius*0.8*shrink
        points.append([int(x), int(y)])
        return points
    def draw(self):
        points = self.getCorners()
        pygame.draw.polygon(self.screen, self.color,
                            points,int(scaling*8))
        pygame.draw.circle(self.screen, self.color,
                        points[-1], int(scaling*12))
    def drawSmall(self, adjust, scale):
        points = self.getCorners(x_adjust=adjust, shrink=scale)
        pygame.draw.polygon(self.screen, self.color,
                            points,int(scaling*8))
        pygame.draw.circle(self.screen, self.color,
                        points[-1], int(scaling*12))


class Sprite:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

def constructMap(filename):
    # Dictionary mapping tileset abbreviations to file names
    image_dict = {'empt': 'tile-clear.png',
                  'hole': 'tile-hole.png',
                  '1wl ': 'tile-wall-1a.png',
                  '1wu ': 'tile-wall-1b.png',
                  '1wr ': 'tile-wall-1c.png',
                  '1wd ': 'tile-wall-1d.png',
                  'chek': 'tile-hammer-wrench.png',
                  'cv1d': 'tile-conveyor-1a.png',
                  'cv1l': 'tile-conveyor-1b.png',
                  'cv1u': 'tile-conveyor-1c.png',
                  'cv1r': 'tile-conveyor-1d.png',

                  'cvlr': 'tile-conveyor-1-turnleft_a.png',
                  'cvld': 'tile-conveyor-1-turnleft_b.png',
                  'cvll': 'tile-conveyor-1-turnleft_c.png',
                  'cvlu': 'tile-conveyor-1-turnleft_d.png',
                  'cvrr': 'tile-conveyor-1-turnright_a.png',
                  'cvrd': 'tile-conveyor-1-turnright_b.png',
                  'cvrl': 'tile-conveyor-1-turnright_c.png',
                  'cvru': 'tile-conveyor-1-turnright_d.png',

                  '2wur': 'tile-wall-2a.png',
                  '2wrd': 'tile-wall-2b.png',
                  '2wdl': 'tile-wall-2c.png',
                  '2wlu': 'tile-wall-2d.png'
                  }
    # Open file to read in text representation of the map
    file_handle = open(filename, 'r')
    line = file_handle.readline()
    line = line.strip()
    images = []  # 2d array of sprites
    board = []   # 2d array of tile names
    while line:
        array = line.split(',')
        row_array_img = []
        row_array_name = []
        for i in range(len(array)):
            img = pygame.image.load('tiles/'+image_dict[array[i]])
            # Scale image
            img = pygame.transform.scale(img, (tile_width, tile_height))
            row_array_img.append(Sprite(i*tile_width, len(images)*tile_width, img))
            row_array_name.append(array[i])
        images.append(row_array_img)
        board.append(row_array_name)
        line = file_handle.readline()
        line = line.strip()
    return images,board



def drawAll(surface, players, flags):
    surface.fill(black)
    for row in images:
        for col in row:
            col.draw(surface)
    for p in players:
        p.draw()
    for f in flags:
        f.draw()
    pygame.display.flip()
    # Delay to get desired fps
    clock.tick(fps)


def boardActions(board, players, flags):
    #Convey any players on conveyors
    for p in players:
        if board[p.row][p.col] in conveyors:
            direction = conveyors.index(board[p.row][p.col])
            p.forceMove(players, direction, flags)
        elif board[p.row][p.col] in left_turn_conveyors:
            direction = left_turn_conveyors.index(board[p.row][p.col])
            p.forceMove(players, direction, flags)
            p.rotateLeft()
        elif board[p.row][p.col] in right_turn_conveyors:
            direction = right_turn_conveyors.index(board[p.row][p.col])
            p.forceMove(players, direction, flags)
            p.rotateRight()



class Waitbot(Robot): #It just waits
    def __init__(self, screen, color,name):
        super().__init__(screen, color,name)
    def chooseAction(self, board, players, flags):
        #Override parent class which chooses action randomly
        self.next_action = 'wait'
        self.text = font.render(self.next_action, True,yellow)
        return self.next_action


class AI1(Robot):
    def __init__(self, screen, color,name):
        super().__init__(screen, color,name)
        #Used for oscillating between moving forward and turning
        self.oscillate = True
    def chooseAction(self, board, players, flags):
        '''
        Useful functions:
        getPlayerAt(players, row, col)
        outOfBounds(board,row,col)
        canMove(board, players, row, col, direction)
        isConveyor(board, row, col)

        self.flagsINeed(flags)
            -Returns a list of flags that this robot still needs

        conveysTo(board, row, col)
            -Returns a triple of row change, col change, and
    rotation, indicating how the requested tile would
    move a robot. All non-conveyor tiles return 0,0,0.

        self.turnTowardDirection(direction)
            -Pre: direction is a string, not an int.
        This function has a bias toward turning left.
        This function will request a turn even if the
        bot is currently facing the desired direction.
            Post: returns a string, left or right,
        representing quickest rotation to turn to face
        direction.

        self.getHeading()
        self.isNorth(col)
        self.isSouth(col)
        self.isEast(row)
        self.isWest(row)

        Board key:
        board[row][col] == 'chek' #Checkpoint
        board[row][col] == 'empt' #empty square. safe
        board[row][col] == 'hole' #Hole. Don't fall in
        '''
        #Override parent class which chooses action randomly
        #Oscillate between rotating toward goal direction
        #and moving.
        self.oscillate = not self.oscillate
        if self.oscillate:
            self.next_action = 'move'
        else:
            #Choose a flag I don't have
            flags_i_need = self.flagsINeed(flags)
            flag_row = flags_i_need[0].row
            flag_col = flags_i_need[0].col
            #Choose a direction, that is not blocked or a hole,
            #that will get me closer to the flag. If multiple
            #directions will work then choose one randomly.
            good_directions = []
            if self.isNorth(flag_row):
                good_directions.append('north')
            if self.isSouth(flag_row):
                good_directions.append('south')
            if self.isEast(flag_col):
                good_directions.append('east')
            if self.isWest(flag_col):
                good_directions.append('west')
            #Randomly choose a good direction
            direction = 'north'
            if len(good_directions)!=0:
                direction = random.choice(good_directions)
            '''print()
            print('goal flag: '+str(flag))
            print('flag loc '+str(flag_row)+','+str(flag_col))
            print('my loc '+str(self.row)+','+str(self.col))
            print('Options: '+str(good_directions))
            print('Choice: '+direction)'''
            if direction == self.getHeading():
                self.next_action = 'move'
            else:
                self.next_action = self.turnTowardDirection(direction)
        #Update text for next direction
        self.text = font.render(self.next_action, True,yellow)
        return self.next_action

class AI2(Robot):
    def __init__(self, screen, color,name):
        super().__init__(screen, color,name)
    def chooseAction(self, board, players, flags):
        '''
        Useful functions:
        getPlayerAt(players, row, col)
        outOfBounds(board,row,col)
        canMove(board, players, row, col, direction)
        isConveyor(board, row, col)

        self.flagsINeed(flags)
            -Returns a list of flags that this robot still needs

        conveysTo(board, row, col)
            -Returns a triple of row change, col change, and
    rotation, indicating how the requested tile would
    move a robot. All non-conveyor tiles return 0,0,0.

        self.turnTowardDirection(direction)
            -Pre: direction is a string, not an int.
        This function has a bias toward turning left.
        This function will request a turn even if the
        bot is currently facing the desired direction.
            Post: returns a string, left or right,
        representing quickest rotation to turn to face
        direction.

        self.getHeading()
        self.isNorth(col)
        self.isSouth(col)
        self.isEast(row)
        self.isWest(row)

        Board key:
        board[row][col] == 'chek' #Checkpoint
        board[row][col] == 'empt' #empty square. safe
        board[row][col] == 'hole' #Hole. Don't fall in
        '''
        #Override parent class which chooses action randomly.

        #TODO slightly simpler than AI1, I hope

        #Choose a flag I don't have
        flags_i_need = self.flagsINeed(flags)
        flag_row = flags_i_need[0].row
        flag_col = flags_i_need[0].col
        #Choose a direction, that is not blocked or a hole,
        #that will get me closer to the flag. If multiple
        #directions will work then choose one randomly.
        #TODO #Encapsulate this big condition in a useful function canMoveWantMove
        if self.isNorth(flag_row) and \
        canMove(board, players, self.row, self.col, direction_list.index['north']) and \
        board[row-1][col] != 'hole':
            good_directions.append('north')
        if self.isSouth(flag_row):
            good_directions.append('south')
        if self.isEast(flag_col):
            good_directions.append('east')
        if self.isWest(flag_col):
            good_directions.append('west')
        #Randomly choose a good direction
        direction = 'north'
        if len(good_directions)!=0:
            direction = random.choice(good_directions)
        '''print()
        print('goal flag: '+str(flag))
        print('flag loc '+str(flag_row)+','+str(flag_col))
        print('my loc '+str(self.row)+','+str(self.col))
        print('Options: '+str(good_directions))
        print('Choice: '+direction)'''
        if direction == self.getHeading():
            self.next_action = 'move'
        else:
            self.next_action = self.turnTowardDirection(direction)
    #Update text for next direction
    self.text = font.render(self.next_action, True,yellow)
    return self.next_action

flag_locations, map_choice, player_locations = createLevel(level_number)

#images is a 2d array of images
#board is a 2d array of the names of tiles
images,board = constructMap(map_choice)

board_width = len(board[0])
board_height = len(board)
map_width = int(board_width*tile_width)
map_height = int(board_height*tile_height)

clock = pygame.time.Clock()
surface = pygame.display.set_mode((map_width, map_height))

player1 = Waitbot(surface, white, 'Waiter')
player2 = AI1(surface, yellow, 'SmartBoi')
player3 = Robot(surface, red, 'Rando1') #Random bot
player4 = Robot(surface, red, 'Rando2') #Random bot
player_list = [player1, player2, player3, player4]
for i in range(4):
    player_list[i].setStart(player_locations[i][0],player_locations[i][1])

flags = []
colors = [red, yellow, blue, green]
for i in range(4):
    flags.append(Flag(surface, flag_locations[i][0], flag_locations[i][1], colors[i]))

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
                action_list.append([p,p.chooseAction(board, player_list, flags)])
            #Randomize ordering of actions
            random.shuffle(action_list)
        else:
            #Take the next action
            player, action = action_list.pop()
            #blink to indicate actor
            for i in range(blink_count):
                player.blink = not player.blink
                drawAll(surface, player_list, flags)
            #Perform action
            player.doAction(board, player_list, flags, action)

    drawAll(surface, player_list, flags)

#Print winners and points scored
print('Winners in order from first to last:')
print(winners)
print('Others:')
for i in range(len(player_list)):
    print(player_list[i].name+' scored '+str(len(player_list[i].flags))+' points.')
pygame.quit()