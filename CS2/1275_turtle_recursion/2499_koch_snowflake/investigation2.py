
'''For 18 points, answer the following questions:

"Recursion" is when a function solves a problem by calling itself.
Recursive functions have at least 2 parts:
    1. Base case - This is where the function is finished.
    2. Recursive case (aka Induction case) - this is where the 
	function calls itself and gets closer to the base case.
'''

#1. Which case (the if or the else) is the base case and which 
#is the recursive case?
def printList(my_list):
    if len(my_list) > 0:
        print(my_list[0])
        printList(my_list[1:])
    else:
        pass

#2. Create a list then pass the list to this function.
#What does this function do?

#Still referring to the above code: This weirdness with a 
#colon inside brackets, my_list[1:], is called a slice.
#Experiment with slices such as the following then answer the 
#question below.
numbers = [8,2,46,7,4,2,1]
print(numbers[1:])
print(numbers[:4])
print(numbers[1:4])
#3. Write a line of code that slices my first name, neal, out of 
#this list and prints it.
letters = ['n','a','l','n','e','a','l','t','y']


#4. Write a loop that does the exact same thing as printList


#5. What is the mysterious calculation that this function is doing?
def mystery(a,b):
    if a==0:
        return 0
    else:
        return b+mystery(a-1,b)


#6. What is the base case and what is the recursive case in the 
#mystery function?


#7. Write a recursive factorial function. Reminder: factorial takes a
#whole number and returns the product of every number less than that
#number. For example: 5 gives 5*4*3*2*1 = 120
#Example: 3 gives 3*2*1 = 6

