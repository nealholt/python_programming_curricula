
#For 35 points, read this and answer the questions.


#1. What does the following program print? Try to answer without 
#running the code, then check your answer.
for i in range(3,7):
    print(i)


#2. What does the following program print? Try to answer without 
#running the code, then check your answer.
numbers = []
for i in range(2,12):
    numbers.append(i)
print(numbers[0])
print(numbers[7])
print(numbers[9])


#3. What does the following program print?
def getList(start, end):
    numbers = []
    for i in range(start, end):
        numbers.append(i)
    return numbers

my_list = getList(0, 5)
print(my_list[0])
print(my_list[2])


#4. What does the following program print?
for i in range(6,0,-1):
    print(i)


#5. What does the following program print?
numbers = []
for i in range(10,4,-2):
    numbers.append(i)
print(numbers[0])
print(numbers[1])
print(numbers[len(numbers)-1])


#6. What does the following program print?
def getList(start, end):
    numbers = []
    for i in range(start, end):
        numbers.append(i)
    return numbers

my_list = getList(3, 8)
for n in my_list:
    print(n)
print(my_list[2])


#7. What does the following program print?
def getList(start, end):
    numbers = []
    for i in range(start, end):
        numbers.append(i)
    return numbers

my_list = getList(5, 9)
for n in my_list:
    print(n)
print(my_list[1])


#8. What are all the possible different sequences the following 
#program could print?
import random
start = random.randint(0,2) #Gets a random number, either 0, 1, or, 2
end = 4
for i in range(start,end):
    print(i)


'''9. The following program is supposed to define a function that 
returns a list of 10 even numbers after a given number, but the 
code got scrambled.
For example, nextEvens(2) should return [2,4,6,8,10,12,14,16,18,20]
For example, nextEvens(5) should return [6,8,10,12,14,16,18,20,22,24]
Rearrange the lines of code so they work as intended. Include proper 
indentation. Test your code by calling the function.'''
return to_return
to_return = []
start = start+1 #make start even
for i in range(10):
start = start+2
def nextEvens(start):
if start%2!=0: #if start is not even
to_return.append(start)


#10. What pair of inputs should you give to the following program 
#to make it print orange?
drink = input("What's your favorite drink?")
apples = input("Do you like apples?")
if drink == 'SunnyD' and apples == 'no':
    print('orange')


#11. What error does this program throw?
my_list = [1,2,3,4]
print(my_list[4])

#12. What does the following program print?
my_list = [9,2,5,1,8,3,6,3,3]
print(my_list[1])
print(my_list[4])
print(len(my_list))

