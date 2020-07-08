'''
-Defining versus calling
-Defining before calling
-What are arguments
-One or more or no arguments
-Arguments as values, variables of the same name,
    or variables of a different name.
-Returning versus not returning.
'''


def bostonAccent(words):
    return words.replace("ar", "ah")

words = input("speak")
words = bostonAccent(words)
print(words)



'''
def multiply(a,b):
    x = 0
    while a>0:
        x = x + b
        a = a-1
    return x

print( multiply(6,3) )
'''



'''
def doWeGetSnack():
    print('yes')

x = doWeGetSnack()
if x == None:
    print("it's a none")
else:
    print('huh?')
print(x)
'''



