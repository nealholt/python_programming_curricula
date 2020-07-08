from tree import *

if __name__=='__main__':
    dogs = getDogData()

    #Testing
    '''#for dog in dogs:
    #    print(dog)

    genders = getAlphabet(dogs, DOG_GENDER)
    e = getEntropy(getColumn(dogs, DOG_GENDER), genders)
    print(e)
    #print(genders)

    breeds = getAlphabet(dogs, BREED)
    e = getEntropy(getColumn(dogs, BREED), breeds)
    print(e)
    #print(breeds)
    '''

    training_set,test_set = getRandomPartition(dogs, 0.75)
    #Given owner age, owner gender, and city, recommend/predict a dog breed
    attributes = [OWNER_AGE,OWNER_GENDER,CITY]
    target = BREED
    num_partitions = 3
    tree = DecTreeNode(training_set, attributes, target, num_partitions)

    #Evaluate random guessing's accuracy.
    breeds = getAlphabet(dogs, BREED)
    correct = 0
    for t in test_set:
        guess = random.choice(breeds)
        if guess == t[BREED]:
            correct+=1
    print()
    print('Accuracy of random guessing '+str(correct/len(test_set)))

    #Evaluate decision tree's accuracy
    correct = 0
    for t in test_set:
        guess = tree.predict(t)
        if guess == t[BREED]:
            correct+=1
    print()
    print('Accuracy of decision tree '+str(correct/len(test_set)))

    print()
    print("I'm a 31-40 year old male living in city 11.")
    print("What sort of dog should I get?")
    t = ['31-40', 'm', '11', '', '', '', '']
    guess = tree.predict(t)
    print(guess)

