'''If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

onesDigits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
def onesDigitToWord(d):
	global onesDigits
	return onesDigits[d-1]


tensdigits = [None, 'twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
def tensDigitToWord(d):
	'''the teens break the pattern and should be dealt with elsewhere.'''
	global tensdigits
	return tensdigits[d-1]


teens = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
def teenToWord(t):
	global teens
	return teens[(t%10)-1]


def underOneHundredToWords(n):
	'''Pre: 10 < n <= 99
	'''
	tensDigit = n % 100
	tensDigit = tensDigit / 10
	if n % 100 == 10:
		tensDigit = 'ten '
	elif tensDigit == 1:
		teen = n % 100
		teen = teenToWord(teen)
		return teen+' '
	elif tensDigit == 0:
		tensDigit = ''
	else:
		tensDigit = tensDigitToWord(tensDigit)+' '

	onesDigit = n % 10
	if onesDigit == 0:
		return tensDigit
	onesDigit = onesDigitToWord(onesDigit)

	return tensDigit+onesDigit


def bigNumberToWords(n):
	'''Pre: 99 < n <= 1000
	'''
	if n == 1000:
		return 'one thousand'

	hundredsDigit = n / 100
	hundredsDigit = onesDigitToWord(hundredsDigit)

	lowerDigits = n % 100
	if lowerDigits == 0:
		return hundredsDigit+' hundred'
	lowerDigits = underOneHundredToWords(lowerDigits)

	return hundredsDigit+' hundred and '+lowerDigits


def numberToWords(n):
	if n < 11:
		return onesDigitToWord(n)
	elif n < 100:
		return underOneHundredToWords(n)
	elif n < 1001:
		return bigNumberToWords(n)
	else:
		print 'Numbers over 1000 not implemented.'

temp = bigNumberToWords(342)
temp = temp.replace(' ', '') #Strip blank spaces
print str(temp)+' has '+str(len(temp))+' letters in it.'
temp = bigNumberToWords(115)
temp = temp.replace(' ', '') #Strip blank spaces
print str(temp)+' has '+str(len(temp))+' letters in it.'


sumLetters = 0
for i in xrange(1, 6):
	temp = numberToWords(i)
	temp = temp.replace(' ', '') #Strip blank spaces
	sumLetters += len(temp)
print 'There are a total of '+str(sumLetters)+' letters in the numbers 1 through 5.'



#TESTING
'''
for i in xrange(1, 50):
	print numberToWords(i)
for i in xrange(90, 122):
	print numberToWords(i)
for i in xrange(490, 522):
	print numberToWords(i)
for i in xrange(980, 1001):
	print numberToWords(i)
'''


sumLetters = 0
for i in xrange(1, 1001):
	temp = numberToWords(i)
	temp = temp.replace(' ', '') #Strip blank spaces
	sumLetters += len(temp)
print sumLetters

#Answer: 21124

