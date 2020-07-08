import pygame

pygame.init()

#Color and eye variables
black = 0,0,0
white = 255,255,255
green = 0,255,0
eye_size = 60
scaling = 1.5 #How much larger to make the image

left_eye_x = 368
left_eye_y = 214
right_eye_x = 590
right_eye_y = 208
eye_move_scaling = 20

#Load image
image = pygame.image.load('images/cat.png')

#Scale up the image
rectangle = image.get_rect()
dimensions = (int(rectangle.width*scaling),
			  int(rectangle.height*scaling))
cutout_image = pygame.transform.scale(image, dimensions)

cursor_image = pygame.image.load('images/mouse.png')
cursor_rect = cursor_image.get_rect()

#Set the screen dimensions to fit the image perfectly.
width = dimensions[0]
height = dimensions[1]
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

#Run the main loop
done = False
while not done:
	#Handle events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				done = True
	screen.fill(white) #fill screen
	#Get mouse coordinates
	pos = pygame.mouse.get_pos()
	#Draw irises
	pygame.draw.ellipse(screen, green,
					[left_eye_x+pos[0]/eye_move_scaling,
					left_eye_y+pos[1]/eye_move_scaling,
					eye_size, eye_size])
	pygame.draw.ellipse(screen, green,
					[right_eye_x+pos[0]/eye_move_scaling,
					right_eye_y+pos[1]/eye_move_scaling,
					eye_size, eye_size])
	#Draw pupils
	pygame.draw.ellipse(screen, black,
					[left_eye_x+pos[0]/eye_move_scaling+eye_size/4,
					left_eye_y+pos[1]/eye_move_scaling,
					eye_size/2, eye_size])
	pygame.draw.ellipse(screen, black,
					[right_eye_x+pos[0]/eye_move_scaling+eye_size/4,
					right_eye_y+pos[1]/eye_move_scaling,
					eye_size/2, eye_size])
	#Draw eyes cutout image
	screen.blit(cutout_image, (0,0))
	#Draw image that follows the cursor
	screen.blit(cursor_image, (pos[0]-cursor_rect.width/2, pos[1]-cursor_rect.height/2))
	#Update screen.
	pygame.display.flip()
	pygame.display.update()
	#Delay to get 30 fps
	clock.tick(30)

pygame.quit()