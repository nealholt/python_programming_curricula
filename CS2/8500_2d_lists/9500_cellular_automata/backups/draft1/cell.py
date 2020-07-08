import pygame

pygame.font.init()
fontMed=pygame.font.Font(None,30)

DEFECT = 0
COOP = 1

red = 255, 0, 0
blue = 0, 0, 255
green = 0, 255, 0
white = 255, 255, 255

defect_color = red
coop_color = blue

rect_height = 20
rect_width = 20

class Cell:
	def __init__(self, surface, column, row, strategy):
		self.surface = surface
		self.row = row
		self.column = column

		self.x = column*rect_width
		self.y = row*rect_height
		self.rect = pygame.Rect(self.x, self.y, rect_width, rect_height)

		self.neighbors = []

		self.strategy = strategy #Either one or zero for cooperate or defect
		self.payoff=0
		self.next_strategy = strategy #aka value after update

		self.color = defect_color
		if self.strategy == COOP:
			self.color = coop_color

	def draw(self, draw_payoff=False):
		self.surface.fill(self.color, self.rect)
		if draw_payoff:
			text=fontMed.render(str(self.payoff),1,white)
			self.surface.blit(text, (self.x, self.y))
		return

	def addNeighbor(self, n):
		self.neighbors.append(n)
		return

	def update(self):
		return

	def getPayoff(self):
		'''Interact with neighbors to get payoff.'''
		return

	def neighborhoodTest(self):
		'''Flash self and all neighbors green briefly. '''
		original_colors = []
		for n in self.neighbors:
			original_colors.append(n.color)
			n.color = green
			n.draw()
		original_colors.append(self.color)
		self.draw()
		pygame.display.flip()
		pygame.time.wait(1000)
		#Revert to original colors
		for i in range(len(self.neighbors)):
			n = self.neighbors[i]
			n.color = original_colors[i]
			n.draw()
		self.color = original_colors[len(original_colors)-1]
		self.draw()
		pygame.display.flip()

