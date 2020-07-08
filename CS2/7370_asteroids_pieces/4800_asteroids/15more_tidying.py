import pygame, math, random

#Setup
pygame.init()
width = 900
height = 600
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 48)
black = 0,0,0
white = 255,255,255
red = 255,0,0


class GameManager:
	def __init__(self, screen, width, height):
		self.screen_width = width
		self.screen_height = height
		#Create randomized asteroids
		self.asteroid_list = []
		min_dx = -2
		max_dx = 2
		for i in range(10):
			x = random.randint(0, width)
			y = random.randint(0, height)
			dx = random.random()*(max_dx-min_dx)+min_dx
			dy = random.random()*(max_dx-min_dx)+min_dx
			self.asteroid_list.append(Asteroid(screen,x,y,dx,dy))
		#Create player
		self.player = Ship(screen, 20, 20)
		#Create bullet list
		self.bullet_list = []

	def update(self, width, height):
		#Move and draw
		for item in self.asteroid_list:
			item.move(self.screen_width, self.screen_height)
			item.draw()
		for item in self.bullet_list:
			item.move(self.screen_width, self.screen_height)
			item.draw()
		self.player.move(self.screen_width, self.screen_height)
		self.player.draw()
		#Remove dead items
		for i in reversed(range(len(self.asteroid_list))):
			if self.asteroid_list[i].remove:
				del self.asteroid_list[i]
		for i in reversed(range(len(self.bullet_list))):
			if self.bullet_list[i].remove:
				del self.bullet_list[i]
	
	def shoot(self, screen):
		#Shoot
		x = self.player.x+math.cos(self.player.angle)*self.player.radius
		y = self.player.y+math.sin(self.player.angle)*self.player.radius
		b = Bullet(screen, x, y, self.player.angle)
		self.bullet_list.append(b)



class Bullet:
	def __init__(self, surface, x, y, angle):
		self.surface = surface
		self.x = x
		self.y = y
		speed = 10
		self.dx = math.cos(angle)*speed
		self.dy = math.sin(angle)*speed
		self.radius = 4
		self.timeout = 90 #frames the bullet will last for
		self.remove = False
	
	def move(self, border_right, border_bottom):
		#Move dx and dy
		self.x += self.dx
		self.y += self.dy
		#Screen wrap
		if self.x+self.radius < 0:
			self.x += border_right
		elif self.x > border_right:
			self.x -= border_right
		if self.y+self.radius < 0:
			self.y += border_bottom
		elif self.y > border_bottom:
			self.y -= border_bottom
	
	def draw(self):
		r = pygame.Rect(self.x-self.radius/2,
						self.y-self.radius/2,
						self.radius,self.radius)
		pygame.draw.ellipse(self.surface, white, r)
		#countdown to removal of bullets
		self.timeout -= 1
		self.remove = self.timeout <= 0




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
		self.lives = 1
		self.remove = False
	
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



class Asteroid:
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
			temp = random.randint(40,self.max_radius)
			self.radii.append(temp)
		self.line_thickness = 2
		self.angle = 0
		#Randomly rotate +-math.pi/256 per frame
		self.rotation_rate = random.random()*math.pi/128
		self.rotation_rate = self.rotation_rate-math.pi/256
		self.remove = False
	
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



def userInputToPlayer(player):
	keys = pygame.key.get_pressed()
	if keys[pygame.K_UP]:
		player.thrust()
	if keys[pygame.K_LEFT]:
		player.rotateLeft()
	if keys[pygame.K_RIGHT]:
		player.rotateRight()



#Create game manager object to manage updating and moving everything
gm = GameManager(screen, width, height)


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
			if event.key == pygame.K_SPACE:
				gm.shoot(screen)
	if gm.player.lives > 0:
		userInputToPlayer(gm.player)
		#fill screen with black
		screen.fill(black)
		gm.update(width, height)
	else:
		#Draw Game Over
		position = (width/2-100, height/2-20)
		screen.blit(font.render("Game Over",True,white),position)
	#Update the screen
	pygame.display.flip()
	pygame.display.update()
	#Delay to get 30 fps
	clock.tick(30)
