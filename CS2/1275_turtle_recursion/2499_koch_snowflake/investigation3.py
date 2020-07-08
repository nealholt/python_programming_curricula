
'''For 18 points, answer the following questions:

"Recursion" is when a function solves a problem by calling itself.
Recursive functions have at least 2 parts:
    1. Base case - This is where the function is finished.
    2. Recursive case (aka Induction case) - this is where the 
	function calls itself and gets closer to the base case.
'''

#The Fibonacci sequence is a classic example of a recursive function.
#The sequence is: 1,1,2,3,5,8,13,21,34,55, and so on.
#You calculate the sequence by starting with two numbers (such as 1,1)
#then you get the next number by adding the previous two numbers.
#Here it is as a recursive function.
def fibonacci(a,b,n):
    '''a and b are the starting numbers. n is how deep into the
    sequence you want to calculate.'''
    if n==0:
        return a+b
    else:
        return fibonacci(b,a+b,n-1)

#1. Which case (the if or the else) is the base case and which 
#is the recursive case?

#2. Write code that uses the function to print out the first 8 numbers
#in the sequence.

#3. What error do you get if you pass a decimal as the third argument
#to the function?

#4. How can you fix that error?

#5. Write this function using loops.


#You can factor using recursion. Check it out.
#Note that start=2 defines an argument with a default value.
#For example: If I write factor(10) then start defaults at the value 2
#If I write: factor(81,3) then start takes the value 3.
def factor(number, start=2):
    if start > number:
        return []
    elif number % start == 0:
        return [start]+factor(number/start, start)
    else:
        return factor(number,start+1)

#6. Find all the factors of 360 using this function.

#7. There are three cases in factor. Which are the base case(s)?
#Which are the recursive case(s)?

