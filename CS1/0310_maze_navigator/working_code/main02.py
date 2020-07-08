import pygame, math

pygame.init()

#Initialize variables:
clock = pygame.time.Clock()
size = 50 #size in pixels of each tile
maze_file = '../maze_navigator_starter_code/mazes/trial00.txt'
green = 0,255,0
red = 255,0,0
yellow = 255,255,0
blue = 0,0,255

'''TODO

'''

class Wall:
	def __init__(self, surface, x, y, size, color):
		self.surface = surface
		self.x = x
		self.y = y
		self.rect = pygame.Rect(x,y,size,size)
		self.color = color
	
	def draw(self):
		pygame.draw.rect(self.surface, self.color, self.rect)


#Open file to read in text representation of the map
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
			temp_row.append(Wall(surface, col*size, row*size, size, green))
			start_row = row
			start_col = col
		elif map_characters[row][col] == 'e':
			temp_row.append(Wall(surface, col*size, row*size, size, red))
			goal_row = row
			goal_col = col
		else:
			temp_row.append(None)
	map.append(temp_row)

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
	for row in map:
		for col in row:
			if col!=None:
				col.draw()
	pygame.display.flip()
	pygame.display.update()
	#Delay to get 30 fps
	clock.tick(30)
	