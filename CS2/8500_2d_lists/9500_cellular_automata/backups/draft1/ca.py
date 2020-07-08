
import pygame
from cell import *
import sys

#First the default values:
input_file = 'input_test.txt'
grid_wrap = True

#Check for user defined input:
if len(sys.argv) > 1:
	input_file = sys.argv[1]
if len(sys.argv) > 2:
	grid_wrap = (1==int(sys.argv[2]))




#Read in a grid of ones and zeroes separated by spaces and line breaks.
#Return a 2-d list of ones and zeroes. 
f = open(input_file, 'r')
init = []
i=0
for line in f:
	init.append([])
	#Remove trailing newline then split on tabs.
	line = line.rstrip("\n")
	temp = line.split(" ")
	for t in temp:
		init[i].append(int(t))
	i = i+1
f.close

#Get max width and height of the grid.
grid_width = len(init[0])
grid_height = len(init)

#Display the pygame view screen
w = 500
h = 500
screen = pygame.display.set_mode((w, h))
black = 0,0,0
screen.fill(black)

#Create clock and run condition
clock = pygame.time.Clock()
running = True

#Populate the grid
grid = []
for r in range(grid_height):
	grid.append([])
	for c in range(grid_width):
		#Cell(surface, column, row, strategy)
		cell = Cell(screen, c, r, init[r][c])
		cell.draw(True) #TODO for now display payoff
		grid[r].append(cell)

#Define neighbor relationships
for r in range(grid_height):
	for c in range(grid_width):
		left = c-1
		right = c+1
		above = r-1
		below = r+1

		cur_cell = grid[r][c]

		#Make allowances for grid wrapping:
		if grid_wrap:
			if left < 0: left = grid_width-1
			right = right % grid_width
			if above < 0: above = grid_height-1
			below = below % grid_height

		#Set neighbors, but be sure to check border conditions.
		if above >= 0:
			if left >= 0: cur_cell.addNeighbor(grid[above][left])
			cur_cell.addNeighbor(grid[above][c])
			if right < grid_width: cur_cell.addNeighbor(grid[above][right])

		if left >= 0: cur_cell.addNeighbor(grid[r][left])
		if right < grid_width: cur_cell.addNeighbor(grid[r][right])

		if below < grid_height:
			if left >= 0: cur_cell.addNeighbor(grid[below][left])
			cur_cell.addNeighbor(grid[below][c])
			if right < grid_width: cur_cell.addNeighbor(grid[below][right])


#Test a neighborhood in the center:
pygame.display.flip()
pygame.time.wait(1000)
grid[3][3].neighborhoodTest()
#Test a neighborhood on the left corner:
pygame.time.wait(1000)
grid[0][0].neighborhoodTest()
#Test a neighborhood on the right corner:
pygame.time.wait(1000)
grid[grid_height-1][grid_width-1].neighborhoodTest()


while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	#pygame.time.wait(50)

	pygame.display.flip()
	clock.tick(240)
