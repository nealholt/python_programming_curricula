'''Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?'''


def getNameScore(name):
	return 0 #TODO LEFT OFF HERE


#Read in and parse the file
file_handle = open('eulerP022_names.txt', 'r')
names = file_handle.readline()
names = names.split(',')
for i in xrange(len(names)):
	names[i] = names[i].strip()
	names[i] = names[i].strip('"')
file_handle.close()

names.sort()

#Get the sum total score of all the names
total = 0
for i in xrange(len(names)):
	score = getNameScore(names[i])
	total += score * (i+1)
print total

#Need to find or create an easy way to match each letter to its index in the alphabet: A=1, B=2, C=3, etc. Check for this online.
#Work with:
import string
string.ascii_letters
