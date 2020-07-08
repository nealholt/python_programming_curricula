import turtle, random

#A turtle race, place your bets
turtle_list = []

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

#Create as many turtles as there are colors
i = 0
while i < len(colors):
    new_turtle = turtle.Turtle()
    new_turtle.penup()
    new_turtle.clear()
    new_turtle.shape("turtle")
    new_turtle.resizemode("auto") #Make turtle shape match size of pen
    new_turtle.pensize(10)
    #Set the color of the turtle to match up with the color in the color list
    new_turtle.color(colors[i])
    new_turtle.setheading(0)
    #Put turtle on starting line
    new_turtle.goto(-200, -180+60*i)
    #Put turtle in the list
    turtle_list.append(new_turtle)
    i = i+1

finish_line = 200
#Draw the finish line
new_turtle = turtle.Turtle()
new_turtle.penup()
new_turtle.clear()
new_turtle.goto(finish_line, 250)
new_turtle.pensize(10)
new_turtle.color('black')
new_turtle.pendown()
new_turtle.goto(finish_line, -250)

#Run the race. Move a random turtle forward each time.
finished = False
while not finished:
    #Move all the turtles
    mover = random.randint(0,len(turtle_list)-1)
    turtle_list[mover].forward(5)
    if turtle_list[mover].xcor() > finish_line:
        finished = True
        print('Winner is '+str(turtle_list[mover].color()[0]))

turtle.done()