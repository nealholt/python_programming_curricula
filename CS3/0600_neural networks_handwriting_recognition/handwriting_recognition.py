'''
A major remaining question is how to write the getError(outputs, target)
function. Currently the idea is that if the correct answer is zero then
the output should be 100000000 and if the correct answer is one then
output should be 010000000, two 0010000000, and so on.
But then even correct answers are given negative feedback to propagate.
Also, maybe just the magnitude that wrong answers are above the
magnitude of the correct output neuron should be the amount of error?
This might be an excellent question for students to investigate.

Students might also investigate decreasing learning rate over time
and size of hidden layer, though there is a significant time cost
involved with putting in a hidden layer.

This runs slow, but has been greatly optimized. Don't spend any more
time optimizing it.

This optimized draft08 neural net HAS NOT been copied over to the car driving
neural net code.
'''

import neural_net_draft08 as neural_net


#This function is a modified version of the function in visualizer
def parseLine(file_handle):
    '''Reads in the next line and parses it into a 2d array of gray scale
    values.'''
    line = file_handle.readline()
    line = line.strip()
    line = line.split(',')
    data = []
    target = int(line[0])
    del line[0]
    for l in line:
        #Put the data in the range 0 to 1
        data.append(int(l)/256)
    return data, target


def isCorrect(outputs, target):
    '''Returns True if the prediction is correct.'''
    largest = -1
    prediction = 0
    for i in range(len(outputs)):
        if outputs[i]>largest:
            prediction = i
            largest = outputs[i]
    #print(prediction)#TODO TESTING
    #print(outputs) #TODO TESTING
    return prediction == target


def getError(outputs, target):
    '''The output corresponding to the target value should have been one.
    All other outputs should have been zero.
    This function returns the list of target outputs.'''
    target_outputs = [0 for _ in range(10)]
    target_outputs[target] = 1
    return target_outputs

#One input for each pixel. 784 pixels.
#One output for each digit. Biggest digit wins.
#No hidden layer for starters.
layer_neuron_counts = [784,10]
nn = neural_net.NeuralNet(layer_neuron_counts)
eta = 0.2 #Learning rate. Higher is faster

passes = 100 #number of passes to do over the training set
line_count = 42001
training_percent = 0.75 #Train on this percent of data

#What is taking all the time?
import time
start = time.time();

for p in range(passes):
    #Start reading in training data
    file_handle = open('data/train.csv', 'r')
    line = file_handle.readline() #burn the first line. It's just the header
    #Count up correct scores to see progress
    correct_count = 0
    for i in range(int(line_count*training_percent)):
        inputs,target = parseLine(file_handle)
        nn.predict(inputs)
        outputs = nn.getOutputs()
        target_outputs = getError(outputs, target)
        if isCorrect(outputs, target):
            correct_count += 1
        #Learn
        neural_net.backpropagate(nn, eta, target_outputs)
    print('Training iteration: '+str(p)+'. Correct answers: '+str(correct_count))
    file_handle.close()
print('Elapsed time '+str(time.time()-start))
exit()