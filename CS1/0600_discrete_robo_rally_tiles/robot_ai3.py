import random, robot
from functions import *

def generateMoveSequence(length):
    sequence = []
    for i in range(length):
        sequence.append(random.choice(['left','right','move','move','move','wait']))
    return sequence

class AI3(robot.Robot):
    def __init__(self, screen, color,name):
        super().__init__(screen, color,name)
        self.move_sequence = []
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
        #Use the next move in the sequence if there is one.
        if len(self.move_sequence)>0:
            self.next_action = self.move_sequence[0]
            del self.move_sequence[0]
            return self.next_action
        #Otherwise determine a new move sequence.

        #Choose nearest flag I don't have
        flags_i_need = self.flagsINeed(flags)
        nearest_flag = flags_i_need[0]
        for f in flags_i_need[1:]:
            if distanceBetween(self.row,self.col,f.row,f.col) < distanceBetween(self.row,self.col,nearest_flag.row,nearest_flag.col):
                nearest_flag = f
        print(nearest_flag.color)
        print(nearest_flag.row,nearest_flag.col)
        '''
        #This does not work well. Random is terrible.
        #Spend a short amount of time finding a sequence of
        #moves that gets this robot closest to the flag.
        tries = 20
        sequence_length = 5
        best_moves = generateMoveSequence(sequence_length)
        best_r,best_c = self.simulateMoveSequence(board, best_moves)
        best_distance = distanceBetween(best_r,best_c,nearest_flag.row,nearest_flag.col)
        print('ALTERNATIVES:')
        for i in range(tries):
            other_moves = generateMoveSequence(sequence_length)
            print(other_moves)
            other_r,other_c = self.simulateMoveSequence(board, other_moves)
            other_distance = distanceBetween(other_r,other_c,nearest_flag.row,nearest_flag.col)
            if best_distance > other_distance:
                best_moves = other_moves
                best_r,best_c = other_r,other_c
                best_distance = other_distance
        '''
        #Choose best sequence from a set of predefined
        #sequences.
        sequences = [ ['move'],
                      ['left','move'],
                      ['right','move'],
                      ['move','move'],
                      ['wait'],
                      ['move','left','move'],
                      ['move','right','move'],
                      ['left','left','move']
                    ]
        best_moves = sequences[0]
        best_r,best_c = self.simulateMoveSequence(board, best_moves)
        best_distance = distanceBetween(best_r,best_c,nearest_flag.row,nearest_flag.col)
        for s in sequences[1:]:
            other_r,other_c = self.simulateMoveSequence(board, s)
            other_distance = distanceBetween(other_r,other_c,nearest_flag.row,nearest_flag.col)
            print('sequence: '+str(s)+' dist: '+str(other_distance))
            print(other_r,other_c)
            if best_distance > other_distance:
                best_moves = s
                best_r,best_c = other_r,other_c
                best_distance = other_distance

        #Select the next best action
        print('BEST distance '+str(best_distance))
        print(best_r,best_c)
        print(best_moves)
        print()
        self.move_sequence = best_moves
        self.next_action = self.move_sequence[0]
        del self.move_sequence[0]
        return self.next_action
