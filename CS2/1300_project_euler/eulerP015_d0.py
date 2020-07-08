'''Starting in the top left corner of a 2x2 grid, there are 6 routes (without backtracking) to the bottom right corner.

How many routes are there through a 20x20 grid?
'''

n=20 #length of a side of the square

#number of paths to each "intersection". Starting one layer down. That is, from the origin you can go either down or right. So there is one path down and one path to the right.
paths = [1,1]

#If the grid is tilted 45 degrees so it's more of a diamond that we are falling 
#down through, then each iteration of the following while loop moves us down one 
#level until we reach the widest level of the diamon in its middle. This level
#has n+1 "intersections".
while len(paths) < n+1:
	#Build up the count of paths at the next level down starting from left to right.
	#There is only ever one path to the left-most intersection and that's the 
	#path where only down moves are performed.
	newpaths = [1]
	#iterate over the numbers from 0 to length of the paths array - 1
	for i in xrange(len(paths)-1):
		#Sum up the paths from "parent" intersections to get the number 
		#of paths to the current intersection.
		temp = paths[i] + paths[i+1]
		newpaths.append(temp)
	#Finally, there is only one way to reach the rightmost intersection and 
	#that's by always taking moves to the right.
	newpaths.append(1)
	#Paths becomes newpaths and we are ready to iterate down the diamond (aka tilted grid).
	paths = newpaths

#If the grid is tilted 45 degrees so it's more of a diamond that we are falling 
#down through, then we have now reached the midpoint, the widest middle layer.
#Now we narrow in.
#The following code is similar to the above.
while len(paths) > 1:
	newpaths = []
	for i in xrange(len(paths)-1):
		temp = paths[i] + paths[i+1]
		newpaths.append(temp)
	paths = newpaths

#Finally print the number of paths.
print paths[0] #Answer for 20x20 grid: 137846528820 paths.

