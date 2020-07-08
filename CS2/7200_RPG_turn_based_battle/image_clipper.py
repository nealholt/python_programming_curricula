import pygame

'''NOTE TODO: There are inconsistencies in the sprite sheet's spacing. Probably best to fix the sheet itself.'''


pygame.init()

def strip_from_sheet(sheet, start, size, columns, rows=1):
	"""
	Strips individual frames from a sprite sheet given a start location,
	sprite size, and number of columns and rows.
	"""
	#7 pixels between each image along the columns
	column_step_size = 7
	#10 pixels between each image along the rows
	row_step_size = 10
	frames = []
	for j in range(rows):
		for i in range(columns):
			location = (start[0]+(size[0]+column_step_size)*i,
						start[1]+(size[1]+row_step_size)*j)
			frames.append(sheet.subsurface(pygame.Rect(location, size)))
	return frames

screen = pygame.display.set_mode((800,600))
screen_rect = screen.get_rect()
done = False
sheet = pygame.image.load('finalfantasy6sheet1.gif')
size = sheet.get_size()
character_dimensions = (16,25)
frames = strip_from_sheet(sheet,
						(11,6), #start
						character_dimensions, #size
						8, #columns
						4) #rows


#Scale up the image x4
for i in range(len(frames)):
	frames[i] = pygame.transform.scale(frames[i], (character_dimensions[0]*4,character_dimensions[1]*4))

image_index = 0

#Draw all images on the screen
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				done = True
			elif event.key == pygame.K_RIGHT:
				image_index = (image_index+1)%len(frames)
	screen.fill((0,0,0)) #fill screen with black
	for i in range(10):
		screen.blit(frames[(image_index+i)%len(frames)], (100*i,0))
	pygame.display.flip()
pygame.quit()
