'''
The following is a decent start. Implement it. Currently you have a jumble of pseudo-ish code.
'''
primes = getPrimesArray() #TODO
start=0
end=0
p=0
#start at 5, the first prime that has two primes (2,3) before it. Index 2 in the array of primes.
i=2
ts=0 #abbreviation for tempstart
te=0 #abbreviation for tempend
while ts < i: #optimization possible here. don't even check anything less than the longest-so-far distance to current prime.
	r = primes[i]
	j = ts
	while r>0:
		r -= primes[j]
		j += 1
	if r == 0 and True: #TODO True needs replaced by a boolean for "this is the longest sequence of primes summing to another prime that we have yet seen"
		pass #TODO then update longest and corresponding prime that the sequence sums to.
	ts++
#TODO oops, you need an outer while loop to increment i.

'''REDO: THE FOLLOWING IS EVEN EASIER THAN THE ABOVE. CONSIDER STARTING HERE.
For each prime, is it a sum of consecutive primes?

The sum either starts with the first prime, or it doesn't.
If it does, then it also includes the next prime and so on until they add up to the target prime.
If it doesn't, then check the next prime for the start of a sequence summing up to the target.
And so on until the target itself.

Assume that addition is cheap, for now.

for each prime p < million
	for each prime p' < p
		if p' starts a sum that sums to p
		then record the start, end, length of sequence, and p
'''

