import turtle

'''
This is the most basic tree.
Students can add many many changes.

What about having an array of colors and changing the branch color with each
increase in depth. Then changing the turtles to green at the end.

Where can randomness fit in? Maybe sometimes there is no branch, or sometimes
3 branches. Maybe the length of branches should vary.
'''

#Make the colors range from 0 to 255
screen = turtle.getscreen()
screen.colormode(255)

#Don't update the screen until the very end. This will greatly speed things up.
#https://stackoverflow.com/questions/16119991/how-to-speed-up-pythons-turtle-function-and-stop-it-freezing-at-the-end
turtle.tracer(0, 0)

#Constants that determine what sort of tree we will have.
branching_angle = 30 #angle between branches
depth = 7 #How many times the tree branches
branch_length = 50
pensize = 20 #Thickness of branches
thinning = 3 #How much thickness decreases as the tree gets closer to the top
brown = (150, 60, 30)

#Create the initial turtle to start the tree
new_turtle1 = turtle.Turtle()
new_turtle1.penup()
new_turtle1.clear()
new_turtle1.shape(None)
new_turtle1.setheading(90)
new_turtle1.color(brown)
new_turtle1.pensize(pensize)
new_turtle1.goto(0,-200)
new_turtle1.pendown()

#Create a list of turtles and put the first turtle in it
turtles = []
turtles.append(new_turtle1)
#Loop from zero to depth to create all the branches of the tree
for i in range(depth):
    #Create another list for the next generation of turtles
    new_turtles = []
    for t in turtles:
        #Move the turtle forward to create a new branch
        t.forward(branch_length)
        #Create the two new branching turtles
        new_turtle1 = turtle.Turtle()
        new_turtle2 = turtle.Turtle()
        new_turtle1.penup()
        new_turtle2.penup()
        new_turtle1.clear()
        new_turtle2.clear()
        new_turtle1.shape(None)
        new_turtle2.shape(None)
        new_turtle1.setheading(t.heading()+branching_angle)
        new_turtle2.setheading(t.heading()-branching_angle)
        new_turtle1.setx(t.xcor())
        new_turtle2.setx(t.xcor())
        new_turtle1.sety(t.ycor())
        new_turtle2.sety(t.ycor())
        new_turtle1.color(brown)
        new_turtle2.color(brown)
        new_turtle1.pensize(pensize-i*thinning)
        new_turtle2.pensize(pensize-i*thinning)
        new_turtle1.pendown()
        new_turtle2.pendown()
        #Add the branch turtles to the new_turtles list
        new_turtles.append(new_turtle1)
        new_turtles.append(new_turtle2)
    #Set the array of turtles to be all the new branches
    turtles = new_turtles
    #If this is the last iteration and turn all the turtles green
    if i==depth-1:
        for t in turtles:
            t.color((0,255,0))
            t.shape("turtle")

#Refresh the screen
turtle.update()
turtle.done()