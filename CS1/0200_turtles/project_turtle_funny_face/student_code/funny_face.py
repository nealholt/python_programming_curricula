#Example program follows.
#Copy this code into a new python file then run it.
​import turtle, time

#Create and name a variable for the turtle
tommy = turtle.Turtle()
tommy.shape("turtle")

#All our circles will be this size
size = 50

#Draw the right eye
tommy.penup()
tommy.color("blue")
tommy.fillcolor("blue")
tommy.goto(200,70)
tommy.begin_fill()
tommy.pendown()
tommy.circle(size)
tommy.penup()
tommy.end_fill()

#Draw the left eye
tommy.penup()
tommy.color("blue")
tommy.fillcolor("blue")
tommy.goto(0,70)
tommy.begin_fill()
tommy.pendown()
tommy.circle(size)
tommy.penup()
tommy.end_fill()

#Draw the smile
tommy.penup()
tommy.color("black")
tommy.goto(50,0)
tommy.setheading(-45)
tommy.pensize(10)
tommy.pendown()
tommy.fd(5)
tommy.left(5)
tommy.fd(5)
tommy.left(5)
tommy.fd(5)
tommy.left(5)
tommy.fd(5)
tommy.left(5)
tommy.fd(5)
tommy.left(5)
tommy.fd(5)
tommy.left(5)
tommy.fd(5)
tommy.left(5)
tommy.fd(5)
tommy.left(5)
tommy.fd(5)
tommy.left(5)
tommy.fd(5)
tommy.left(5)
tommy.fd(5)
tommy.left(5)
tommy.fd(5)
tommy.left(5)
tommy.fd(5)
tommy.left(5)
tommy.fd(5)
tommy.left(5)
tommy.fd(5)
tommy.left(5)
tommy.fd(5)
tommy.left(5)
tommy.fd(5)
tommy.left(5)
tommy.fd(5)
tommy.left(5)
tommy.fd(5)
tommy.left(5)
tommy.fd(5)
tommy.left(5)

time.sleep(4) #Wait some number of seconds to see the result​