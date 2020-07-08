import robot, random
from functions import *

class Greedybot(robot.Robot):
    def __init__(self, screen, color,name):
        super().__init__(screen, color,name)
    def chooseAction(self, board, players, flags):
        #This bot attempts to greedily follow the shortest path
        #Choose a flag I don't have
        flags_i_need = self.flagsINeed(flags)
        flag_row = flags_i_need[0].row
        flag_col = flags_i_need[0].col
        #Get all neighboring cells
        neighbors = getAllNeighbors(board,self.row,self.col)
        #Figure out which neighboring cell is closest to goal. There could
        #be more than one, in which case, select randomly.
        closest = 2**31
        best_indicies = []
        for i in range(len(neighbors)):
            if neighbors[i]!=None:
                d = distanceBetween(flag_row,flag_col,neighbors[i][0],neighbors[i][1])
                if closest>d:
                    closest = d
                    best_indicies = [i]
                elif closest==d:
                    best_indicies.append(i)
        #Either turn to face best neighbor or move ahead
        index = random.choice(best_indicies)
        if direction_list[index] == self.direction:
            self.next_action = 'move'
        else:
            print()
            print(direction_list[index])
            print(flags_i_need[0].color)

            self.next_action = self.turnTowardDirection(direction_list[index])
        return self.next_action

