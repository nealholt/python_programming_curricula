#This is a modification of Sarah Maurice's tree
#Tree
import turtle
from random import randint
turtle.tracer(0, 0)
t = turtle.Turtle()
screen= turtle.getscreen()
screen.screensize(1000,700)

tangle = 20

#creates the turtles, the branch that goes in different directions,
#the size of the turtle also set up the color of the the tree and branch
def drawTree(branchLen, size):
    if branchLen > 5:
        if branchLen < 2000:
            t.color("green")

        if size<0:
            size=1
            rsize = size
        else:
            rsize = size + 1

        t.pensize(size)
        t.forward(branchLen)
        t.right(tangle)
        drawTree(branchLen-randint(8, 15),size-1)

        t.left(2*tangle)
        drawTree(branchLen-randint(8, 15),size-1)
        t.right(tangle)

        t.pensize(rsize)
        t.color("purple")
        t.backward(branchLen)
    else:
        t.write("tree")
#creates the original turtle and move it
t.hideturtle()
t.penup()
t.color("purple")
t.pensize(10)
t.goto(-50,-300)
t.pendown()
t.left(90)
drawTree(100, 8)

turtle.done()