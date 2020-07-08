import turtle, random

screen = turtle.getscreen()
screen.colormode(255)

new_turtle1 = turtle.Turtle()
new_turtle1.penup()
new_turtle1.setheading(90)
new_turtle1.color((165,42,42))
new_turtle1.pensize(20)
new_turtle1.goto(0,-200)
new_turtle1.pendown()

angle_range = 50
depth = 5
branch_length = 50

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
        new_turtle1.color((165,42,42))
        new_turtle2.color((165,42,42))
        new_turtle1.pensize(20)
        new_turtle2.pensize(20)
        new_turtle1.pendown()
        new_turtle2.pendown()
        new_turtles.append(new_turtle1)
        new_turtles.append(new_turtle2)
    turtles = new_turtles
turtle.done()