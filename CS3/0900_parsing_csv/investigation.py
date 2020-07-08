
#For 35 points, answer the following questions.
#Be careful to run each program separately!

'''1. What does this program print? Open data.txt to see if that's what you
would have expected.'''
#Open for reading. The 'r' stands for reading. We could alternatively use
#'w' for writing, but let's save that for later.
file_handle = open('data.txt', 'r')
#Read the first line
line = file_handle.readline()
print(line)
file_handle.close()


'''2. What's different if we call readline() again?'''
file_handle = open('data.txt', 'r')
line = file_handle.readline()
line = file_handle.readline()
print(line)
file_handle.close()


'''3. So readline() automatically goes to the next line each time you call it.
What happens if you read and print every line?'''
#Open for reading. The 'r' stands for reading.
file_handle = open('data.txt', 'r')
#Fill the line variable with anything except an empty string so it will be
#treated like True.
line = 'temporary'
#Read and print every line.
while line:
	line = file_handle.readline()
	print(line)
file_handle.close()


'''4. What happens in the previous program if you try to read and print another
line after the while loop?'''


'''5. The reason there are blank lines when we print, but no blank lines in
our data.txt file is because there is an invisible symbol at the end of each
line that tells Python to make a new line.
Experiment with     line = line.strip()      then rewrite the previous program
to use strip to avoid printing this extra line.
'''


#Suppose I want a list of 1,2,3 or A,B,C. This is how can I split those up:
file_handle = open('data.txt', 'r')
file_handle.readline() #Skip the first line
file_handle.readline() #Skip the second line
line = file_handle.readline() #Read the third line
line = line.strip() #strip it
my_list = line.split(',') #split it
print(my_list)
print(my_list[0])
print(my_list[1])
print(my_list[2])

'''6. Something weird happens if you don't use strip. Comment that line out in
the previous program, re-run it. What is the weird thing that happens?'''


'''7. Write a program that reads in the line A,B,C, prints the line as a
list and then just prints the letter C from the list.'''


'''8. Copy data.txt to another file such as data_backup.txt then
run the following program and write down what the result is in data.txt.'''
file_handle = open('data.txt', 'w')
file_handle.write('All your text is gone!')
file_handle.close()


'''9. What is different between the first line of code in question 8 and the
first line of code in question 1?'''
