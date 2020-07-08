'''n! means n x (n - 1) x ... x 3 x 2 x 1

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

#Store digits in an array.
#Perform multiplication on each digit.
#Carry over to subsequent digits.
#Sum up all digits and return value.
x = 100 #Our factorial
digits = [] #the digits in the number we are building up.
digits.append(1)
for i in xrange(1, x+1): #For the numbers that we are multiplying (we can take the numbers from the bottom up because multiplication is commutative)...
	carry = 0 #Initialize the carry over to zero
	#For each digit in our growing number...
	for d in xrange(len(digits)):
		#Multiply the digit by the multiplier and add the carry.
		digits[d] = digits[d]*i + carry
		carry = 0
		#Carry over digits that became more than one digit
		while digits[d] > 9:
			carry = digits[d] / 10
			digits[d] = digits[d] % 10
	#Append the final carry over to the end of digits
	if carry > 0:
		digits.append(carry)
	#While the last digit is more than one digit, keep carrying over into further digits.
	while digits[-1] > 9:
		carry = digits[-1] / 10
		digits[-1] = digits[-1] % 10
		digits.append(carry)

print digits
print sum(digits) #Answer 648

