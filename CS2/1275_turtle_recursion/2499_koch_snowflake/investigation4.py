
#For 18 points, answer the following question:

#Challenge: The following function divides one number from another
#recursively, but can't handle decimal answers.

#For example, you can do this  print(divide(8,2))
#or this  print(divide(100,5))
#but you can't do this  print(divide(9,2))
#or this  print(divide(9,4))

#Change this function so that it can do decimal divisions such as
#print(divide(9,2))  or this  print(divide(9,4))  correctly.

#Does your function also work for other decimal results?
def divide(divisee, divisor):
    if divisee==0:
        return 0
    elif divisee<0:
        print("Sorry. This simple divide doesn't handle decimals.")
        exit()
    else:
        return 1 + divide(divisee-divisor, divisor)

