import pygame

DEFECT = 0
COOP = 1

red = 255, 0, 0
blue = 0, 0, 255

defect_color = red
coop_color = blue

class Cell:
	def __init__(self, surface, x, y, strategy):
		self.surface = surface
		self.x = x
		self.y = y

		self.rect = pygame.Rect(x, y, rect_width, rect_height)

		self.neighbors = []

		self.strategy = strategy #Either one or zero for cooperate or defect
		self.payoff=0
		self.next_strategy = strategy #aka value after update

		self.color = defect_color
		if self.strategy == COOP:
			self.color = coop_color

	def draw(self):
		self.surface.fill(self.color, self.rect)
		return

	def update(self):
		return

	def getPayoff(self):
		'''Interact with neighbors to get payoff.'''
		return
