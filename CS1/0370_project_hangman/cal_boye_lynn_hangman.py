import math, random

def choosePhrase():
    #Chooses a quote to use as the secret phrase, of ten.
    #These are all Adam Savage quotes, the majority from his talk
    #"The Ten Commandments of Making at the San Fransisco Maker Faire
    #in 2014(?)
    num = random.randint(0, 10)

    if num == 0:
        return "i reject your reality and substitue my own"
    elif num == 1:
        return "make something"
    elif num == 2:
        return "make something useful"
    elif num == 3:
        return "start right now"
    elif num == 4:
        return "find a project"
    elif num == 5:
        return "ask for help, advise, feedback"
    elif num == 6:
        return "share"
    elif num == 7:
        return "recognize that discouragement and failure is part of the project"
    elif num == 8:
        return "measure carefully"
    elif num == 9:
        return "make things for other people"
    else:
        return "use more cooling fluid"

def checkWin(revealed_letters, secret_letters):
    #Checks if you got all the letters. Removes spaces from problematic list.
    truth = []

    modded_secret_letters = []

    for item in secret_letters:
        if item != " ":
            modded_secret_letters.append(item)

    for item in modded_secret_letters:
        if item in revealed_letters:
            truth.append(True)
        else:
            truth.append(False)

    if False in truth:
        return False
    else:
        return True


def makeListWithSpaces(string):
    #Translates string into list of letters.
    li = []
    for item in string:
        #if item != " ":
        li.append(item)
    return li

def makeListOfStringsIntoString(li):
    #Translates list of strings into a single string.
    string = ""
    for item in li:
        string = string + item
    return string

def checkGuess(guess_letter, secret_list):
    #Will check if the user's guess is in the list of values.
    for item in secret_list:
        if guess_letter == item:
            return True
    return False

def drawHangman(guess_num):
    #Depending on guesses, will draw different levels of hanged man.

    print("   ")
    print("-|-")
    print(" | ")

    if guess_num > 0:
        print(" * ")
    else:
        print("   ")

    if guess_num > 3 and guess_num < 5:
        print(" | ")
    elif guess_num > 4 and guess_num < 6:
        print("-| ")
    elif guess_num > 5 and guess_num < 7:
        print("-|-")
    else:
        print("   ")

    if guess_num > 1 and guess_num < 3:
        print("/")
    elif guess_num > 2:
        print("/ |")
    else:
        print("   ")

    print("   ")


secret_phrase = choosePhrase()

secret_list = makeListWithSpaces(secret_phrase)

guess_num = 0

revealed_letters = []
incorrect_letters = []
temp_letters = []

win = False
 #This will check of you run out of guesses or win.
while guess_num < 7 and win == False:
    #Draws the hanged man and the letters that were incorrect.
    drawHangman(guess_num)
    print(incorrect_letters)

    #Prints the empty spaces and revealed letters in the phrase.
    for item in secret_list:
        if item in revealed_letters:
            temp_letters.append(item)
        elif item == " ":
            temp_letters.append(" ")
        else:
            temp_letters.append("_")
    print(makeListOfStringsIntoString(temp_letters))

    #Resets a list.
    temp_letters = []

    #Accepts and checks user's guess.
    guess_letter = input("What letter do you guess next?")
    if checkGuess(guess_letter, secret_list):
        revealed_letters.append(guess_letter)

    else:
        incorrect_letters.append(guess_letter)
        guess_num = guess_num + 1

    win = checkWin(revealed_letters, secret_list)
    if win == True:
        print("You Win!")

print("Game Over!")









