import pygame, math

pygame.init()

'''TODO next steps:
	1 smooth moving and rotations with booleans
	2 keep initially separate then make a third project integrating this with maze navigator.
'''

class DiepCritter:
	def __init__(self, surface, x, y, radius):
		self.surface = surface
		self.color = blue
		self.x = x+radius #center x
		self.y = y+radius #center y
		self.angle = 0
		self.radius = radius
		self.rect = pygame.Rect(self.x-self.radius,
								self.y-self.radius,
								self.radius*2,
								self.radius*2)
	
	def move(self):
		self.x += math.cos(self.angle)*20
		self.y += math.sin(self.angle)*20
		self.rect = pygame.Rect(self.x-self.radius,
								self.y-self.radius,
								self.radius*2,
								self.radius*2)
	
	def rotate(self, turn_rate):
		self.angle += turn_rate
	
	def draw(self):
		pygame.draw.ellipse(self.surface, self.color, self.rect)
		#Draw little heading circle
		heading_radius = 10
		heading = pygame.Rect(	self.x-heading_radius+math.cos(self.angle)*100,
								self.y-heading_radius+math.sin(self.angle)*100,
								heading_radius*2,
								heading_radius*2)
		pygame.draw.ellipse(self.surface, self.color, heading)


#Initialize variables:
clock = pygame.time.Clock()
surface = pygame.display.set_mode((600,600))
green = 0,255,0
red = 255,0,0
blue = 0,0,255
yellow = 255,255,0
white = 255,255,255
black = 0,0,0
critter = DiepCritter(	surface,
						100,#x
						100,#y
						50)#radius

#Main program loop
done = False
while not done:
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.KEYDOWN:
			#print(event.key) #Print value of key press
			if event.key == pygame.K_ESCAPE:
				done = True
			elif event.key == pygame.K_RIGHT:
				critter.rotate(math.pi/32)
			elif event.key == pygame.K_LEFT:
				critter.rotate(-math.pi/32)
			elif event.key == pygame.K_UP:
				critter.move()
			elif event.key == pygame.K_DOWN:
				critter.color = yellow
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				critter.color = green
			elif event.key == pygame.K_LEFT:
				critter.color = red
			elif event.key == pygame.K_UP:
				critter.color = yellow
			elif event.key == pygame.K_DOWN:
				critter.color = blue

	surface.fill((0,0,0)) #fill surface with black
	critter.draw()
	pygame.display.flip()
	pygame.display.update()
	#Delay to get 30 fps
	clock.tick(30)
	