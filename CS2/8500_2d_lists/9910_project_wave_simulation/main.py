#Netlogo -> Models Library -> Chemistry & Physics -> Waves -> unverified -> Raindrops

'''
Step 1: Create and draw 2d array of water blobs
Step 2: getClickedRowColumn. Test this by clicking to change individual cell colors.
Step 3: sumNeighborsZs. Test this by having the click change the color and use this to average the colors of neighboring cells.
Step 4: releaseDrop, computeDeltaZ, updatePosAndColor. Don't forget to compute all delta z's before updating in the main loop. Also explain the rationale behind computeDeltaZ. The surface tension acts like a trampoline surface. If neighboring cells are above middle cell, then they pull it up. If they are below, they pull it down.
'''
import pygame


#Simulation variables
default_impact = 30
surface_tension = 0.65
friction = 0.99


class blob:
	def __init__(self, surface, color, x, y, radius):
		self.surface = surface
		#x and y are the center of this object
		self.x = x
		self.y = y
		self.z = 0
		self.delta_z = 0
		self.color = color
		self.radius = radius
	
	def getRect(self):
		return pygame.Rect(
			[self.x-self.radius, #x
			self.y-self.radius, #y
			self.radius*2, #width
			self.radius*2]) #height
	
	def draw(self):
		pygame.draw.ellipse(self.surface, self.color, self.getRect())



def sumNeighborsZs(water2d, row, column):
	'''Sum up neighbors' z values and count the number of neighbors.'''
	z_sum = 0
	neighbor_count = 0
	if row > 0:
		z_sum = z_sum + water2d[row-1][column].z
		neighbor_count = neighbor_count + 1
	if row < len(water2d)-1:
		z_sum = z_sum + water2d[row+1][column].z
		neighbor_count = neighbor_count + 1
	if column > 0:
		z_sum = z_sum + water2d[row][column-1].z
		neighbor_count = neighbor_count + 1
	if column < len(water2d[0])-1:
		z_sum = z_sum + water2d[row][column+1].z
		neighbor_count = neighbor_count + 1
	return (z_sum, neighbor_count)


def getClickedRowCol(water2d, pos):
	for row in range(len(water2d)):
		for column in range(len(water2d[row])):
			if water2d[row][column].getRect().collidepoint(pos):
				return (row,column)
	return None


def releaseDrop(water2d, pos):
	row,column = getClickedRowCol(water2d, pos)
	computeDeltaZ(water2d, row, column, default_impact)


def computeDeltaZ(water2d, row, column, impact):
	k = 1 - surface_tension
	z_sum, neighbor_count = sumNeighborsZs(water2d, row, column)
	water2d[row][column].delta_z = water2d[row][column].delta_z + (k * ((z_sum - (neighbor_count * water2d[row][column].z)) - impact))


def updatePosAndColor(droplet):
	droplet.z = (droplet.z + droplet.delta_z) * friction
	#Suppress delta_z back to zero also. I couldn't find this in the netlogo
	#code, but it prevents my water from blacking out after 2 clicks.
	droplet.delta_z = droplet.delta_z * friction
	#print(droplet.delta_z)
	if abs(droplet.z) < 1:
		droplet.color = (0, 0, int(255*(1-abs(droplet.z))) )
	else:
		droplet.color = (0,0,0)



#Setup
BLACK = (0,0,0)
BLUE = (0,0,255)
width = 600
height = 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

#Make a 2D array of water blobs
water = []
dimensions = 30
radius = 10
for row in range(dimensions):
	water_row = []
	for column in range(dimensions):
		new_water = blob(screen,
						BLUE,
						radius+column*2*radius, #x
						radius+row*2*radius, #y
						radius) #radius
		water_row.append(new_water)
	water.append(water_row)


#Primary simulation loop
running = True
while running:
	#Fill the screen with black
	screen.fill(BLACK)
	#Update water
	for row in range(dimensions):
		for column in range(dimensions):
			computeDeltaZ(water, row, column, 0)
	#Draw water
	for row in range(dimensions):
		for column in range(dimensions):
			updatePosAndColor(water[row][column])
			water[row][column].draw()
	#Respond to events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False
		elif event.type == pygame.MOUSEBUTTONUP:
			pos = pygame.mouse.get_pos()
			releaseDrop(water, pos)
	#Update screen display
	pygame.display.flip()
	#Delay to get 30 fps
	clock.tick(30)
