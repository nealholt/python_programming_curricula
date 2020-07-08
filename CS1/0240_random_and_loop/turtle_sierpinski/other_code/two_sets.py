import pygame, sys, random

pygame.init()#TODO what exactly does this do?

#Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
#Surface on which to draw the game
DISPLAY_SURFACE = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

set1 = [(20,380), (300,10), (250,350)]

set2 = [(420,250), (500,390), (520,280)]

stay_chance1 = 0.5
stay_chance2 = 0.4

in_set_1 = True

white = 255, 255, 255

x = random.randint(0,SCREEN_WIDTH)
y = random.randint(0,SCREEN_HEIGHT)

#Main game loop
running = True
while running:
	
	DISPLAY_SURFACE.set_at((x, y), white)
	pygame.display.flip()

	#Decide to stay in set or transition
	if in_set_1 and random.random() > stay_chance1:
		in_set_1 = False
	elif not in_set_1 and random.random() > stay_chance2:
		in_set_1 = True
	#Select from set
	if in_set_1:
		destination = random.choice(set1)
	else:
		destination = random.choice(set2)
	
	x = int((x+destination[0])/2)
	y = int((y+destination[1])/2)
	
	#Handle events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		#The following detects left or right mouse clicks.
		#For more on pygame mouse events see: pygame.org/docs/ref/mouse.html
		elif event.type == pygame.MOUSEBUTTONDOWN:
			x, y = event.pos
			print('Mouse down at x='+str(x)+'   y='+str(y))
			(left_click, other_mouse_button, right_click) = pygame.mouse.get_pressed()
			if left_click:
				print('left click')
			if right_click:
				print('right click')
			if other_mouse_button:
				print('other mouse button click')
		#The following detects left or right mouse clicks.
		#For more on pygame mouse events see: pygame.org/docs/ref/mouse.html
		elif event.type == pygame.MOUSEBUTTONUP:
			x, y = event.pos
			print('Mouse up at   x='+str(x)+'   y='+str(y))
		#Keyboard input can be done like so:
		elif event.type == pygame.KEYDOWN:
			print("key pressed with id:"+str(event.key))
			if event.key == 27: #Escape key pressed
				running = False

pygame.quit()
sys.exit()