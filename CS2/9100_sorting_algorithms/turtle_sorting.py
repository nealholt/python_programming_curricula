import turtle, random

#Make random list of numbers
sizes = []
limit = 9
for i in range(1,limit):
    sizes.append(i)
random.shuffle(sizes)

print(sizes)

#Make corresponding list of turtles.
turtles = []
for i in range(len(sizes)):
    t = turtle.Turtle()
    t.shape("turtle")
    t.shapesize(sizes[i],sizes[i])
    t.color(sizes[i]/limit,0,sizes[i]/limit)
    t.penup()
    t.goto(-600+140*i, 0)
    t.speed(1) #Slow down for easier viewing
    turtles.append(t)

def sortDone(sizes):
    '''Returns true if sorting is complete'''
    for i in range(len(sizes)-1):
        if sizes[i] > sizes[i+1]:
            return False
    return True

def swapTurtles(a, b):
    '''Swaps locations of turtles a and b.'''
    temp_x = turtles[a].xcor()
    temp_y = turtles[a].ycor()
    turtles[a].goto(turtles[b].xcor(),turtles[b].ycor())
    turtles[b].goto(temp_x, temp_y)
    #Swap the turtles in the list too
    temp = turtles[a]
    turtles[a] = turtles[b]
    turtles[b] = temp


comparisons = 0
while not sortDone(sizes):
    #Do a pass of bubble sort
    '''for i in range(len(sizes)-1):
        comparisons += 1
        if sizes[i] > sizes[i+1]:
            temp = sizes[i]
            sizes[i] = sizes[i+1]
            sizes[i+1] = temp
            swapTurtles(i, i+1)'''
    #Insertion sort
    i = 0
    while i < len(sizes)-1:
        comparisons += 1
        if sizes[i] > sizes[i+1]:
            temp = sizes[i]
            sizes[i] = sizes[i+1]
            sizes[i+1] = temp
            swapTurtles(i, i+1)
            #sort backward
            j = i-1
            while j > 0:
                comparisons += 1
                if sizes[j] > sizes[j+1]:
                    temp = sizes[j]
                    sizes[j] = sizes[j+1]
                    sizes[j+1] = temp
                    swapTurtles(j, j+1)
                else:
                    break
                j = j-1
        i = i+1


print("It took "+str(comparisons)+" comparisons to sort the list.")
print(sizes)
turtle.done()