
#For 18 points, read this and answer the questions.


#1. What does this code print? Try to answer without running it.
my_list = [0,1,2,3]
print(len(my_list))


#2. What does this code print?
letter = "Dee"
print(len(letter))


#3. What might you conclude about the relationship between 
#lists and strings?


#4. Write code that creates a list named numbers and puts the values 1, 2, and 3 in the list.


#5. Write code that creates a list named contacts and puts the strings Carrie, Mark, and Harrison in the list.


#6. What does this code print? Guess before running it.
list = ["comments", "Bux", "English", "Moses", "homework", "Turkey"]
print(list[2])


#7. What does the following program do? Try to figure it out without
#running it.
numbers = [2,-5,1,9,-12,-3]
negative_sum = 0
for n in numbers:
    if n<0:
        negative_sum = negative_sum + n
print(negative_sum)


#8. Write a program that adds up all the numbers greater than 1 in 
#the following list
numbers = [2,-5,1,9,-12,-3]


#A common way to loop over a list using the locations,
#or indicies, of values in the list is with a loop like
#the following:
numbers = [2,-5,1,9,-12,-3]
for i in range(len(numbers)):
    print(i, numbers[i])

'''9. Write a program that prints the indicies and letters of your name
like this:
0 N
1 e
2 a
3 l
'''


#10. What does the following code do?
numbers = [2,-5,1,9,-12,-3]
total = 0
for n in numbers:
    total = total + n
print(total)


#11. Rewrite the previous program using for i in range(len(numbers))


#12. What does the following code do? If you're not sure,
#change the values in the numbers list and see if 
#(and how) your results change.
import sys
minimum = sys.maxsize
print(minimum)
index = -1
numbers = [2,-5,1,9,-12,-3]
for i in range(len(numbers)):
    if numbers[i] < minimum:
        minimum = numbers[i]
        index = i
print(minimum)
print('The index of minimum is '+str(index))
