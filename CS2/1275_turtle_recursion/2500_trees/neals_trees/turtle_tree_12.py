import turtle, random

'''
TODO:
How much can you simplify this? Make a recursive version?
Incorporate a random seed so these are replicable.

You could have a student-written genetic algorithm too.
'''

#Don't update the screen until the very end. This will greatly speed things up.
#https://stackoverflow.com/questions/16119991/how-to-speed-up-pythons-turtle-function-and-stop-it-freezing-at-the-end
turtle.tracer(0, 0)

screen = turtle.getscreen()
screen.colormode(255)

#Change screen dimensions
screen.setup (width=800, height=650, startx=500, starty=0)

min_angle_range = 15
angle_range = 35
angle_range_increase = 2
depth = 10
branch_length = 80
length_decrease = 4
pensize = 50
thinning = 3
thinning_random = 6
red = 90
green = 70
blue = 30
d_red1 = 10
d_green1 = 8
d_blue1 = 4
color_change_threshold = 220*3
d_red2 = -20
d_green2 = -2
d_blue2 = -20
single_branch = 0.05 #chance of branching once, not twice
layering_factor = 2/3
rand_color_adjust = 4

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
new_turtle1.goto(0,-270)
new_turtle1.shape("turtle")
new_turtle1.pendown()

def getChildColor(parent):
    parent_red, parent_green, parent_blue = parent.color()[0]
    if parent_red + parent_green + parent_blue > color_change_threshold:
        new_red = int(max(min(parent_red+i*d_red2+random.randint(-rand_color_adjust,rand_color_adjust), 255), 0))
        new_green = int(max(min(parent_green+i*d_green2+random.randint(-rand_color_adjust,rand_color_adjust), 255), 0))
        new_blue = int(max(min(parent_blue+i*d_blue2+random.randint(-rand_color_adjust,rand_color_adjust), 255), 0))
    else:
        new_red = int(max(min(parent_red+i*d_red1+random.randint(-rand_color_adjust,rand_color_adjust), 255), 0))
        new_green = int(max(min(parent_green+i*d_green1+random.randint(-rand_color_adjust,rand_color_adjust), 255), 0))
        new_blue = int(max(min(parent_blue+i*d_blue1+random.randint(-rand_color_adjust,rand_color_adjust), 255), 0))
    return (new_red, new_green, new_blue)

def getLayeringColor(turt):
    c = turt.color()[0]
    return (int(max(0,min(255,c[0]*layering_factor))), int(max(0,min(255,c[1]*layering_factor))), int(max(0,min(255,c[2]*layering_factor))))

def getChild(parent, depth, left):
    heading = parent.heading()
    child = turtle.Turtle()
    child.penup()
    child.shape("turtle")
    #Increase the angle range as depth increases
    rand_int = random.randint(min_angle_range,angle_range+angle_range_increase*depth)
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
        if t.pensize() > 1 and branch_length-length_decrease*i > 0:
            #Draw the branch
            t.forward(branch_length-length_decrease*i)
            #Create first child to continue the branch
            direction = random.random()>0.5
            new_turtle1 = getChild(t, i, direction)
            new_turtles.append(new_turtle1)
            #Chance to have single branch instead of two forking branches
            if random.random()>single_branch:
                new_turtle2 = getChild(t, i, not direction)
                new_turtles.append(new_turtle2)
            #Create layered effect by changing color and walking back over
            #same branch twice more
            t.pensize(int(max(1,t.pensize()*3/4)))
            t.color(getLayeringColor(t))
            t.backward(branch_length-length_decrease*i)
            t.pensize(int(max(1,t.pensize()*3/4)))
            t.color(getLayeringColor(t))
            t.forward(branch_length-length_decrease*i)
    turtles = new_turtles
#Refresh the screen
turtle.update()
turtle.done()