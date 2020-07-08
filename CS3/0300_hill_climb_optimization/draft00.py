'''
Introduce students to the idea of hill climbing optimization
and simulated annealing.
'''
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

def mutate(inputs):
    r = random.randint(0,len(inputs)-1)
    inputs[r] += random.random()*2-1

time_steps = 200000
best = []
for _ in range(10):
    best.append(random.random()*5)
fitness = functionToMaximize(best)
print(fitness)

for _ in range(time_steps):
    c = best.copy()
    mutate(c)
    c_fit = functionToMaximize(c)
    if c_fit > fitness:
        best = c
        fitness = c_fit
        print(fitness)

print(best)
print(fitness)