import turtle, random

'''
TODO:
walk back and forth over each branch three times to create the layered look that exists in the image

make the brown deeper.
change color to white before changing to green.
vary the thinning of branches randomly and have branches that thin too far simply stop
Does branch length vary over time or stay the same? seems like it might decrease.
How much can you simplify this? Make a recursive version?
Incorporate a random seed so these are replicable.

You could have a student-written genetic algorithm too.
'''

#Don't update the screen until the very end. This will greatly speed things up.
#https://stackoverflow.com/questions/16119991/how-to-speed-up-pythons-turtle-function-and-stop-it-freezing-at-the-end
turtle.tracer(0, 0)

screen = turtle.getscreen()
screen.colormode(255)

angle_range = 35
depth = 9
branch_length = 50
pensize = 40
thinning = 5
thinning_random = 2
red = 165
green = 82
blue = 42
d_red = -22
d_green = 20
d_blue = -5
single_branch = 0.1 #chance of branching once, not twice
layering_factor = 2/3

'''
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
'''

new_turtle1 = turtle.Turtle()
new_turtle1.penup()
new_turtle1.setheading(90)
new_turtle1.color((red,green,blue))
new_turtle1.pensize(pensize)
new_turtle1.goto(0,-200)
new_turtle1.shape("turtle")
new_turtle1.pendown()

def getChildColor(parent):
    parent_red, parent_green, parent_blue = parent.color()[0]
    new_red = int(max(min(parent_red+i*d_red+random.randint(-4,4), 255), 0))
    new_green = int(max(min(parent_green+i*d_green+random.randint(-4,4), 255), 0))
    new_blue = int(max(min(parent_blue+i*d_blue+random.randint(-4,4), 255), 0))
    return (new_red, new_green, new_blue)

def getLayeringColor(turt):
    c = turt.color()[0]
    return (int(max(0,min(255,c[0]*layering_factor))), int(max(0,min(255,c[1]*layering_factor))), int(max(0,min(255,c[2]*layering_factor))))

def getChild(parent, left):
    heading = parent.heading()
    child = turtle.Turtle()
    child.penup()
    child.shape("turtle")
    rand_int = random.randint(0,angle_range)
    if left:
        child.setheading(heading-rand_int)
    else:
        child.setheading(heading+rand_int)
    child.setx(parent.xcor())
    child.sety(parent.ycor())
    child.color(getChildColor(parent))
    new_pensize = parent.pensize()-thinning-random.randint(0,thinning_random)
    if new_pensize <= 0:
        new_pensize = 1
    child.pensize(new_pensize)
    child.pendown()
    return child

turtles = []
turtles.append(new_turtle1)
for i in range(depth):
    new_turtles = []
    for t in turtles:
        #Only grow the branch if the branch thickness supports it
        if t.pensize() > 1:
            #Draw the branch
            t.forward(branch_length)
            #Create first child to continue the branch
            direction = random.random()>0.5
            new_turtle1 = getChild(t, direction)
            new_turtles.append(new_turtle1)
            #Chance to have single branch instead of two forking branches
            if random.random()>single_branch:
                new_turtle2 = getChild(t, not direction)
                new_turtles.append(new_turtle2)
            #Create layered effect by changing color and walking back over
            #same branch twice more
            t.pensize(int(max(1,t.pensize()*3/4)))
            t.color(getLayeringColor(t))
            t.backward(branch_length)
            t.pensize(int(max(1,t.pensize()*3/4)))
            t.color(getLayeringColor(t))
            t.forward(branch_length)
    turtles = new_turtles
#Refresh the screen
turtle.update()
turtle.done()