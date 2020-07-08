'''
The following turtle program draws an interesting pattern.

Using lists of colors, write your own turtle program to draw an interesting
pattern. Turn it in along with how many points you think it should be worth.
'''

import turtle

pen = turtle.Turtle()
pen.speed(0)
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
for x in range(200):
    pen.color(colors[x % 6])
    pen.width(x / 100 + 1)
    pen.forward(x)
    pen.left(59)

turtle.done()