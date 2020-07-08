import pygame
pygame.init()
clock = pygame.time.Clock()

fps = 30 #Frames per second

#Import for controlling the size that tiles appear and how the robots and
#flags scale.
scaling = 0.5

font = pygame.font.SysFont('Arial', int(48*scaling))

direction_list = ['north', 'east', 'south', 'west']

#If the index of the conveyor in this list matches up
#to the index of the direction in direction_list
#then we can use index to force move players on conveyors
conveyors = ['cv1u', 'cv1r', 'cv1d', 'cv1l']
left_turn_conveyors = ['cvlu', 'cvlr', 'cvld', 'cvll', ]
right_turn_conveyors = ['cvru', 'cvrr', 'cvrd', 'cvrl', ]

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
yellow = (255,255,0)
green = (0,255,0)
blue = (0,0,255)

#Used to control stepping through turns with the space bar
step_forward = False

initial_width = 144
initial_height = 144

tile_width = int(initial_width*scaling)
tile_height = int(initial_height*scaling)

