import random

original_word = "a t t a c k"

#Scramble a copy of the word and convert it back to a string
scrambled_word = original_word.split()
random.shuffle(scrambled_word)
scrambled_word = "".join(scrambled_word)

#Remove spaces from the original word
original_word = "".join(original_word.split())

print(original_word)
print(scrambled_word)

guess = input("The scrambled letters are "+scrambled_word+".\nGuess the word:")
while guess != original_word:
    guess = input("Nope. Try again.\nThe scrambled letters are "+scrambled_word+".\nGuess the word:")
print("You guessed it right!")