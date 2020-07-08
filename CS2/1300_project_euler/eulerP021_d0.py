'''Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''
from functions import *

'''
#TESTING
temp = getAllDivisors(220)
temp.sort()
print temp
print sum(temp)
print

temp = getAllDivisors(284)
temp.sort()
print temp
print sum(temp)
'''

#Get a list of all sums of divisors for starters
divSums = [0]
for i in xrange(1, 10000):
	divSums.append(sum(getAllDivisors(i)))

#Get a list of all the amicable numbers
amicable = []
for i in xrange(2, 10000):
	num = divSums[i]
	if num < len(divSums) and divSums[num] == i and num != i:
		amicable.append(num)
		print str(i)+', '+str(divSums[i])
print amicable
print sum(amicable) #Answer: 31626

