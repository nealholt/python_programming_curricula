import pygame, random

class Wall:
	def __init__(self, screen):
		#Create a wall
		self.gap = 230 #Gap between the top and bottom pieces of wall
		self.width = 100 #Width of the wall
		self.screen = screen #Keep a reference to the screen for drawing
		#Set the initial location of this wall just off the 
		#right side of the screen.
		self.resetLocation()

	def collided(self, other_sprite):
		#Return true if either the top or bottom wall collided with other_sprite
		return self.toprect.colliderect(other_sprite.rect) or self.bottomrect.colliderect(other_sprite.rect)
	
	def moveAmount(self, amountx, amounty):
		#Move both pieces of wall the specified amounts
		self.toprect.x = self.toprect.x + amountx
		self.toprect.y = self.toprect.y + amounty
		self.bottomrect.x = self.bottomrect.x + amountx
		self.bottomrect.y = self.bottomrect.y + amounty
		
	def resetLocation(self):
		#Set the location of this wall just off the 
		#right side of the screen.
		width, height = self.screen.get_size()
		self.toprect = pygame.Rect(width, #x
									0, #y
									self.width, #wall width
									random.randint(0, height-self.gap)) #wall height
		self.bottomrect = pygame.Rect(width, #x
									self.toprect.height+self.gap, #y
									self.width, #wall width
									height-self.toprect.height+self.gap) #wall height

	def draw(self):
		#Draw the top and bottom walls as green rectangles
		green = (0, 255, 0)
		pygame.draw.rect(self.screen, green, self.toprect)
		pygame.draw.rect(self.screen, green, self.bottomrect)
