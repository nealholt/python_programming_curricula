import pygame

class Bullet:
	def __init__(self, surface, color, radius, x, y, dx, dy):
		self.surface = surface
		#x and y are the center of this object
		self.x = x
		self.y = y
		self.dx = dx
		self.dy = dy
		self.color = color
		self.radius = radius

	def draw(self):
		pygame.draw.ellipse(self.surface,
			self.color, 
			[self.x-self.radius, #x
			self.y-self.radius, #y
			self.radius*2, #width
			self.radius*2]) #height

	def move(self):
		self.x = self.x + self.dx
		self.y = self.y + self.dy
		self.dy = self.dy + gravity

	def distanceTo(self, other):
		'''Calculate and return distance between self and other.'''
		return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

	def touched(self, other):
		'''Return true if self touched other. Assume both are circles, then
		they touched if the distance between them is less than the sum of 
		their radii.'''
		return self.distanceTo(other) < self.radius + other.radius

