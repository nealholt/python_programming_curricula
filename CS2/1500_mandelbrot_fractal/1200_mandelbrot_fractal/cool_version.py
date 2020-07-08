import pygame, math, colors

'''This version contains a bigger, more detailed fractal, and some efficiency
improvements.'''

pygame.init()
width = 1100
height = 650
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

max_iterations = 25

'''
left_border = -2
right_border = 2
bottom_border = -2
top_border = 2
'''
#Zoom in on more interesting section of fractal
left_border = -2
right_border = -1.5
bottom_border = -.5
top_border = .5


fractal_width = right_border - left_border
fractal_height = top_border - bottom_border

#Save time by storing fractal_width/width
a_constant = fractal_width/width
b_constant = fractal_height/height
for x in range(width):
    for y in range(height):
        a_start = x*a_constant+left_border
        b_start = y*b_constant+bottom_border
        #Since there is always at least one iteration, start on the
        #first iteration
        a = a_start
        b = b_start
        iterations = 0
        while a*a+b*b<4 and iterations<max_iterations:
            a = a_start + a*a - b*b
            b = b_start + 2*a*b
            iterations += 1
        #depending on the number of iterations, color a pixel.
        #Use gray scale 0,0,0 through 250,250,250
        screen.set_at((x,y), (iterations*10,iterations*10,iterations*10))

#Update the screen
pygame.display.flip()

#Main loop
done = False
while not done:
    #Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
    #Delay to get 10 fps
    clock.tick(10)
pygame.quit()
