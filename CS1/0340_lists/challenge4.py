
'''For 70 points, write a function, that finds all the sub lists
in a list that add up to a particular number. Examples follow.'''

numbers = [1, 3, 6, 11, 1, 5, 4]
target = 4
result = getSubSum(numbers, target)
print(result) #Correct answers are [1,3] and [4] since these sum to 4

numbers = [2, 4, 45, 6, 0, 19]
target = 51
result = getSubSum(numbers, target)
print(result) #Correct answers: [2,4,45], [45,6], and [45,6,0]

numbers = [1, 11, 100, 1, 0, 200, 3, 2, 1, 280]
target = 280
result = getSubSum(numbers, target)
print(result) #Only one correct answer: [280]
