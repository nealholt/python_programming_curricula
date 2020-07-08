import pygame

class Sprite:
	#Constructor
	def __init__(self, x, y, image_file, screen):
		'''Create a sprite.'''
		self.dx = 1
		self.dy = 1
		self.screen = screen
		self.image = pygame.image.load(image_file)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def moveAmount(self, amountx, amounty):
		self.rect.x = self.rect.x + amountx
		self.rect.y = self.rect.y + amounty

	def move(self):
		'''Move this sprite. Bounce off the
		edges of the screen.'''
		self.rect = self.rect.move((self.dx, self.dy))
		width, height = self.screen.get_size()
		if self.rect.left < 0 or self.rect.right > width:
			self.dx = -self.dx
		if self.rect.top < 0 or self.rect.bottom > height:
			self.dy = -self.dy

	def setLocation(self, x, y):
		self.rect.x = x
		self.rect.y = y

	def collided(self, other_sprite):
		if self.rect.colliderect(other_sprite.rect):
			return True
		else:
			return False

	def draw(self):
		self.screen.blit(self.image, self.rect)
