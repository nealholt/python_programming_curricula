import pygame, time, math

def squareNum(a, b):
    a = a**2
    b = (b**2)*-1
    c = 2*a*b
    a = a+b
    return a, c


def processNum(x, y, a, b):
    a = x+a
    b = y+b
    return a, b

def allOfIt(x, y, a, b):
    tempx = a*a - b*b + x
    tempy = 2*a*b + y
    return(tempx, tempy)

def findDistance(x, y):
    return ((x)**2+(y)**2)

def getColor(i):

    i = i/100
    blue = 0
    red = math.sin(i-(math.pi/2))+1
    if i > (math.pi/2):
        red = math.sin((math.pi/2)-(math.pi/2))+1
        blue = math.sin(i-(math.pi/2))

    green = math.sin(i)
    if i > (math.pi):
        green = 0
        red = -(math.sin(i-(math.pi)))+1


    red = (red/2)*255
    green = (green/2)*255
    blue = (blue/2)*255
    return (red, green, blue)


surface = pygame.display.set_mode((1440,900))

r = 255
b = 0
g = 0

display_x = 1
display_y = 1

A = 0
B = 0

white = (255, 255, 255)
red = (255,0,0)
lightred = (200, 0, 0)
dred = (220, 20, 60)
orange = (255, 165, 0)
yellow = (255, 255, 0)
green = (0, 255, 64)
blue = (0, 0, 255)
lpurple = (148,0,211)
purple = (255, 0, 255)
dpurple = (139,0,139)
black = (0,0,0)

colorlist = [white, lightred, red, dred, orange, yellow, green, blue, dpurple, purple, lpurple, black]


screen_width = 1000
screen_height = 1000
fractal_xmin = -2
fractal_xmax = 2
fractal_ymin = -2
fractal_ymax = 2
fractal_width = fractal_xmax-fractal_xmin
fractal_height = fractal_ymax-fractal_ymin
x = fractal_xmin
y = fractal_ymin
distance = 0
counter =0
increase =0.005
limit = int(150*math.pi)

for display_x in range(screen_height):
    x = ((display_x/screen_width)*fractal_width)+fractal_xmin
    for display_y in range(screen_width):
        counter = 0
        #y = ((y-fractal_ymin)/fractal_height)*(screen_height)
        y = ((display_y/screen_height)*fractal_height)+fractal_ymin

        A, B = allOfIt(x, y, 0, 0)
        distance = findDistance(A, B)
        while distance <= 4 and counter <= limit:
            counter = counter + 1
            A, B = allOfIt(x, y, A, B)
            distance = findDistance(A, B)
        surface.set_at((display_x,display_y), getColor(counter))

    pygame.display.flip()


pygame.quit()