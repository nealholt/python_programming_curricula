
#For 40 points answer the following questions.


#Lists and objects are not treated the same way as ints, floats,
#booleans, and strings.


#1. What does this code print?
x = 0
y = x
x = x+1
print(x, y)


#2. In the previous question, was the value of y changed by
#   x = x+1   ?


#3. What does this code print?
list1 = [1,2,3]
list2 = list1
list1[1] = 0
print(list1, list2)

#4. In the previous question, was the value of list2 changed by
#   list1[1] = 0   ?


#5. Let's see that again. What does this code print?
name1 = "Bill"
name2 = name1
name1 = "Ted"
print(name1, name2)


#6. In the previous question, was the value of name2 changed by
#   name1 = "Ted"   ?


#7. What does this code print?
import turtle
pen = turtle.Turtle()
pen.color("red")
print(pen.color())
brush = pen
pen.color("blue")
print(brush.color())
turtle.done()


#8. In the previous question, was the color of brush changed by
#   pen.color("blue")   ?


#9. What does this code print?
list1 = [1,2,3]
list2 = list1.copy()
list1[1] = 0
print(list1, list2)


#10. In the previous question, was the value of list2 changed by
#   list1[1] = 0   ?



#11. How is the code in question #9 different from the code
#in question #3?


#12. How is what gets printed in question #9 different from
#what gets printed in question #3?


#13. In your own words, how does Python treat lists and objects
#differently from other types of values?

