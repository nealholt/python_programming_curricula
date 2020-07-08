
#Run the following program:
'''
#Open for reading. The 'r' stands for reading. We could alternatively use 'w' for writing, but let's save that for later.
file_handle = open('data.txt', 'r')
#Read the first line
line = file_handle.readline()
print(line)
'''

#What's different if we call readline() again?
'''
#Open for reading. The 'r' stands for reading. We could alternatively use 'w' for writing, but let's save that for later.
file_handle = open('data.txt', 'r')
#Read the first line
line = file_handle.readline()
#Read another line
line = file_handle.readline()
print(line)
'''

#So readline() automatically goes to the next line each time you call it.
#What happens if you read and print every line?
'''
#Open for reading. The 'r' stands for reading.
file_handle = open('data.txt', 'r')
#Fill the line variable with anything except an empty string so it will be treated like True.
line = 'temporary'
#Read and print every line.
while line:
	line = file_handle.readline()
	print(line)
'''

#Why are there blank lines when we print, but no blank lines in our data.txt file?
#It's because there is an invisible symbol at the end of each line that tells Python to make a new line.
#Let's strip that invisible symbol off.
'''
#Open for reading. The 'r' stands for reading.
file_handle = open('data.txt', 'r')
#Fill the line variable with anything except an empty string so it will be treated like True.
line = 'temporary'
#Read and print every line.
while line:
	line = file_handle.readline()
	line = line.strip()
	print(line)
'''

#Suppose I want a list of 1,2,3 or A,B,C. How can I split those up?
#Open for reading. The 'r' stands for reading. We could alternatively use 'w' for writing, but let's save that for later.
file_handle = open('data.txt', 'r')
file_handle.readline() #Skip the first line
file_handle.readline() #Skip the second line
#Read the third line
line = file_handle.readline()
line = line.strip()
list = line.split(',')
print(list)
print(list[0])
print(list[1])
print(list[2])
#Something weird happens if you don't use strip. Comment that line out in the previous program, re-run it, then write down the weird thing that happens.


#Write a program that reads in the line A,B,C, prints the line as a list and then just prints the letter C from the list.

