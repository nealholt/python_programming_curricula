import random, robot
from functions import *

class AI2(robot.Robot):
    def __init__(self, screen, color,name):
        super().__init__(screen, color,name)
    def isInDirection(self,row,col,direction):
        if direction == 'north':
            return row<self.row
        elif direction == 'south':
            return row>self.row
        elif direction == 'east':
            return col>self.col
        else: #if direction == 'west':
            return col<self.col
    def canMoveWantMove(self, board, players, goal_row, goal_col, direction):
        '''The goal is in the proposed direction and we can move that
        direction and there is not a hole in that direction.'''
        row_change,col_change = getRowColChange(direction)
        return self.isInDirection(goal_row, goal_col, direction) and \
        canMove(board,players,self.row,self.col,direction) and \
        board[self.row+row_change][self.col+col_change] != 'hole'
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
        #Throw in some randomization to get unstuck
        r = random.random()
        if r < 0.25: #1/4th of the time, act randomly
            r = random.randint(0,2)
            if r == 0:
                self.next_action = 'left'
            elif r == 1:
                self.next_action = 'right'
            else:
                self.next_action = 'move'
        else:
            self.next_action = 'move'
            #Choose a flag I don't have
            flags_i_need = self.flagsINeed(flags)
            flag_row = flags_i_need[0].row
            flag_col = flags_i_need[0].col
            #Choose a direction, that is not blocked or a hole,
            #that will get me closer to the flag.
            for direction in direction_list:
                if self.canMoveWantMove(board, players, flag_row, flag_col,direction):
                    if self.direction == direction:
                        self.next_action = 'move'
                    else:
                        self.next_action = self.turnTowardDirection(direction)
                    break
        return self.next_action
