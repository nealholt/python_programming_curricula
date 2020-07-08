#Mandelbrot Code
import math, pygame, time

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

def findPoints(c_r, c_i, limit):

    con_div_list = []

    colors = createColorPallet(limit)

    for i in range(-400, 400):
        temp_list = []
        for j in range(-400, 400):
            temp_list.append(checkForDivergence(i/200, j/200, c_r, c_i, limit))
        con_div_list.append(temp_list)

    return con_div_list

def drawSet(set_list):
    for i in range(len(set_list)):
        for j in range(len(set_list[i])):
            screen.set_at((i, j), colors[set_list[i][j] - 1])

    pygame.display.update()

limit = 20
c_real = float(input("cr"))
num = int(input("num"))

list_of_sets = []
colors = createColorPallet(limit)
#The constants in the "findPoints function can be changed to change the fractels
#diplayed.

for i in range(num):
    list_of_sets.append(findPoints(c_real, (i - ((num - 1)/2))/ ((num - 1)/2), limit))
    print("Done with " + str((i + 1)) + " out of " + str(num) +  "! Please be patient!")

pygame.init()

width = 800
height = 800
screen = pygame.display.set_mode((width, height))

for i in range(len(list_of_sets)):
    drawSet(list_of_sets[i])
    pygame.image.save(screen, "julia_cr" + str(c_real) + "_cineg1to1_by0,01" + str(i + 1) + "of" + str(len(list_of_sets)) + ".jpg")













