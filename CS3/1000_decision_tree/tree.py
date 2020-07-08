from functions import *

class DecTreeNode:
    def __init__(self, data, attribute_indicies, target, num_partitions):
        '''data is a 2d array of our categorical data.
        attribute_indicies is a list of indicies that we are using as our attributes.
        target is the index of the attribute we want to predict
        num_partitions is the number of further splits we want to make in the tree.
        '''
        #Attribute being split on at this point in the tree.
        self.attribute = None
        #Children is a dictionary associating categories with sub trees
        #or with the final prediction if this is a terminal branch of
        #the tree
        self.children = None
        #What outcome we would predict at this point
        self.prediction = None

        #Keep splitting and building sub trees unless there are no more splits
        #to make
        if num_partitions>0 and len(attribute_indicies)>0:
            #find highest entropy attribute
            self.attribute = getLowestEntropyAtt(data, attribute_indicies, target)
            print('Partitions remaining: '+str(num_partitions-1))
            #split data on that attribute
            splits = splitOnAttribute(data,self.attribute)
            #recurse with more trees
            attribute_indicies.remove(self.attribute)
            self.children = {}
            for key in splits.keys():
                #print('Key: '+key)
                tree = DecTreeNode(splits[key], attribute_indicies, target, num_partitions-1)
                self.children[key] = tree
        #All done. Determine the most common prediction
        else:
            alphabet = getAlphabet(data, target)
            values = getColumn(data, target)
            #Which is the most common
            most_common = alphabet[0]
            count = values.count(most_common)
            for a in alphabet:
                temp = values.count(a)
                if temp>count:
                    most_common = a
                    count = temp
            self.prediction = most_common


    def predict(self,example):
        '''example is a list of attributes.'''
        if self.children==None:
            return self.prediction
        elif not(example[self.attribute] in self.children.keys()):
            #Attribute was missing from training set or missing
            #field in example. Just return nothing.
            return ""
        else:
            return self.children[example[self.attribute]].predict(example)
