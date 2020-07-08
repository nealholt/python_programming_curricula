import pygame, math, random

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
		self.sides = random.randint(5,12)
		self.max_radius = 60
		self.radii = []
		for i in range(self.sides):
			self.radii.append(random.randint(40,self.max_radius))
		self.line_thickness = 2
		self.angle = 0
		self.rotation_rate = math.pi/256
	
	def move(self, border_right, border_bottom):
		#Rotate a little
		self.angle = (self.angle + self.rotation_rate) % (math.pi*2)
		#Move dx and dy
		self.x += self.dx
		self.y += self.dy
		#print(self.x)
		if self.x+self.max_radius < 0:
			self.x += border_right
		elif self.x > border_right:
			self.x -= border_right
		if self.y+self.max_radius < 0:
			self.y += border_bottom
		elif self.y > border_bottom:
			self.y -= border_bottom
	
	def draw(self):
		point_list = []
		for i in range(self.sides):
			angle = self.angle+math.pi*2*(i/self.sides)
			x = self.x + math.cos(angle)*self.radii[i]
			y = self.y + math.sin(angle)*self.radii[i]
			point_list.append([x, y])
		pygame.draw.polygon(self.surface, white, point_list, self.line_thickness)




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
