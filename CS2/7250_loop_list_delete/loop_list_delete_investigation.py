'''For 35 points, answer the questions below.
'''
################ PART 1 ################
#Compare code A and code B below.
#1. How is the code different?

#2. How is what gets printed different?

#A
numbers = []
for i in range(10):
    numbers.append(i)
print(numbers)

#B
numbers = []
for i in reversed(range(10)):
    numbers.append(i)
print(numbers)

################ PART 2 ################
#3. Guess how many times the following loop repeats.

#4. How many times does the loop actually repeat?
#(You may use print statements or use other methods to answer.)

#5. Numbers gets longer each time the loop repeats. Does range(len(numbers))
#change as the loop repeats?

#6. What would happen if range(len(numbers)) updated each time the loop
#repeated?
numbers = [1,2,3]
for i in range(len(numbers)):
    numbers.append(i)

################ PART 3 ################
#A train is in the middle of 20 miles of track. In other words,
#there is ten miles of track to the west and ten miles to the east.
#For every mile the train travels, one mile of track is destroyed
#on the eastern end.
#7. What happens if the train travels 10 miles east?
#8. What happens if the train travels 10 miles west?

#Compare code A and code B below.
#9. Code A is broken. What error does it throw?

#10. How is the code different between the two parts?

#11. Why does B work, but A does not?

#A
#Delete even numbers
numbers = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(numbers)):
    print()
    print("i is "+str(i))
    print("numbers is "+str(numbers))
    if numbers[i]%2 == 0: #if numbers[i] is odd
        del numbers[i]

#B
#Delete even numbers
numbers = [1,2,3,4,5,6,7,8,9,10]
for i in reversed(range(len(numbers))):
    print()
    print("i is "+str(i))
    print("numbers is "+str(numbers))
    if numbers[i]%2 == 0: #if numbers[i] is odd
        del numbers[i]
