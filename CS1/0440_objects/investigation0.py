'''
For 18 points, answer the following questions.

Objects are ways of grouping data and actions that use that data. 
Classes describe how to make objects and what the object can do.

3 important words:
    constructor - a function for making objects
    methods - functions (or actions) that an object can do
    attributes - variables that belong to an object

We've already been using objects. Turtles are objects, as are Pygame's
rectangles.

We call a constructor when we say
    my_turtle = turtle.Turtle()
Names of classes always begin with capital letters. That is why 
Turtle is capitalized

Remember that . means belongs to.
    my_turtle.forward(10)
means call the forward method that belongs to my_turtle.
'''

import turtle 

#create an instance of the Turtle class
ninja = turtle.Turtle()
#ninja is now a variable that refers to a Turtle object

#Turtles have a function named speed.
#This line calls the Turtle's speed function
ninja.speed(10)

#Repeatedly tell the Turtle named ninja to do other things.
for i in range(180):
    ninja.forward(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30)
    
    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()
    
    ninja.right(2)

turtle.done()
'''
1. Names of classes should be what?
A. lowercase
B. capitalized
C. hyphenated
D. use underscores

2. Name 4 methods that belong to the class Turtle.

3. How are methods different from other functions?
 
4. Dot . means what?

5. ninja is a variable that refers to an object. Do you think that 
turtle is also a variable that refers to an object? Why or why not?
'''