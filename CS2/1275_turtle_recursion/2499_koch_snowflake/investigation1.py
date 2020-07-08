
'''For 18 points, answer the following questions:

"Recursion" is when a function solves a problem by calling itself.
Recursive functions have at least 2 parts:
    1. Base case - This is where the function is finished.
    2. Recursive case (aka Induction case) - this is where the 
	function calls itself and gets closer to the base case.
'''

#1. Here is a very dumb recursive function. Which case (the if 
#or the else) is the base case and which is the recursive case?
def whatWeAreStudying(n):
    if n == 0:
        print('Recursion!')
    else:
        print('Inception?')
        whatWeAreStudying(n-1)

#2. What is printed when you call the function with the argument 3?

#3. What is the name of the error that occurs when you call the 
#function with the argument 3.1?

#4. How can you adjust the code to prevent the error in the 
#previous question?

#5. Here is a more useful recursive function. Which is the base case
#and which is the recursive case?
def raiseToPower(base,power):
    if power == 0:
        return 1
    else:
        return base * raiseToPower(base, power-1)


#6. What does this function calculate? Give an example.

#7. How would you ask this function to calculate 2 cubed?

#8. How would you ask this function to calculate 12 squared?

#9. Write a non-recursive function that uses a loop to do the same
#thing raiseToPower does.

