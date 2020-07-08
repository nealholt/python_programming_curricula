import pygame, random, math

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
		self.dx = 0
		self.dy = 0
		self.color = color
		self.radius = radius

	def move(self):
		self.x += self.dx
		self.y += self.dy
		if self.x<0:
			self.x=0
			self.dx = -self.dx
		elif self.x+self.radius*2 > self.surface.get_width():
			self.x=self.surface.get_width()-self.radius*2
			self.dx = -self.dx
		if self.y<0:
			self.y=0
			self.dy = -self.dy
		elif self.y+self.radius*2 > self.surface.get_height():
			self.y=self.surface.get_height()-self.radius*2
			self.dy = -self.dy


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


ball = Blob(screen,
			ORANGE,
			250, #x
			250, #y
			40) #radius




#Create platorms
platform_list = []
r = pygame.Rect(50,100,100, 100)
platform_list.append(Platform(screen, ORANGE, r))

running = True
while running:
	#Fill the screen with black
	screen.fill(BLACK)
	hippo.move()
	#Check for collision with platform
	for p in platform_list:
		if p.rect.colliderect(hippo.getRect()):
			pass
	#Draw the "hippo"
	hippo.draw()
	ball.draw()
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
	if keys[pygame.K_UP]:
		hippo.dy -= 0.1
	if keys[pygame.K_DOWN]:
		hippo.dy += 0.1
	if keys[pygame.K_LEFT]:
		hippo.dx -= 0.1
	if keys[pygame.K_RIGHT]:
		hippo.dx += 0.1
	#Update screen display
	pygame.display.flip()
	#Delay to get 60 fps
	clock.tick(60)
pygame.quit()