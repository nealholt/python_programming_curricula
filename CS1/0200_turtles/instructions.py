'''Read the following guide to learn how to write turtle code.

turtle is a python library that makes it easy to draw on the
screen. To get started using turtle we need to import turtle.'''
import turtle
'''import is a Python command that lets us use code that
someone else has written. By calling import turtle we give
ourselves access to functions in the turtle library.

Use the following code to create a new turtle:'''
tom = turtle.Turtle()
'''The name of the variable referring to our turtle is tom
but we could have named our turtle variable almost anything.

Common names are the letter t, or pen, brush, or pencil because
the turtle is frequently used like a writing implement.

You can change the shape of the turtle with the shape command.
Your options include: arrow, circle, square, triangle, classic
or, of course, turtle.'''
tom.shape("turtle")
'''You can tell a turtle to move forward with the following command.
Change the number in parentheses to change how far the turtle moves.'''
tom.forward(100)
'''The turtle's speed can be changed like so. Confusingly the top speed
is 0. So, from slowest to fastest, the speeds are 1,2,3,4,5,6,7,8,9,10,0'''
tom.speed(5)
'''If you don't want your turtle to draw, simply lift up its pen.'''
tom.penup() #no drawing when moving.
tom.goto(0,100) #go to x,y coordinates 0,100
'''To draw again, put the pen back down.'''
tom.pendown()
tom.goto(-100,30) #go to x,y coordinates -100,30
'''Draw with a thicker or thinner pen.'''
tom.pensize(8)
tom.backward(150) #turtles can move forward or backward
'''Change the pen's color.'''
tom.color('green')
'''Change the direction the turtle is facing. The number in parentheses
is in degrees from 0 to 360.'''
tom.left(45) #Turn left 45 degrees
tom.forward(50)
tom.right(90) #Turn right 45 degrees
'''The turtle can also be told to face a particular direction, again
in degrees.'''
tom.setheading(90) #Turn tom to face 90 degrees (North)
'''As you have already seen, the goto command sends the turtle to a
particular location given a horizontal x coordinate and a vertical
y coordinate.'''
tom.goto(250, -50)
'''The turtle screen will close before you can see the art your
turtle has made unless you declare that you are done.
IMPORTANT: note that this is turtle.done() NOT tom.done()'''
turtle.done()