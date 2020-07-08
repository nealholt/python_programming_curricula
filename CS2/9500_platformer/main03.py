import pygame, random, math

gravity = 0.8

class Platform:
	def __init__(self, surface, color, rect):
		self.surface = surface
		self.rect = rect
		self.color = color

	def draw(self):
		pygame.draw.rect(self.surface, self.color, self.rect)

	def putAbove(self, other):
		r = other.getRect()
		other.y = self.rect.y-r.height
	
	def putBelow(self, other):
		r = other.getRect()
		#Plus 1 so no more collisions occur
		other.y = self.rect.y+self.rect.height+1



class Blob:
	def __init__(self, surface, color, x, y, radius):
		self.surface = surface
		self.x = x
		self.y = y
		self.dy = 0
		self.color = color
		self.radius = radius
		
	def getRect(self):
		return pygame.Rect(self.x,
							self.y,
							self.radius*2, #width
							self.radius*2) #height

	def draw(self):
		pygame.draw.ellipse(self.surface, self.color, self.getRect())




BLACK = (0,0,0)
WHITE = (255,255,255)
ORANGE = (255,100,0)

#Width and height of the screen are both 500
width = 500
height = 500
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

#Put blob in center of the screen
hippo = Blob(screen,
			WHITE,
			250, #x
			250, #y
			15) #radius

#Create platorms
platform_list = []
r = pygame.Rect(350,250,100, 10)
platform_list.append(Platform(screen, ORANGE, r))
r = pygame.Rect(150,350,100, 10)
platform_list.append(Platform(screen, ORANGE, r))
r = pygame.Rect(150,150,100, 10)
platform_list.append(Platform(screen, ORANGE, r))

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
	#Check for collision with platform
	for p in platform_list:
		if p.rect.colliderect(hippo.getRect()):
			#Push hippo up or down
			if hippo.dy > 0: #hippo was headed down
				p.putAbove(hippo)
			else: #hippo was headed up
				p.putBelow(hippo)
			#Reset dy to zero
			hippo.dy = 0
	#Draw the "hippo"
	hippo.draw()
	for p in platform_list:
		p.draw()
	#Respond to events such as closing the game or moving the hippo
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False
	keys = pygame.key.get_pressed()
	#The second condition checks to see if the hippo is stationary
	if keys[pygame.K_UP] and hippo.dy == 0:
		hippo.dy = hippo.dy-20
	if keys[pygame.K_LEFT]:
		hippo.x = hippo.x-4
	if keys[pygame.K_RIGHT]:
		hippo.x = hippo.x+4
	#Update screen display
	pygame.display.flip()
	#Delay to get 60 fps
	clock.tick(60)
