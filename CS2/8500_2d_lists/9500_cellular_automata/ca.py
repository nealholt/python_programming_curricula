#Run with: python ca.py input_file.txt gridwrap? output_frames? pause_between_frames?
#Example: python ca.py input_file.txt 1 1 1

import pygame
import numpy as np
import matplotlib.pyplot as plt
import sys
from cell import *

#First the default values:
input_file = 'input_test.txt'
grid_wrap = True
#Payoff values:
#    C  D
# C  a  c
# D  b  d

coopcoop = 1
defccoop = 1.9
coopdefc = 0
defcdefc = 0

#Settings for hawks and doves questions:
#coopcoop = 31
#defccoop = 50
#coopdefc = 20
#defcdefc = 10

#Pause between generations for this many milliseconds
pause = 100

#Whether or not to make an image output of each time step.
output_frames =False
frame_counter=0

#Whether or not to pause completely between frames
pause_between_frames=False

#Check for user defined input:
if len(sys.argv) > 1:
	input_file = sys.argv[1]
if len(sys.argv) > 2:
	grid_wrap = (1==int(sys.argv[2]))
if len(sys.argv) > 3:
	output_frames = (1==int(sys.argv[3]))
if len(sys.argv) > 4:
	pause_between_frames = (1==int(sys.argv[4]))


#Store a count of cooperators and defectors in the population in order 
#to view the dynamics of how these change over time.
c_count = 0
d_count = 0
strat_proportions = []


#Read in a grid of ones and zeroes separated by spaces and line breaks.
#Return a 2-d list of ones and zeroes. 
f = open(input_file, 'r')
init = []
for line in f:
	init.append([])
	#Remove trailing newline then split on tabs.
	line = line.rstrip("\n")
	line = line.split(" ")
	init[-1] = [int(t) for t in line]
f.close

#Get max width and height of the grid.
grid_width = len(init[0])
grid_height = len(init)

#Display the pygame view screen
#dynamically size it:
rect_width = 500/grid_width
rect_height = 500/grid_height
w = grid_width * rect_width
h = grid_height * rect_height
screen = pygame.display.set_mode((int(w), int(h)))
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
		cell = Cell(screen, c, r, init[r][c], rect_width, rect_height)
		cell.draw()
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

def testNeighborhood():
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
	return

#testNeighborhood()

step_count = 0
step_limit = 250
while running and step_count < step_limit:
	pygame.display.flip()
	pygame.time.wait(pause)
	clock.tick(240)

	##Every few steps stop and take a picture.
	#if step_count % 10 == 0:
	#	raw_input('Step: '+str(step_count)+'. Press any key to continue...')
	#	filename = 'vis%03d.jpg' % (frame_counter)
	#	frame_counter = frame_counter + 1
	#	pygame.image.save(screen, 'images/'+filename)

	#push forward one step at a time.
	if pause_between_frames:
		raw_input('Step: '+str(step_count)+'. Press any key to continue...')

	if output_frames:
		filename = 'vis%03d.jpg' % (frame_counter)
		frame_counter = frame_counter + 1
		pygame.image.save(screen, 'images/'+filename)

	#Listen for quit command.
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	#The following do need broken out into different loops to simulate parallelism

	#Update payoff values
	#This could be done more efficiently with map function and lambda expression
	#but for now I just don't care enough.
	for r in range(grid_height):
		for c in range(grid_width):
			grid[r][c].calculatePayoff(coopcoop,defccoop,coopdefc,defcdefc)

			#Count number of each strategy in the population:
			if grid[r][c].isCooperator():
				c_count = c_count + 1
			else:
				d_count = d_count + 1
	strat_proportions.append(float(c_count)/(c_count+d_count))


	#Survey neighbors for strategy with the best payoff 
	#aka apply update rule
	#OLD WAY - Keep this for readability. Don't delete.
	#for r in range(grid_height):
	#	for c in range(grid_width):
	#		grid[r][c].surveyNeighbors()
	#NEW WAY - equivalent to old way, but faster!
	map(lambda row: map( lambda col: col.surveyNeighbors(), row), grid)


	#update
	#OLD WAY - Keep this for readability. Don't delete.
	#for r in range(grid_height):
	#	for c in range(grid_width):
	#		grid[r][c].update()
	#		grid[r][c].draw()
	#NEW WAY - equivalent to old way, but faster!
	map(lambda row: map( lambda col: col.update(), row), grid)
	map(lambda row: map( lambda col: col.draw(), row), grid)

	step_count = step_count +1


##print results
#print 
#for p in strat_proportions:
#	print p
#print 


#display chart
plt.figure(1)
plt.plot(strat_proportions,'b')
plt.title('Percentage of Cooperators in the Population')
plt.xlabel('Time step')
plt.show()


#Print final frame
pygame.image.save(screen, 'images/final_frame.jpg')

