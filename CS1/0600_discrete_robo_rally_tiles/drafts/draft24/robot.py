import random, math, flag
from functions import *

class Robot:
    def __init__(self, screen, color, name):
        self.screen = screen
        self.name = name
        self.row = 0
        self.col = 0
        self.color = color
        self.sides = 3
        self.radius = 40*scaling
        self.direction = 'east'
        self.checkpoint = (0,0)
        self.next_action = ''
        self.text = font.render('', True,yellow)
        self.blink = False
        self.flags = []
        self.hp = 8
        self.max_hp = 12
        self.laser_end = None
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
        if direction == 'north':
            if self.direction == 'west':
                return 'right'
            else:
                return 'left'
        elif direction == 'south':
            if self.direction == 'east':
                return 'right'
            else:
                return 'left'
        elif direction == 'east':
            if self.direction == 'north':
                return 'right'
            else:
                return 'left'
        else: #elif direction == 'west':
            if self.direction == 'south':
                return 'right'
            else:
                return 'left'
    def shootLaser(self, board, players):
        #Get the limit of the laser in terms of walls before checking player collisions
        row_limit, col_limit = blockedByWall(board, self.row, self.col, self.direction)
        #Return if the laser is immediately blocked by a wall
        if row_limit == self.row and col_limit == self.col:
            return row_limit, col_limit
        #Check for a robot that got hit
        robot_hit = None
        row_change,col_change = getRowColChange(self.direction)
        temp_row = self.row + row_change
        temp_col = self.col + col_change
        p = getPlayerAt(players, temp_row, temp_col)
        while p==None and not(temp_row==row_limit and temp_col==col_limit):
            temp_row = temp_row + row_change
            temp_col = temp_col + col_change
            p = getPlayerAt(players, temp_row, temp_col)
        #If a player got hit, deal 3 damage
        if p!=None:
            p.hp -= 3
            #Remember previous row and col so you know where to send the robot
            temp_row = p.row
            temp_col = p.col
            #Check for sending player back to checkpoint
            if p.hp <= 0:
                p.hp = 1
                p.row,p.col = p.checkpoint
            return temp_row,temp_col
        #Return the end location of the laser
        else:
            return row_limit,col_limit
    def doAction(self, board, players, flags, action):
        if action == 'left':
            self.rotateLeft()
        elif action == 'right':
            self.rotateRight()
        elif action == 'move':
            self.move(board, players, flags)
        elif action == 'zap':
            self.laser_end = self.shootLaser(board, players)
        elif action == 'wait':
            self.eventAtLocation(board, flags)
        self.next_action = ''
        self.text = font.render('', True,yellow)
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
        r = random.randint(0,4)
        if r == 0:
            self.next_action = 'left'
        elif r == 1:
            self.next_action = 'right'
        elif r == 2:
            self.next_action = 'move'
        elif r == 3:
            self.next_action = 'wait'
        else:
            self.next_action = 'zap'
        return self.next_action
    def rotateLeft(self):
        index = direction_list.index(self.direction)
        index -= 1
        if index < 0:
            index = len(direction_list)-1
        self.direction = direction_list[index]
    def rotateRight(self):
        index = direction_list.index(self.direction)
        index = (index+1)%len(direction_list)
        self.direction = direction_list[index]
    def forceMove(self, board, players, direction, flags):
        row_change,col_change = getRowColChange(direction)
        temp_row = self.row + row_change
        temp_col = self.col + col_change
        #Check for another player that got shoved and
        #pass the shove down the line.
        p = getPlayerAt(players, temp_row, temp_col)
        if p != None:
            p.forceMove(board, players, direction, flags)
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
                p.forceMove(board, players, self.direction, flags)
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
            #Lose half health rounded up
            self.hp = int(self.hp/2)
            if self.hp == 0:
                self.hp = 1
        #Update our checkpoint if we landed on a checkpoint
        elif board[self.row][self.col] == 'chek':
            self.checkpoint = (self.row, self.col)
            #Also gain 4 health
            self.hp = min(self.max_hp, self.hp+4)
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
        if self.direction == 'north':
            heading = -math.pi/2
        elif self.direction == 'south':
            heading = math.pi/2
        elif self.direction == 'west':
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
            temp = flag.Flag(self.screen, self.row, self.col, f)
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
        #Draw health bar
        r = pygame.Rect(offset_x-tile_width/2.4,
                        offset_y+tile_height*0.3,
                        tile_width*0.8,
                        tile_height*0.1)
        pygame.draw.rect(self.screen, red, r)
        r = pygame.Rect(offset_x-tile_width/2.4,
                        offset_y+tile_height*0.3,
                        tile_width*0.8*(self.hp/self.max_hp),
                        tile_height*0.1)
        pygame.draw.rect(self.screen, green, r)
        #Draw laser beam
        if self.laser_end!=None:
            x = self.laser_end[1]*tile_width + tile_width/2
            y = self.laser_end[0]*tile_height + tile_height/2
            start = (offset_x, offset_y)
            end = (x,y)
            pygame.draw.line(self.screen, red, start, end, 3)
            pygame.draw.line(self.screen, white, start, end, 1)

