import random, robot
from functions import *

class SmartRandomBot(robot.Robot):
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
        #Choose a random action
        self.next_action = random.choice(['left','right','move'])

        #avoid walking into holes
        cell_type = self.getCellAheadType(board)
        if cell_type == 'hole':
            self.next_action = random.choice(['left','right'])

        #Zap enemies when possible
        if self.enemyInSight(board, players):
            self.next_action = 'zap'

        return self.next_action
