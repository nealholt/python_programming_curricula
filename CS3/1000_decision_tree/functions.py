import math,random


OWNER_AGE=0
OWNER_GENDER=1
CITY=2
BREED=3
BIRTH_YEAR=4
DOG_GENDER=5
DOG_COLOR=6
named_indicies = ['OWNER_AGE','OWNER_GENDER','CITY','BREED','BIRTH_YEAR','DOG_GENDER','DOG_COLOR']


def getDogData():
    '''Returns a list of lists of data from Zurich dog dataset.
    Omits dog id, secondary breeds, district, and RASSENTYP'''
    file_handle = open('20160307hundehalter.csv', 'r')
    line = file_handle.readline() #Skip the first line
    line = file_handle.readline()
    line = line.strip()
    temp = line.split(',')
    data = []
    while line:
        #Append data on owner and dog. omit some data
        data.append([temp[1],temp[2],temp[3],temp[5],temp[10],temp[11],temp[12]])
        #Get the next line
        line = file_handle.readline()
        line = line.strip()
        temp = line.split(',')
    file_handle.close()
    return data

def getAlphabet(data, column):
    '''Given a 2d array of data and a numeric column. Return a list of
    all the unique pieces of data in that column.'''
    unique = []
    for i in range(len(data)):
        if not(data[i][column] in unique):
            unique.append(data[i][column])
    return unique

def getColumn(data, column):
    '''Given a 2d array of data and a numeric column. Return a list of
    all the values in that column.'''
    values = []
    for i in range(len(data)):
        values.append(data[i][column])
    return values

def getEntropy(data_list, alphabet):
    entropy = 0
    for a in alphabet:
        Px = data_list.count(a) / len(data_list)
        if Px > 0:
            entropy -= Px * math.log(Px, 2)
    return entropy

def splitOnAttribute(data,column):
    splits = {}
    for d in data:
        if not(d[column] in splits.keys()):
            splits[d[column]] = [d]
        else:
            splits[d[column]].append(d)
    return splits

def getSplitsEntropy(splits, alphabet, target):
    entropy = 0
    for key in splits.keys():
        column = getColumn(splits[key], target)
        entropy += getEntropy(column, alphabet)
    return entropy

def getLowestEntropyAtt(data, attribute_indicies, target):
    '''data is a 2d list of categorical data.
    attribute_indicies is a list of indicies that we are using as our attributes.
    target is the index of the attribute we want to predict/classify.
    Returns index of the attribute that yields the lowest entropy
    groupings of the target after we split on it.'''
    lowest_e = 2**31
    index = attribute_indicies[0]
    for column in attribute_indicies:
        if column != target:
            #Make sure to get the alphabet for the target, not the column
            #you are splitting on.
            alphabet = getAlphabet(data, target)
            splits = splitOnAttribute(data,column)
            e = getSplitsEntropy(splits, alphabet, target)
            if e < lowest_e:
                lowest_e = e
                index = column
    print()
    print('Splitting on '+named_indicies[index])
    print('With entropy of '+str(lowest_e))
    return index

def getRandomPartition(data, ratio):
    '''Split up and return the data randomly in two sizes by ratio.'''
    part1 = []
    part2 = []
    for d in data:
        if random.random() < ratio:
            part1.append(d)
        else:
            part2.append(d)
    return part1,part2
