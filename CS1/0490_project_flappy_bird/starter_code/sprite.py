import pygame

class Sprite:
	def __init__(self, x, y, image_file, screen):
		#Create a Sprite object
		self.dx = 1
		self.dy = 1
		self.screen = screen
		self.image = pygame.image.load(image_file)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def moveAmount(self, amountx, amounty):
		#Move this sprite the specified amounts
		self.rect.x = self.rect.x + amountx
		self.rect.y = self.rect.y + amounty

	def setLocation(self, x, y):
		#Set the location of this sprite to the given x and y values
		self.rect.x = x
		self.rect.y = y

	def collided(self, other_sprite):
		#Return true if self collided with other_sprite
		return self.rect.colliderect(other_sprite.rect)

	def draw(self):
		#Draw this sprite on the screen
		self.screen.blit(self.image, self.rect)
