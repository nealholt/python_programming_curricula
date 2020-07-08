import pygame, math

#Setup
pygame.init()
width = 900
height = 600
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 24)
black = 0,0,0
white = 255,255,255


class Blob:
	'''Generic circle-drawing class.'''
	def __init__(self, surface, x, y, dx, dy):
		self.surface = surface
		self.x = x
		self.y = y
		self.dx = dx
		self.dy = dy
	
	def move(self, border_right, border_bottom):
		self.x += self.dx
		self.y += self.dy
		#print(self.x)
		if self.x < 0:
			self.x += border_right
		elif self.x > border_right:
			self.x -= border_right
		if self.y < 0:
			self.y += border_bottom
		elif self.y > border_bottom:
			self.y -= border_bottom
	
	def draw(self):
		'''
		http://learnrich.org/pygame-drawing-shapes
		pygame.draw.polygon(screen, COLOUR, point list, line_thickness)
		This example will draw a polygon as a line 
		pygame.draw.polygon(screen, WHITE, [[100, 100], [100, 400],[400, 300]], 2)
		'''
		point_list = [[100, 100], [100, 400],[400, 300]]
		for i in range(len(point_list)):
			point_list[i][0] = point_list[i][0]+self.x
			point_list[i][1] = point_list[i][1]+self.y
		line_thickness = 2
		pygame.draw.polygon(self.surface, white, point_list, line_thickness)



#Test blob
test = Blob(screen, 20, 20, 1, 3)


#Main loop
done = False
while not done:
	#Handle events
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				done = True
	#fill screen with black
	screen.fill(black)
	test.move(width, height)
	test.draw()
	#Update the screen
	pygame.display.flip()
	pygame.display.update()
	#Delay to get 30 fps
	clock.tick(30)
