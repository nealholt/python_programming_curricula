import turtle, random

'''
TODO:
DONE 1. Make a little tree as a step toward genetic algorithm.
DONE 2. Add a seed
3. Put all the parameters in a list.
4. produce a couple rows of trees with random parameters
5. make it so you can click to further evolve a particular tree.

How much can you simplify this? Make a recursive version?
Incorporate a random seed so these are replicable.
'''

#Don't update the screen until the very end. This will greatly speed things up.
#https://stackoverflow.com/questions/16119991/how-to-speed-up-pythons-turtle-function-and-stop-it-freezing-at-the-end
turtle.tracer(0, 0)

screen = turtle.getscreen()
screen.colormode(255)

#Change screen dimensions
screen.setup (width=800, height=650, startx=500, starty=0)

seed = 9428
min_angle_range = 15
angle_range = 35
angle_range_increase = 2
depth = 10
branch_length = 10#80
length_decrease = 0.4#4
pensize = 5#50
thinning = 0.3#3
thinning_random = 0.6#6
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

turtle.hideturtle()

random.seed(seed)

def getChildColor(parent, depth):
    i = depth
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
    child.hideturtle()
    child.penup()
    child.clear()
    #child.shape("turtle")
    #Increase the angle range as depth increases
    rand_int = random.randint(min_angle_range,angle_range+angle_range_increase*depth)
    if left:
        child.setheading(heading-rand_int)
    else:
        child.setheading(heading+rand_int)
    child.setx(parent.xcor())
    child.sety(parent.ycor())
    child.color(getChildColor(parent, depth))
    temp = int(thinning_random)
    rand_temp = 0
    if temp>0:
        rand_temp = random.randint(0,thinning_random)
    new_pensize = parent.pensize()-thinning-rand_temp
    if new_pensize <= 0:
        new_pensize = 1
    child.pensize(new_pensize)
    child.pendown()
    return child

def makeTree(startx, starty):
    new_turtle1 = turtle.Turtle()
    new_turtle1.penup()
    new_turtle1.clear()
    new_turtle1.setheading(90)
    new_turtle1.color((red,green,blue))
    new_turtle1.pensize(pensize)
    new_turtle1.goto(startx, starty)
    #new_turtle1.shape("turtle")
    new_turtle1.hideturtle()
    new_turtle1.pendown()
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

makeTree(0,-270)
#Refresh the screen
turtle.update()
turtle.done()