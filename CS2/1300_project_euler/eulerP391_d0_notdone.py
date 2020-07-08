'''
let s_k be the number of 1's when writing the numbers from 0 to k in binary.
For example, writing 0 to 5 in binary, we have 0, 1, 10, 11, 100, 101. There are seven 1's, so s_5 = 7

The sequence S = {s_k : k >= 0} starts {0, 1, 2, 4, 5, 7, 9, 12, ...}.

A game is played by two players. Before the game starts, a number n is chosen. A counter c starts at 0. At each turn, the player chooses a number from 1 to n (inclusive) and increases c by that number. The resulting value of c must be a member of S. If there are no more valid moves, the player loses.

For example:
Let n = 5. c starts at 0.
Player 1 chooses 4, so c becomes 0 + 4 = 4.
Player 2 chooses 5, so c becomes 4 + 5 = 9.
Player 1 chooses 3, so c becomes 9 + 3 = 12.
etc.
Note that c must always belong to S, and each player can increase c by at most n.

Let M(n) be the highest number the first player can choose at her first turn to force a win, and M(n) = 0 if there is no such move. For example, M(2) = 2, M(7) = 1 and M(20) = 4.

Given \sum(M(n))^3 = 8150 for 1 \leq n \leq 20.

Find \sum(M(n))^3 for 1 \leq n \leq 1000.



First I would want to generate s_k?
I don't fully understand the game.

s_k = 0, 1, 2, 4, 5, 7, 9, 12, 13, 15
difference between consecutive terms:
        1, 1, 2, 1, 2, 2, 3,  1,  2... 
wait no... it's not in binary so it doesn't pertain, right?
'''

def countOnes(binaryString):
	count = 0
	for b in binaryString:
		if b == '1':
			count += 1
	return count


count = 0
for i in xrange(10):
	count += countOnes(str(bin(i)))
	print str(i)+' '+str(bin(i))+' \tsk='+str(count)

