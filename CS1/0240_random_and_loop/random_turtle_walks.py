'''
For 70 points, write a program that draws some abstract piece of
art using loops, functions, and a little randomness.

Below are 5 different examples of how to make turtles move as well
as an important function called "seed" that lets you make your
randomness repeatable.

You must make significant changes to the following code for full
credit. You must also put any repeated patterns into functions
and use comments to describe the purpose of the functions.
'''


import turtle, random

'''IMPORTANT: You can repeat the behavior of your random numbers
by first setting the seed with the following command.
Meaning that no matter how many times I run this program, I
will always get the same result, but if I change 7 to a different
number, I will get a different result.'''
random.seed(7)

pen = turtle.Turtle()
pen.speed(0)
pen.pensize(4)
pen.setheading(random.randint(0,360))
pen.color('red')


#EXAMPLE 1
#Turn more with each loop
turn_amt = 0
for i in range(100):
    pen.forward(4)
    pen.right(turn_amt)
    turn_amt = turn_amt + 0.1


#EXAMPLE 2
#Turn more or turn less randomly
pen.penup()
pen.goto(0,0)
pen.pendown()
pen.color('blue')
for i in range(100):
    pen.forward(4)
    pen.right(turn_amt)
    turn_amt = turn_amt + random.randint(-1,1)


#EXAMPLE 3
#Turn a random amount each loop. This turtle wanders.
pen.penup()
pen.goto(0,0)
pen.pendown()
pen.color('green')
for i in range(100):
    pen.forward(4)
    pen.right(random.randint(-30,30))


#EXAMPLE 4
#Face a random direction and move that way.
pen.penup()
pen.goto(0,0)
pen.pendown()
pen.color('yellow')
for i in range(100):
    pen.forward(50)
    pen.setheading(random.randint(0,360))


#EXAMPLE 5
#Dotted line.
pen.penup()
pen.goto(0,0)
pen.pendown()
pen.color('black')
for i in range(10):
    pen.forward(10)
    pen.penup()
    pen.forward(10)
    pen.pendown()


turtle.done()