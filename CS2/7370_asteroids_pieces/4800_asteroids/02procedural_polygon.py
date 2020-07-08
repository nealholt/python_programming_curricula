import pygame, math, random

'''
Pygame: asteroids: image rotation, screen wrap, draw a shape. That's it. Build it in incremental pieces such that each sub piece could be a lesson.
For screen wrap something like if x > whatever, then set x equal to (other side of the screen)

http://learnrich.org/pygame-drawing-shapes
pygame.draw.polygon(screen, COLOUR, point list, line_thickness)
This example will draw a polygon as a line 
pygame.draw.polygon(screen, WHITE, [[100, 100], [100, 400],[400, 300]], 2)

https://www.pygame.org/docs/ref/draw.html#pygame.draw.polygon
pygame.draw.line()
draw a straight line segment
line(Surface, color, start_pos, end_pos, width=1) -> Rect

pygame.draw.ellipse()
draw a round shape inside a rectangle
ellipse(Surface, color, Rect, width=0) -> Rect
'''

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
		self.sides = random.randint(3,10)
		self.radius = 20
		self.point_list = []
		for i in range(self.sides):
			x = self.x + math.cos(math.pi*2*(i/self.sides))*self.radius
			y = self.y + math.sin(math.pi*2*(i/self.sides))*self.radius
			self.point_list.append([x, y])
		self.line_thickness = 2
	
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
	
	def draw(self):
		temp_point_list = []
		for i in range(len(self.point_list)):
			temp_point_list.append([self.point_list[i][0]+self.x,
									self.point_list[i][1]+self.y])
		pygame.draw.polygon(self.surface, white, temp_point_list, self.line_thickness)



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
