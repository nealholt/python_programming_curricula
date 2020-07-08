import pygame

class Sprite:
	def __init__(self, x, y, image_file, screen):
		self.dx = 1
		self.dy = 1
		self.screen = screen
		self.image = pygame.image.load(image_file)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def move(self):
		self.rect = self.rect.move((self.dx, self.dy))
		width, height = self.screen.get_size()
		if self.rect.left < 0 or self.rect.right > width:
			self.dx = -self.dx
		if self.rect.top < 0 or self.rect.bottom > height:
			self.dy = -self.dy

	def draw(self):
		self.screen.blit(self.image, self.rect)
