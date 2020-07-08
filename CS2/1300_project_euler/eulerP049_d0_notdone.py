'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?


Naive approach may work:
Get all 4 digit primes.
For each 4 digit prime, get all permutations. If two of the other permutations are prime then print out all 3 prime permutations.

There are 4*3*2*1=24 permutations of 4 digits.
'''
from functions import *

fourDigitPrimes = getAllPrimesInRange(1000, 9999)
for p in fourDigitPrimes:
	primePerms = [] #List of permutations initially containing only p
	perms = permutations(str(p)) #Get all permutations of p
	for perm in perms:
		#If it is 4 digits, prime, and not already in the prime array, then add it.
		#It could already be in the prime array because 1009 and 1009 are both
		#"distinct" permutations of 9001, because the zeroes are swapped.
		#The str(int(perm)) business is to make sure that 0109 doesn't count as 
		#a 4 digit prime.
		if len(str(int(perm))) == 4 and isPrime(int(perm)) and \
		not int(perm) in primePerms:
			primePerms.append(int(perm))
	#If more than 2 prime permutations were found, print them out
	if len(primePerms) > 2:
		primePerms = sorted(primePerms)
		#See if the increase is consistent.
		increase = primePerms[1] - primePerms[0]
		isConsistent = True
		for i in xrange(len(primePerms)-1):
			if primePerms[i+1] - primePerms[i] != increase:
				isConsistent = False
				break
		if isConsistent:
			print primePerms
			#exit()

#You need a little more. You need to look for the steady increases between some of the permutations.

