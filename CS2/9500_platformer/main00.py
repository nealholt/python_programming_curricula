import pygame, random, math

gravity = 0.8

class blob:
	def __init__(self, surface, color, x, y, radius):
		self.surface = surface
		#x and y are the center of this object
		self.x = x
		self.y = y
		self.dy = 0
		self.color = color
		self.radius = radius

	def draw(self):
		pygame.draw.ellipse(self.surface,
			self.color, 
			[self.x-self.radius, #x
			self.y-self.radius, #y
			self.radius*2, #width
			self.radius*2]) #height

	def shoveUp(self, other):
		'''Shove other up until self and other are not touching.'''
		while self.touched(other):
			other.y = other.y-0.01
			other.dy = 0



BLACK = (0,0,0)
WHITE = (255,255,255)
ORANGE = (255,100,0)

#Width and height of the screen are both 500
width = 500
height = 500
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

#Put large blob in center of the screen
hippo = blob(screen,
			WHITE,
			250, #x
			250, #y
			15) #radius

running = True
while running:
	#Fill the screen with black
	screen.fill(BLACK)
	#Make hippo fall
	hippo.dy = hippo.dy + gravity
	hippo.y = hippo.y + hippo.dy
	#Keep hippo on screen
	if hippo.y+hippo.radius*2 > height:
		hippo.y = height-hippo.radius*2
		hippo.dy = 0
	#Draw the "hippo"
	hippo.draw()
	#Respond to events such as closing the game or moving the hippo
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False
	keys = pygame.key.get_pressed()
	#The second condition checks to see if the hippo is on the ground.
	if keys[pygame.K_UP] and hippo.y == height-hippo.radius*2:
		hippo.dy = hippo.dy-20
	if keys[pygame.K_LEFT]:
		hippo.x = hippo.x-2
	if keys[pygame.K_RIGHT]:
		hippo.x = hippo.x+2
	#Update screen display
	pygame.display.flip()
	#Delay to get 60 fps
	clock.tick(60)
