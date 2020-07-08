import string, random

'''
"," in string.ascii_lowercase-> False

theme could be escape from Griselduh's gingerbread house.
Ask user favorite candy.
'''

#list of most common english words
#https://en.wikipedia.org/wiki/Most_common_words_in_English
most_common_words = ["be", "have", "do", "dont", "say", "get", "make", "go", "know", "take", "see", "come", "think", "look", "want", "give", "use", "find", "tell", "ask", "work", "seem", "feel", "try", "leave", "call", "good", "new", "first", "last", "long", "great", "little", "own", "other", "old", "right", "big", "high", "different", "small", "large", "next", "early", "young", "important", "few", "public", "bad", "same", "able", "to", "of", "in", "for", "on", "with", "at", "by", "from", "up", "about", "into", "over", "after", "the", "and", "a", "that", "i", "me", "it", "not", "he", "as", "you", "this", "but", "his", "they", "her", "she", "or", "an", "will", "my", "one", "all", "would", "there", "their", "hi", "is", "was", "were", "am", "name", "who", "what", "where", "when", "why", "how"]

def processString(str):
	'''Strip all the punctuation out of str. Remove all the 
	most common words. Return the result as an array of split 
	up words. '''
	#print(str)
	str = str.lower() #lowercase
	#print(str)
	#remove punctuation
	for i in reversed(range(len(str))):
		if str[i] in string.punctuation:
			str = str[:i] + str[i+1:]
	#print(str)
	#remove most common words
	array = str.split(" ")
	for i in reversed(range(len(array))):
		if array[i] in most_common_words:
			del array[i]
	#print(array)
	return array


def askForName():
	'''Ask player for their name and return what we think is their name.'''
	str = input("\nWhat's your name?   ")
	word_list = processString(str)
	return (random.choice(word_list)).title()


def getName():
	'''Repeatedly ask player for their name and repeat until we get confirmation that we got their name accurately.'''
	name = askForName()
	response = input("\nYour name is "+name+"?   ")
	response = response.lower()
	name_options = ["Don't use that attitude with me!", "My mistake.", "If you spoke more clearly there wouldn't be any confusion."]
	while(not "yes" in response and not "right" in response and not "correct" in response):
		print("\n"+random.choice(name_options))
		name = askForName()
		response = input("\nYour name is "+name+"?   ")
		response = response.lower()
	return name


def matchingWords(list1, list2):
	'''Returns the first matching value in the two lists.
	Returns the empty string if there are no matches.'''
	for l in list1:
		if l in list2:
			return l
	return ""




running_words = ['escape', 'leave', 'run', 'flee', 'go']
fighting_words = ['fight', 'attack', 'strike', 'hit', 'rush', 'charge', 'kill', 'kick', 'punch', 'bite', 'tackle', 'beat', 'shoot']
game_words = ['challenge', 'chess', 'checkers', 'uno', 'dice', 'poker', 'monopoly', 'bridge', 'solitaire', 'tetris', 'overwatch', 'league', 'pacman', 'parcheesi', 'blockus', 'go']
#Interaction
print("\nMy name is Griselduh the witch.")
name = getName()
str = input("\nYou have found my gingerbread house. What will you do now?   ")
escaped = False
while not escaped:
	word_list = processString(str)
	if matchingWords(running_words, word_list):
		word = matchingWords(running_words, word_list)
		str = input("\nThe door slams shut behind you. Griselduh says, \"You cannot "+word+"!\" What will you do now?   ")
	elif matchingWords(fighting_words, word_list):
		word = matchingWords(fighting_words, word_list)
		str = input("\nGriselduh is surprisingly strong and nimble for an old lady. She says, \"You cannot "+word+" me!\" and you believe her. What will you do now?   ")
	elif matchingWords(game_words, word_list):
		word = matchingWords(game_words, word_list)
		print("\n\"I accept your challenge to a game of "+word.title()+",\" says Griselduh.")
		escaped = True
	elif len(word_list) == 0:
		str = input("\n\"Speak up!\" Griselduh must be hard of hearing. What will you do now?   ")
	elif "game" in word_list or "games" in word_list:
		str = input("\n\"Yes, a game! Choose one!\" Griselduh urges you.   ")
	else:
		word = random.choice(word_list)
		str = input("\n\"I'm not interested in "+word+". What about a game instead?\" says Griselduh.   ")
print("Griselduh trounces you in the game, but she lets you leave. Turns out all she really wanted was someone to play a game with. It\'s lonely living in the forest all by yourself.")
