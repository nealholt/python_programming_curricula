'''A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.'''
from functions import *

#Get all abundant numbers for starters
abundant = []
for i in xrange(2, 28123+1):
	total = sum(getAllDivisors(i))
	if total > i:
		abundant.append(i)
#print abundant


#def isSumOfAbundant(abundant, number):
#	'''Returns true if number is a sum of abundant numbers.'''
#	if number == 0:
#		return True
#	else:
#		#Then check if number minus the largest number in abundant is a sum of abundants
#		smallerNumber = number - abundant[-1]
#		lessAbundant = abundant[0:len(abundant)-1]
		
#Get a list of all the numbers under 28123+1 that can be written as a sum of abundant numbers


#Durrrr need some paper to work this out.
