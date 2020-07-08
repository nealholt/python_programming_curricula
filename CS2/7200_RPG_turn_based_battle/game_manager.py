import pygame, sprite, random, text_splash, colors

class GameManager:
	#Constructor
	def __init__(self, screen):
		sprite_sheet = pygame.image.load('enemy_sprite_sheet.png')
		self.screen = screen

		#Create the player's characters
		self.player_characters = []
		for i in range(5):
			character = sprite.Sprite('characters/syclich.txt', sprite_sheet, screen, False)
			self.player_characters.append(character)

		#Set player characters in position
		player_back_row_x = 50
		player_back_row_y = 300
		player_rise = 200
		player_run = 50
		for i in range(2):
			self.player_characters[i].rect.x = player_back_row_x + i*player_run
			self.player_characters[i].rect.y = player_back_row_y - i*player_rise
		player_front_row_x = 200
		player_front_row_y = 500
		for i in range(2,5):
			self.player_characters[i].rect.x = player_front_row_x + (i-2)*player_run
			self.player_characters[i].rect.y = player_front_row_y - (i-2)*player_rise

		#Create enemy characters
		self.enemy_characters = []
		for i in range(5):
			character = sprite.Sprite('characters/lobo.txt', sprite_sheet, screen, True)
			self.enemy_characters.append(character)

		#Select first enemy character
		self.selected_index = 0
		self.enemy_characters[self.selected_index].selected = True

		#Set enemy characters in position
		enemy_back_row_x = 950
		enemy_back_row_y = 300
		enemy_rise = 200
		enemy_run = -50
		for i in range(2):
			self.enemy_characters[i].rect.x = enemy_back_row_x + i*enemy_run
			self.enemy_characters[i].rect.y = enemy_back_row_y - i*enemy_rise
		enemy_front_row_x = 800
		enemy_front_row_y = 500
		for i in range(2,5):
			self.enemy_characters[i].rect.x = enemy_front_row_x + (i-2)*enemy_run
			self.enemy_characters[i].rect.y = enemy_front_row_y - (i-2)*enemy_rise
		
		#Variables to keep track of animation
		self.animating = False
		self.animation_phase = 0
		self.animation_countdown = 0
		self.target_coords = (0,0)
		self.target = None
		self.animation_list = []
	
	
	def update(self):
		selected = self.getSelected()
		#Perform animation
		if self.animating:
			self.animate()
		#If a player is selected, wait for 
		#player to select an action
		elif selected in self.player_characters:
			pass #TODO?
		else:
			#enemy attacks
			self.startAnimation()
	
	
	def attack(self, attacker):
		#TODO temporary function for performing attacks
		#Get random target that is still alive
		target = None
		if attacker in self.player_characters:
			while target == None or target.health <= 0:
				target = random.choice(self.enemy_characters)
		else:
			while target == None or target.health <= 0:
				target = random.choice(self.player_characters)
		#Check for evasion
		'''Dodge / Evade calculation:
		chance to evade = evasion - (enemy accuracy-100)
		Example: evasion = 27  acc = 97
			chance to evade = 27-(97-100) = 30%
		Example: evasion = 10  acc = 105
			chance to evade = 10-(105-100) = 5%  '''
		chance_to_evade = target.evasion - (attacker.accuracy-100)
		if random.randint(0,100) < chance_to_evade:
			self.animation_list.append(
				text_splash.TextSplash(self.screen, "DODGE", colors.white, 40, #Size
				target.getCenterX(), target.getCenterY(), 50) #Timeout
			)
			return None
		#Deal damage
		'''Damage calculation:
		if not evaded:
			if crit chance:
				damage = max(1, offense*crit_percent-defense)
			else:
				damage = max(1, offense-defense)  '''
		if random.randint(0,100) < attacker.crit_chance:
			damage = max(1, int(attacker.offense * (1+attacker.crit_percent/100)) - target.defense)
			#Animate the critical hit
			self.animation_list.append(
					text_splash.TextSplash(self.screen, "CRITICAL", colors.yellow, 40,
					target.getCenterX(), target.getCenterY()+30, 50))
		else:
			damage = max(1, attacker.offense - target.defense)
		target.health -= damage
		#Animate the damage
		self.animation_list.append(
				text_splash.TextSplash(self.screen, str(-damage), colors.red, 40, #Size
				target.getCenterX(), target.getCenterY(), 50) #Timeout
			)
		#Return the target for animation purposes
		return target
	
	
	def startAnimation(self):
		#Only trigger an animation if one is not currently in progress
		if not self.animating:
			self.animating = True
			self.animation_phase = 3
			self.animation_countdown = 30
	
	
	def animate(self):
		selected = self.getSelected()
		#Attacker steps forward
		if self.animation_phase == 3:
			#Players and enemies step "forward"
			#in different directions
			if selected in self.player_characters:
				selected.rect.x += 2
			else:
				selected.rect.x -= 2
		#Attacker pauses and attacks (deals damage)
		elif self.animation_phase == 2:
			#This if makes it only attack once.
			if self.animation_countdown == 30:
				self.target = self.attack(selected)
				if self.target != None:
					self.target_coords = (self.target.rect.x,
										self.target.rect.y)
			#Jiggle the target to show it got hit
			if self.target != None:
				self.target.rect.x = self.target_coords[0]\
									+random.randint(-20,20)
				self.target.rect.y = self.target_coords[1]\
									+random.randint(-20,20)
		#Attacker steps back
		elif self.animation_phase == 1:
			#Put target back in original location
			if self.target != None:
				self.target.rect.x = self.target_coords[0]
				self.target.rect.y = self.target_coords[1]
			#Players and enemies step "backward"
			#in different directions
			if selected in self.player_characters:
				selected.rect.x -= 2
			else:
				selected.rect.x += 2
		#Cease animating
		else:
			self.animating = False
			self.target_coords = (0,0)
			self.target = None
			#Reset cooldown of selected
			selected.cooldown = selected.getMaxCooldown()
			#See who goes next
			self.advanceCooldown()
		#Countdown to end of animation
		self.animation_countdown -= 1
		if self.animation_countdown == 0:
			self.animation_phase -= 1
			self.animation_countdown = 30
	
	
	def advanceCooldown(self):
		#Loop through all cooldowns, finding the lowest one
		least_cool = 999999999
		temp_list = self.player_characters+self.enemy_characters
		for t in temp_list:
			#Only check living characters
			if t.health > 0 and t.cooldown < least_cool:
				least_cool = t.cooldown
		#Decrement all cooldowns by the lowest amount
		for t in temp_list:
			t.cooldown = t.cooldown - least_cool
			#Change which character is selected to be the
			#one with zero cooldown
			if t.health > 0 and t.cooldown == 0:
				self.deselect() #deselect current
				t.selected = True
				self.selected_index = self.getIndexOf(t)


	def draw(self):
		#Draw player's characters
		for p in reversed(self.player_characters):
			p.draw()
		#Draw enemy's characters
		for e in reversed(self.enemy_characters):
			e.draw()
		#Animate and draw animations
		for i in reversed(range(len(self.animation_list))):
			self.animation_list[i].move()
			if self.animation_list[i].timeout < 0:
				del self.animation_list[i]
			else:
				self.animation_list[i].draw()
	
	
	def getIndexOf(self, character):
		for i in range(len(self.player_characters)):
			if character == self.player_characters[i]:
				return i
		for i in range(len(self.enemy_characters)):
			if character == self.enemy_characters[i]:
				return i
		print("ERROR in GameManager.getIndexOf")
		exit()
	
	
	def deselect(self):
		self.player_characters[self.selected_index].selected = False
		self.enemy_characters[self.selected_index].selected = False
	
	
	def getSelected(self):
		'''Returns the selected character.'''
		if self.player_characters[self.selected_index].selected:
			return self.player_characters[self.selected_index]
		else:
			return self.enemy_characters[self.selected_index]

