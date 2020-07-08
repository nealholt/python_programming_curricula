
x = int(input('Give me a number:'))
print(str(x)+"'s collatz sequence is:")
while x!=1:
    if x%2==0: #if x is even
        x = x/2
    else:
        x = 3*x+1
    print(int(x))
