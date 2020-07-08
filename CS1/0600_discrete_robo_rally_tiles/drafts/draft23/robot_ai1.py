import random, robot
from functions import *

class AI1(robot.Robot):
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
            if direction == self.direction:
                self.next_action = 'move'
            else:
                self.next_action = self.turnTowardDirection(direction)
        return self.next_action
