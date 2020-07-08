import turtle, random

screen = turtle.getscreen()
screen.colormode(255)

angle_range = 50
depth = 7
branch_length = 50
pensize = 20
thinning = 3
red = 165
green = 42
blue = 42
d_red = -22
d_green = 27
d_blue = -5

#Sanity check
limit = thinning*depth
print('Branch width will ultimately be '+str(limit))
if limit >= pensize:
    print('ERROR: thinning*depth must be less than pensize')
limit = red+d_red*depth
print('Red will ultimately be '+str(limit))
if limit > 255 or limit < 0:
    print('ERROR: red out of bounds')
    turtle.done()
limit = green+d_green*depth
print('Green will ultimately be '+str(limit))
if limit > 255 or limit < 0:
    print('ERROR: green out of bounds')
    turtle.done()
limit = blue+d_blue*depth
print('Blue will ultimately be '+str(limit))
if limit > 255 or limit < 0:
    print('ERROR: blue out of bounds')
    turtle.done()

new_turtle1 = turtle.Turtle()
new_turtle1.penup()
new_turtle1.setheading(90)
new_turtle1.color((red,green,blue))
new_turtle1.pensize(pensize)
new_turtle1.goto(0,-200)
new_turtle1.pendown()

def getChild(parent, cur_depth, left):
    heading = parent.heading()
    child = turtle.Turtle()
    child.penup()
    rand_int = random.randint(0,angle_range)
    if left:
        child.setheading(heading-rand_int)
    else:
        child.setheading(heading+rand_int)
    child.setx(parent.xcor())
    child.sety(parent.ycor())
    c = (red+i*d_red, green+i*d_green, blue+i*d_blue)
    child.color(c)
    #TODO
    #Get color of parent so the branches' color can vary
    #print(new_turtle2.color())
    #print(new_turtle2.color()[0])
    #print()
    child.pensize(pensize-cur_depth*thinning)
    child.pendown()
    return child

turtles = []
turtles.append(new_turtle1)
for i in range(depth):
    new_turtles = []
    for t in turtles:
        t.forward(branch_length)
        new_turtle1 = getChild(t, i, True)
        new_turtle2 = getChild(t, i, False)
        new_turtles.append(new_turtle1)
        new_turtles.append(new_turtle2)
    turtles = new_turtles
turtle.done()