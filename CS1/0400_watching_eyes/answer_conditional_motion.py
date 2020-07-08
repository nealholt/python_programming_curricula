import pygame

pygame.init()

#Color and eye variables
black = 0,0,0
white = 255,255,255
eye_size = 40
scaling = 1.5 #How much larger to make the image

left_eye_x_default = 733
left_eye_y_default = 347
right_eye_x_default = 869
right_eye_y_default = 324
eye_move_scaling = 20

#Load image
image = pygame.image.load('eyes_student_starter_files/images/homer.png')

#Scale up the image
rectangle = image.get_rect()
dimensions = (int(rectangle.width*scaling),
			  int(rectangle.height*scaling))
cutout_image = pygame.transform.scale(image, dimensions)

cursor_image = pygame.image.load('eyes_student_starter_files/images/donut.png')
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
	#print(pos)
	#Position eyes based on mouse movement
	left_eye_x = left_eye_x_default
	left_eye_y = left_eye_y_default
	right_eye_x = right_eye_x_default
	right_eye_y = right_eye_y_default
	#Horizontal position
	if pos[0] < 600:
		left_eye_x -= 50
		right_eye_x -= 50
	elif pos[0] > 1200:
		left_eye_x += 40
		right_eye_x += 40
	elif pos[0]<1000 and pos[0]>800:
		left_eye_x += 40
		right_eye_x -= 50
	#Vertical position
	if pos[1] < 200:
		left_eye_y -= 50
		right_eye_y -= 50
	elif pos[1] > 500:
		left_eye_y += 40
		right_eye_y += 40
	#Draw pupils
	pygame.draw.ellipse(screen, black,
					[left_eye_x,
					left_eye_y,
					eye_size, eye_size])
	pygame.draw.ellipse(screen, black,
					[right_eye_x,
					right_eye_y,
					eye_size, eye_size])
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