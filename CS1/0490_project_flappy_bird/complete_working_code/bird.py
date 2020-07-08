import pygame

class Bird:
	def __init__(self, x, y, screen):
		#Create a Bird object
		self.dy = 0
		self.screen = screen
		self.image1 = pygame.image.load('flappy1.png')
		self.image2 = pygame.image.load('flappy2.png')
		self.rect = self.image1.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.y = y
		self.image1_on = True
		self.image_countdown = 8

	def update(self):
		#Change the height of the bird by self.dy
		self.y = self.y + self.dy
		#Don't let the bird go above the top of the screen
		if self.y<0:
			self.y = 0
			self.dy = 0
		#Don't let the bird go below the bottom of the screen
		width, height = self.screen.get_size()
		if self.y>height-self.rect.height:
			self.y = height-self.rect.height
			self.dy = 0
		#Update the bird's height
		self.rect.y = self.y
		#Apply gravity to pull the bird down
		self.dy = self.dy + 0.1
		#Countdown to changing the bird's current image
		#in order to animate the flapping.
		self.image_countdown = self.image_countdown-1
		if self.image_countdown<0:
			self.image_countdown = 8
			self.image1_on = not self.image1_on

	def collided(self, other_sprite):
		#Return true if the bird collided with other_sprite
		return self.rect.colliderect(other_sprite.rect)

	def draw(self):
		#Draw the bird on the screen. Choose which image to draw
		#based on the variable self.image1_on in order to animate
		#the flapping wings
		if self.image1_on:
			self.screen.blit(self.image1, self.rect)
		else:
			self.screen.blit(self.image2, self.rect)
