import turtle

'''http://www.algorithm.co.il/blogs/computer-science/fractals-in-10-minutes-no-6-turtle-snowflake/
This would be a good introduction to recursion. I don't see how students
would invent this on their own, but they could modify it and see what
other fractals they could generate.
'''
pen = turtle.Turtle()
pen.penup()
pen.goto(-200,0)
pen.pendown()
pen.speed(0)

def fractal(pen, length, depth):
    #Base case
    if depth == 0:
        pen.forward(length)
    #Recursive case
    else:
        fractal(pen, length/3, depth-1)
        pen.right(60)
        fractal(pen, length/3, depth-1)
        pen.left(120)
        fractal(pen, length/3, depth-1)
        pen.right(60)
        fractal(pen, length/3, depth-1)

#Draw the fractal
fractal(pen, 500, 4)
turtle.done()
