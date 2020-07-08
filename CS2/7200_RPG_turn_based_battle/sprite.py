import pygame, colors, random, action

def getNextAttribute(file_handle):
	line = file_handle.readline()
	line = line.rstrip()
	return int(line.split(':')[1])



class Sprite:
	#Constructor
	def __init__(self, text_file, sprite_sheet, screen, flip):
		'''Create a sprite.'''
		file_handle = open(text_file, 'r')
		
		line = file_handle.readline()
		line = line.rstrip()
		self.name = line.split(':')[1]
		
		x = getNextAttribute(file_handle)
		y = getNextAttribute(file_handle)
		width = getNextAttribute(file_handle)
		height = getNextAttribute(file_handle)
		
		self.base_health = getNextAttribute(file_handle)
		self.health = getNextAttribute(file_handle)
		self.health_change = getNextAttribute(file_handle)
		self.base_offense = getNextAttribute(file_handle)
		self.offense = getNextAttribute(file_handle)
		self.offense_change = getNextAttribute(file_handle)
		self.base_defense = getNextAttribute(file_handle)
		self.defense = getNextAttribute(file_handle)
		self.defense_change = getNextAttribute(file_handle)
		self.base_accuracy = getNextAttribute(file_handle)
		self.accuracy = getNextAttribute(file_handle)
		self.accuracy_change = getNextAttribute(file_handle)
		self.base_evasion = getNextAttribute(file_handle)
		self.evasion = getNextAttribute(file_handle)
		self.evasion_change = getNextAttribute(file_handle)
		self.base_crit_chance = getNextAttribute(file_handle)
		self.crit_chance = getNextAttribute(file_handle)
		self.crit_chance_change = getNextAttribute(file_handle)
		self.base_crit_percent = getNextAttribute(file_handle)
		self.crit_percent = getNextAttribute(file_handle)
		self.crit_percent_change = getNextAttribute(file_handle)
		self.base_debuff_resist = getNextAttribute(file_handle)
		self.debuff_resist = getNextAttribute(file_handle)
		self.debuff_resist_change = getNextAttribute(file_handle)
		self.base_stealth = getNextAttribute(file_handle)
		self.stealth = getNextAttribute(file_handle)
		self.stealth_change = getNextAttribute(file_handle)
		self.base_perception = getNextAttribute(file_handle)
		self.perception = getNextAttribute(file_handle)
		self.perception_change = getNextAttribute(file_handle)
		self.base_cooldown = getNextAttribute(file_handle)
		self.cooldown = getNextAttribute(file_handle)
		self.cooldown = random.randint(0, self.base_cooldown) #TESTING
		self.cooldown_change = getNextAttribute(file_handle)
		self.level = getNextAttribute(file_handle)
		
		line = file_handle.readline()
		line = line.rstrip()
		self.action1 = action.Action('actions/'+line.split(':')[1]+'.txt')
		line = file_handle.readline()
		line = line.rstrip()
		self.action2 = action.Action('actions/'+line.split(':')[1]+'.txt')

		self.screen = screen
		self.image = sprite_sheet.subsurface(pygame.Rect((x,y), (width,height)))
		#Scale up the image
		scaling = 3
		self.image = pygame.transform.scale(self.image,(width*scaling,height*scaling))
		#Flip the image horizontally
		if flip:
			self.image = pygame.transform.flip(self.image, True, False)
		#Make drawing this image more efficient
		self.image = self.image.convert()
		#Make the white pixels transparent
		self.image.set_colorkey((255,255,255))
		self.rect = self.image.get_rect()
		#Whether or not this character is currently selected
		self.selected = False
	
	
	def getCenterX(self):
		return self.rect.x + self.rect.width/2
	
	
	def getCenterY(self):
		return self.rect.y + self.rect.height/2
	

	def getMaxHealth(self):
		return self.base_health + self.level * self.health_change
	
	
	def getMaxCooldown(self):
		return self.base_cooldown + self.level * self.cooldown_change
	
	
	def draw(self):
		''''''
		#Only draw living characters
		if self.health <= 0:
			return 
		if self.selected:
			#Draw a glow behind the image
			for i in range(10):
				shift = (35-3*i)
				cvalue = 255-shift*7
				color = (cvalue, cvalue, cvalue)
				pygame.draw.ellipse(self.screen, color,
					[self.rect.x-shift, #x
					self.rect.y-shift, #y
					self.rect.width+shift*2, #width
					self.rect.height+shift*2]) #height
		#Draw the image
		self.screen.blit(self.image, self.rect)
		#Draw the health bars
		'''Health display: rectangles each one representing 200 health. green. if below 25% red, elif below 50% yellow.'''
		#rectangle_health determines the number of health
		#rectangles to display in the health bar, 
		#in order to indicate higher health levels visually
		rectangle_health = 200
		max_health = self.getMaxHealth()
		num_rectangles = max(1,int(max_health/rectangle_health))
		width = 100
		height = 20
		rect_width = width/num_rectangles
		health_color = colors.green
		if self.health/max_health < 0.25:
			health_color = colors.red
		elif self.health/max_health < 0.5:
			health_color = colors.yellow
		health_rect = pygame.Rect(
					self.rect.x, 
					self.rect.y+self.rect.height, 
					int(width*(self.health/max_health)),
					height)
		pygame.draw.rect(self.screen,
						health_color,
						health_rect)
		#draw the frames
		for i in range(num_rectangles):
			pygame.draw.rect(self.screen,
					colors.gray,
					pygame.Rect(
						self.rect.x+rect_width*i, 
						self.rect.y+self.rect.height, 
						rect_width, 	
						height),
					1) #edge thickness
		#Draw the cooldown bar
		cooldown_rect = pygame.Rect(
					self.rect.x, 
					self.rect.y+self.rect.height+height, 
					int(width*(self.cooldown/self.getMaxCooldown())),
					height)
		pygame.draw.rect(self.screen,
						colors.cyan,
						cooldown_rect)
		#draw the frame
		cooldown_rect.width = width
		pygame.draw.rect(self.screen,
						colors.gray,
						cooldown_rect,
						1) #edge thickness
