import pygame

class TextSplash:
	def __init__(self, surface, text, color, size, x, y, timeout, dy=-15, gravity=0.8):
		self.surface = surface
		self.text = text
		self.x = x
		self.y = y
		self.dy = dy
		self.gravity = gravity
		self.color = color
		self.timeout = timeout
		self.font = pygame.font.SysFont('Arial', size)
	
	
	def draw(self):
		self.surface.blit(self.font.render(self.text,
					True,self.color), (self.x, self.y))
	
	
	def move(self):
		self.y = self.y + self.dy
		self.dy = self.dy + self.gravity
		self.timeout -= 1

