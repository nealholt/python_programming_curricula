import robot, random
from functions import *

class BFSbot(robot.Robot):
    def __init__(self, screen, color,name):
        super().__init__(screen, color,name)
        #This list holds row,col pairs that get added in
        #a breadth first manner.
        self.locations = []
        #This list holds indicies of the parent cell
        #from which the corresponding cell in the locations
        #list is a neighbor.
        self.parent_indicies = []
        #List of directions from which to enter the neighboring cell
        self.direction_into = []
    def chooseAction(self, board, players, flags):
        #This bot attempts to greedily follow the shortest path
        #Choose a flag I don't have
        flags_i_need = self.flagsINeed(flags)
        #Get nearest flag
        i = 0
        flag_row = flags_i_need[i].row
        flag_col = flags_i_need[i].col
        d = distanceBetween(self.row,self.col,flag_row,flag_col)
        for j in range(1,len(flags_i_need)):
            flag_row = flags_i_need[j].row
            flag_col = flags_i_need[j].col
            temp = distanceBetween(self.row,self.col,flag_row,flag_col)
            if temp < d:
                i = j
                d = temp
        flag_row = flags_i_need[i].row
        flag_col = flags_i_need[i].col
        #Start with current location.
        self.locations = [(self.row,self.col)]
        self.parent_indicies = [-1]
        self.direction_into = ['north'] #Any initial value will do
        index = 0
        #Create breadth first search of all cells until
        #the chosen flag is found
        while not( (flag_row,flag_col) in self.locations): # and index < len(self.locations):
            #Get all neighboring cells. Ignore previously
            #visited cells in the self.locations list.
            r = self.locations[index][0]
            c = self.locations[index][1]
            neighbors = getAllNeighbors(board,r,c,self.locations)
            #Add all the neighbors to the list of locations
            #identify their parent cell using index
            for i in range(len(neighbors)):
                if neighbors[i] != None: # and not (neighbors[i] in self.locations):
                    self.locations.append(neighbors[i])
                    self.parent_indicies.append(index)
                    self.direction_into.append(direction_list[i])
            #Advance the index to find all neighbors of the
            #next cell.
            index = index + 1
        #Get index of the goal
        i = self.locations.index((flag_row,flag_col))
        j = i
        #Calculate path to goal working backwards from
        #destination, until you get a neighbor of the
        #current cell.
        while self.parent_indicies[i] != -1:
            j = i
            i = self.parent_indicies[i]
        #If destination cell is ahead, then move,
        #otherwise turn toward it.
        '''#OLD WAY
        goal_row,goal_col = self.locations[j]
        direction = 'west'
        if self.isNorth(goal_row):
            direction = 'north'
        elif self.isSouth(goal_row):
            direction = 'south'
        elif self.isEast(goal_col):
            direction = 'east'
        if self.direction == direction:
            self.next_action = 'move'
        else:
            self.next_action = self.turnTowardDirection(direction)'''
        #print()
        #print(j)
        #print(self.direction_into)
        goal_direction = self.direction_into[j]
        if self.direction == goal_direction:
            self.next_action = 'move'
        else:
            self.next_action = self.turnTowardDirection(goal_direction)
        return self.next_action

    def connectCells(self, r1,c1,r2,c2, thickness):
        '''Draw a line between the two cells.'''
        center_x1 = c1*tile_width + tile_width/2
        center_y1 = r1*tile_height + tile_height/2
        center_x2 = c2*tile_width + tile_width/2
        center_y2 = r2*tile_height + tile_height/2
        start = (center_x1, center_y1)
        end = (center_x2, center_y2)
        pygame.draw.line(self.screen, white, start, end, thickness)

    def draw(self):
        super().draw()
        #Draw the path.
        for i in reversed(range(1,len(self.locations))):
            r1 = self.locations[i][0]
            c1 = self.locations[i][1]
            parenti = self.parent_indicies[i]
            r2 = self.locations[parenti][0]
            c2 = self.locations[parenti][1]
            self.connectCells(r1,c1,r2,c2,5)
