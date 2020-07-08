
import pygame


def getInitialConditions():
	'''Read in a grid of ones and zeroes separated by spaces and line breaks.
	Return a 2-d list of ones and zeroes. '''
	f = open('input_test.txt', 'r')

	initial = []
	i=0
	for line in f:
		initial.append([])
		#Remove trailing newline then split on tabs.
		line = line.rstrip("\n")
		temp = line.split(" ")
		for t in temp:
			initial[i].append(int(t))
		i = i+1

	f.close
	return initial


red = 255, 0, 0
blue = 0, 0, 255
black = 0,0,0

w = 500
h = 500

screen = pygame.display.set_mode((w, h))
screen.fill(black)
clock = pygame.time.Clock()
running = True

rect_height = 20
rect_width = 20

init = getInitialConditions()
for r in range(len(init)):
	for c in range(len(init[r])):
		rect1 = pygame.Rect(c*rect_width, r*rect_height, rect_width, rect_height)
		color = red
		if init[r][c] == 1:
			color=blue
		pygame.draw.rect(screen, color, rect1, 1) #last argument is thickness of outer edge.
		screen.fill(color, rect1)




while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	#pygame.time.wait(50)

	pygame.display.flip()
	clock.tick(240)
