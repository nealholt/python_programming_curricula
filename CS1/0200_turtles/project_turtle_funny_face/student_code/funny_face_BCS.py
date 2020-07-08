#Brendan Clark-Slakey
#9/27/2017
# Funny Face Project
import turtle, time

#Create and name a variable for the turtle
tommy = turtle.Turtle()
tommy.shape("turtle")

#All our circles will be this size
size = 30

#Draw the right eye
tommy.penup()
tommy.color("red")
tommy.fillcolor("red")
tommy.goto(200,70)
tommy.begin_fill()
tommy.pendown()
tommy.circle(size)
tommy.penup()
tommy.end_fill()

#draw the right eyebrow
tommy.penup()
tommy.color("black")
tommy.goto(175,125)
tommy.setheading(-45)
tommy.pensize(10)
tommy.pendown()
tommy.left(75)
tommy.fd(75)

#Draw the left eye
tommy.penup()
tommy.color("red")
tommy.fillcolor("red")
tommy.goto(0,70)
tommy.pensize(1)
tommy.begin_fill()
tommy.pendown()
tommy.circle(size)
tommy.penup()
tommy.end_fill()

#draw the left eyebrow
tommy.penup()
tommy.color("black")
tommy.goto(0,125)
tommy.setheading(-45)
tommy.pensize(10)
tommy.pendown()
tommy.right(155)
tommy.fd(75)

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

#draw one of the horns
tommy.penup()
tommy.color("red")
tommy.goto(175,200)
tommy.setheading(80)
tommy.pensize(10)
tommy.pendown()
tommy.fd(50)
tommy.right(130)
tommy.fd(50)

#draw the other horn
tommy.penup()
tommy.color("red")
tommy.goto(-50,200)
tommy.setheading(60)
tommy.pensize(10)
tommy.pendown()
tommy.fd(50)
tommy.right(130)
tommy.fd(50)

#Makes turtle not visible in final product
tommy.shape("circle")
tommy.shapesize(.01)

time.sleep(4) #Wait some number of seconds to see the result?