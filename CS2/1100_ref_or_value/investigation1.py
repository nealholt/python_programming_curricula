
#For 20 points answer the following questions.


#1. What does this code print?
def changeX(x):
    x = x+2

x = 5
changeX(x)
print(x)


#2. What does this code print?
def changeX(x):
    return x+2

x = 5
changeX(x)
print(x)


#3. What does this code print?
def changeX(x):
    return x+2

x = 5
x = changeX(x)
print(x)


#4. What does this code print?
def changeList(numbers):
    numbers[0] = 99

my_list = [1,2,3,4]
changeList(my_list)
print(my_list)


#5. The code in question 4 is most similar to the code from
#question 1, 2, or 3?


#When a variable with a list or object value is passed to a
#function, what gets passed is something like a phone number
#that lets the function contact that list or object.
#When a variable with a number or string gets passed,
#a copy of the number or string gets passed.

#The reason is size. Lists and objects can be very big, but
#numbers and strings are usually quite small.

#6. A floop is a new type of information that takes up a
#small amount of space in memory. If I create a variable
#of type floop and pass it to a function, will the function
#get a copy or a reference?


#7. What does this code print?
def returnChangedList(my_list):
    my_list.append(7)
    return my_list

my_list = [1,2,3,4]
my_list = returnChangedList(my_list)
print(my_list)


#8. What does this code print?
def returnChangedList(my_list):
    my_list.append(7)

my_list = [1,2,3,4]
returnChangedList(my_list)
print(my_list)


#9. Which code is easier to write? The code in question 7 or 8?


'''
KEY POINT: lists and objects are passed by reference (in
other words, the function gets a reference to the original).
Other variables are passed by value, meaning that a copy of
the value is passed. The original variable cannot be changed.
'''
