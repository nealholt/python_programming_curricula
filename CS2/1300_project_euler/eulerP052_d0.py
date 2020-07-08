'''
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''
from functions import *

def allSameDigits(two, three, four, five, six):
	'''Pre: the 5 arguments are all strings that have the same length.
	Post: returns true if all the strings have the same digits.'''
	#sort all of them
	#TODO it might be more efficient to sort only two at a time and compare them before moving on to the next pair, but I don't care enough about a few milliseconds to make this change.
	two = sorted(two)
	three = sorted(three)
	four = sorted(four)
	five = sorted(five)
	six = sorted(six)
	#compare value at each index
	for i in range(len(two)):
		if two[i] != three[i] or three[i] != four[i] or \
		four[i] != five[i] or five[i] != six[i]:
			return False
	return True

def solveEuler052(dummy):
	x=1
	while True:
		#See if 2*x and 6*x have the same number of digits, otherwise we can safely move on
		two=2*x
		six=str(3*two)
		two=str(two)
		if len(two) == len(six):
			three=str(3*x)
			four=str(4*x) #TODO More efficient to store two as a number and multiply it by 2 here? For example: four=str(2*two)
			five=str(5*x)
			if allSameDigits(two, three, four, five, six):
				print two, three, four, five, six
				print x
				return x
		x += 1



timeFunction(solveEuler052, None)

