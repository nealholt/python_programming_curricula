import random

def ohWisePythonGiveMeAValue():
	return random.randint(-100,100)



#Variables.
#NOTE: Make this interactive with the students. The students are to take
#little breaks and write their own version of this code as you go through and
#then submit it for a grade at the end of the lesson.

#Creating a variable means giving it a name and a value. Create your own
#variable and give it a name and value now:
x = 10 #The name is x, the value is 10.

#Assignment goes from right to left.
#Give your own example of all 3 of the following. You may use the input
#function for the third example or create your own function.
name = "Anderson"
#        calculated values,
solution = 4*(x**2) - 18*x - 7/4
#        or return values of functions.
best_value = ohWisePythonGiveMeAValue()

print(x)
print(name)
print(solution)
print(best_value)


#Variables can be increased or decreased after they have been created
x = x + 5
print(x)

solution = solution/2
print(solution)


#Variables can be copied to other variables
print(x)
y = x
print(y)
y = 0
print(x) #What do you think this prints?


#Swapping the value of two variables might be harder than you think.
a = "red"
b = "blue"
a = b
b = a
print("Should print blue: "+a)
print("Should print red: "+b)
#What went wrong and how do I fix it?
