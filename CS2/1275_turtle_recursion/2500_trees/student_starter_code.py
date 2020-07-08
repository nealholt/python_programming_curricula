import turtle

#This function uses multiple turtles to draw a branch.
def manyTurtleBranch(t, depth):
    #t is a turtle.
    #Depth controls how far we keep going, in other words,
    #how deep the branching goes.
    if depth > 0:
        #Draw a branch
        t.forward(50)
        #Create a new turtle at t's same location and angle
        u = turtle.Turtle()
        u.penup()
        u.setx(t.xcor())
        u.sety(t.ycor())
        u.setheading(t.heading())
        u.pendown()
        #Send t left
        t.left(20)
        manyTurtleBranch(t, depth-1)#Less deep
        #Send u right
        u.right(20)
        manyTurtleBranch(u, depth-1)#Less deep
    else:
        pass #Base case: Do nothing.


#This function uses only one turtle to draw its branches.
def singleTurtleBranch(t, depth):
    #t is a turtle.
    #Depth controls how far we keep going, in other words,
    #how deep the branching goes.
    if depth > 0:
        #Draw a branch
        t.forward(50)
        #Draw a new branch off the left
        t.left(20)
        singleTurtleBranch(t, depth-1)#Less deep
        #Draw a new branch off to the right
        t.right(40)
        singleTurtleBranch(t, depth-1)#Less deep
        #Turn back to center
        t.left(20)
        #Reverse course to end up back where we started
        t.backward(50)
    else:
        pass #Base case: Do nothing.


#Uncomment this for SPEED
#turtle.tracer(0, 0)

#Draw a branch of depth 3 with this new turtle we created.
drawer1 = turtle.Turtle()
drawer1.penup()
drawer1.goto(0,100)
drawer1.pendown()
depth = 3
singleTurtleBranch(drawer1,depth)


#Draw a branch of depth 3 with this new turtle we created.
drawer2 = turtle.Turtle()
drawer2.penup()
drawer2.goto(0,-100)
drawer2.pendown()
depth = 3
manyTurtleBranch(drawer2,depth)

turtle.update()
turtle.done()
