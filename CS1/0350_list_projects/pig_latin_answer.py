
sentence = input('Say something')
sentence = sentence.lower()
print(sentence)
word_list = sentence.split(' ')

def convertToPigLatin(word):
    vowels = ['a','e','i','o','u']
    if word[0] in vowels:
        return word
    else:
        word = word[1:]+word[0]+"ay"
    return word

pig_latin = ''
for word in word_list:
    pig_latin += convertToPigLatin(word)+' '

print(pig_latin)
