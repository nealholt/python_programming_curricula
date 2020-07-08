
#Answer:
import turtle
t = turtle.Turtle()
roygbiv = ['red','orange','yellow','green','blue','purple']
size = 100
for color in roygbiv:
    t.color(color)
    t.pensize(size)
    t.forward(250)
    t.backward(250)
    size -= 16

turtle.done()
