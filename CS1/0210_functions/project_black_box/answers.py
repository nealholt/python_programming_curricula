import math

#ANSWER: always returns 5, no matter what x is.
def clearBox1(x):
    return int(((1.0-math.cos(2.0*x))/2.0)**2 + math.sin(math.pi/2.0 - x)**2)+5

#ANSWER: returns the larger of a and b
def clearBox2(a, b):
    if(a > b):
        return a
    else:
        return b

#ANSWER: returns the remainder of a divided by b
def clearBox3(a, b):
    return a % b

#ANSWER: returns n copies of s as a string
def	clearBox4(n, s):
    accumulator = ""
    for i in range(n):
        accumulator += str(s)
    return accumulator


print("Part 1")
print(clearBox1(7.0))
print(clearBox1(17.0))
print(clearBox1(888.0))
print(clearBox1(82.0))

print("\nPart 2")
print(clearBox2(88, 1))
print(clearBox2(1,88))
print(clearBox2(0,0))
print(clearBox2(7,-6))

print("\nPart 3")
print(clearBox3(88, 6))
print(clearBox3(0,1))
print(clearBox3(14,3))
print(clearBox3(7,2))

print("\nPart 4")
print(clearBox4(4, "quad"))
print(clearBox4(1,"uno"))
print(clearBox4(7,""))
print(clearBox4(10,"lol"))
