
import random

def functionToMaximize(inputs):
    total = 0
    if len(inputs)!=10:
        return total
    weights = [6,2,3,6,8,3,2,2,5,4]
    for i in range(len(inputs)):
        total = total - inputs[i]**2 + inputs[i]*weights[i]
    total += inputs[0]*inputs[7]/2+inputs[4]*inputs[8]/2
    return total*1000000

