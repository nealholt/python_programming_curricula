'''
For 35 points, answer the following questions.

Methods are functions that belong to a class. Every method has at
least one argument, the first argument, which is self.

Methods, just like functions, are activated by using their name followed
by parentheses.
'''

class Snake:
    def __init__(self, name, length, is_constrictor):
        self.name = name
        self.length = length
        self.is_constrictor = is_constrictor

    def changeName(self, new_name):
        self.name = new_name

# two variables are instantiated
python = Snake("python", 20, True)
anaconda = Snake("anaconda", 15, True)

# print the names of the two variables
print(python.name)
print(anaconda.name)

if python.is_constrictor:
    print('SQUEEZE!')

anaconda.changeName('rattler')
#is_constrictor is a variable that belongs to anaconda, in other words an
#attribute. We don't use parentheses to change it. Dot . still means belongs to.
anaconda.is_constrictor = False
if anaconda.is_constrictor:
    print(anaconda.name+' does not squeeze ya!')

'''
1. What is the name of the class in the example program above.

2. Name all the methods that belong to the class.

3. Name all the attributes that belong to the class.

4. What does the program print?

5. If the program had this line
anaconda.is_constrictor = False
replaced with this line
anaconda.is_constrictor = True
what would it print? (Be careful. What's the snake's name?)

6. Why aren't parentheses needed on this line of code?
anaconda.is_constrictor = False

7. Add a new attribute, venomous, to the snake class. You will have to choose
values for venomous for the snakes.

8. Modify the above code to change the value of venomous when the anaconda
changes names.

9. Modify the above program to check to see if the newly-named rattler is
venomous and if so print the snake's name.

10. Modify the above program to change the length of the anaconda after it
changes names. You can choose the new length.
'''

#Source: hackerearth.com/practice/python/object-oriented-programming/classes-and-objects-i/tutorial/
