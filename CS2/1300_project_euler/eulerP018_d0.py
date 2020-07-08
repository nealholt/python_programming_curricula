'''By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3_
7_ 4
2 4_ 6
8 5 9_ 3


That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;)
'''

triangle = [
[75],
[95, 64],
[17, 47, 82],
[18, 35, 87, 10],
[20,  4, 82, 47, 65],
[19,  1, 23, 75,  3, 34],
[88,  2, 77, 73,  7, 63, 67],
[99, 65, 04, 28,  6, 16, 70, 92],
[41, 41, 26, 56, 83, 40, 80, 70, 33],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
[63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23],
]


#A greedy algorithm follows.
def solveTriangleGreedy(triangle):
	position = 0
	path = [triangle[0][0]] #Start the path with the first number
	for i in xrange(1, len(triangle)):
		if triangle[i][position] > triangle[i][position+1]:
			path.append(triangle[i][position])
		else:
			position += 1
			path.append(triangle[i][position])

	print 'This does not necessarily give the correct solution.'
	print 'Greedy path: '+str(path)
	print 'Greedy path sum: '+str(sum(path))



#Superior approach:
def solveTriangleSmart(triangle):
	triangleRow = 0
	for i in xrange(1, len(triangle)):
		for j in xrange(len(triangle[i])):
			#Get both parents. There might be only one.
			parentLeft = 0
			if j-1 >= 0:
				parentLeft = triangle[i-1][j-1]
			parentRight = 0
			if len(triangle[i-1]) > j:
				parentRight = triangle[i-1][j]
			#Determine which parent is larger to sum in
			if parentLeft < parentRight:
				triangle[i][j] += parentRight
			else:
				triangle[i][j] += parentLeft

	print 'Dynamic programming approach: '+str(max(triangle[-1])) #Answer: 1074


solveTriangleGreedy(triangle)
solveTriangleSmart(triangle)

