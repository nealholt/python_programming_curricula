'''
This program is based on a NetLogo model found at
Netlogo -> Models Library -> Chemistry & Physics -> Waves -> unverified -> Raindrops

Step 1: Create and draw 2d array of water blobs.
	See TODO1 and TODO2
Step 2: getClickedRowCol. Test this by clicking to change individual cell colors.
	See #TODO3
Step 3: sumNeighborsZs. Test this by having the click change the color and use this to average the colors of neighboring cells.
	See #TODO4
Step 4: releaseDrop, computeDeltaZ, updatePosAndColor. Don't forget to compute all delta z's before updating in the main loop. Also explain the rationale behind computeDeltaZ. The surface tension acts like a trampoline surface. If neighboring cells are above middle cell, then they pull it up. If they are below, they pull it down.
You are given the code for these functions, but you have to put everything together to make them work.

In the main loop, before drawing, loop through and update all delta z's by caling the computeDeltaZ function on each water blob.
	See #TODO5

Uncomment the call to releaseDrop that happens when the mouse is clicked.
	See #TODO6

Don't forget to call updatePosAndColor right before drawing each water blob.
'''
import pygame


#Simulation variables. Feel free to modify these to see how they affect the running
#of the program.
default_impact = 30
surface_tension = 0.65
friction = 0.99


#This is a generic circle-drawing object that has been modified with 
#z and delta_z variables.
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
	'''Sum up neighbors' z values and count the number of neighbors.
	Return both values.
	Watchout for edges so you don't get IndexOutOfBounds errors.'''
	#TODO4



def getClickedRowCol(water2d, pos):
	'''This function takes the 2D array of blobs and a mouse click position.
	The function returns the row and column in the array of the blob
	that was clicked on.'''
	pass #TODO3


def releaseDrop(water2d, pos):
	'''This function should be called when the user clicks on the screen.
	This function begins the simulation of a raindrop striking the surface
	of the water.'''
	row,column = getClickedRowCol(water2d, pos)
	computeDeltaZ(water2d, row, column, default_impact)


def computeDeltaZ(water2d, row, column, impact):
	'''Delta-Z is the change in height of the surface of the water.
	Delta-Z is based on the impact on the water, but also the height
	of the surrounding water and the surface tension.'''
	k = 1 - surface_tension
	z_sum, neighbor_count = sumNeighborsZs(water2d, row, column)
	water2d[row][column].delta_z = water2d[row][column].delta_z + (k * ((z_sum - (neighbor_count * water2d[row][column].z)) - impact))


def updatePosAndColor(droplet):
	'''Update the height of the given droplet of water and reduce the
	droplet's delta_z.'''
	droplet.z = (droplet.z + droplet.delta_z) * friction
	#Suppress delta_z back to zero also. I couldn't find this in the netlogo
	#code, but it prevents my water from blacking out after 2 clicks.
	droplet.delta_z = droplet.delta_z * friction
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
#TODO1



#Primary simulation loop
running = True
while running:
	#Fill the screen with black
	screen.fill(BLACK)

	#Update water
	#TODO5
	
	#Draw all the water blobs
	#TODO2
	
	#Respond to events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False
		elif event.type == pygame.MOUSEBUTTONUP:
			pos = pygame.mouse.get_pos()
			#TODO6
			#releaseDrop(water, pos)
	#Update screen display
	pygame.display.flip()
	#Delay to get 30 fps
	clock.tick(30)
