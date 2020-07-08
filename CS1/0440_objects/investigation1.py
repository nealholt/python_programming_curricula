'''
For 35 points, answer the following questions.

Every class has the same name for its constructor. The name is
__init__
that is double underscore _ _ init then another double underscore _ _.
This is not my favorite thing, but you get used to it.

It is convenient for objects to refer to themselves. In Python, objects
refer to themself with the keyword 'self'. (A different programming 
language, Java, uses 'this'.)
'''

#Start defining a class.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
#Lack of indentation means we are done defining this class

#But now we can use the class. Here we create 3 instances of the class.
#p1, p2, and p3 are all Persons, but they have different names and ages.
p1 = Person("John", 36)
p2 = Person("Jalen", 32)
p3 = Person("Jane", 51)

print(p1.name)
print(p3.age)
#Inspired by: w3schools.com/python/python_classes.asp

'''
1. What does the above program print?

2. On what line number is the constructor for the Person class?

3. How does Python determine when the programmer is done defining
a class?

4. How does a Python class refer to itself?

5. How does a Java class refer to itself?

6. Every class constructor in Python has the same name, how many 
underscores are in this name?

7. Modify the above code to create a fourth person named Jekyll age 40.

8. Modify the above code to print Jalen's name and Jekyll's age.

9. Modify the above code so that the Person object keeps track of each
person's weight. You can make up the values for the 4 people's weights.
'''