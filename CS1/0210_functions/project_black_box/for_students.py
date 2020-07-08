import math


def clearBox1(x):
    if x == math.pi:
        return 5
    else:
        return int(((1.0-math.cos(2.0*x))/2.0)**2 + math.sin(math.pi/2.0 - x)**2)+5


def clearBox2(a, b):
    if(a > b):
        return a
    else:
        return b


def clearBox3(a, b):
    return a % b


def	clearBox4(n, s):
    accumulator = ""
    for i in range(n):
        accumulator += str(s)
    return accumulator
