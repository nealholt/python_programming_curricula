'''I used this as an extensive example during
lecture. It might be useful to make a video
about this.

Note: The turtle's hitbox is very small compared
tp how big the turtle appears. It might be nice
to fix that.
'''
import turtle, random, math, time

#Define most of the variables we need
eater_size = 5
screen_left = -500
screen_right = 500
screen_top = 400
screen_bottom = -400
screen_width = screen_right-screen_left
screen_height = screen_top-screen_bottom

#Make the program go fast
turtle.tracer(0,0)

#Draw a border around the screen
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(screen_left,screen_top)
pen.pendown()
pen.goto(screen_left,screen_bottom)
pen.goto(screen_right,screen_bottom)
pen.goto(screen_right,screen_top)
pen.goto(screen_left,screen_top)

#Keep the turtle within the border
def stayOnScreen(turt):
    x = turt.xcor()
    y = turt.ycor()
    if x < screen_left:
        x = x+screen_width
    if x > screen_right:
        x = x-screen_width
    if y < screen_bottom:
        y = y+screen_height
    if y > screen_top:
        y = y-screen_height
    turt.goto(x,y)

#Send the turtle to a random location within the
#border
def sendToRandom(turt):
    x = random.randint(screen_left,screen_right)
    y = random.randint(screen_bottom,screen_top)
    turt.goto(x,y)

#Move the turtle forward a little and turn it
#a little randomly.
def wander(turt):
    distance = random.randint(10,40)
    turt.forward(distance)
    turn = random.randint(-10,10)
    turt.right(turn)
    stayOnScreen(turt)

#Return the distance between the turtles
def distance(turt1, turt2):
    x_diff = turt1.xcor()-turt2.xcor()
    y_diff = turt1.ycor()-turt2.ycor()
    return math.sqrt(x_diff**2+y_diff**2)

#Check for and eat up to one turtle near the eater
def feed(eater, eatees):
    eater_size = eater.turtlesize()[0]
    for i in range(len(eatees)):
        dist = distance(eater,eatees[i])
        if dist < eater_size*3:
            eatees[i].hideturtle()
            del eatees[i]
            eater_size = eater_size+2
            eater.turtlesize(eater_size,eater_size)
            return eater_size
    return eater_size

#Create the hungry turtle
hungry = turtle.Turtle()
hungry.shapesize(eater_size, eater_size)
hungry.color("green")
hungry.penup()
hungry.shape("turtle")
hungry.setheading(random.randint(0,360))
sendToRandom(hungry)

#Create the turtles to be eaten
guppies = []
for i in range(40):
    temp = turtle.Turtle()
    temp.shapesize(1, 1)
    temp.color("red")
    temp.penup()
    temp.shape("turtle")
    temp.setheading(random.randint(0,360))
    sendToRandom(temp)
    guppies.append(temp)


#Main loop:
#Repeatedly move and eat
while eater_size < 42:
    wander(hungry)
    for g in guppies:
        wander(g)
    eater_size = feed(hungry, guppies)
    turtle.update() #update the canvas
    time.sleep(0.1) #Pause


turtle.done()