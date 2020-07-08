"""LIST OF ALL FUNCTIONS
	timeFunction
Takes a function with one argument. Runs and times the function. Printing the resulting time and output.

	isPrime
Takes one integer argument and returns true if the int is prime.
Used on problems: 10.

	getAllPrimesInRange(start, end)
Takes 2 integer arguments, the range start and the range end. Returns a list of primes between start and end. Though this implementation is fairly naive, it's fast enough for my needs thus far.
Used on problems: 49

	getGreatestPrimeFactor
Takes one integer argument and returns its greatest prime factor.
Used on problems: 10.

	getAllPrimeFactorsNoDupes
Takes one integer argument, x, and returns a list of x's prime factors without duplicates. For example: getAllPrimeFactorsNoDupes(4) = [2].
Used on problems: 10.

	getAllPrimeFactorsDupes
Takes one integer argument, x, and returns a list of x's prime factors with duplicates. For example: getAllPrimeFactorsNoDupes(4) = [2, 2].
Used on problems: 10.

	countDivisors
Takes one integer argument, x, and returns a count of x's divisors.
Used on problems: 12.

	getAllDivisors
Takes one integer argument, x, and returns a count of x's divisors EXCEPT for x itself. This function was based on countDivisors
Used on problems: 21.

	digits2toThe
Takes one integer argument, power, and returns a list of all digits in the number 2**power.
Used on problems: 16

	permutations
Function that takes a list (array) and returns a generator for all permutations of the list.
Used on problems: 49
"""

import time

#Global variable storing all the primes seen so far.
all_primes = [2,3]

def timeFunction(func, arg):
	start = time.time()
	temp = func(arg)
	end = time.time()
	print 'runs in '+str(end - start)+' seconds with out put '+str(temp)

def isPrime(x):
	"""Pre: x is an integer that is 2 or greater.
	Post: returns true if x is a prime number.
	TODO: this could be sped up slightly by not checking if x is divisible by every number of the form 3 + 6n for all n. These will be things like 9, 15, 21, etc which are odd, but not prime."""
	#2 and 3 are prime
	if x == 2 or x == 3:
		return True
	#even numbers are not prime
	elif x%2 == 0:
		return False
	else:
		#So check all the odd numbers to see if they divide x
		i = 3
		while True:
			if x%i == 0:
				return False
			#if i is now greater than x divided by i, then x is 
			#divided by some number less than i (which we've already
			#ruled out), or x is prime. x must be prime.
			elif i > x/i:
				return True
			#Check the next odd number.
			i += 2

'''TESTING
print '2 True '+str(isPrime(2))
print '3 True '+str(isPrime(3))
print '13 True '+str(isPrime(13))
print '16 False '+str(isPrime(16))
print '29 True '+str(isPrime(29))
print '101 True '+str(isPrime(101))
print '7907 True '+str(isPrime(7907))
print '7909 False '+str(isPrime(7909))
'''

def getGreatestPrimeFactor(x):
	#Set the greatest divisor so far to one
	greatest = 1

	#Test 2
	i = 2
	#If i divides x then i is now the greatest so far. If other larger primes divide
	#x then they will also divide x/i
	while x%i == 0:
		greatest = i
		x = x/i
	#Now check all the odd numbers greater than 2.
	i = 3
	while True:
		#If i divides x then i is now the greatest so far. If other 
		#larger primes divide x then they will also divide x/i
		while x%i == 0:
			greatest = i
			x = x/i
		if i > x/i:
			if isPrime(x) and x > greatest:
				return x
			else:
				return greatest
		i += 2 #Check the next prime number
		while not isPrime(i):
			i += 2

'''TESTING
timeFunction(getGreatestPrimeFactor, 843756)
timeFunction(getGreatestPrimeFactor, 600851475143)
'''

def getAllPrimeFactorsNoDupes(x):
	factors = []
	#Test 2
	i = 2
	#If i divides x then i is now the greatest so far. If other larger primes divide
	#x then they will also divide x/i
	if x%i == 0:
		factors.append(i)
	while x%i == 0:
		x = x/i
	#Now check all the odd numbers greater than 2.
	i = 3
	while True:
		#If i divides x then i is now the greatest so far. If other 
		#larger primes divide x then they will also divide x/i
		if x%i == 0:
			factors.append(i)
		while x%i == 0:
			x = x/i
		if i > x/i:
			if isPrime(x):
				factors.append(x)
			return factors
		i += 2 #Check the next prime number
		while not isPrime(i):
			i += 2

'''TESTING
timeFunction(getAllPrimeFactorsNoDupes, 843756)
'''

def getAllPrimeFactorsDupes(x):
	factors = []
	#Test 2
	i = 2
	#If i divides x then i is now the greatest so far. If other larger primes divide
	#x then they will also divide x/i
	while x%i == 0:
		factors.append(i)
		x = x/i
	#Now check all the odd numbers greater than 2.
	i = 3
	while True:
		#If i divides x then i is now the greatest so far. If other 
		#larger primes divide x then they will also divide x/i
		while x%i == 0:
			factors.append(i)
			x = x/i
		if i > x/i:
			if isPrime(x):
				factors.append(x)
			return factors
		i += 2 #Check the next prime number
		while not isPrime(i):
			i += 2

'''TESTING
timeFunction(getAllPrimeFactorsDupes, 843756)
'''

def sumOfPrimesBelow(x):
	'''Returns a sum of all primes below x.'''
	total = 2
	i = 3
	while i < x:
		if isPrime(i):
			total += i
		i += 2
	return total


def countDivisors(x):
	'''Let us list the factors of the first seven triangle numbers:
	 1: 1
	 3: 1,3
	 6: 1,2,3,6
	10: 1,2,5,10
	15: 1,3,5,15
	21: 1,3,7,21
	28: 1,2,4,7,14,28

	There's a symmetry. 
	First non-one divisor times last non-x divisor equals x.
	Second non-one divisor times second-to-last non-x divisor equals x.
	And so on.
	This narrows the search space significantly.'''
	#count of divisors. Start off with 2. Everything is divisible by 1 and itself.
	#We treat specially the special case of 1 being itself.
	if x == 1:
		return 1
	count = 2
	end = x
	if x%2 == 0: #If x is even
		start = 2
		while start < end:
			if x%start == 0:
				count += 1
				end = x/start
				if start != end:
					count += 1
			start += 1
	else: #x is odd
		#Start the odds at 3 and go up by two, only checking the odds.
		start = 3
		while start < end:
			if x%start == 0:
				count += 1
				end = x/start
				if start != end:
					count += 1
			start += 2
	return count


def getAllDivisors(x):
	'''Let us list the factors of the first seven triangle numbers:
	 1: 1
	 3: 1,3
	 6: 1,2,3,6
	10: 1,2,5,10
	15: 1,3,5,15
	21: 1,3,7,21
	28: 1,2,4,7,14,28

	There's a symmetry. 
	First non-one divisor times last non-x divisor equals x.
	Second non-one divisor times second-to-last non-x divisor equals x.
	And so on.
	This narrows the search space significantly.'''
	divisors = [1]
	#List of divisors. Start off with 2. Everything is divisible by 1 and itself.
	#We treat specially the special case of 1 being itself.
	if x == 1:
		return divisors
	end = x
	if x%2 == 0: #If x is even
		start = 2
		while start < end:
			if x%start == 0:
				divisors.append(start)
				end = x/start
				if start != end:
					divisors.append(end)
			start += 1
	else: #x is odd
		#Start the odds at 3 and go up by two, only checking the odds.
		start = 3
		while start < end:
			if x%start == 0:
				divisors.append(start)
				end = x/start
				if start != end:
					divisors.append(end)
			start += 2
	return divisors


def digits2toThe(power):
	'''Return a list of all digits in the number 2**power.'''
	#Start off with 2 raised to the first power in the ones place.
	digits = [2]
	for _ in xrange(2, power+1):
		#Double all the digits
		for i in xrange(len(digits)):
			digits[i] = digits[i]*2
		#For digits which have been raised above 9 (ie, those now taking up 2 digits),
		#truncate them and perform a carry operation
		for i in xrange(len(digits)):
			if digits[i] > 9:
				digits[i] = digits[i]%10
				if len(digits) <= i+1:
					digits.append(1)
				else:
					digits[i+1] += 1
	return digits

def permutations(elements):
	'''Function to get all the permutations of a given list.
	Source: http://code.activestate.com/recipes/252178/
	Example usage:
	for p in permutations([1,2,3]):
		print p
	What are generators and why do we like them?
	http://wiki.python.org/moin/Generators
	The short answer is a reduced memory footprint'''
	if len(elements) <=1:
		yield elements
	else:
		for perm in permutations(elements[1:]):
			for i in range(len(elements)):
				#nb elements[0:1] works in both string and list contexts
				yield perm[:i] + elements[0:1] + perm[i:]

def getAllPrimesInRange(start, end):
	'''Though this is fairly naive, it's fast enough for my needs thus far.'''
	primes = []
	if start%2 == 0: #If start is even
		start += 1
	for i in xrange(start, end+1, 2): #Step size of 2 to skip even numbers.
		if isPrime(i):
			primes.append(i)
	return primes

