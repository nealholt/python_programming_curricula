'''
2^{15} = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^{1000}?
'''

from functions import *

#timeFunction(digits2toThe, 1000)
print sum(digits2toThe(1000)) #Answer: 1366
