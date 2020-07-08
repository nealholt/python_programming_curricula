import pygame, random, time

pygame.init()

#Initialize variables:
clock = pygame.time.Clock()
size = 50 #size in pixels of each tile
maze_file = '../maze_navigator_starter_code/mazes/trial00.txt'
fps = 3 #Frames per second
green = 0,255,0
red = 255,0,0
yellow = 255,255,0
blue = 0,0,255
white = 255,255,255
north = 1
south = 2
east = 3
west = 4
victory = False
font = pygame.font.SysFont('Arial', 25)
font = pygame.font.SysFont('Arial', 64)


def draw():
    surface.fill((0,0,0)) #fill surface with black
    for row in map:
        for col in row:
            if col!=None:
                col.draw()
    pygame.display.flip()
    #Delay to get desired frames per second
    clock.tick(fps)

class Wall:
    def __init__(self, surface, x, y, size, color):
        self.surface = surface
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x,y,size,size)
        self.color = color

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rect)



class MazeRunner:
    def __init__(self, surface, row, column, size, color):
        self.surface = surface
        self.col = column
        self.row = row
        self.color = color
        self.heading = north
        #Memory slots to use. For advanced navigation
        self.memory0 = 0
        self.memory1 = 0
        self.memory2 = 0
        self.memory3 = 0
        self.memory4 = 0
        self.memory5 = 0
        self.memory6 = 0
        self.memory7 = 0
        self.memory8 = 0
        self.memory9 = 0

    def wallAhead(self, maze):
        if self.heading == north:
            return maze[self.row-1][self.col] != None and maze[self.row-1][self.col].color==blue
        elif self.heading == south:
            return maze[self.row+1][self.col] != None and maze[self.row+1][self.col].color==blue
        elif self.heading == east:
            return maze[self.row][self.col+1] != None and maze[self.row][self.col+1].color==blue
        elif self.heading == west:
            return maze[self.row][self.col-1] != None and maze[self.row][self.col-1].color==blue
        else:
            print('ERROR in wallAhead')
            exit()

    def setHeading(self, heading):
        self.heading = heading
        draw()

    def turnLeft(self):
        if self.heading == north:
            self.setHeading(west)
        elif self.heading == south:
            self.setHeading(east)
        elif self.heading == east:
            self.setHeading(north)
        elif self.heading == west:
            self.setHeading(south)

    def turnRight(self):
        if self.heading == north:
            self.setHeading(east)
        elif self.heading == south:
            self.setHeading(west)
        elif self.heading == east:
            self.setHeading(south)
        elif self.heading == west:
            self.setHeading(north)

    def moveAhead(self, maze):
        '''Move ahead one space if there is no wall blocking your path.'''
        if not self.wallAhead(maze):
            global victory
            if self.heading == north:
                victory = maze[self.row-1][self.col] != None and maze[self.row-1][self.col].color == red
                maze[self.row-1][self.col] = self
                maze[self.row][self.col] = None
                self.row = self.row-1
            elif self.heading == south:
                victory = maze[self.row+1][self.col] != None and maze[self.row+1][self.col].color == red
                maze[self.row+1][self.col] = self
                maze[self.row][self.col] = None
                self.row = self.row+1
            elif self.heading == east:
                victory = maze[self.row][self.col+1] != None and maze[self.row][self.col+1].color == red
                maze[self.row][self.col+1] = self
                maze[self.row][self.col] = None
                self.col = self.col+1
            elif self.heading == west:
                victory = maze[self.row][self.col-1] != None and maze[self.row][self.col-1].color == red
                maze[self.row][self.col-1] = self
                maze[self.row][self.col] = None
                self.col = self.col-1
            draw()

    def draw(self):
        rect = pygame.Rect(self.col*size,self.row*size,size,size)
        pygame.draw.rect(self.surface, self.color, rect)
        #Draw a heading indicator
        if self.heading == north:
            rect = pygame.Rect(self.col*size+size/4,self.row*size+size/4-size/2,size/2,size/2)
        elif self.heading == south:
            rect = pygame.Rect(self.col*size+size/4,self.row*size+size/4+size/2,size/2,size/2)
        elif self.heading == east:
            rect = pygame.Rect(self.col*size+size/4+size/2,self.row*size+size/4,size/2,size/2)
        elif self.heading == west:
            rect = pygame.Rect(self.col*size+size/4-size/2,self.row*size+size/4,size/2,size/2)
        pygame.draw.rect(self.surface, green, rect)

    def goToGoal(self, maze, goal_row, goal_col):
        #self.openNavigation(maze, goal_row, goal_col)
        #self.randomNavigation(maze)
        #self.deadEndNavigation(maze)
        #self.handWallNavigation(maze)
        #self.randomHybridNavigation(maze, goal_row, goal_col)
        self.deterministicHybridNavigation(maze, goal_row, goal_col)

    def deterministicHybridNavigation(self, maze, goal_row, goal_col):
        '''This uses open navigation until it gets stuck at which
        point it remembers how far it was from the goal and then
        engages wall following until it gets closer than when it got
        stuck, at which point it reverts to wall following.
        This requires additional variables in order to remember the closest
        distance.
        There is one tiny randomness involved here and that's whether to
        use left or right handed wall following procedures. It makes a
        difference.'''
        #Set memory of best_distance
        if self.memory1 == 0:
            self.memory1 = 999999 #closest we've gotten to goal
        #Navigate to goal
        if self.memory0: #Whether or not we are open navigating
            #Use these variables to detect progress
            self.memory2 = self.row
            self.memory3 = self.col
            #Take one open navigation step
            self.openNavigation(maze, goal_row, goal_col)
            print('open nav step')
            #Detect if stuck and if so, revert to other navigation mode
            stuck = (self.memory2==self.row and self.memory3==self.col)
            if stuck:
                self.memory0 = False #Whether or not we are open navigating
                #Remember distance
                temp_distance = abs(self.col-goal_col)+abs(self.row-goal_row)
                if temp_distance<self.memory1: #closest we've gotten to goal
                    self.memory1 = temp_distance
                #Choose to be left or right handed
                self.memory4 = random.random()<0.5
                if self.memory4: #Left handed if true
                    self.turnRight() #To put the wall on our left
                else:
                    self.turnLeft() #To put the wall on our right
                #Remember where we started
                self.memory2=self.row
                self.memory3=self.col
        else:
            #Take one step along the wall
            if self.memory4: #Left handed if true
                print('left hand step')
                self.handWallNavigation(maze)
            else:
                self.handWallNavigationRight(maze)
                print('right hand step')
            #Check distance
            new_distance = abs(self.col-goal_col)+abs(self.row-goal_row)
            if new_distance <= self.memory1: #closest distance to goal
                print('best distance: '+str(self.memory1))
                self.memory1 = new_distance
                self.memory0 = True #Whether or not we are open navigating
            else:
                #If we're back where we started then kick over to the
                #other navigation
                self.memory0 = (self.memory2==self.row and self.memory3==self.col) #Whether or not we are open navigating

    def randomHybridNavigation(self, maze, goal_row, goal_col):
        '''This is a combination wall following and open maze navigation
        strategy that randomly switches between the behaviors. It is
        weighted towards wall following. This DOES succeed on all mazes,
        but it can take a long time.'''
        if random.random() < 0.8:
            self.handWallNavigation(maze)
        else:
            self.openNavigation(maze, goal_row, goal_col)

    def handWallNavigation(self, maze):
        '''This is your standard, put your hand on the wall and never
        take it off strategy for a typical corn maze.
        This strategy is stumped by trial05, when the goal is not against a
        wall, but does well up until then.
        This ASSUMES your left hand is on the wall. The version below
        assumes a right hand on the wall.'''
        self.turnLeft()
        if self.wallAhead(maze):
            self.turnRight()
            if self.wallAhead(maze):
                self.turnRight()
            self.moveAhead(maze)
        else:
            self.moveAhead(maze)

    def handWallNavigationRight(self, maze):
        '''This is your standard, put your hand on the wall and never
        take it off strategy for a typical corn maze.
        This strategy is stumped by trial05, when the goal is not against a
        wall, but does well up until then.
        This ASSUMES your right hand is on the wall. The version above
        is left handed.'''
        self.turnRight()
        if self.wallAhead(maze):
            self.turnLeft()
            if self.wallAhead(maze):
                self.turnLeft()
            self.moveAhead(maze)
        else:
            self.moveAhead(maze)

    def deadEndNavigation(self, maze):
        '''Moves straight until there is a wall then turns to next open
        direction and moves again. This will miss openings along the sides.
        This strategy is stumped by trial03, but does well up until then.'''
        if self.wallAhead(maze):
            self.turnLeft()
            if self.wallAhead(maze):
                self.turnRight()
                self.turnRight()
        self.moveAhead(maze)

    def openNavigation(self, maze, goal_row, goal_col):
        '''Navigation for open spaces.
        Calls to draw are inserted to better see what's going on.'''
        #Take one step in the best north/south direction
        if goal_row<self.row:
            self.setHeading(north)
            self.moveAhead(maze)
        elif goal_row>self.row:
            self.setHeading(south)
            self.moveAhead(maze)
        #Take one step in the best east/west direction
        if goal_col<self.col:
            self.setHeading(west)
            self.moveAhead(maze)
        elif goal_col>self.col:
            self.setHeading(east)
            self.moveAhead(maze)

    def randomNavigation(self, maze):
        '''Move by pure randomness'''
        r = random.randint(0,2)
        if r == 0:
            self.moveAhead(maze)
        elif r == 1:
            self.turnLeft()
        elif r == 2:
            self.turnRight()



#Open file to read in text representation of the maze
file_handle = open(maze_file, 'r')
line = file_handle.readline()
line = line.strip()
map_characters = [] #2d array
while line:
    map_characters.append(line)
    line = file_handle.readline()
    line = line.strip()

#Now map_characters contains the maze file read in as a 2d array of characters.
#Create a screen of the appropriate dimensions
map_width = len(map_characters[0]) #width in number of tiles
map_height = len(map_characters) #height in number of tiles
surface = pygame.display.set_mode((map_width*size,map_height*size))

#Coordinates of the start and goal tiles
start_row = start_col = goal_row = goal_col = 0
#Convert map_characters to a 2d array of sprites now.
map = []
for row in range(len(map_characters)):
    temp_row = []
    for col in range(len(map_characters[row])):
        if map_characters[row][col] == 'w':
            temp_row.append(Wall(surface, col*size, row*size, size, blue))
        elif map_characters[row][col] == 's':
            temp_row.append(None)
            start_row = row
            start_col = col
        elif map_characters[row][col] == 'e':
            temp_row.append(Wall(surface, col*size, row*size, size, red))
            goal_row = row
            goal_col = col
        else:
            temp_row.append(None)
    map.append(temp_row)

#Create maze runner
runner = MazeRunner(surface, start_row, start_col, size, yellow)
map[start_row][start_col] = runner

#Main program loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
    if victory:
        surface.blit(font.render('Winner!', True,white), (10,10))
        pygame.display.flip()
        #Delay to get desired frames per second
        clock.tick(fps)
    else:
        runner.goToGoal(map, goal_row, goal_col)
pygame.quit()