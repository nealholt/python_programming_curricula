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

class Cell:
	def __init__(self, surface, column, row, strategy, rect_width, rect_height):
		self.surface = surface
		self.row = row
		self.column = column

		self.rect_width = rect_width
		self.rect_height = rect_height

		self.x = column*self.rect_width
		self.y = row*self.rect_height
		self.rect = pygame.Rect(self.x, self.y, self.rect_width, self.rect_height)

		self.neighbors = []

		self.strategy = strategy #Either one or zero for cooperate or defect
		self.payoff=0
		self.next_strategy = strategy #aka value after update

		self.color = defect_color
		self.update() #This will set this node's color correctly.

	def draw(self, draw_payoff=False):
		#Use frame view for now to count cells.
		#self.surface.fill(self.color, self.rect)
		pygame.draw.rect(self.surface, self.color, self.rect, 3) #Edge thickness of 3
		if draw_payoff:
			#Display payoff
			text=fontMed.render(str(self.payoff),1,white)
			self.surface.blit(text, (self.x, self.y))
		return

	def addNeighbor(self, n):
		self.neighbors.append(n)
		return

	def surveyNeighbors(self):
		'''Survey neighbors for the highest payoff strategy and set that to be my next strategy.
		In the event of a tie, majority rules. If there is still a tie, remain the same.'''
		#Create two variables to tally votes in terms of a tie, and third variable to remember the tieing payoff.
		tie_payoff = self.payoff
		coop_votes = 0
		defect_votes = 0

		best_payoff = self.payoff #My payoff is the best one seen so far.
		best_strategy = self.strategy

		#Put in one vote for self payoff.
		if self.strategy == COOP:
			coop_votes = 1
			defect_votes = 0
		else:
			coop_votes = 0
			defect_votes = 1

		for n in self.neighbors:
			if n.payoff > best_payoff:
				best_payoff = n.payoff
				best_strategy = n.getStrategy()
				#reset the tie variables:
				tie_payoff = best_payoff
				if n.strategy == COOP:
					coop_votes = 1
					defect_votes = 0
				else:
					coop_votes = 0
					defect_votes = 1
			elif n.payoff == best_payoff:
				if n.strategy == COOP: coop_votes = coop_votes + 1
				else: defect_votes = defect_votes + 1
		#Set the strategy to adopt to be the best one seen.
		#If there is a tie, majority rules.
		if coop_votes > defect_votes:
			self.next_strategy = COOP
		elif coop_votes < defect_votes:
			self.next_strategy = DEFECT
		else:
			self.next_strategy = self.strategy

		#Testing revert back to old method to test the glider:
		#Nope, still doesn't seem to work.
		#self.next_strategy = best_strategy

		#if coop_votes > 0 and defect_votes > 0: #TESTING
		#	print('tie breaker. coop votes: '+str(coop_votes)+'. defect votes: '+str(defect_votes)+'. new strategy: '+str(self.next_strategy))


	def update(self):
		'''Update my strategy to next_strategy, reset payoff, and 
		set my color correctly. '''
		self.strategy = self.next_strategy
		#set color:
		if self.isCooperator():
			self.color = coop_color
		else:
			self.color = defect_color
		return

	def getStrategy(self):
		return self.strategy

	def isCooperator(self):
		return self.strategy == COOP

	def calculatePayoff(self,coopcoop,defccoop,coopdefc,defcdefc):
		'''Interact with neighbors to get payoff.'''
		#Reset  payoff to zero.
		self.payoff = 0
		for n in self.neighbors:
			if self.strategy and n.getStrategy(): #Both cooperate
				self.payoff = self.payoff + coopcoop
			elif self.strategy: #I cooperate and neighbor defects
				self.payoff = self.payoff + coopdefc
			elif n.getStrategy(): #I defect and neighbor cooperates
				self.payoff = self.payoff + defccoop
			else: #We both defect
				self.payoff = self.payoff + defcdefc

		#Also play game against self:
		if self.strategy == COOP:
			self.payoff = self.payoff + coopcoop
		elif self.strategy == DEFECT:
			self.payoff = self.payoff + defcdefc
		else:
			print('ERROR: WHAT IS MY STRATEGY? "'+str(self.strategy)+'"')

		#If there are less than 8 neighbors then we are on an edge and
		#the grid is set to not wrap. Add in average values for the
		#phantom neighbors.
		if len(self.neighbors) < 8:
			average = float(self.payoff) / len(self.neighbors)
			for i in range(len(self.neighbors), 8):
				self.payoff = self.payoff + average
			self.payoff = int(self.payoff)
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

