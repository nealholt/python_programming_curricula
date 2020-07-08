import pygame, random, time

pygame.init()

#Initialize variables:
clock = pygame.time.Clock()
size = 50 #size in pixels of each tile
maze_file = '../maze_navigator_starter_code/mazes/trial00.txt'
fps = 10 #Frames per second
green = 0,255,0
red = 255,0,0
yellow = 255,255,0
blue = 0,0,255
north = 1
south = 2
east = 3
west = 4

'''TODO
	write straight to corner then turn
	Write left hand on wall algorithm.
	Write combination wall following and open maze navigation naive version which randomly switches between the behaviors.
	Write combination wall following and open maze navigation version that tracks distance to goal.
'''

def draw():
	for row in map:
		for col in row:
			if col!=None:
				col.draw()
	pygame.display.flip()
	pygame.display.update()
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
		
	def turnLeft(self):
		if self.heading == north:
			self.heading = west
		elif self.heading == south:
			self.heading = east
		elif self.heading == east:
			self.heading = north
		elif self.heading == west:
			self.heading = south
	
	def turnRight(self):
		if self.heading == north:
			self.heading = east
		elif self.heading == south:
			self.heading = west
		elif self.heading == east:
			self.heading = south
		elif self.heading == west:
			self.heading = north
	
	def moveAhead(self, maze):
		if not self.wallAhead(maze):
			if self.heading == north:
				maze[self.row-1][self.col] = self
				maze[self.row][self.col] = None
				self.row = self.row-1
			elif self.heading == south:
				maze[self.row+1][self.col] = self
				maze[self.row][self.col] = None
				self.row = self.row+1
			elif self.heading == east:
				maze[self.row][self.col+1] = self
				maze[self.row][self.col] = None
				self.col = self.col+1
			elif self.heading == west:
				maze[self.row][self.col-1] = self
				maze[self.row][self.col] = None
				self.col = self.col-1

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
	
	def update(self, maze, goal_row, goal_col):
		self.openNavigation(maze, goal_row, goal_col)
		#self.randomNavigation(maze)
	
	def openNavigation(self, maze, goal_row, goal_col):
		'''Navigation for open spaces.
		Calls to draw are inserted to better see what's going on.'''
		#Take one step in the best north/south direction
		if goal_row<self.row:
			self.heading = north
			draw()
			self.moveAhead(maze)
			draw()
		elif goal_row>self.row:
			self.heading = south
			draw()
			self.moveAhead(maze)
			draw()
		#Take one step in the best east/west direction
		if goal_col<self.col:
			self.heading = west
			draw()
			self.moveAhead(maze)
			draw()
		elif goal_col>self.col:
			self.heading = east
			draw()
			self.moveAhead(maze)
			draw()
	
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
print(map_characters)

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
	surface.fill((0,0,0)) #fill surface with black
	runner.update(map, goal_row, goal_col)
	draw()
	