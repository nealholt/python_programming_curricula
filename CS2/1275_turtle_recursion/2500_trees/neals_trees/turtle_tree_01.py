import turtle, random

screen = turtle.getscreen()
screen.colormode(255)

angle_range = 50
depth = 5
branch_length = 50
pensize = 20
thinning = 3 #thinning*depth must be greater than pensize
red = 165
green = 42
blue = 42

new_turtle1 = turtle.Turtle()
new_turtle1.penup()
new_turtle1.setheading(90)
new_turtle1.color((red,green,blue))
new_turtle1.pensize(pensize)
new_turtle1.goto(0,-200)
new_turtle1.pendown()

turtles = []
turtles.append(new_turtle1)
for i in range(depth):
    new_turtles = []
    for t in turtles:
        t.forward(branch_length)
        heading = t.heading()
        new_turtle1 = turtle.Turtle()
        new_turtle2 = turtle.Turtle()
        new_turtle1.penup()
        new_turtle2.penup()
        new_turtle1.setheading(heading+random.randint(-angle_range,angle_range))
        new_turtle2.setheading(heading+random.randint(-angle_range,angle_range))
        new_turtle1.setx(t.xcor())
        new_turtle2.setx(t.xcor())
        new_turtle1.sety(t.ycor())
        new_turtle2.sety(t.ycor())
        new_turtle1.color((red-i*30, green+i*30, blue-i*5))
        new_turtle2.color((red-i*30, green+i*30, blue-i*5))
        new_turtle1.pensize(pensize-i*thinning)
        new_turtle2.pensize(pensize-i*thinning)
        new_turtle1.pendown()
        new_turtle2.pendown()
        new_turtles.append(new_turtle1)
        new_turtles.append(new_turtle2)
    turtles = new_turtles
turtle.done()