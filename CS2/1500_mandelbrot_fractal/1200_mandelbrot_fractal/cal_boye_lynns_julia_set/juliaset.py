#Mandelbrot Code
import math, pygame

#Z(n+1) = Z(n) + C

def createColorPallet(limit_num):
    #Creates a color pallet using
    color_list = []
    for i in range(limit_num):
        color_list.append((0, ((255 * (i + 1))/limit_num), 0))

    return color_list


def squareImaginaryNum(real, imaginary):
    realpart = (real ** 2) - (imaginary ** 2)
    imaginarypart = 2 * real * imaginary

    return [realpart, imaginarypart]

def checkForDivergence(real, imaginary, constant_real, constant_imag, stop):
    temp_real = real
    temp_imag = imaginary
    times = 0
    while math.sqrt(temp_real ** 2 + temp_imag ** 2) <= 2 and times < stop:
        num = squareImaginaryNum(temp_real, temp_imag)
        temp_real = num[0] + constant_real
        temp_imag = num[1] + constant_imag
        times = times + 1
    return times

con_div_list = []

limit = int(input("What's the cutoff point for converg/diverg checking?"))
c_r = float(input("cr (Typically between -1 and 1) A good value is -0.5"))
c_i = float(input("ci (Typically between -0.5 and 0.5) A good value is -0.75"))

colors = createColorPallet(limit)

for i in range(-400, 400):
    temp_list = []
    for j in range(-400, 400):
        temp_list.append(checkForDivergence(i/200, j/200, c_r, c_i, limit))
    con_div_list.append(temp_list)

pygame.init()

width = 800
height = 800
screen = pygame.display.set_mode((width, height))

quit = False

while quit != "Yes" and quit != "yes":
    for i in range(len(con_div_list)):
        for j in range(len(con_div_list[i])):
            screen.set_at((i, j), colors[con_div_list[i][j] - 1])

    pygame.display.update()
    quit = str(input("Do you want to quit?"))
pygame.quit()