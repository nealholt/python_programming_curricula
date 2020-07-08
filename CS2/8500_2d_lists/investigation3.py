
#Lists can contain other lists. For 70 points, answer the following
#questions about two-dimensional lists.

#1. Compare what this prints
flat_list = [1, 2, 3, 'a', 'b', 'c']
print(flat_list)
#versus what this prints
nested_list = [[1,2,3],['a', 'b', 'c']]
print(nested_list)


#2. In the program above, I print 'a' in the flat list with
print(flat_list[3])
#and I print the 'a' in nested_list with
print(nested_list[1][0])
#because 'a' is the first item [0] in the second sub list [1].
#How would I print 3 in the nested list?


#3. How would I print 'c' in the nested list?


#4. What does this code print?
triples = [
	[1,2,3],
	['a','b','c'],
	["red","green","blue"]
	]
print(triples[1][2])


#5. How would you print blue from the list in question 4?

#6. In the nested list of tic-tac-tow below, what is the winning
#move for O?
list = [
			["","",""],
			["","",""],
			["","",""]
		]
list[0][1] = "X"
list[1][1] = "O"
list[2][0] = "X"
list[1][0] = "O"
list[2][1] = "X"
print(list)

#7. Two loops are needed to print out the values in a nested list, like
#this:
for row in list:
    for column in row:
        print(column)
#or like this:
for r in range(len(list)):
    for c in range(len(list[r])):
        print(list[r][c])
#Use this information to write a program to find the largest number in
#the following nested list named numbers and print the row and column
#of this number.
import random
numbers = []
for i in range(10):
    row = []
    for j in range(10):
        row.append(random.randint(0,1000))
    numbers.append(row)
print(numbers)
