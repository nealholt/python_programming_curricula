'''
For 8 points, answer the following questions.

Rectangle objects, pygame.Rect, have their own x and y values. It seems like
we could write less code and use those x and y values when moving objects
on the screen, rather than creating separate x,y variables. Here is why
that can be risky.

1. Run this program. What does it print?

2. What is happening to the rectangle's x value that is not happening to
the x variable's value?

3. Suppose we have an object in Pygame that we are representing with a
Rect and we are moving the Rect at a speed of 3.5 pixels per frame. How
fast will the rectangle actually move?

4. What if we move a rect at 0.7 pixels per frame. How fast will the
rectangle actually move?

5. Is there any problem if the rectangle is moved a whole number of pixels
per frame?

The solution then is to keep separate x and y variables and only update the
rectangle's x and y values before drawing or checking for collisions.
'''

import pygame

#Create a rectangle
r = pygame.Rect(0,0,10,10)

#Set two x values
r.x = 3.5
x = 3.5

print(r.x)
print(x)

print()

#Add 0.1 to two x values
r.x = r.x + 0.1
x = x + 0.1

print(r.x)
print(x)

pygame.quit()