'''
For 35 points, answer the following questions.

Create a new folder named file_io and create a new Python file in the
folder. Run this 4 line program. Then look in the folder.
1) What did the program do?
'''
f = open('workfile.txt', 'w')
f.write('Bazarr 10 points\n')
f.write('Iko 3 points')
f.close()


'''Run this short program.
2) What did the program do?
'''
f = open('workfile.txt', 'r')
line = f.readline()
while line:
    print(line)
    line = f.readline()
f.close()


'''Run this short program.
3) What did the program do?
'''
f = open('value.txt', 'w')
f.write('14')
f.close()


'''Run this short program.
4) What did the program do?
'''
f = open('value.txt', 'r')
line = f.readline()
f.close()
x = int(line)
print(x*2)


'''Run this short program. Make sure to look at the value.txt file 
before and after running this program.
5) What did the program do?
'''
f = open('value.txt', 'r')
line = f.readline()
f.close()
x = int(line)
x = x*2
f = open('value.txt', 'w')
f.write(str(x))
f.close()
