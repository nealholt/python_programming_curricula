import pygame, random, time

pygame.init()
#Initialize variables:
clock = pygame.time.Clock()
size = 50 #size in pixels of each tile
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
font = pygame.font.SysFont('Arial', 64)
surface = None
map = None


def draw(fps):
    '''Draw the maze.'''
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
    def __init__(self, surface, row, column, size, color, fps):
        self.surface = surface
        self.col = column
        self.row = row
        self.color = color
        self.fps = fps
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
        self.memorylist = []

    def distanceToGoal(self, goal_row, goal_col):
        return abs(self.row-goal_row) + abs(self.col-goal_col)

    def wallAhead(self, maze):
        '''Returns true if there is a wall directly ahead.'''
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
        '''Sets the heading of the maze runner to the given value.'''
        self.heading = heading
        draw(self.fps)

    def turnLeft(self):
        '''Rotate left (counterclockwise).'''
        if self.heading == north:
            self.setHeading(west)
        elif self.heading == south:
            self.setHeading(east)
        elif self.heading == east:
            self.setHeading(north)
        elif self.heading == west:
            self.setHeading(south)

    def turnRight(self):
        '''Rotate right (clockwise).'''
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
            draw(self.fps)

    def draw(self):
        rect = pygame.Rect(self.col*size,self.row*size,size,size)
        pygame.draw.rect(self.surface, self.color, rect, 4)
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


def main(maze_file, fps, goToGoal):
    global surface, map
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
    runner = MazeRunner(surface,start_row,start_col,size,yellow,fps)
    map[start_row][start_col] = runner

    #Main program loop
    draw(fps)
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
            goToGoal(runner, map, goal_row, goal_col)
    pygame.quit()
    exit()