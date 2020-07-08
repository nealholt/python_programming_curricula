import random

#The following program demonstrates a sorting algorithm
#called Bubble Sort

#Create a list of of length random numbers between low and high
#For example getRandomList(20, 1, 100) would return a list
#of 20 random numbers between 1 and 100.
def getRandomList(length, low, high):
    list = []
    for i in range(length):
        list.append(random.randint(low, high))
    return list

#Sorts the given list
def bubbleSort(list):
    #Repeat for as many times as there are items in the list
    for _ in range(len(list)):
        #Repeat up to but not including the last item in the list
        for i in range(len(list)-1):
            #Compare adjacent values in the list.
            if list[i] > list[i+1]:
                #If the adjacent values are out of order,
                #then swap them.
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp


list = getRandomList(20, 1, 100)
print(list)
bubbleSort(list)
print(list)
