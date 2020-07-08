import random, robot
from functions import *

class RandomBot(robot.Robot):
    def __init__(self, screen, color,name):
        super().__init__(screen, color,name)

    def chooseAction(self, board, players, flags):
        '''
        Useful functions:
        getPlayerAt(players, row, col)
        outOfBounds(board,row,col)
        canMove(board, players, row, col, direction)
        isConveyor(board, row, col)

        self.enemyInSight(board, players)
            -Returns True if shooting a laser now would
        hit another player.

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

        row,col = self.getCellAheadCoordinates()
            -Returns row,col of cell immediately ahead
        of this robot.

        cell_type = self.getCellAheadType(board)
            -Returns the cell type of the cell immediately
        ahead of this robot as a string.

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
        r = random.randint(0,4)
        if r == 0:
            self.next_action = 'left'
        elif r == 1:
            self.next_action = 'right'
        elif r == 2:
            self.next_action = 'move'
        elif r == 3:
            self.next_action = 'zap'
        elif r == 4:
            self.next_action = 'wait'
        return self.next_action
