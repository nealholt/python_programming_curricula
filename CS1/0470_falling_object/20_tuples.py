''' For 18 points, answer the following questions about tuples.

1) In the following three-line program, what do you get when you print
coordinate?

2) What do you get when you print coordinate[0]?

3) What do you get when you print coordinate[1]?

4) What happens if you try to increase the first part of
coordinate like this:
    coordinate[0] = coordinate[0]+1   ? '''
x = 3
y = 7
coordinate = (x,y)

'''Pairs, also known as tuples, are groups of numbers that
cannot be changed as easily as lists. The following program
demonstrates how to increase the x coordinate by one.
You don't need to answer any question for this part.'''
coordinate = (3,7)
x,y = coordinate
coordinate = (x+1,y)
print(coordinate)

'''The following program makes a list and puts coordinates in it.
5) Modify this program to print out each coordinate on separate lines.'''
import random
coordinates = []
for i in range(10):
    x = random.randint(0,100)
    y = random.randint(0,100)
    coordinates.append((x,y))

'''The following program modifies all of the coordinates
by adding one to their x values.
6) Print out all the coordinates before and after to confirm
this is working correctly.'''
import random
coordinates = []
for i in range(10):
    x = random.randint(0,100)
    y = random.randint(0,100)
    coordinates.append((x,y))
#Increase all x coordinates
for i in range(len(coordinates)):
    x,y = coordinates[i]
    coordinates[i] = (x+1,y)

'''The following program modifies all of the x and y
coordinates randomly, but consistently. Notice the
second list and how it is used.
7) What's the purpose of the first of the two for loops?

8) Write code to print the coordinates before and after the change.
'''
import random
coordinates = []
changes = []
for i in range(10):
    x = random.randint(0,100)
    y = random.randint(0,100)
    coordinates.append((x,y))
    change_x = random.randint(-5,5)
    change_y = random.randint(-5,5)
    changes.append((change_x,change_y))
#Change all x coordinates
for i in range(len(coordinates)):
    x,y = coordinates[i]
    change_x,change_y = changes[i]
    coordinates[i] = (x+change_x, y+change_y)
