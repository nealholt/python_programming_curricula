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
red = 255,0,0


class Ship:
	def __init__(self, surface, x, y):
		self.surface = surface
		self.x = x
		self.y = y
		self.dx = 0
		self.dy = 0
		self.speed = 0.3
		self.sides = 3
		self.radius = 20
		self.angle = 0
		self.rotation_rate = math.pi/16
		self.thrust_on = False
	
	def rotateLeft(self):
		self.angle -= self.rotation_rate
	
	def rotateRight(self):
		self.angle += self.rotation_rate
	
	def thrust(self):
		self.dx += math.cos(self.angle)*self.speed
		self.dy += math.sin(self.angle)*self.speed
		self.thrust_on = True
	
	def move(self, border_right, border_bottom):
		#Move dx and dy
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
	
	def draw(self):
		#Draw thrust
		if self.thrust_on:
			angle = self.angle+math.pi
			x = self.x + math.cos(angle)*self.radius*0.7
			y = self.y + math.sin(angle)*self.radius*0.7
			radius = 10
			r = pygame.Rect(x-radius/2,y-radius/2,radius,radius)
			pygame.draw.ellipse(self.surface, red, r)
		#Reset thrust
		self.thrust_on = False
		#Draw outline of ship:
		points = []
		#Nose
		angle = self.angle+math.pi*2
		x = self.x + math.cos(angle)*self.radius*1.5
		y = self.y + math.sin(angle)*self.radius*1.5
		points.append([x, y])
		#wing 1
		angle = self.angle+math.pi*2*(1.2/self.sides)
		x = self.x + math.cos(angle)*self.radius
		y = self.y + math.sin(angle)*self.radius
		points.append([x, y])
		#rear
		angle = self.angle+math.pi
		x = self.x + math.cos(angle)*self.radius*0.5
		y = self.y + math.sin(angle)*self.radius*0.5
		points.append([x, y])
		#wing 2
		angle = self.angle+math.pi*2*(1.8/self.sides)
		x = self.x + math.cos(angle)*self.radius
		y = self.y + math.sin(angle)*self.radius
		points.append([x, y])
		#Draw. Note: 3 is line thickness.
		pygame.draw.polygon(self.surface, white, points,3)




test = Ship(screen, 20, 20)


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
	#Move ship
	keys = pygame.key.get_pressed()
	if keys[pygame.K_UP]:
		test.thrust()
	if keys[pygame.K_LEFT]:
		test.rotateLeft()
	if keys[pygame.K_RIGHT]:
		test.rotateRight()
	#fill screen with black
	screen.fill(black)
	test.move(width, height)
	test.draw()
	#Update the screen
	pygame.display.flip()
	pygame.display.update()
	#Delay to get 30 fps
	clock.tick(30)
