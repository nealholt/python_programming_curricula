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
		self.radius = 5
		self.rect = pygame.Rect(self.x,self.y, self.radius*2, self.radius*2)
	
	def move(self, border_right, border_bottom):
		self.x += self.dx
		self.y += self.dy
		#print(self.x)
		if self.x+self.radius < 0:
			self.x += border_right
		elif self.x > border_right:
			self.x -= border_right
		if self.y+self.radius < 0:
			self.y += border_bottom
		elif self.y > border_bottom:
			self.y -= border_bottom
		self.rect = pygame.Rect(self.x,self.y, self.radius*2, self.radius*2)
	
	def draw(self):
		pygame.draw.ellipse(self.surface, white, self.rect)


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
