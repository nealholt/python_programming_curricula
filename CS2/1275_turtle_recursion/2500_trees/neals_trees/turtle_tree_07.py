import turtle, random

'''
TODO:
mess with trunk size next.
make the shape a turtle.
make the brown deeper.
walk back and forth over each branch three times to create the layered look that exists in the image
change color to white before changing to green.
vary the thinning of branches randomly and have branches that thin too far simply stop
Does branch length vary over time or stay the same? seems like it might decrease.
'''

#Don't update the screen until the very end. This will greatly speed things up.
#https://stackoverflow.com/questions/16119991/how-to-speed-up-pythons-turtle-function-and-stop-it-freezing-at-the-end
turtle.tracer(0, 0)

screen = turtle.getscreen()
screen.colormode(255)

angle_range = 35
depth = 7
branch_length = 50
pensize = 20
thinning = 3
red = 165
green = 82
blue = 42
d_red = -22
d_green = 20
d_blue = -5
single_branch = 0.1 #chance of branching once, not twice

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
    #Get color of parent so the branches' color can vary
    parent_red, parent_green, parent_blue = parent.color()[0]
    new_red = int(max(min(parent_red+i*d_red+random.randint(-4,4), 255), 0))
    new_green = int(max(min(parent_green+i*d_green+random.randint(-4,4), 255), 0))
    new_blue = int(max(min(parent_blue+i*d_blue+random.randint(-4,4), 255), 0))
    print()
    print(new_red)
    print(new_green)
    print(new_blue)
    child.color((new_red, new_green, new_blue))
    child.pensize(pensize-cur_depth*thinning)
    child.pendown()
    return child

turtles = []
turtles.append(new_turtle1)
for i in range(depth):
    new_turtles = []
    for t in turtles:
        t.forward(branch_length)
        direction = random.random()>0.5
        new_turtle1 = getChild(t, i, direction)
        if random.random()>single_branch:
            new_turtle2 = getChild(t, i, not direction)
        new_turtles.append(new_turtle1)
        new_turtles.append(new_turtle2)
    turtles = new_turtles
#Refresh the screen
turtle.update()
turtle.done()