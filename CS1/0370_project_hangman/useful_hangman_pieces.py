word = "hello"

list_string = []
mystery_word = []
for letter in word:
    list_string.append(letter)
    mystery_word.append('_')
print(list_string)

string = ''.join(list_string)
print(string)

string = ' '.join(mystery_word)
print(string)

guess = input("Give me a letter.")
if guess in word:
    print('good guess')
else:
    print('bad guess')



#Big helpful hint:
guessed_letters = ["a", "j", "x", "o"]
secret_word = "marathon"

#Reveal parts of mystery word
display = []
for letter in secret_word:
    if letter in guessed_letters:
        display.append(letter)
    else:
        display.append("_")

string = ' '.join(display)
print(string)


#HANGMAN EXAMPLES
word = "hello"
for letter in word:
    if letter == "l":
        print("found l")
    else:
        print("Not our letter")

exit()



#More useful for replacement
word="hello"
for i in range(len(word)):
    if word[i] == "l":
        word[i] = "p" #Uh oh!
print("New word: "+word)



#This works:
word = ["h","e","l","l","o"]
for i in range(len(word)):
    if word[i] == "l":
        word[i] = "p" #Uh oh!
print("New word: "+str(word))
print("New word: "+"".join(word))

exit()
