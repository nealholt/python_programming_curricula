'''The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.'''

#Store in an array (memoize) the length of each collatz chain for every number. 0 isn't really defined, but I added it so that the indices aren't off by one. That is, each index in the array will store the length of the index's collatz chain.
#Memoize for numbers up to 10,000,000
memoizeLimit = 10000000
chainLength = [0 for _ in xrange(memoizeLimit)]
chainLength[1] = 1


def nextCollatz(n):
	if n % 2 == 0:
		return n/2
	else:
		return 3*n + 1

def getCollatxChainLength(n):
	'''Recursively calculate chain length with memoization. Haha!'''
	global chainLength, memoizeLimit
	if n < memoizeLimit and chainLength[n] != 0:
		return chainLength[n]
	else:
		length = 1 + getCollatxChainLength(nextCollatz(n))
		if n < memoizeLimit:
			chainLength[n] = length
		return length


'''TESTING
i = 13
while i != 1:
	print i
	i = nextCollatz(i)
'''

for x in xrange(2, 999999):
	length = getCollatxChainLength(x)
	#print str(x)+', '+str(length) #TESTING

print max(chainLength[0:1000000]) #The longest chain is 525 elements long.
print chainLength.index(525) #This chain is produced by the number 837799, which is the correct answer.

