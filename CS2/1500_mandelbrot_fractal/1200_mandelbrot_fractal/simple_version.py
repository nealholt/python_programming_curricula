import pygame, math, colors

pygame.init()
width = 400
height = 400
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

#increasing this will give you a more detailed fractal
max_iterations = len(colors.color_list)-1

left_border = -2
right_border = 2
bottom_border = -2
top_border = 2

fractal_width = right_border - left_border
fractal_height = top_border - bottom_border

def getIterations(x,y):
    a_start = (x/width)*fractal_width+left_border
    b_start = (y/height)*fractal_height+bottom_border
    a = 0
    b = 0
    iterations = 0
    while a*a+b*b<4 and iterations<max_iterations:
        a = a_start + a*a - b*b
        b = b_start + 2*a*b
        iterations += 1
    return iterations


#Sanity check 1
if getIterations(width/2,height/2) != max_iterations:
    print('ERROR in getIterations. Point width/2,height/2 should return max_iterations')
    print('instead it returns '+str(getIterations(width/2,height/2)))
    pygame.quit(); exit()

#Sanity check 2
if getIterations(0,0) != 1:
    '''This highlights an innefficiency in the code given on stack over flow.
    It would be better if 0 was returned instead of 1, but at least
    one iteration always runs. This is fixed in "cool_version.py" '''
    print('ERROR in getIterations. Point 0,0 should return 1')
    print('instead it returns '+str(getIterations(0,0)))
    pygame.quit(); exit()

for x in range(width):
    for y in range(height):
        iterations = getIterations(x,y)
        #depending on the number of iterations, color a pixel.
        screen.set_at((x,y), colors.color_list[iterations])

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
