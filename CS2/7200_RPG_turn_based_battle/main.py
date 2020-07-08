import pygame, sprite, colors, game_manager

pygame.init()

screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

gm = game_manager.GameManager(screen)

#Draw all images on the screen
done = False
while not done:
	#Handle events and inputs
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.KEYDOWN:
			#Press enter to attack with current character
			if event.key == pygame.K_RETURN:
				gm.startAnimation()
			#Press escape to quit
			elif event.key == pygame.K_ESCAPE:
				done = True
	screen.fill(colors.black)
	gm.update()
	gm.draw()
	pygame.display.flip()
	#Delay to get 60 fps
	clock.tick(60)
pygame.quit()