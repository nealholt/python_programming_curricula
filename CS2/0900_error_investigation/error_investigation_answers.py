'''
x = 1
name = 'Dahlia'
name = name + x
#What is the error in your words?
#Answer: Can't add str and int
#What is the error in Python's words?
#Answer: TypeError: must be str, not int
#What is one way to fix it?
#Answer: name = name + str(x)
'''

'''
x = 0
y = 146
x = y/x
#What is the error in your words?
#Answer: Can't divide by zero
#What is the error in Python's words?
#Answer: ZeroDivisionError: division by zero
#What is one way to fix it?
#Answer: don't divide by zero
'''

'''
x = x+5
#What is the error in your words?
#Answer: Can't add 5 to x before it exists
#What is the error in Python's words?
#Answer: NameError: name 'x' is not defined
#What is one way to fix it?
#Answer: Set x = 0 earlier
'''

'''
william = 'student'
wiliam += 'grade 10'
#What is the error in your words?
#Answer: typo in variable name
#What is the error in Python's words?
#Answer: NameError: name 'wiliam' is not defined
#What is one way to fix it?
#Answer: Spell "wiliam" correctly.
'''

'''
echo()
#What is the error in your words?
#Answer: Can't call a function that doesn't exist
#What is the error in Python's words?
#Answer: NameError: name 'echo' is not defined
#What is one way to fix it?
#Answer: Define the function or call a different function that actually exists.
'''

'''
pirnt()
#What is the error in your words?
#Answer: Misspelled print
#What is the error in Python's words?
#Answer: NameError: name 'pirnt' is not defined
#What is one way to fix it?
#Answer: Spell it correctly
'''

'''
The previous 4 errors were all NameErrors. What is common among such errors?
'''

'''
x = 4
print(x
x = x+2
#What is the error in your words?
#Answer: Missing parend
#What is the error in Python's words?
#Answer: SyntaxError: invalid syntax
#What line of code does Python say the error is on?
#Answer: Line 3
#What line of code is the error actually on?
#Answer: Line 2
#What is one way to fix it?
#Answer: Add a parend
'''

'''
x = 2
if x > 1
    print('ok')
#What is the error in your words?
#Answer: Missing colon
#What is the error in Python's words?
#Answer: SyntaxError: invalid syntax
'''

'''
x = 2
if x > 1:
print('ok')
#What is the error in your words?
#Answer: Missing indentation
#What is the error in Python's words?
#Answer: IndentationError: expected an indented block
'''

'''
x = 2
if x > 1:
    print('ok')
        x = x+1
#What is the error in your words?
#Answer: Un-needed indentation
#What is the error in Python's words?
#Answer: IndentationError: unexpected indent
'''

'''
letters = ['A','B','C','D']
for i in range(5):
    print(letters[i])
#What is the error in your words?
#Answer: Ran off the end of the list
#What is the error in Python's words?
#Answer: IndexError: list index out of range
#What is one way to fix it?
#Answer: range(4) or range(len(letters))
'''

'''
letters = ['A','B','C','D']
x = 1/2
print(letters[x])
#What is the error in your words?
#Answer: Can't index with a fraction
#What is the error in Python's words?
#Answer: TypeError: list indices must be integers or slices, not float
#What is one way to fix it?
#Answer: x = 1 or x = 2
'''

'''
letters = ['A','B','C','D']
for i in range(2,8):
    x = i/2
    print(letters[x])
#What is the error in your words?
#Answer: Can't index with a fraction
#What is the error in Python's words?
#Answer: TypeError: list indices must be integers or slices, not float
#What is one way to fix it?
#Answer: range(2,8,2) or various other fixes
'''